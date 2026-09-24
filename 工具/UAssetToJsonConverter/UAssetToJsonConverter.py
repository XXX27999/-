# -*- coding: utf-8 -*-
r"""
UAssetToJsonConverter —— 绿洲编辑器 .uasset -> JSON 同步工具（工程外置版）

来源：IslandAuctionKing 工程根 `ConvertUAssetToJson.ps1` 的整理与移植版。
原脚本按 `$PSScriptRoot` 推断工程根、把结果写到工程内 `_JsonOutput`，属于「非地图运行所需」
的外部工具资料，已迁出 UGC 工程到知识库统一调用。

本版本的改动（相对原 ps1）：
  1. 工程根、输出根、UAssetGUI 路径、UE 版本全部可配置，不再依赖脚本自身所在目录；
     默认输出到知识库，保证工程目录里不再产生 `_JsonOutput`。
  2. 保留原行为：只扫描 *.uasset；按 LastWriteTime 做增量跳过；转换后清理「源 uasset 已删除」
     的孤儿 JSON；监视模式每 2 秒轮询增/改/删。
  3. 新增命令行模式（--mode/--dry-run/--report）与 --selftest 环境自检，便于自动化验证；
     无参数时启动 tkinter 图形界面。
  4. v1.1.0：界面「工程根」「输出根」改为与 FolderTreeTranslator 一致的选择式交互——
     工程根可下拉（探测 UGCProjects 下含 Asset 的项目）或「浏览…」选目录；
     输出根可下拉（知识库 raw 下已存在的 _JsonOutput）或「浏览…」选目录，
     默认随工程派生为 知识库 raw\<项目名>\_JsonOutput。转换逻辑与命令行参数不变。

用法（图形界面）：双击 UAssetToJsonConverter.exe
用法（命令行）：
  UAssetToJsonConverter.exe --selftest "D:\report.json"
  UAssetToJsonConverter.exe --mode convert --report "D:\report.json"
  UAssetToJsonConverter.exe --mode watch
"""

import argparse
import json
import os
import subprocess
import sys
import threading
import time

APP_TITLE = "UAsset 转 JSON 同步工具"
APP_VERSION = "1.1.0"

# ---------------- 默认配置（可通过命令行或界面覆盖） ----------------
DEFAULT_PROJECT = r"D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing"
DEFAULT_OUTPUT = r"D:\知识库\和平精英绿洲起源\raw\IslandAuctionKing\_JsonOutput"
DEFAULT_UASSETGUI = r"C:\Program Files (x86)\UAssetGUI.exe"
DEFAULT_UE_VERSION = "VER_UE4_24"
DEFAULT_POLL_INTERVAL = 2

# 界面下拉探测用：工程集合根、知识库 raw 根、镜像目录名
# 与 FolderTreeTranslator 的 DEFAULT_PROJECTS_ROOT 取值一致，判据同为「含 Asset 子目录」
DEFAULT_PROJECTS_ROOT = r"D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects"
KB_RAW_ROOT = r"D:\知识库\和平精英绿洲起源\raw"
OUTPUT_DIR_NAME = "_JsonOutput"

# 原脚本的排除规则：不把 _JsonOutput / UAssetGUI 自身当输入
EXCLUDE_MARKERS = ("_JsonOutput", "UAssetGUI")


# ---------------- 路径探测（图形界面「快速选择」用，与 FolderTreeTranslator 行为对齐） ----------------
def detect_projects(projects_root=DEFAULT_PROJECTS_ROOT):
    r"""列出工程集合根下可用地图项目（含 Asset 子目录）。"""
    result = []
    if os.path.isdir(projects_root):
        try:
            for name in sorted(os.listdir(projects_root)):
                full = os.path.join(projects_root, name)
                if os.path.isdir(full) and os.path.isdir(os.path.join(full, "Asset")):
                    result.append(os.path.normpath(full))
        except OSError:
            pass
    return result


def derive_output_root(project_path):
    r"""按 `知识库 raw\<项目名>\_JsonOutput` 派生输出根；工程名为空时返回空串。"""
    name = os.path.basename(os.path.normpath(project_path)) if project_path else ""
    if not name:
        return ""
    return os.path.join(KB_RAW_ROOT, name, OUTPUT_DIR_NAME)


def detect_output_roots(raw_root=KB_RAW_ROOT):
    r"""列出知识库 raw 下已存在的 `_JsonOutput` 目录，供输出根下拉选择。"""
    result = []
    if os.path.isdir(raw_root):
        try:
            for name in sorted(os.listdir(raw_root)):
                full = os.path.join(raw_root, name, OUTPUT_DIR_NAME)
                if os.path.isdir(full):
                    result.append(os.path.normpath(full))
        except OSError:
            pass
    return result


def log_line(sink, text):
    r"""统一日志出口；sink 可为 callable(图形界面) 或 None(命令行模式)。"""
    line = "[%s] %s" % (time.strftime("%H:%M:%S"), text)
    if sink is not None:
        sink(line)
    else:
        try:
            print(line, flush=True)
        except Exception:
            pass


def iter_uassets(project_root):
    r"""枚举工程内全部 .uasset，按原脚本规则排除输出目录与 UAssetGUI。"""
    result = []
    for root, dirs, files in os.walk(project_root):
        if any(m in root for m in EXCLUDE_MARKERS):
            dirs[:] = []
            continue
        for name in files:
            if name.lower().endswith(".uasset"):
                result.append(os.path.join(root, name))
    return result


def relative_dir(project_root, file_path):
    r"""取文件相对工程根的目录（与 ps1 的 Substring+TrimStart('\') 等价）。"""
    rel = os.path.relpath(os.path.dirname(file_path), project_root)
    return "" if rel == "." else rel


def dest_json_path(project_root, output_root, file_path):
    r"""按源 uasset 路径镜像出目标 JSON 路径。"""
    base = os.path.splitext(os.path.basename(file_path))[0]
    rel_dir = relative_dir(project_root, file_path)
    return os.path.join(output_root, rel_dir, base + ".json") if rel_dir else os.path.join(output_root, base + ".json")


def run_uassetgui(uassetgui, ue_version, src, dst):
    r"""调用 UAssetGUI tojson，返回退出码（异常返回 -1）。"""
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    try:
        proc = subprocess.run([uassetgui, "tojson", src, dst, ue_version],
                              capture_output=True, text=True)
        return proc.returncode
    except Exception:
        return -1


# ---------------- 核心：增量全量转换 ----------------
def run_full_conversion(cfg, sink, dry_run=False):
    r"""增量转换全量 .uasset；随后清理源已删除的孤儿 JSON。返回统计字典。"""
    project_root = cfg["project"]
    output_root = cfg["output"]
    log_line(sink, "=== 增量全量转换开始 ===")
    log_line(sink, "入口 工程根=%s" % project_root)
    log_line(sink, "出口 输出根=%s" % output_root)
    log_line(sink, "参数 UAssetGUI=%s UE版本=%s dry_run=%s" % (cfg["uassetgui"], cfg["ue_version"], dry_run))

    if not os.path.isdir(project_root):
        log_line(sink, "错误 工程根不存在，终止")
        return {"ok": False, "error": "project_not_found", "total": 0, "converted": 0, "skipped": 0,
                "failed": 0, "cleaned": 0, "failures": []}
    if not os.path.isfile(cfg["uassetgui"]):
        log_line(sink, "错误 UAssetGUI 不存在：%s" % cfg["uassetgui"])
        return {"ok": False, "error": "uassetgui_not_found", "total": 0, "converted": 0, "skipped": 0,
                "failed": 0, "cleaned": 0, "failures": []}

    os.makedirs(output_root, exist_ok=True)
    uassets = iter_uassets(project_root)
    log_line(sink, "关键数据 命中 uasset=%d 个" % len(uassets))

    total = len(uassets)
    converted = skipped = failed = 0
    failures = []

    for idx, src in enumerate(uassets, 1):
        dst = dest_json_path(project_root, output_root, src)
        name = os.path.basename(src)
        if os.path.isfile(dst):
            try:
                if os.path.getmtime(src) <= os.path.getmtime(dst):
                    skipped += 1
                    log_line(sink, "[%d/%d] 跳过（无变化）: %s" % (idx, total, name))
                    continue
            except OSError:
                pass
        if dry_run:
            converted += 1
            log_line(sink, "[%d/%d] 待转换(dry-run): %s -> %s" % (idx, total, name, dst))
            continue
        code = run_uassetgui(cfg["uassetgui"], cfg["ue_version"], src, dst)
        if code == 0:
            converted += 1
            log_line(sink, "[%d/%d] 转换成功: %s" % (idx, total, name))
        else:
            failed += 1
            failures.append({"source": src, "target": dst, "exit_code": code})
            log_line(sink, "[%d/%d] 转换失败(exit=%s): %s" % (idx, total, code, name))

    cleaned = 0
    log_line(sink, "--- 清理孤儿 JSON（源 uasset 已删除）---")
    valid = set()
    for src in uassets:
        valid.add(os.path.normcase(dest_json_path(project_root, output_root, src)))
    for root, dirs, files in os.walk(output_root):
        for name in files:
            if not name.lower().endswith(".json"):
                continue
            p = os.path.join(root, name)
            if os.path.normcase(p) not in valid:
                if dry_run:
                    cleaned += 1
                    log_line(sink, "待删除孤儿(dry-run): %s" % p)
                else:
                    try:
                        os.remove(p)
                        cleaned += 1
                        log_line(sink, "已删除孤儿: %s" % p)
                    except OSError as exc:
                        log_line(sink, "删除孤儿失败: %s error=%s" % (p, exc))

    stats = {"ok": failed == 0, "total": total, "converted": converted, "skipped": skipped,
             "failed": failed, "cleaned": cleaned, "failures": failures}
    log_line(sink, "出口 统计 total=%d converted=%d skipped=%d failed=%d cleaned=%d"
             % (total, converted, skipped, failed, cleaned))
    return stats


# ---------------- 核心：监视模式 ----------------
def run_watch(cfg, sink, stop_event, dry_run=False):
    r"""每 poll_interval 秒轮询增/改/删并同步；stop_event 置位后退出。"""
    project_root = cfg["project"]
    output_root = cfg["output"]
    log_line(sink, "=== 监视模式开始（每 %s 秒轮询，Ctrl+C / 停止按钮结束）===" % cfg["poll_interval"])
    if not os.path.isfile(cfg["uassetgui"]):
        log_line(sink, "错误 UAssetGUI 不存在：%s" % cfg["uassetgui"])
        return
    os.makedirs(output_root, exist_ok=True)

    state = {}
    for src in iter_uassets(project_root):
        try:
            state[src] = os.path.getmtime(src)
        except OSError:
            pass
    log_line(sink, "入口 已装载 %d 个 uasset 初始状态" % len(state))

    try:
        while not stop_event.is_set():
            time.sleep(cfg["poll_interval"])
            current = iter_uassets(project_root)
            paths = set()
            for src in current:
                paths.add(src)
                try:
                    mtime = os.path.getmtime(src)
                except OSError:
                    continue
                dst = dest_json_path(project_root, output_root, src)
                if src not in state:
                    log_line(sink, "检测到新增: %s" % os.path.basename(src))
                    if not dry_run:
                        code = run_uassetgui(cfg["uassetgui"], cfg["ue_version"], src, dst)
                        log_line(sink, "新增转换 exit=%s -> %s" % (code, dst))
                    state[src] = mtime
                elif state[src] != mtime:
                    log_line(sink, "检测到修改: %s" % os.path.basename(src))
                    if not dry_run:
                        code = run_uassetgui(cfg["uassetgui"], cfg["ue_version"], src, dst)
                        log_line(sink, "修改转换 exit=%s -> %s" % (code, dst))
                    state[src] = mtime
            for old in list(state.keys()):
                if old not in paths:
                    log_line(sink, "检测到删除: %s" % os.path.basename(old))
                    dst = dest_json_path(project_root, output_root, old)
                    if os.path.isfile(dst):
                        if dry_run:
                            log_line(sink, "待删除同步 JSON(dry-run): %s" % dst)
                        else:
                            try:
                                os.remove(dst)
                                log_line(sink, "已删除同步 JSON: %s" % dst)
                            except OSError as exc:
                                log_line(sink, "删除同步 JSON 失败: %s error=%s" % (dst, exc))
                    del state[old]
    except KeyboardInterrupt:
        log_line(sink, "收到 Ctrl+C，监视模式退出")
    log_line(sink, "出口 监视模式结束")


# ---------------- 环境自检 ----------------
def selftest(cfg):
    r"""打包后自动化验证入口：检查依赖、路径与 uasset 命中数，返回 JSON 可序列化字典。"""
    checks = []
    checks.append({"item": "uassetgui_exists", "value": os.path.isfile(cfg["uassetgui"]), "target": cfg["uassetgui"]})
    checks.append({"item": "project_exists", "value": os.path.isdir(cfg["project"]), "target": cfg["project"]})
    checks.append({"item": "output_exists", "value": os.path.isdir(cfg["output"]), "target": cfg["output"]})
    uassets = iter_uassets(cfg["project"]) if os.path.isdir(cfg["project"]) else []
    checks.append({"item": "uasset_count", "value": len(uassets), "target": cfg["project"]})
    checks.append({"item": "output_inside_project",
                   "value": os.path.normcase(cfg["output"]).startswith(os.path.normcase(cfg["project"])),
                   "target": cfg["output"]})
    sample = uassets[0] if uassets else ""
    if sample:
        checks.append({"item": "sample_target", "value": dest_json_path(cfg["project"], cfg["output"], sample),
                       "target": sample})
    json_hits = 0
    if os.path.isdir(cfg["output"]):
        for root, dirs, files in os.walk(cfg["output"]):
            json_hits += sum(1 for f in files if f.lower().endswith(".json"))
    checks.append({"item": "existing_json_count", "value": json_hits, "target": cfg["output"]})
    ok = all(c["value"] for c in checks if c["item"] in ("uassetgui_exists", "project_exists")
             and isinstance(c["value"], bool))
    return {"app": APP_TITLE, "version": APP_VERSION, "frozen": bool(getattr(sys, "frozen", False)),
            "python": sys.version, "config": cfg, "ok": ok, "checks": checks}


# ---------------- 图形界面 ----------------
def launch_gui(cfg):
    r"""tkinter 界面：「工程根」「输出根」改为下拉 + 浏览选择（与 FolderTreeTranslator 一致，
    无需手敲路径），其余参数仍可手填；可跑增量转换与监视模式、日志可见。"""
    import tkinter as tk
    from tkinter import ttk, filedialog, messagebox

    root = tk.Tk()
    root.title("%s  v%s" % (APP_TITLE, APP_VERSION))
    root.geometry("1120x700")
    root.minsize(960, 600)
    style = ttk.Style()
    try:
        style.theme_use("clam")
    except tk.TclError:
        pass
    font = ("Microsoft YaHei UI", 9)

    state = {"stop": threading.Event(), "worker": None}
    entries = {}          # 仍需手填的三个参数：UAssetGUI / UE 版本 / 轮询秒

    form = ttk.Frame(root, padding=8)
    form.pack(fill="x")

    project_var = tk.StringVar(value=str(cfg["project"]))
    output_var = tk.StringVar(value=str(cfg["output"]))
    auto_var = tk.BooleanVar(value=True)

    def build_output_choices(project_path=None):
        r"""输出根候选：当前工程的派生路径优先，其后补齐 raw 下已存在的 _JsonOutput。"""
        src = project_path if project_path is not None else project_var.get()
        choices = []
        derived = derive_output_root(src)
        if derived:
            choices.append(derived)
        for item in detect_output_roots():
            if item not in choices:
                choices.append(item)
        return choices

    def set_project(path, sync_combo=True):
        r"""设置工程根；勾选了自动派生时同步刷新输出根。"""
        path = os.path.normpath(path)
        project_var.set(path)
        if auto_var.get():
            output_var.set(derive_output_root(path))
        if sync_combo:
            values = list(state.get("projects") or [])
            if path and path not in values:
                values.insert(0, path)
            state["projects"] = values
            combo_project["values"] = values
            combo_project.set(path)
        combo_output["values"] = build_output_choices(path)

    # —— 第 0 行：工程根（可浏览） ——
    ttk.Label(form, text="工程根", font=font).grid(row=0, column=0, sticky="w", padx=4, pady=2)
    ttk.Entry(form, textvariable=project_var, width=110, font=font).grid(row=0, column=1, sticky="we", padx=4, pady=2)

    def on_browse_project():
        init = project_var.get().strip().strip('"')
        chosen = filedialog.askdirectory(title="选择 UGC 工程根目录（含 Asset 文件夹）",
                                         initialdir=init if os.path.isdir(init) else DEFAULT_PROJECTS_ROOT,
                                         parent=root)
        if chosen:
            set_project(chosen)
            sink("[提示] 已选择工程根：%s" % project_var.get())

    ttk.Button(form, text="浏览…", command=on_browse_project).grid(row=0, column=2, padx=4, pady=2)

    # —— 第 1 行：工程快速选择（探测 UGCProjects 下含 Asset 的项目） ——
    ttk.Label(form, text="快速选择工程", font=font).grid(row=1, column=0, sticky="w", padx=4, pady=2)
    combo_project = ttk.Combobox(form, values=[], state="readonly", font=font)
    combo_project.grid(row=1, column=1, sticky="we", padx=4, pady=2)

    def on_pick_project(_event=None):
        idx = combo_project.current()
        values = list(combo_project["values"])
        if 0 <= idx < len(values):
            set_project(values[idx], sync_combo=False)
            sink("[提示] 已选择工程根：%s" % project_var.get())

    combo_project.bind("<<ComboboxSelected>>", on_pick_project)
    ttk.Button(form, text="打开工程目录", command=lambda: open_dir(project_var.get(), "工程根")).grid(
        row=1, column=2, padx=4, pady=2)

    # —— 第 2 行：输出根（可浏览） ——
    ttk.Label(form, text="输出根", font=font).grid(row=2, column=0, sticky="w", padx=4, pady=2)
    ttk.Entry(form, textvariable=output_var, width=110, font=font).grid(row=2, column=1, sticky="we", padx=4, pady=2)

    def on_browse_output():
        init = output_var.get().strip().strip('"')
        fallback = KB_RAW_ROOT if os.path.isdir(KB_RAW_ROOT) else "D:\\"
        chosen = filedialog.askdirectory(
            title="选择 JSON 输出根目录（建议 知识库 raw\\<项目名>\\_JsonOutput）",
            initialdir=init if os.path.isdir(init) else fallback, parent=root)
        if chosen:
            set_auto(False)
            output_var.set(os.path.normpath(chosen))
            sink("[提示] 已选择输出根：%s（已关闭随工程派生）" % output_var.get())

    ttk.Button(form, text="浏览…", command=on_browse_output).grid(row=2, column=2, padx=4, pady=2)

    # —— 第 3 行：输出根快速选择 + 自动派生开关 ——
    ttk.Label(form, text="快速选择输出根", font=font).grid(row=3, column=0, sticky="w", padx=4, pady=2)
    combo_output = ttk.Combobox(form, values=[], state="readonly", font=font)
    combo_output.grid(row=3, column=1, sticky="we", padx=4, pady=2)

    def on_pick_output(_event=None):
        idx = combo_output.current()
        values = list(combo_output["values"])
        if 0 <= idx < len(values):
            set_auto(False)
            output_var.set(os.path.normpath(values[idx]))
            sink("[提示] 已选择输出根：%s（已关闭随工程派生）" % output_var.get())

    combo_output.bind("<<ComboboxSelected>>", on_pick_output)

    def set_auto(flag):
        r"""切换「随工程派生」开关，并把状态写进标签文本（clam 主题的勾选符号形似 ✕，易误读）。"""
        auto_var.set(bool(flag))
        chk_auto.configure(text="输出根随工程派生（%s）" % ("已开启" if flag else "已关闭"))

    def on_auto_toggle():
        set_auto(auto_var.get())
        if auto_var.get():
            derived = derive_output_root(project_var.get())
            if derived:
                output_var.set(derived)
                sink("[提示] 输出根随工程派生：%s" % derived)
        else:
            sink("[提示] 已关闭随工程派生，输出根固定为：%s" % output_var.get())

    ttk.Button(form, text="打开输出目录", command=lambda: open_dir(output_var.get(), "输出根", create=True)).grid(
        row=3, column=2, padx=4, pady=2)
    chk_auto = ttk.Checkbutton(form, text="输出根随工程派生（已开启）", variable=auto_var,
                               command=on_auto_toggle)
    chk_auto.grid(row=3, column=3, sticky="w", padx=4, pady=2)

    # —— 第 4~6 行：仍需手填的三个参数 ——
    for row, (label, key) in enumerate([("UAssetGUI", "uassetgui"), ("UE 版本", "ue_version"),
                                        ("轮询秒", "poll_interval")], start=4):
        ttk.Label(form, text=label, font=font).grid(row=row, column=0, sticky="w", padx=4, pady=2)
        var = tk.StringVar(value=str(cfg[key]))
        ttk.Entry(form, textvariable=var, width=110, font=font).grid(row=row, column=1, sticky="we", padx=4, pady=2)
        entries[key] = var
    form.columnconfigure(1, weight=1)

    log_box = tk.Text(root, height=24, font=("Consolas", 9), wrap="none")
    log_box.pack(fill="both", expand=True, padx=8, pady=4)

    def sink(line):
        log_box.insert("end", line + "\n")
        log_box.see("end")

    def refresh_choices():
        r"""刷新两个下拉：工程列表（UGCProjects 下含 Asset 的项目）+ 输出根候选。"""
        projects = detect_projects()
        current = project_var.get().strip().strip('"')
        if current and current not in projects:
            projects.insert(0, current)
        state["projects"] = projects
        combo_project["values"] = projects
        if current:
            combo_project.set(current)
        elif projects:
            set_project(projects[0], sync_combo=False)
        combo_output["values"] = build_output_choices()
        combo_output.set(output_var.get().strip().strip('"'))
        sink("[提示] 快速选择已刷新：工程 %d 项 / 输出根 %d 项（工程集合根=%s，知识库 raw=%s）"
             % (len(projects), len(combo_output["values"]), DEFAULT_PROJECTS_ROOT, KB_RAW_ROOT))

    def open_dir(path, what, create=False):
        p = (path or "").strip().strip('"')
        if not p:
            messagebox.showwarning("未指定目录", "尚未指定%s。" % what, parent=root)
            return
        if not os.path.isdir(p):
            if create and messagebox.askyesno("目录不存在", "%s尚不存在：\n%s\n\n现在创建？" % (what, p), parent=root):
                try:
                    os.makedirs(p, exist_ok=True)
                except OSError as exc:
                    messagebox.showerror("创建失败", str(exc), parent=root)
                    return
            else:
                messagebox.showwarning("路径无效", "%s不存在：\n%s" % (what, p), parent=root)
                return
        os.startfile(p)

    def read_cfg():
        c = dict(cfg)
        c["project"] = project_var.get().strip().strip('"')
        c["output"] = output_var.get().strip().strip('"')
        if auto_var.get():
            c["output"] = derive_output_root(c["project"]) or c["output"]
        for key, var in entries.items():
            if key == "poll_interval":
                try:
                    c[key] = int(var.get())
                except ValueError:
                    c[key] = DEFAULT_POLL_INTERVAL
            else:
                c[key] = var.get().strip().strip('"')
        return c

    def start(mode):
        if state["worker"] and state["worker"].is_alive():
            sink("[提示] 已有任务在运行，请先停止")
            return
        c = read_cfg()
        if not os.path.isdir(c["project"]):
            messagebox.showwarning("工程根无效", "工程根目录不存在，请重新选择：\n%s" % c["project"], parent=root)
            return
        if not c["output"]:
            messagebox.showwarning("未指定输出根", "请选择 JSON 输出根目录（可点「浏览…」或勾选随工程派生）。",
                                   parent=root)
            return
        state["stop"] = threading.Event()

        def job():
            if mode == "convert":
                stats = run_full_conversion(c, sink)
                sink("汇总: " + json.dumps(stats, ensure_ascii=False))
            else:
                run_watch(c, sink, state["stop"])

        state["worker"] = threading.Thread(target=job, daemon=True)
        state["worker"].start()

    buttons = ttk.Frame(root, padding=(8, 0, 8, 8))
    buttons.pack(fill="x")
    ttk.Button(buttons, text="1) 增量全量转换", command=lambda: start("convert")).pack(side="left", padx=4)
    ttk.Button(buttons, text="2) 监视模式", command=lambda: start("watch")).pack(side="left", padx=4)
    ttk.Button(buttons, text="停止", command=lambda: state["stop"].set()).pack(side="left", padx=4)
    ttk.Button(buttons, text="清空日志", command=lambda: log_box.delete("1.0", "end")).pack(side="left", padx=4)
    ttk.Button(buttons, text="刷新列表", command=refresh_choices).pack(side="left", padx=4)
    ttk.Button(buttons, text="环境自检", command=lambda: sink(json.dumps(selftest(read_cfg()), ensure_ascii=False, indent=2))).pack(side="left", padx=4)

    sink("%s v%s 已启动" % (APP_TITLE, APP_VERSION))
    sink("工程根可直接下拉/浏览选择；输出根默认随工程派生为 知识库 raw\\<项目名>\\_JsonOutput，也可手选。")
    refresh_choices()
    root.mainloop()
    return 0


# ---------------- 入口 ----------------
def parse_args(argv=None):
    p = argparse.ArgumentParser(prog="UAssetToJsonConverter", description="绿洲编辑器 .uasset -> JSON 同步工具")
    p.add_argument("--project", default=DEFAULT_PROJECT, help="UGC 工程根目录")
    p.add_argument("--output", default=DEFAULT_OUTPUT, help="JSON 输出根目录（默认知识库）")
    p.add_argument("--uassetgui", default=DEFAULT_UASSETGUI, help="UAssetGUI.exe 路径")
    p.add_argument("--ue-version", dest="ue_version", default=DEFAULT_UE_VERSION, help="UE 版本标记，如 VER_UE4_24")
    p.add_argument("--poll-interval", dest="poll_interval", type=int, default=DEFAULT_POLL_INTERVAL)
    p.add_argument("--mode", choices=["convert", "watch"], help="命令行模式：convert 增量全量转换；watch 监视")
    p.add_argument("--dry-run", dest="dry_run", action="store_true", help="只列计划，不实际转换/删除")
    p.add_argument("--report", help="把本次运行结果 JSON 写到该文件")
    p.add_argument("--selftest", help="环境自检并把结果 JSON 写到该文件")
    return p.parse_args(argv)


def config_from_args(args):
    return {"project": args.project, "output": args.output, "uassetgui": args.uassetgui,
            "ue_version": args.ue_version, "poll_interval": args.poll_interval}


def main(argv=None):
    # --windowed 打包后没有控制台，stdout/stderr 为 None，先兜底避免写日志时崩溃
    if sys.stdout is None:
        sys.stdout = open(os.devnull, "w")
    if sys.stderr is None:
        sys.stderr = open(os.devnull, "w")

    args = parse_args(argv)
    cfg = config_from_args(args)

    if args.selftest:
        result = selftest(cfg)
        with open(args.selftest, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        return 0 if result["ok"] else 3

    if args.mode == "convert":
        stats = run_full_conversion(cfg, None, dry_run=args.dry_run)
        if args.report:
            with open(args.report, "w", encoding="utf-8") as f:
                json.dump({"mode": "convert", "config": cfg, "dry_run": args.dry_run, "stats": stats},
                          f, ensure_ascii=False, indent=2)
        return 0 if stats.get("ok") else 4

    if args.mode == "watch":
        run_watch(cfg, None, threading.Event(), dry_run=args.dry_run)
        return 0

    return launch_gui(cfg)


if __name__ == "__main__":
    sys.exit(main())
