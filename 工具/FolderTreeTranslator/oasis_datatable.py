# -*- coding: utf-8 -*-
r"""
绿洲起源 · 表格蓝图（DataTable）MCP 读写服务

职责
    1. 定位：把「资产路径 / 磁盘路径 / 表名」解析为编辑器资产路径 /<项目名>/Asset/...
    2. 读取：经 UGCAskQ MCP 的 ue_py 只读读取行结构体字段与行数据（纯查询，无需 PRV plan）
    3. 校验：行名规范、ValueType 合法、值与类型一致、未知字段、重复行名
    4. 回写：Resolve → Plan（ue_plan_submit）→ Execute（ue_py + plan_id）→ 保存 → 回读比对
    5. 备份：写前把当前表导出 JSON 到知识库备份目录，写后回读不一致时给出差异清单

证据依据（知识库）
    - raw/知识/通用/工具与流程/配置表与结构体的MCP编辑.md：
      data_table_as_dict / data_table_empty_row / data_table_add_row（返回 None 也算成功）/
      data_table_modify_row / data_table_remove_row / save_package 是对象方法。
    - raw/知识/通用/工具与流程/蓝图与MCP写入流程.md：写前备份、写后回读、资产路径用 /<项目名>/。
"""

import datetime
import json
import os
import re

from oasis_mcp_client import McpError, McpToolError, UgcMcpClient

BACKUP_ROOT = r"D:\知识库\和平精英绿洲起源\备份"

# 项目规范四列（IslandAuctionKing 约定）；非四列表也支持，只是校验放宽
STANDARD_FIELDS = ["ValueType", "Value", "Description", "ModificationNotes"]
VALUE_TYPES = ("int", "float", "bool", "string")

# 行名规则（2026-09-16 修订）
#   行名是 DataTable 内部的 FName 键，**不是文件名**，不受 UGC 文件命名规则约束：
#   不要求英文点号路径，中文、空格、连字符都可以。
#   写入时行名走 base64 + JSON 传参，不会拼进 ue_py 代码，任意字符都安全。
#   这里只保留「非空」一条硬约束，避免误建空行。
#   历史记录：旧规则要求 ^[A-Za-z][A-Za-z0-9_]*(\.[A-Za-z][A-Za-z0-9_]*)*$（英文点号路径），
#   该正则已废弃并移除，不再参与校验。


# --------------------------------------------------------------------------
# 一、本地校验（不依赖 MCP，写入前先跑）
# --------------------------------------------------------------------------

def validate_row_name(name):
    """校验行名；返回 (是否通过, 提示)。只校验非空，不套文件命名规则。"""
    name = (name or "").strip()
    if not name:
        return False, "行名不能为空"
    # 行名不套文件命名规则：中文 / 空格 / 连字符都允许，只要非空即可
    return True, ""


def validate_value(value_type, value):
    """按 ValueType 校验 Value；返回 (是否通过, 提示)。"""
    value = "" if value is None else str(value)
    vtype = (value_type or "").strip().lower()
    if vtype and vtype not in VALUE_TYPES:
        return False, "ValueType 必须是 %s 之一，当前为「%s」" % ("/".join(VALUE_TYPES), value_type)
    if not vtype:
        return True, ""          # 非四列表不做类型校验
    if vtype == "int":
        try:
            int(value)
        except Exception:
            return False, "ValueType=int 但 Value「%s」不是整数" % value
    elif vtype == "float":
        try:
            float(value)
        except Exception:
            return False, "ValueType=float 但 Value「%s」不是数值" % value
    elif vtype == "bool":
        if value.lower() not in ("true", "false", "1", "0", "yes", "no"):
            return False, "ValueType=bool 但 Value「%s」不是 true/false" % value
    return True, ""


def validate_changes(field_names, changes, existing_rows=None):
    """校验一批变更。

    changes      : {"upsert": {行名: {字段: 值}}, "delete": [行名]}
    existing_rows: 现有行名集合，用于区分新增/更新并检测重复
    返回         : {"errors": [(定位, 原因)], "warnings": [(定位, 原因)]}
    """
    existing_rows = existing_rows or set()
    errors, warnings = [], []
    known = set(field_names or [])

    upsert = changes.get("upsert") or {}
    for row_name, fields in upsert.items():
        ok, msg = validate_row_name(row_name)
        if not ok:
            errors.append(("行名 %s" % row_name, msg))
        for field, value in (fields or {}).items():
            if known and field not in known:
                errors.append(("%s.%s" % (row_name, field),
                               "字段「%s」不在行结构体中（现有字段：%s）"
                               % (field, "、".join(sorted(known)) or "无")))
        if "ValueType" in (fields or {}) or "Value" in (fields or {}):
            vtype = (fields or {}).get("ValueType")
            value = (fields or {}).get("Value")
            if vtype is not None and value is not None:
                ok, msg = validate_value(vtype, value)
                if not ok:
                    errors.append(("%s.Value" % row_name, msg))
        if row_name in existing_rows:
            warnings.append(("行名 %s" % row_name, "行已存在，将逐字段修改（modify_row）"))
        else:
            missing = [f for f in STANDARD_FIELDS if f in known and not str((fields or {}).get(f, "")).strip()]
            if missing:
                warnings.append(("行名 %s" % row_name,
                                 "新增行缺少 %s，写入后为空串" % "、".join(missing)))

    for row_name in changes.get("delete") or []:
        if row_name not in existing_rows:
            warnings.append(("行名 %s" % row_name, "表中不存在该行，删除将被忽略"))

    return {"errors": errors, "warnings": warnings}


# --------------------------------------------------------------------------
# 二、资产路径解析
# --------------------------------------------------------------------------

def normalize_asset_path(raw, project_name=None):
    """把常见写法归一化成 /<项目名>/Asset/... 形式（不含扩展名）。"""
    text = (raw or "").strip().strip('"').strip()
    if not text:
        return ""
    text = text.replace("\\", "/")
    if text.lower().endswith(".uasset"):
        text = text[: -len(".uasset")]
    # 磁盘路径：截取 Asset 之后的部分
    if ":" in text or text.lower().startswith("d/") or "/" not in text[:1]:
        pass
    idx = text.find("/Asset/")
    if idx >= 0:
        text = text[idx:]
    elif text.startswith("Asset/"):
        text = "/" + text
    if not text.startswith("/"):
        text = "/" + text
    # 补项目名前缀（编辑器要求 /<ProjectName>/Asset/...）
    if project_name and not text.startswith("/" + project_name + "/"):
        if text.startswith("/Asset/"):
            text = "/" + project_name + text
        elif not text.startswith("/") or text.count("/") == 1:
            text = "/" + project_name + "/Asset/Data/" + text.lstrip("/")
    return text


def find_table_candidates(project_root, keyword):
    """在项目 Asset/Data 下按表名模糊搜索，返回磁盘 .uasset 路径列表（最多 20 条）。"""
    hits = []
    if not project_root or not os.path.isdir(project_root):
        return hits
    data_dir = os.path.join(project_root, "Asset", "Data")
    if not os.path.isdir(data_dir):
        data_dir = os.path.join(project_root, "Asset")
    key = (keyword or "").strip().lower()
    for dirpath, _dirnames, filenames in os.walk(data_dir):
        for fn in filenames:
            if not fn.lower().endswith(".uasset"):
                continue
            base = fn[: -len(".uasset")]
            if not key or key in base.lower():
                hits.append(os.path.join(dirpath, fn))
            if len(hits) >= 20:
                return hits
    return hits


# --------------------------------------------------------------------------
# 三、编辑器内执行代码模板
# --------------------------------------------------------------------------

_READ_CODE = r'''
import unreal_engine as ue, json
from unreal_engine.classes import DataTable

P = __PATH__
LIMIT = __LIMIT__
PREFIX = __PREFIX__

def _safe(v):
    try:
        json.dumps(v)
        return v
    except Exception:
        return getattr(v, "get_path_name", lambda: str(v))()

try:
    dt = ue.load_object(DataTable, P)
except Exception as e:
    dt = None
    err = str(e)

if dt is None:
    __askq_result = json.dumps({"ok": False,
        "error": "无法加载 DataTable：%s。确认路径为 /<项目名>/Asset/... 且资产类型正确。" % P},
        ensure_ascii=False)
else:
    fields = []
    try:
        for v in dt.RowStruct.struct_get_variables():
            try:
                fields.append({"name": str(v.get_field("VarName")),
                               "friendly": str(v.get_field("FriendlyName")),
                               "type": str(v.get_field("Category"))})
            except Exception:
                fields.append({"name": str(v.VarName), "friendly": str(v.FriendlyName), "type": ""})
    except Exception:
        try:
            fields = [{"name": str(x), "friendly": str(x), "type": ""} for x in dt.RowStruct.properties()]
        except Exception:
            fields = []

    try:
        raw = dt.data_table_as_dict()
    except Exception as e:
        raw = {}
    names = sorted(raw.keys())
    if PREFIX:
        names = [n for n in names if str(n).startswith(PREFIX)]
    total = len(names)
    truncated = False
    if LIMIT > 0 and total > LIMIT:
        names = names[:LIMIT]
        truncated = True
    rows = {}
    for n in names:
        try:
            d = raw[n].as_dict()
        except Exception:
            d = {}
        rows[str(n)] = {str(k): _safe(v) for k, v in d.items()}
    __askq_result = json.dumps({"ok": True, "path": P, "fields": fields,
                                "row_count": total, "returned": len(rows),
                                "truncated": truncated, "rows": rows}, ensure_ascii=False)
'''

_SCHEMA_CODE = r'''
import unreal_engine as ue, json
from unreal_engine.classes import DataTable

P = __PATH__

dt = ue.load_object(DataTable, P)
if dt is None:
    __askq_result = json.dumps({"ok": False, "error": "无法加载 DataTable：%s" % P}, ensure_ascii=False)
else:
    fields = []
    try:
        for v in dt.RowStruct.struct_get_variables():
            try:
                fields.append({"name": str(v.get_field("VarName")),
                               "friendly": str(v.get_field("FriendlyName")),
                               "type": str(v.get_field("Category"))})
            except Exception:
                fields.append({"name": str(v.VarName), "friendly": str(v.FriendlyName), "type": ""})
    except Exception:
        try:
            fields = [{"name": str(x), "friendly": str(x), "type": ""} for x in dt.RowStruct.properties()]
        except Exception:
            fields = []
    try:
        names = [str(n) for n in dt.data_table_as_dict().keys()]
    except Exception:
        names = []
    __askq_result = json.dumps({"ok": True, "path": P, "fields": fields,
                                "row_names": names, "row_count": len(names)}, ensure_ascii=False)
'''

_RESOLVE_CODE = r'''
import unreal_engine as ue, json

KEY = __KEY__
out = {"ok": False, "matches": [], "tables": []}
items = None
try:
    items = ue.resolve_asset(KEY)
except Exception as e:
    out["error"] = repr(e)[:300]

if isinstance(items, dict):
    items = [items]

for it in (items or []):
    if not isinstance(it, dict):
        continue
    out["matches"].append({"name": it.get("name"),
                           "asset_class": it.get("asset_class"),
                           "load_path": it.get("load_path") or it.get("object_path") or it.get("package_name")})

out["tables"] = [m for m in out["matches"] if "DataTable" in (m.get("asset_class") or "")]
if out["tables"]:
    out["ok"] = True
    out["path"] = out["tables"][0]["load_path"]
elif out["matches"]:
    out["ok"] = True
    out["path"] = out["matches"][0]["load_path"]
__askq_result = json.dumps(out, ensure_ascii=False)
'''

_LIST_CODE = r'''
import unreal_engine as ue, json

DIRS = json.loads(base64.b64decode(__DIRS__).decode("utf-8"))
out = {"ok": True, "tables": [], "errors": []}
for d in DIRS:
    try:
        items = ue.list_assets(d)
    except Exception as e:
        out["errors"].append("%s -> %s" % (d, repr(e)[:200]))
        continue
    if isinstance(items, dict):
        items = [items]
    for it in (items or []):
        if not isinstance(it, dict):
            continue
        cls = it.get("asset_class") or ""
        if "DataTable" not in cls:
            continue
        out["tables"].append({"name": it.get("name"),
                              "asset_class": cls,
                              "load_path": it.get("load_path") or it.get("object_path") or it.get("package_name"),
                              "package_path": it.get("package_path") or it.get("category_path")})
__askq_result = json.dumps(out, ensure_ascii=False)
'''

_EXPORT_CODE = r'''
import unreal_engine as ue, json, io
from unreal_engine.classes import DataTable

P = __PATH__
OUT = __OUTFILE__

def _safe(v):
    try:
        json.dumps(v)
        return v
    except Exception:
        return getattr(v, "get_path_name", lambda: str(v))()

dt = ue.load_object(DataTable, P)
if dt is None:
    __askq_result = json.dumps({"ok": False, "error": "无法加载 DataTable：%s" % P}, ensure_ascii=False)
else:
    fields = []
    try:
        for v in dt.RowStruct.struct_get_variables():
            fields.append({"name": str(v.get_field("VarName")),
                           "friendly": str(v.get_field("FriendlyName"))})
    except Exception:
        fields = []
    raw = dt.data_table_as_dict()
    rows = {}
    for n, r in raw.items():
        try:
            d = r.as_dict()
        except Exception:
            d = {}
        rows[str(n)] = {str(k): _safe(v) for k, v in d.items()}
    payload = {"path": P, "exported_at": "__STAMP__", "fields": fields,
               "row_count": len(rows), "rows": rows}
    with io.open(OUT, "w", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=False, indent=2))
    __askq_result = json.dumps({"ok": True, "file": OUT, "row_count": len(rows)}, ensure_ascii=False)
'''

_WRITE_CODE = r'''
import unreal_engine as ue, json, base64
from unreal_engine.classes import DataTable

P = __PATH__
CH = json.loads(base64.b64decode(__PAYLOAD__).decode("utf-8"))

log = []
dt = ue.load_object(DataTable, P)
if dt is None:
    __askq_result = json.dumps({"ok": False, "error": "无法加载 DataTable：%s" % P}, ensure_ascii=False)
else:
    try:
        current = dt.data_table_as_dict()
    except Exception:
        current = {}

    delres = {}
    for rn in CH.get("delete", []):
        key = str(rn)
        before = key in current
        try:
            ok = dt.data_table_remove_row(key)
        except Exception as e:
            ok = False
            log.append("DEL %s ERR %s" % (key, e))
        log.append("DEL %s -> %s (before=%s)" % (key, ok, before))
        delres[key] = {"before": before, "ok": bool(ok)}

    for rn, fields in (CH.get("upsert") or {}).items():
        rn = str(rn)
        if rn in current:
            for f, v in fields.items():
                try:
                    ok = dt.data_table_modify_row(rn, str(f), str(v))
                    log.append("MOD %s.%s -> %s" % (rn, f, ok))
                except Exception as e:
                    log.append("MOD %s.%s ERR %s" % (rn, f, e))
        else:
            row = dt.data_table_empty_row()
            for f, v in fields.items():
                try:
                    row.set_field(str(f), str(v))
                except Exception:
                    try:
                        setattr(row, str(f), str(v))
                    except Exception as e:
                        log.append("SET %s.%s ERR %s" % (rn, f, e))
            try:
                dt.data_table_add_row(rn, row)      # 成功也返回 None，不能当判据
                log.append("ADD %s" % rn)
            except Exception as e:
                log.append("ADD %s ERR %s" % (rn, e))

    try:
        saved = bool(dt.save_package())
    except Exception as e:
        saved = False
        log.append("SAVE ERR %s" % e)

    # 回读校验：add_row 返回 None，唯一判据是回读
    dt2 = ue.load_object(DataTable, P)
    after = {}
    try:
        after = dt2.data_table_as_dict()
    except Exception as e:
        log.append("RELOAD ERR %s" % e)

    verify = {}
    for rn, fields in (CH.get("upsert") or {}).items():
        rn = str(rn)
        if rn not in after:
            verify[rn] = None
            continue
        try:
            d = after[rn].as_dict()
        except Exception:
            d = {}
        item = {}
        for f in fields:
            v = d.get(str(f))
            try:
                json.dumps(v)
            except Exception:
                v = getattr(v, "get_path_name", lambda: str(v))()
            item[str(f)] = v
        verify[rn] = item
    still_exists = [str(rn) for rn in (CH.get("delete") or []) if str(rn) in after]
    __askq_result = json.dumps({"ok": True, "saved": saved, "log": log,
                                "verify": verify, "delete_result": delres,
                                "still_exists": still_exists,
                                "row_count_after": len(after)}, ensure_ascii=False)
'''


# --------------------------------------------------------------------------
# 四、服务
# --------------------------------------------------------------------------

class DataTableService(object):
    """基于 UGCAskQ MCP 的表格蓝图数据读写服务。"""

    def __init__(self, client=None, project_name=None, project_root=None, logger=None):
        self.client = client or UgcMcpClient(logger=logger)
        self.project_name = project_name
        self.project_root = project_root
        self.logger = logger or (lambda _msg: None)

    # ---------------- 连接 ----------------
    def ensure_connected(self):
        if not self.client.connected:
            self.client.connect()
        return self.client.connected

    # ---------------- 定位 ----------------
    def resolve(self, raw, use_editor=True):
        """解析目标表，返回 {"path", "candidates", "matches", "source"}。

        优先级：
            1. 完整资产路径 / 磁盘路径 → 归一化（/项目名/Asset/...）
            2. 纯表名或关键字 → 编辑器 ue.resolve_asset（权威，走 AssetPathRemapping）
            3. 编辑器解析不到 → 本地文件系统搜索 Asset/Data
        """
        text = (raw or "").strip().strip('"').strip().replace("\\", "/")
        if not text:
            raise ValueError("请输入表格资产路径或表名")
        if text.lower().endswith(".uasset"):
            text = text[: -len(".uasset")]

        looks_like_path = ("/" in text) or (":" in text) or text.lower().startswith("asset/")
        if looks_like_path:
            path = normalize_asset_path(text, self.project_name)
            return {"path": path, "candidates": [], "matches": [], "source": "路径归一化"}

        # 纯标识：先问编辑器
        matches = []
        if use_editor:
            try:
                self.ensure_connected()
                code = _RESOLVE_CODE.replace("__KEY__", repr(text))
                result = self.client.call_ue_py(
                    code, instruction="FolderTreeTranslator 按名称定位表格资产", timeout=45)
                if isinstance(result, dict):
                    matches = result.get("matches") or []
                    if result.get("ok") and result.get("path"):
                        return {"path": result["path"], "candidates": [],
                                "matches": matches, "source": "编辑器 resolve_asset"}
            except Exception as exc:
                self.logger("[定位] 编辑器解析失败：%s" % exc)

        # 退回本地文件系统
        candidates = find_table_candidates(self.project_root, text)
        if candidates:
            return {"path": normalize_asset_path(candidates[0], self.project_name),
                    "candidates": candidates, "matches": matches, "source": "本地文件搜索"}
        return {"path": normalize_asset_path(text, self.project_name),
                "candidates": [], "matches": matches, "source": "规范推断（未验证）"}

    def list_tables(self, dirs=None):
        """列出项目表格资产（默认 Asset/Data 下各级目录），供界面下拉选择。"""
        self.ensure_connected()
        if not dirs:
            if not (self.project_name and self.project_root):
                return []
            dirs = self._data_dirs()
        import base64
        payload = base64.b64encode(json.dumps(dirs).encode("utf-8")).decode("ascii")
        code = _LIST_CODE.replace("__DIRS__", repr(payload))
        result = self.client.call_ue_py(
            code, instruction="FolderTreeTranslator 列举项目 DataTable 资产", timeout=60)
        if isinstance(result, dict):
            return result.get("tables") or []
        return []

    def _data_dirs(self):
        """扫描磁盘得到 Asset/Data 下所有目录，转成编辑器资产目录路径。"""
        dirs = []
        data_dir = os.path.join(self.project_root, "Asset", "Data")
        if not os.path.isdir(data_dir):
            return dirs
        for dirpath, _d, _f in os.walk(data_dir):
            rel = os.path.relpath(dirpath, self.project_root).replace("\\", "/")
            dirs.append("/%s/%s" % (self.project_name, rel))
        return dirs

    # ---------------- 读取 ----------------
    def read_table(self, asset_path, limit=300, prefix=""):
        """只读读取表格；返回结构化 dict。limit<=0 表示不限（可能被 MCP 截断）。"""
        self.ensure_connected()
        code = (_READ_CODE
                .replace("__PATH__", repr(asset_path))
                .replace("__LIMIT__", str(int(limit or 0)))
                .replace("__PREFIX__", repr(prefix or "")))
        result = self.client.call_ue_py(
            code,
            instruction="FolderTreeTranslator 只读读取 DataTable 行数据",
            timeout=90,
        )
        if isinstance(result, dict):
            if not result.get("ok"):
                raise McpToolError(result.get("error") or "读取失败（无错误信息）")
            return result
        raise McpToolError("读取返回格式异常：%r" % (result,))

    def get_schema(self, asset_path):
        """只读取行结构体字段与行名列表（不带行值，回包小，用于校验）。"""
        self.ensure_connected()
        code = _SCHEMA_CODE.replace("__PATH__", repr(asset_path))
        result = self.client.call_ue_py(
            code,
            instruction="FolderTreeTranslator 只读读取 DataTable 结构与行名",
            timeout=60,
        )
        if isinstance(result, dict):
            if not result.get("ok"):
                raise McpToolError(result.get("error") or "读取表结构失败")
            return result
        raise McpToolError("读取表结构返回格式异常：%r" % (result,))

    def export_table(self, asset_path, backup_dir):
        """把整表导出为 JSON 文件（编辑器侧写文件，避免 MCP 回包截断）。"""
        self.ensure_connected()
        if not os.path.isdir(backup_dir):
            os.makedirs(backup_dir)
        safe_name = os.path.basename(str(asset_path)).split(".")[0] or "DataTable"
        outfile = os.path.join(backup_dir, "%s_%s.json"
                               % (safe_name,
                                  datetime.datetime.now().strftime("%H%M%S")))
        code = (_EXPORT_CODE
                .replace("__PATH__", repr(asset_path))
                .replace("__OUTFILE__", repr(outfile))
                .replace("__STAMP__", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        result = self.client.call_ue_py(
            code,
            instruction="FolderTreeTranslator 导出 DataTable 全量 JSON 备份",
            timeout=120,
        )
        if isinstance(result, dict) and result.get("ok"):
            return outfile
        raise McpToolError("导出失败：%s" % (result if not isinstance(result, dict) else result.get("error")))

    def backup_table(self, asset_path, theme="表格回写"):
        """写前备份到知识库备份目录：备份/<项目名>/<YYYYMMDD>_<主题>/"""
        if not self.project_name:
            raise ValueError("未指定项目名，无法确定备份目录")
        day = datetime.datetime.now().strftime("%Y%m%d")
        target = os.path.join(BACKUP_ROOT, self.project_name, "%s_%s" % (day, theme))
        return self.export_table(asset_path, target)

    # ---------------- 写入 ----------------
    @staticmethod
    def build_plan(asset_path, changes):
        """构造 PRV 计划 YAML（ue_plan_submit 要求 intent/asset_path/mutations）。"""
        upserts = changes.get("upsert") or {}
        deletes = changes.get("delete") or []
        summary = "修改 %d 行 / 删除 %d 行" % (len(upserts), len(deletes))
        mutations = [
            '- property: RowData\n    value: "%s"' % summary,
        ]
        for row_name in list(upserts)[:5]:
            mutations.append('- property: Row.%s\n    value: "更新字段"' % row_name)
        lines = [
            'intent: "FolderTreeTranslator 表格数据回写：%s"' % summary,
            "asset_path: %s" % asset_path,
            "pre_write_snapshot: true",
            "apis_to_call:",
            "  - py:load_object",
            "  - py:data_table_as_dict",
            "  - py:data_table_modify_row",
            "  - py:data_table_add_row",
            "  - py:data_table_remove_row",
            "  - py:save_package",
            "mutations:",
        ]
        lines.extend(mutations)
        return "\n".join(lines)

    def write_table(self, asset_path, changes, do_backup=True):
        """回写变更，返回报告 dict。

        流程：本地校验 → 写前备份 → plan_submit → ue_py(plan_id) → 回读比对。
        """
        self.ensure_connected()

        # 1) 先取结构（字段 + 行名，回包小）
        schema = self.get_schema(asset_path)
        field_names = [f["name"] for f in schema.get("fields", [])]
        existing = set(schema.get("row_names") or [])

        check = validate_changes(field_names, changes, existing)
        if check["errors"]:
            return {"ok": False, "stage": "校验", "errors": check["errors"],
                    "warnings": check["warnings"], "message": "本地校验未通过，未写入编辑器"}

        # 2) 写前备份（失败不阻断，但要在报告里说明）
        backup_file = None
        backup_error = ""
        if do_backup:
            try:
                backup_file = self.backup_table(asset_path)
            except Exception as exc:
                backup_error = str(exc)

        # 3) Plan
        plan = self.build_plan(asset_path, changes)
        plan_id = self.client.submit_plan(
            plan, reasoning="FolderTreeTranslator 表格数据回写（%s）" % asset_path)

        # 4) Execute
        import base64
        payload = base64.b64encode(
            json.dumps(changes, ensure_ascii=False).encode("utf-8")).decode("ascii")
        code = (_WRITE_CODE
                .replace("__PATH__", repr(asset_path))
                .replace("__PAYLOAD__", repr(payload)))
        kwargs = {"instruction": "FolderTreeTranslator 表格数据回写（修改/新增/删除行）",
                  "transaction_name": "FolderTreeTranslator 表格回写",
                  "timeout": 180}
        if plan_id:
            kwargs["plan_id"] = plan_id
        else:
            kwargs["plan"] = plan

        result = self.client.call_ue_py(code, **kwargs)
        if not isinstance(result, dict) or not result.get("ok"):
            return {"ok": False, "stage": "执行",
                    "errors": [("ue_py", result if not isinstance(result, dict) else result.get("error"))],
                    "warnings": check["warnings"], "backup": backup_file,
                    "backup_error": backup_error, "message": "编辑器执行失败"}

        # 5) 回读比对（唯一判据）
        diffs = []
        notes = []
        for row_name, expect in (changes.get("upsert") or {}).items():
            actual = (result.get("verify") or {}).get(row_name)
            if actual is None:
                diffs.append((row_name, "回读不到该行（写入未生效）"))
                continue
            for field, value in expect.items():
                got = actual.get(field)
                if got is None and str(value) != "":
                    diffs.append(("%s.%s" % (row_name, field), "回读为空，期望「%s」" % value))
                elif got is not None and str(got) != str(value):
                    diffs.append(("%s.%s" % (row_name, field), "期望「%s」，回读「%s」" % (value, got)))
        for row_name in (result.get("still_exists") or []):
            diffs.append((row_name, "删除后仍存在"))
        for row_name, info in (result.get("delete_result") or {}).items():
            if info.get("before") and not info.get("ok"):
                diffs.append((row_name, "表中有该行但 remove_row 返回失败"))
            elif not info.get("before"):
                notes.append((row_name, "表中不存在该行，删除被忽略"))

        return {
            "ok": not diffs,
            "stage": "回读校验",
            "saved": result.get("saved"),
            "backup": backup_file,
            "backup_error": backup_error,
            "plan_id": plan_id,
            "log": result.get("log") or [],
            "diffs": diffs,
            "notes": notes,
            "warnings": check["warnings"],
            "row_count_after": result.get("row_count_after"),
            "message": ("回写成功并回读一致（%d 行）；配置表改动需重新 PIE 生效"
                        % result.get("row_count_after", 0)) if not diffs
            else "回写完成但回读存在差异，请看差异清单",
        }
