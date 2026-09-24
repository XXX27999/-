---
name: oasis-mcp-port-discover
description: 定位并验证《和平精英》绿洲编辑器 UGCAskQ MCP Server 的真实监听端口，并在客户端侧 MCP 工具未注册时用 Python 直连 SSE 通道完成 JSON-RPC 握手。当用户说「启用 MCP」「MCP 已启用但工具用不了」「MCP 连不上」「ue_py / ue_read / ue_plan_submit 找不到」或需要在不依赖 ToolSearch 注册的情况下操作编辑器资产时使用。
agent_created: true
---

# 绿洲编辑器 UGCAskQ MCP 端口发现与直连

## 何时使用

- 用户报告「启用 MCP」后工具仍不可用，或 `ToolSearch` 查不到 `ue_read` / `ue_py` / `ue_plan_submit` / `ue_pie`。
- 需要确认 UGCAskQ MCP Server 是否在运行、监听哪个端口。
- 客户端 MCP 工具未注入本会话，但仍需操作编辑器资产（读控件树、写 UMG、执行 Python）。

## 核心事实（已验证，务必先读）

1. **官方 Wiki 写的 `33444` 只是默认值；本机编辑器实际使用固定端口 `12463`**（用户确认 2026-09-16；2026-09-07~09-16 多次会话实测均为 `12463`），**不是**随编辑器实例动态分配。
   - ⚠️ **订正（2026-09-16）**：本行旧表述为「实际端口随编辑器实例分配」，据此会误推「必须每次自动发现端口」。现已确认 `12463` 为固定端口，三处客户端配置写死该值即为正确做法。
   - → **永远不要直接信任文档端口**：文档写 `33444`，本机是 `12463`；但 `12463` 在本机是稳定的，不需每次重新发现。
   - → 只有**换机器、重装编辑器或改过 MCP Server 控制面板的 Port** 时，才需重新走完整复核流程；日常「工具不可用」多属服务没起来或客户端未注册，直接跳到步骤 1、2 即可。
2. **`mcp.json` 里配 `"type":"sse"` + `http://127.0.0.1:<port>/sse` 不能直接工作。**
   SSE 传输需要两步：先 `GET /sse` 拿到动态的 `POST /messages?session_id=<hex>`，
   再往该地址 POST JSON-RPC。
3. **`POST /messages?session_id=...` 返回 HTTP `202` 且 body 为空。**
   真正的 JSON-RPC 响应从 SSE 流下行。只读 POST 回包的客户端会拿到空响应，
   表现为"工具不可用"。
4. `Mcp-Session-Id` 响应头在本实现下**不必须**，session 由 URL query 承载。
5. `serverInfo` 期望为 `{"name":"UGCEditor-PIE","version":"2.0.0"}`。

## 步骤 1：确认编辑器在跑

```powershell
Get-Process -Name ShadowTrackerExtraUGCEditor |
  Select-Object Id, MainWindowHandle, MainWindowTitle
```

同名进程通常有两个，**取 `MainWindowHandle` 非 0 且标题非空的那个**（另一个是空壳）。

## 步骤 2：确认 MCP 日志活跃（判断 Server 是否健康）

```
<编辑器根>\ShadowTrackerExtra\Saved\log\MCP\MCP_<YYYYMMDD>.log
```

看 `LastWriteTime` 是否接近当前时间，以及是否有 `<Call #N>` / `<Response>` 成功记录。
日志活跃 ⇒ Server 侧健康，问题在端口或客户端。

## 步骤 3：枚举编辑器进程的监听端口（关键步骤）

```python
import subprocess
out = subprocess.check_output(['netstat','-ano','-p','TCP'], text=True, encoding='utf-8', errors='ignore')
editor_pids = {'22064', '12048', '2440'}   # 换成步骤 1 拿到的真实 pid
for line in out.splitlines():
    if 'LISTENING' not in line: continue
    parts = line.split()
    if len(parts) >= 5 and parts[-1] in editor_pids:
        print(line.strip())
```

实测会看到类似：`59183` / `59184`（0.0.0.0）、`12463` / `27019`（127.0.0.1）。

## 步骤 4：逐端口判型，找到 `/sse`

对每个候选端口探测 `/sse`，**认 `200` + `Content-Type: text/event-stream`**：

| 表现 | 含义 |
|---|---|
| `200` + `text/event-stream` | ✅ MCP SSE 命中 |
| 请求 timeout | 非 HTTP 服务（如编辑器内部 IPC） |
| `RemoteDisconnected` | 非 HTTP 服务 |
| `404 Not Found` | HTTP 服务但不是 MCP（例如 Clash 代理端口 `33331`）|
| `/mcp` 返回 `405 Method Not Allowed` | 存在但需要 POST |

**陷阱**：`33300–33600` 段常见的 `33331` 属于 `clash-verge` 代理，不是 MCP。

## 步骤 5：完成 JSON-RPC 全握手（验证通道可用）

```python
import http.client, json, threading, time

HOST, PORT = '127.0.0.1', 12463          # 换成步骤 4 命中值

sse = http.client.HTTPConnection(HOST, PORT, timeout=30)
sse.request('GET', '/sse', headers={'Accept': 'text/event-stream'})
resp = sse.getresponse()

lines, stop = [], threading.Event()
def reader():
    try:
        while not stop.is_set():
            ln = resp.fp.readline()
            if not ln: break
            lines.append(ln.decode('utf-8', 'replace').rstrip('\r\n'))
    except Exception as e:
        lines.append('READER_END:' + type(e).__name__)
threading.Thread(target=reader, daemon=True).start()

# 等 endpoint 事件
endpoint, deadline = None, time.time() + 8
while time.time() < deadline and endpoint is None:
    for ln in list(lines):
        if ln.startswith('data:') and 'session_id=' in ln:
            endpoint = ln.split('data:', 1)[1].strip(); break
    if endpoint is None: time.sleep(0.15)

def rpc(method, params=None, notify=False):
    p = {'jsonrpc': '2.0', 'method': method}
    if params is not None: p['params'] = params
    if not notify: p['id'] = 1
    c = http.client.HTTPConnection(HOST, PORT, timeout=15)
    c.request('POST', endpoint, body=json.dumps(p).encode(),
              headers={'Content-Type': 'application/json',
                       'Accept': 'application/json, text/event-stream'})
    c.getresponse().read()          # 202 空体，正常

rpc('initialize', {'protocolVersion': '2024-11-05', 'capabilities': {},
                   'clientInfo': {'name': 'wb', 'version': '1.0'}})
rpc('notifications/initialized', {}, notify=True)
time.sleep(0.5)
rpc('tools/list', {})
time.sleep(2.5); stop.set()

for ln in lines:
    if ln.startswith('data:'): print(ln[:1200])
```

**成功标志**：SSE 流中出现
`"serverInfo":{"name":"UGCEditor-PIE","version":"2.0.0"}` 与 `tools` 清单。

## 步骤 6：修正客户端配置（如仍希望走原生 MCP）

写入 `C:\Users\Administrator\.workbuddy\mcp.json`（**合并写入，勿覆盖其他 server**）：

```json
{
  "mcpServers": {
    "ugcaskq": { "type": "sse", "url": "http://127.0.0.1:<真实端口>/sse" }
  }
}
```

注意：如「核心事实 2/3」所述，SSE 配置通常无法直接生效，
**本机可行路径是步骤 5 的 Python 直连**。若坚持原生路径，需用户
重启 AI 客户端 → 连接器管理页右上角「自定义连接器」→ 对 `ugcaskq` 点「信任」。

## 步骤 5 的补充坑（2026-09-15 实测）

- **SSE 长连接必须单独设大 timeout**：示例里 `HTTPConnection(HOST, PORT, timeout=30)` 会同时作用于
  读线程的 `readline()`，30 秒后抛 `timed out` 并断开通道（表现为后续调用全部失败）。
  建流用 `timeout=3600`，请求用独立短超时。
- **`endpoint` 事件不是 JSON**：`data:` 行是纯路径 `/messages?session_id=<hex>`，
  读线程要单独识别（不含 `{` 且含 `session_id=`），否则永远等不到 endpoint。
- **`POST` 回包 202 空体**，结果从 SSE 下行，`tools/call` 的返回在 `result.content[0].text`，
  通常是 JSON 字符串（`ue_py` 形如 `{"success":true,"result":<__askq_result>,"prv":{...}}`）。

## 资产定位：不要拼路径

拼错时编辑器会明确提示 `Package ... does NOT exist on disk` 并给出三个安全 API：

- `ue.resolve_asset('<名称>')` → `list[dict]`（含 `name` / `asset_class` / `load_path`）
- `ue.list_assets('<目录>')` → 同结构
- `ue.search_game_assets('<关键字>')` → UGC 项目实测返回**空数组**

DataTable 的 `asset_class` 是 **`UAEDataTable`**（不是 `DataTable`），同目录行结构体一并返回，
必须按 `asset_class` 过滤后取 `load_path` 原样使用。

## 编辑器侧工具用法（直连时通过 tools/call 调用）

- `ue_read`：只读查询，`{"queries":["py:widget_inspect AuctionSettlementUI"]}`，支持批量数组。
- `ue_plan_submit`：PRV 计划，**`mutations` 必须是 `[{property, value}]` 对象列表**，
  传字符串列表会报 `PRV_PLAN_INVALID: missing/invalid: mutations|scene_ops`。
  **实测 `plan_id` 可能返回 `None`，但写入仍然成功——以写后回读为准。**
- `ue_py`：执行 Python，带 `plan_id` 关联计划。
- `ue_pie`：PIE 控制；运行中优先 `reloadlua`（热更 Lua，秒级）/ `doluastring`，
  避免 `stop+start`（1–2 分钟）。

### ⚠️ `ue_read` 的 query 里没有 `resolve_asset`

`py:resolve_asset AuctionSettlementUI` 会返回
`No API found for 'resolve_asset ...' Use 'py:index' to see all categories.`
**不要把它当查询用。** 正确做法是走 `ue_py` 直连反射：

```python
import unreal_engine as ue
cls = ue.find_class('UGCWidgetBlueprint')          # 控件蓝图类名，classes 模块不暴露
wbp = ue.load_object(cls, FULL_PATH)               # FULL_PATH 见下
```

**资产路径必须是完整 `.AssetName` 形式**，例如
`/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/AuctionSettlementUI.AuctionSettlementUI`
（注意：**不是** `/Asset/UI/...`，也**不是** `/Game/...`）。传错会得到
`Package does NOT exist on disk. The path is wrong.` 并提示 asset path remapping。

### 控件对象属性反射（三个入口，容易混）

| 入口 | 返回 | 可用于 |
|---|---|---|
| `w.as_dict()` | **真实值** dict | ✅ 读 Brush / Background / Slot / Visibility |
| `w.get_uproperty(name)` | **FProperty 描述符**，不是值 | ❌ 读值会误导 |
| `w.get_value_prop(holder)` | 值 | ⚠️ **只对 Map 属性有效**，否则报 `object is not a UMapProperty` |

控件对象**没有 `get_editor_property`**（会 `AttributeError`）。
`WidgetTree.AllWidgets` 是遍历入口（list）；`get_name()` / `get_class()` 可用，
`GetClass()` / `GetChildrenCount()`（UE 大写驼峰）不可用。

### Border 画刷读法

`Border.Brush` **恒为 `None`**；真正生效的是 `Background`：

```python
bg = w.as_dict()['Background']          # FSlateBrush 结构体
d = dict(bg.as_dict())                  # ResourceName / ResourceObject / DrawAs / Margin / TintColor
```

判断「这个 Border 是否自己画东西」看 `DrawAs == 0` + `ResourceObject is None`
→ 自身零绘制，所见边线来自**外挂图片层**（`ContentCanvas` 绝对坐标层），
**改 Border 画刷不可能影响它**。

### CanvasPanelSlot 几何读法

```python
# 方式 1（省事）：人类可读，直接给 Pos/Size
ins = ue.widget_inspect(wbp, 'SkipButton')     # -> "Slot: CanvasPanel (Pos: 900,985, Size: 298,77)"

# 方式 2（精确）：嵌套 FAnchorData
d = slot.as_dict()['LayoutData']
dict(d.as_dict())['Offsets']                   # {Left,Top,Right,Bottom} 语义即 (x,y,w,h)
```

## 🔴 截图量化比对：必须按外框归一化 + 用连续段判覆盖

两张截图缩放通常不同（实测编辑器 1936×1048 vs 参考图 1150×663），
**目视直接比对会系统性产生假差异**。实测首轮目视报出 5 条差异，量化后 **5 条全部证伪**。

铁律：

1. **先按各自外框归一化再比**，否则缩放差会被误读成布局差。
2. **判定「局部 vs 通栏」必须用「最长连续段 / 外框宽」**，
   不能用「行内像素总数」——后者把该行所有内容（文字/图标/竖线）都计入，
   同一个数字既可读成"很短"也可读成"很长"。
3. **必须在全图测量，不能先裁剪再统计**。裁剪会改变坐标系、切掉目标区间。
   实测同一行：裁剪口径得 `n=35/238`（判"局部"）→ 全图口径得
   最长连续段占外框 **0.397 vs 参考 0.397**（实为完全一致）→ **结论翻转**。

```python
def longest_run(xs, gap=3):
    """xs = 该行命中像素的 x 列表（升序）；返回最长连续段长度与起止。"""
    best = 0; bs = be = xs[0]; s = prev = xs[0]
    for x in xs[1:]:
        if x - prev > gap:
            if prev - s > best: best, bs, be = prev - s, s, prev
            s = x
        prev = x
    return max(best, prev - s), bs, be
```

## 必须遵守的约束

- 排查/验证用的临时 `.py` 一律写到 `D:\知识库\和平精英绿洲起源\备份\<项目名>\<YYYYMMDD>_<主题>\`
  或用户目录，**严禁留在 UGC 工程内**（工程内残留会中断 PIE 调试）。
  PowerShell 的 `Remove-Item` 可能被策略静默拦截 → 改用 Python `os.remove` 并回读校验。
- 未确认通道可用前，**禁止直接改 `.uasset` 或 `_JsonOutput` JSON**。
- 蓝图/UI 写入必须走 `Resolve → Plan → Execute`，写前备份、写后回读。

## 已知环境坑

- `Bash` 工具在部分机器上因 PortableGit shim 损坏不可用
  （`dirname` / `cd` / `ls` / `head` / `tail` / `grep` not found）
  → 改用**绝对路径 Python 调用**（`cd <dir> && <abs python> script.py`），
  文件枚举/删除也用 Python 做；或改用 `PowerShell` 工具 + `Glob` / `Grep` 内置工具。
- `PowerShell` 工具有时不回传 stdout → 用「PowerShell 写文件 → Read 工具读取」两步法。
- **Pillow 只装在 venv**：`C:\Users\Administrator\.workbuddy\binaries\python\envs\default\Scripts\python.exe`。
  用托管解释器 `.../python/versions/3.13.12/python.exe` 跑 PIL 脚本会
  `ModuleNotFoundError: No module named 'PIL'`。凡涉及图像处理一律用 venv 那个解释器。
- MCP 回包对长文本会 truncate → 让 `ue_py` 把大 payload **写文件到备份目录**，只回传短确认。

## 窗口截图（FlaUI 不可用时的 GDI 路径）

Win32 + GDI 在 64 位 Python 下有两个必踩的坑：

1. **必须为每个函数声明 `restype` / `argtypes`**，否则句柄被截断为 int32，
   进程**静默崩溃**（exit code 1、无输出）。症状：HDC 打印成 `18446744072887548579`。
2. **`GetDIBits` 用负 `biHeight` 得 top-down 缓冲，而 BMP 文件格式要求 BOTTOM-UP**
   → 写文件时**倒序迭代行**，否则整图上下翻转。

窗口选择：编辑器标题可能是 mojibake（`ShadowTrackerExtra (64 浣嶏紝PCD3D_SM5)...`），
**不可按标题文本匹配**；按 PID 选（优先），或 `title.lower().startswith("shadowtrackerextra")` + 尺寸过滤（`w>=640 h>=480`）。
