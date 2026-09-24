# -*- coding: utf-8 -*-
r"""
绿洲起源 · UGCAskQ MCP 轻量客户端（仅依赖 Python 标准库）

用途
    FolderTreeTranslator 等知识库工具直连编辑器 MCP Server，调用
    ue_read / ue_py / ue_plan_submit 读取与修改表格蓝图（DataTable）数据。

连接要点（实测结论，来源：知识库技能 oasis-mcp-port-discover）
    1. 端口由编辑器实例分配，官方文档默认值 33444 不可信；
       优先读 ~/.workbuddy/mcp.json，其次用 netstat + 编辑器进程 PID 枚举候选端口。
    2. SSE 通道分两步：先 GET /sse 从事件流拿到 data: /messages?session_id=<hex>，
       再向该地址 POST JSON-RPC；POST 只回 202 空体，真正结果从 SSE 流下行，
       只读 POST 回包的客户端会表现为“工具不可用”。
    3. tools/call 的返回体在 result.content[0].text，通常是 JSON 字符串。

设计约束
    - 只用标准库，便于 PyInstaller 单文件打包。
    - 所有异常收敛为 Mcp* 异常，调用方只处理中文可读错误。
    - 线程安全：请求用自增 id + 事件等待，可在 GUI 后台线程调用。
"""

import json
import os
import re
import socket
import subprocess
import threading
import time

from concurrent.futures import ThreadPoolExecutor
from http.client import HTTPConnection, HTTPException

__all__ = [
    "McpError", "McpConnectionError", "McpTimeoutError", "McpToolError",
    "UgcMcpClient", "discover_candidate_ports",
]

DEFAULT_HOST = "127.0.0.1"
EDITOR_PROCESS_NAME = "ShadowTrackerExtraUGCEditor.exe"
MCP_JSON_CANDIDATES = (
    os.path.join(os.path.expanduser("~"), ".workbuddy", "mcp.json"),
    os.path.join(os.path.expanduser("~"), ".workbuddy", ".mcp.json"),
)
SERVER_NAME_EXPECTED = "UGCEditor-PIE"

# 无窗口启动子进程（Windows）；非 Windows 平台忽略
def _no_window_startupinfo():
    if os.name != "nt":
        return None
    info = subprocess.STARTUPINFO()
    try:
        info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    except Exception:
        pass
    return info


class McpError(Exception):
    """MCP 调用失败的基类。"""


class McpConnectionError(McpError):
    """编辑器未启动、端口未发现或 SSE 通道建立失败。"""


class McpTimeoutError(McpError):
    """等待 MCP 响应超时。"""


class McpToolError(McpError):
    """工具执行返回错误（编辑器侧报错，如资产路径不存在）。"""


def _run(cmd, timeout=8):
    """执行命令并取 stdout；失败返回空串，不抛异常。"""
    try:
        out = subprocess.check_output(
            cmd,
            stderr=subprocess.STDOUT,
            timeout=timeout,
            startupinfo=_no_window_startupinfo(),
        )
    except Exception:
        return ""
    try:
        return out.decode("utf-8", "replace")
    except Exception:
        return ""


def _port_from_mcp_json():
    """从 WorkBuddy 的 mcp.json 读取已配置的 ugcaskq 端口。"""
    for path in MCP_JSON_CANDIDATES:
        if not os.path.isfile(path):
            continue
        try:
            with open(path, "r", encoding="utf-8") as fp:
                cfg = json.load(fp)
        except Exception:
            continue
        servers = cfg.get("mcpServers") or {}
        for name, server in servers.items():
            if "ugc" not in name.lower() and "ugc" not in json.dumps(server, ensure_ascii=False).lower():
                continue
            url = str(server.get("url") or "")
            m = re.search(r":(\d+)", url)
            if m:
                return int(m.group(1))
    return None


def _editor_pids():
    """返回编辑器进程 PID 集合（同名进程通常有两个，取全部候选）。"""
    text = _run(["tasklist", "/FI", "IMAGENAME eq %s" % EDITOR_PROCESS_NAME, "/FO", "CSV", "/NH"])
    pids = set()
    for line in text.splitlines():
        parts = [p.strip().strip('"') for p in line.split(",")]
        if len(parts) >= 2 and parts[0].lower().endswith(".exe"):
            if parts[1].isdigit():
                pids.add(parts[1])
    return pids


def _listening_ports_of(pids):
    """从 netstat 输出中筛出指定 PID 的 LISTENING 端口（本地回环优先）。"""
    if not pids:
        return []
    text = _run(["netstat", "-ano", "-p", "TCP"])
    loopback, other = [], []
    for line in text.splitlines():
        if "LISTENING" not in line.upper():
            continue
        parts = line.split()
        if len(parts) < 5 or parts[-1] not in pids:
            continue
        m = re.search(r"[:](\d+)\s*$", parts[1])
        if not m:
            continue
        port = int(m.group(1))
        (loopback if parts[1].startswith("127.0.0.1") else other).append(port)
    # 去重保序：回环端口优先，其余按端口号升序（MCP 端口通常较小）
    seen, ordered = set(), []
    for port in loopback + sorted(other):
        if port not in seen:
            seen.add(port)
            ordered.append(port)
    return ordered


def discover_candidate_ports():
    """返回按优先级排序的 MCP 候选端口列表。"""
    ports = []

    env_port = os.environ.get("UGC_MCP_PORT", "").strip()
    if env_port.isdigit():
        ports.append(int(env_port))

    json_port = _port_from_mcp_json()
    if json_port:
        ports.append(json_port)

    ports.extend(_listening_ports_of(_editor_pids()))

    seen, ordered = set(), []
    for port in ports:
        if 1 <= port <= 65535 and port not in seen:
            seen.add(port)
            ordered.append(port)
    return ordered


class UgcMcpClient(object):
    """UGCAskQ MCP SSE 客户端（一次连接，可反复调用）。"""

    def __init__(self, host=DEFAULT_HOST, port=None, connect_timeout=6,
                 call_timeout=120.0, sse_timeout=3600.0, logger=None,
                 on_progress=None, probe_timeout=1.5, connect_budget=25.0):
        self.host = host
        self.port = port
        self.connect_timeout = connect_timeout
        self.call_timeout = call_timeout
        # SSE 是长连接：读线程会一直 readline，超时太短会主动断开通道
        self.sse_timeout = sse_timeout
        # 端口探测：单端口超时 + 整体预算（多编辑器实例时候选端口可达 10 个以上，
        # 串行探测会累计到十几秒，主观表现为“连接超时”）
        self.probe_timeout = probe_timeout
        self.connect_budget = connect_budget
        self.logger = logger or (lambda _msg: None)
        self.on_progress = on_progress or (lambda _msg: None)

        self.candidate_ports = [port] if port else discover_candidate_ports()
        self.server_info = None
        self.connected = False

        self._lock = threading.RLock()
        self._id = 0
        self._results = {}
        self._events = {}
        self._conn = None
        self._resp = None
        self._reader = None
        self._stop = threading.Event()
        self._endpoint = None

    # ---------------- 日志与生命周期 ----------------
    def _log(self, msg):
        try:
            self.logger(str(msg))
        except Exception:
            pass

    def _progress(self, msg):
        """进度回调（GUI 用于展示“正在尝试哪个端口”）。"""
        self._log(msg)
        try:
            self.on_progress(str(msg))
        except Exception:
            pass

    def close(self):
        """关闭 SSE 连接与读线程，并立即唤醒所有在途请求。

        只关 socket 是不够的：Windows 上另一个线程阻塞在 readline() 时，
        关连接不一定立刻把它打断。额外调用 _wake_all_waiters()，
        让在途请求直接以「连接已断开」返回，保证「中止」是确定性的。
        """
        self._stop.set()
        self.connected = False
        try:
            if self._conn is not None:
                self._conn.close()
        except Exception:
            pass
        self._conn = None
        self._resp = None
        self._wake_all_waiters()

    def _wake_all_waiters(self):
        """唤醒所有等待中的请求；拿不到结果时调用方按「连接已断开」报错返回。"""
        with self._lock:
            events = list(self._events.values())
        for event in events:
            event.set()

    # ---------------- SSE 读线程 ----------------
    def _reader_loop(self):
        """持续读取 SSE 流，把带 id 的响应投递给等待者。"""
        try:
            while not self._stop.is_set():
                line = self._resp.fp.readline()
                if not line:
                    break
                try:
                    text = line.decode("utf-8", "replace").rstrip("\r\n")
                except Exception:
                    continue
                if not text.startswith("data:"):
                    continue
                payload = text[5:].strip()
                if not payload:
                    continue
                # endpoint 事件：纯路径（/messages?session_id=...），没有 JSON-RPC id
                if not payload.startswith("{") and ("session_id=" in payload or payload.startswith("/")):
                    self._endpoint = payload
                    continue
                try:
                    msg = json.loads(payload)
                except Exception:
                    continue
                # 服务端偶发下发非对象负载（如裸数字心跳/批量响应），不是 JSON-RPC 响应。
                # 不判类型就直接 msg.get 会抛异常并把读线程打死，表现为「连接静默失效」，
                # 界面只剩一句 [MCP] SSE 读线程结束… —— 这里跳过并继续读下一条。
                if not isinstance(msg, dict):
                    continue
                mid = msg.get("id")
                if mid is None:
                    continue
                with self._lock:
                    self._results[mid] = msg
                    event = self._events.get(mid)
                if event is not None:
                    event.set()
        except Exception as exc:
            self._log("[MCP] SSE 读线程结束：%s" % exc)
        finally:
            # 连接断开后唤醒所有等待者，避免调用方永久阻塞
            self._wake_all_waiters()

    def _open_stream(self, port):
        """建立 SSE 长连接并等待 endpoint 事件。"""
        conn = HTTPConnection(self.host, port, timeout=self.sse_timeout)
        conn.request("GET", "/sse", headers={"Accept": "text/event-stream"})
        resp = conn.getresponse()
        ctype = (resp.getheader("Content-Type") or "").lower()
        if resp.status != 200 or "text/event-stream" not in ctype:
            try:
                resp.read()
            except Exception:
                pass
            conn.close()
            raise McpConnectionError("端口 %s 不是 MCP SSE 服务（HTTP %s）" % (port, resp.status))

        self._conn, self._resp, self.port = conn, resp, port
        self._stop.clear()
        self._reader = threading.Thread(target=self._reader_loop, daemon=True)
        self._reader.start()

        deadline = time.time() + self.connect_timeout
        while time.time() < deadline:
            if self._endpoint:
                return
            time.sleep(0.05)
        # 兜底：部分实现首帧即给 endpoint，读线程需要一点时间
        raise McpConnectionError("端口 %s 未在 %.1fs 内返回 session endpoint" % (port, self.connect_timeout))

    def _initialize(self):
        """完成 initialize + notifications/initialized 握手。"""
        result = self._request(
            "initialize",
            {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {"name": "FolderTreeTranslator", "version": "1.4.0"},
            },
            timeout=self.connect_timeout,
        )
        self.server_info = result.get("serverInfo") or {}
        self._notify("notifications/initialized", {})

    def _probe_one(self, port):
        """只判断该端口是否为 MCP SSE 服务（不建立长连接），返回 (port, 是否命中, 说明)。"""
        try:
            conn = HTTPConnection(self.host, port, timeout=self.probe_timeout)
            conn.request("GET", "/sse", headers={"Accept": "text/event-stream"})
            resp = conn.getresponse()
            ctype = (resp.getheader("Content-Type") or "").lower()
            ok = (resp.status == 200 and "text/event-stream" in ctype)
            try:
                resp.read(1)
            except Exception:
                pass
            conn.close()
            return port, ok, "HTTP %s" % resp.status
        except Exception as exc:
            return port, False, type(exc).__name__

    def probe_alive_ports(self, ports=None):
        """并行探测候选端口，返回仍保序的存活端口列表。"""
        ports = list(ports or self.candidate_ports or [])
        if not ports:
            return []
        ok_set = set()
        notes = []
        workers = min(8, max(1, len(ports)))
        with ThreadPoolExecutor(max_workers=workers) as pool:
            for port, ok, info in pool.map(self._probe_one, ports):
                notes.append("%s:%s" % (port, info))
                if ok:
                    ok_set.add(port)
        self._progress("端口探测完成（%d/%d 命中）：%s" % (len(ok_set), len(ports), " ".join(notes)))
        return [p for p in ports if p in ok_set]

    def connect(self):
        """按候选端口顺序建立连接；返回命中的端口号。

        流程：并行探测 /sse 存活（单端口 probe_timeout）→ 对存活端口依次做
        initialize 握手（受 connect_budget 总预算约束）→ 成功即返回。
        """
        if self.connected:
            return self.port
        if not self.candidate_ports:
            raise McpConnectionError(
                "未发现 MCP 候选端口：请确认绿洲编辑器已启动，或在 ~/.workbuddy/mcp.json 配置 ugcaskq 端口。")

        self._progress("正在探测 %d 个候选端口…" % len(self.candidate_ports))
        alive = self.probe_alive_ports(self.candidate_ports)
        if not alive:
            raise McpConnectionError(
                "未发现可用的 MCP SSE 端口（%s）。请确认绿洲编辑器已启动且 MCP 已启用；"
                "编辑器重启后端口会变化，可在 ~/.workbuddy/mcp.json 更新 ugcaskq 端口。"
                % "、".join(str(p) for p in self.candidate_ports[:12]))

        errors = []
        deadline = time.time() + self.connect_budget
        for port in alive:
            if time.time() > deadline:
                errors.append("总预算 %.0fs 用尽，停止尝试" % self.connect_budget)
                break
            self._endpoint = None
            try:
                self._progress("端口 %s 正在握手…" % port)
                self._open_stream(port)
                # endpoint 由读线程写入，这里再等一次
                wait_until = time.time() + self.connect_timeout
                while time.time() < wait_until and not self._endpoint:
                    time.sleep(0.05)
                if not self._endpoint:
                    raise McpConnectionError("未拿到 session endpoint")
                self._initialize()
                self.connected = True
                self._log("[MCP] 已连接 127.0.0.1:%s（%s）"
                          % (port, self.server_info.get("name", "未知服务")))
                return port
            except Exception as exc:
                errors.append("%s：%s" % (port, exc))
                self.close()

        raise McpConnectionError("无法连接 UGCAskQ MCP。已尝试：%s" % "；".join(errors))

    # ---------------- JSON-RPC ----------------
    def _post(self, method, params=None, notify=False, msg_id=None):
        """POST 一条 JSON-RPC；响应通过 SSE 流异步返回。"""
        body = {"jsonrpc": "2.0", "method": method}
        if params is not None:
            body["params"] = params
        if not notify:
            body["id"] = msg_id
        conn = HTTPConnection(self.host, self.port, timeout=self.call_timeout)
        try:
            conn.request("POST", self._endpoint,
                         body=json.dumps(body, ensure_ascii=False).encode("utf-8"),
                         headers={"Content-Type": "application/json",
                                  "Accept": "application/json, text/event-stream"})
            resp = conn.getresponse()
            resp.read()          # 202 空体，正常
        finally:
            conn.close()

    def _request(self, method, params=None, timeout=None):
        with self._lock:
            self._id += 1
            mid = self._id
            event = threading.Event()
            self._events[mid] = event
        self._post(method, params, msg_id=mid)
        if not event.wait(timeout or self.call_timeout):
            with self._lock:
                self._events.pop(mid, None)
            raise McpTimeoutError("%s 超时（%.0fs）：编辑器可能正忙或未响应。" % (method, timeout or self.call_timeout))
        with self._lock:
            msg = self._results.pop(mid, None)
            self._events.pop(mid, None)
        if msg is None:
            raise McpConnectionError("MCP 连接已断开，%s 未拿到响应。" % method)
        if "error" in msg and msg["error"]:
            err = msg["error"]
            raise McpToolError("%s：%s" % (err.get("code", "ERROR"), err.get("message", err)))
        return msg.get("result") or {}

    def _notify(self, method, params=None):
        try:
            self._post(method, params, notify=True)
        except Exception as exc:
            self._log("[MCP] 通知发送失败（可忽略）：%s" % exc)

    # ---------------- 工具调用 ----------------
    @staticmethod
    def _extract_json(text):
        """从工具返回文本中解析 JSON；失败时返回 None。"""
        if not text:
            return None
        text = text.strip()
        try:
            return json.loads(text)
        except Exception:
            pass
        # 兼容带前缀日志的返回：截取首个 {...} 或 [...] 块
        for opener, closer in (("{", "}"), ("[", "]")):
            start = text.find(opener)
            end = text.rfind(closer)
            if start >= 0 and end > start:
                try:
                    return json.loads(text[start:end + 1])
                except Exception:
                    continue
        return None

    def call_tool(self, name, arguments=None, timeout=None):
        """调用 MCP 工具，返回 {text, json, is_error, raw}。"""
        if not self.connected:
            self.connect()
        result = self._request("tools/call",
                               {"name": name, "arguments": arguments or {}},
                               timeout=timeout)
        content = result.get("content") or []
        texts = []
        for item in content:
            if isinstance(item, dict) and item.get("type") == "text":
                texts.append(item.get("text", ""))
        text = "\n".join(texts).strip()
        is_error = bool(result.get("isError"))
        if is_error:
            raise McpToolError(text or "工具 %s 返回错误（无详细信息）" % name)
        return {"text": text, "json": self._extract_json(text), "is_error": False, "raw": result}

    def list_tools(self, timeout=None):
        result = self._request("tools/list", {}, timeout=timeout or self.call_timeout)
        return result.get("tools") or []

    # ---------------- ue_py 便捷封装 ----------------
    def call_ue_py(self, code, instruction=None, plan=None, plan_id=None,
                   transaction_name=None, timeout=None):
        """执行编辑器内 Python；返回 __askq_result 对应的 result 字段。

        ue_py 返回形如 {"success":true,"result":<__askq_result>,"prv":{...}}。
        success 为 False 时抛 McpToolError，错误文本取 result/output/warnings。
        """
        args = {"code": code}
        if instruction:
            args["instruction"] = instruction
        if plan:
            args["plan"] = plan
        if plan_id:
            args["plan_id"] = plan_id
        if transaction_name:
            args["transaction_name"] = transaction_name
        res = self.call_tool("ue_py", args, timeout=timeout)
        payload = res["json"]
        if isinstance(payload, dict):
            if payload.get("success") is False:
                detail = payload.get("result") or payload.get("error") or res["text"][:800]
                raise McpToolError("ue_py 执行失败：%s" % (detail,))
            return payload.get("result")
        return payload

    def submit_plan(self, plan, reasoning=None, timeout=None):
        """提交 PRV 计划，返回 plan_id（失败返回 None，由调用方降级）。"""
        args = {"plan": plan}
        if reasoning:
            args["reasoning"] = reasoning
        try:
            res = self.call_tool("ue_plan_submit", args, timeout=timeout or self.call_timeout)
        except McpError as exc:
            self._log("[MCP] plan 提交失败，将改用内联 plan：%s" % exc)
            return None
        payload = res["json"] or {}
        if isinstance(payload, dict):
            return payload.get("plan_id") or (payload.get("result") or {}).get("plan_id")
        return None
