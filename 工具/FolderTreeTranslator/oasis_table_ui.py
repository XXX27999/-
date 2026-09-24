# -*- coding: utf-8 -*-
r"""
绿洲起源 · 表格蓝图数据编辑器（FolderTreeTranslator 子窗口）

功能
    1. 通过 UGCAskQ MCP 连接编辑器，按「资产路径 / 表名 / 磁盘路径」定位 DataTable
    2. 读取行结构与行数据，树表展示，支持关键字筛选
    3. 编辑行：新增 / 修改 / 删除，改动进入「待回写变更」队列
    4. 回写：本地校验 → 写前备份（知识库备份目录）→ PRV 计划 → 执行 → 回读比对 → 报告
    5. 导出 / 导入 JSON（批量修改与离线编辑）

线程约定
    所有 MCP 调用在后台线程执行，结果一律经 _ui_post() 投递回主线程执行，
    避免长时间阻塞导致界面假死。
    注意：Tk 禁止从非主线程调用 after()/控件方法（实测抛
    RuntimeError: main thread is not in main loop），因此后台线程绝不能
    直接 self.after(...)，必须走 _ui_post() 队列。
"""

import json
import os
import queue
import threading
import time
import traceback

import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from oasis_datatable import (BACKUP_ROOT, DataTableService,
                             validate_row_name, validate_value)
from oasis_mcp_client import McpError

FONT = ("Microsoft YaHei UI", 10)
FONT_SMALL = ("Microsoft YaHei UI", 9)

# 分栏尺寸约束（单位：像素）
DATA_MIN_H = 120       # 数据区（行表格）最小高度
TOOL_MIN_H = 300       # 工具区（行编辑 + 变更队列）最小高度
TOOL_MAX_H = 580       # 工具区最大高度，避免把数据区挤没
EDIT_FIELDS_H = 120    # 行编辑字段区默认可视高度，字段更多时内部滚动


def _short(text, limit=90):
    text = str(text).replace("\n", " ")
    return text if len(text) <= limit else text[: limit - 3] + "..."


class TableEditorWindow(tk.Toplevel):
    """表格蓝图数据编辑器窗口。"""

    def __init__(self, master, project_root="", project_name="", initial_path="",
                 logger=None):
        tk.Toplevel.__init__(self, master)
        self.title("表格蓝图数据（MCP 读写）")
        self.geometry("1180x760")
        self.minsize(960, 620)

        self.project_root = project_root or ""
        self.project_name = project_name or (os.path.basename(project_root.rstrip("\\/"))
                                             if project_root else "")
        self.logger = logger or (lambda _m: None)
        self.service = DataTableService(project_name=self.project_name,
                                        project_root=self.project_root,
                                        logger=self._log)
        # 端口探测/握手进度回传界面（多编辑器实例时候选端口很多，避免长时间无反馈）
        try:
            self.service.client.on_progress = self._progress
        except Exception:
            pass
        self.fields = []                 # [{"name","friendly"}]
        self.rows = {}                   # 行名 -> {字段: 值}
        self.pending = {"upsert": {}, "delete": []}
        self.busy = False
        self._sash_inited = False          # 初始分栏比例是否已完成
        self._sash_user_moved = False      # 用户是否手动拖过 sash（拖过就不再自动收窄）
        self._press_on_sash = False
        self._press_sash_y = 0
        self._recheck_scheduled = False   # 是否已排定 sash 夹紧复查
        self._bars_map = {}                # 各内容区的 (横向条, 纵向条)，供滚动状态自检
        self._edit_frame = None      # 行编辑容器
        self._pend_frame = None      # 变更队列容器
        self._status_label = None    # 窗口底部状态栏

        self._ui_queue = queue.Queue()   # 后台线程 -> 主线程的界面更新队列
        self._last_progress = ""         # 最近一次 MCP 进度文本
        self._task_seq = 0               # 任务代次，用于丢弃过期回调

        self.path_var = tk.StringVar(value=initial_path or "")
        self.filter_var = tk.StringVar()
        self.status_var = tk.StringVar(value="未连接：点击「连接编辑器」后读取表格数据。")

        self._build_ui()
        self._poll_ui()                  # 启动主线程界面更新轮询
        self._fit_min_height()           # 最小高度跟随内容，防止缩到装不下
        self._init_sash()                # 先尝试一次（此时高度可能还是 1）
        self.after_idle(self._init_sash)  # 初始分栏比例：工具区按自然高度
        # 窗口映射后 Tk 会按 pane 的 -stretch / 请求高度自行重算一次分配，
        # 可能把 sash 推回不合适的位置；而 sash_place 不改变 paned 自身几何，
        # 不会再触发 <Configure>，所以前几帧主动复查，把 sash 拉回合法区间。
        for _delay in (80, 200, 400, 700):
            self.after(_delay, self._clamp_sash)
        if initial_path:
            self.after(150, self.on_read)
        else:
            self.after(150, self.on_connect)

    def _fit_min_height(self):
        """把窗口最小高度设为「内容自然高度」，避免用户缩到内容装不下。

        装不下时 Tk 会把底部状态栏挤出窗口（表现为状态栏消失/被裁掉），
        所以这里按构建后的请求高度兜底，而不是写死一个数字。
        """
        try:
            self.update_idletasks()
            req = self.winfo_reqheight()
        except Exception:
            return
        if not req or req <= 0:
            return
        try:
            cur_w = self.minsize()[0] or 960
            self.minsize(cur_w, max(560, min(req, 820)))
        except Exception:
            pass

    # ---------------- 日志 / 状态 / 线程安全派发 ----------------
    def _ui_post(self, fn):
        """把界面更新投递到主线程执行（线程安全）。

        Tk 不允许非主线程调用 after()/控件方法，工作线程直接 after 会抛
        RuntimeError 并静默打死线程；这里统一走队列，由 _poll_ui 在主线程消费。
        """
        if threading.current_thread() is threading.main_thread():
            try:
                fn()
            except Exception:
                pass
            return
        try:
            self._ui_queue.put(fn)
        except Exception:
            pass

    def _poll_ui(self):
        """主线程轮询：消费后台线程投递进来的界面更新。"""
        while True:
            try:
                fn = self._ui_queue.get_nowait()
            except queue.Empty:
                break
            except Exception:
                break
            try:
                fn()
            except Exception:
                pass
        try:
            if self.winfo_exists():
                self.after(30, self._poll_ui)
        except Exception:
            pass

    def _log(self, msg):
        """后台线程安全的状态更新。"""
        try:
            self.logger(str(msg))
        except Exception:
            pass
        self._ui_post(lambda: self.status_var.set(_short(msg)))

    def _set_status(self, msg):
        self._ui_post(lambda: self.status_var.set(_short(msg)))

    def _progress(self, msg):
        """MCP 客户端的进度回调（工作线程）：记下最新步骤，状态栏同步显示。"""
        self._last_progress = str(msg)
        self._set_status(msg)

    def _busy(self, flag, text=""):
        # self.busy 必须同步置位：_tick() 在 _run_async 里是同步调用的，
        # 若只放在派发回调里置位，计时器第一拍就会因 busy 仍为 False 而自杀。
        self.busy = flag

        def apply():
            state = "disabled" if flag else "normal"
            for btn in self.action_buttons:
                try:
                    btn.configure(state=state)
                except Exception:
                    pass
            if text:
                self.status_var.set(_short(text))
        self._ui_post(apply)

    # ---------------- 界面 ----------------
    def _build_ui(self):
        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass
        style.configure("TLabel", font=FONT)
        style.configure("TButton", font=FONT, padding=(8, 3))
        style.configure("Treeview", font=FONT_SMALL, rowheight=23)
        style.configure("Treeview.Heading", font=FONT_SMALL)

        top = ttk.Frame(self, padding=(12, 10, 12, 4))
        top.pack(fill="x")

        ttk.Label(top, text="表格：").grid(row=0, column=0, sticky="w")
        self.path_entry = ttk.Entry(top, textvariable=self.path_var, font=("Consolas", 10))
        self.path_entry.grid(row=0, column=1, sticky="ew", padx=(0, 6))
        top.columnconfigure(1, weight=1)

        self.btn_connect = ttk.Button(top, text="连接编辑器", command=self.on_connect)
        self.btn_pick = ttk.Button(top, text="选择表格…", command=self.on_pick_table)
        self.btn_read = ttk.Button(top, text="读取", command=self.on_read)
        for i, btn in enumerate((self.btn_connect, self.btn_pick, self.btn_read)):
            btn.grid(row=0, column=2 + i, padx=2)

        ttk.Label(top, text="提示：可填资产路径 /IslandAuctionKing/Asset/...、磁盘路径或表名（如 UIConfigTable）。"
                 ).grid(row=1, column=1, columnspan=4, sticky="w", pady=(4, 0))

        # ---- 主体分栏：上=数据区，下=工具区，中间 sash 可上下拖拽 ----
        self.paned = tk.PanedWindow(self, orient="vertical", sashrelief="raised",
                                    sashwidth=7, opaqueresize=True,
                                    # height 是「请求高度」：只用来允许窗口变小时分栏跟着收缩，
                                    # 有富余空间时 pack(expand=True) 仍会把分栏撑满。
                                    # 不设的话分栏按窗格自然高度请求，窗口缩小时 pack 压不动它，
                                    # 多出来的高度会把底部状态栏顶出窗口。
                                    height=DATA_MIN_H + TOOL_MIN_H)
        self.paned.pack(fill="both", expand=True, padx=12, pady=(4, 0))

        # ---- 数据区 ----
        # 主体用 Tk 垂直 PanedWindow：sash 给工具区提供上下拖拽手柄；
        # 最小高度由 minsize 保证，最大高度由 _clamp_sash 兜住（Tk 的 pane 没有 -maxsize）。
        self.data_frame = ttk.Frame(self.paned)
        self.paned.add(self.data_frame, minsize=DATA_MIN_H)
        self.data_frame.rowconfigure(1, weight=1)
        self.data_frame.columnconfigure(0, weight=1)

        filter_bar = ttk.Frame(self.data_frame)
        filter_bar.grid(row=0, column=0, sticky="ew")
        ttk.Label(filter_bar, text="筛选：").pack(side="left")
        filt = ttk.Entry(filter_bar, textvariable=self.filter_var, width=28, font=FONT)
        filt.pack(side="left", padx=(0, 8))
        filt.bind("<KeyRelease>", lambda _e: self.render_rows())

        self.tree_frame = ttk.Frame(self.data_frame)
        self.tree_frame.grid(row=1, column=0, sticky="nsew", pady=(6, 0))
        self.tree_frame.rowconfigure(0, weight=1)
        self.tree_frame.columnconfigure(0, weight=1)
        # height 只决定「请求高度」：pane 有富余时仍会填满，窗口变小时才允许收缩，
        # 避免表格把分栏撑得过大、把底部状态栏挤出窗口。
        self.tree = ttk.Treeview(self.tree_frame, show="tree headings",
                                 selectmode="browse", height=3)
        self.tree.grid(row=0, column=0, sticky="nsew")
        self.tree.bind("<<TreeviewSelect>>", self.on_select_row)
        # 横/纵滚动条：内容超出才出现，不足时自动隐藏
        self._refresh_tree_bars = self._attach_scrollbars(self.tree_frame, self.tree, "tree")

        # ---- 工具区（编辑 + 变更队列，可随 sash 上下拉伸） ----
        self.tool_frame = ttk.Frame(self.paned)
        self.paned.add(self.tool_frame, minsize=TOOL_MIN_H)
        self.paned.bind("<Configure>", self._clamp_sash, add="+")
        self.paned.bind("<ButtonPress-1>", self._on_sash_press, add="+")
        self.paned.bind("<ButtonRelease-1>", self._on_sash_release, add="+")
        self.tool_frame.rowconfigure(0, weight=0)   # 行编辑：按内容取高
        self.tool_frame.rowconfigure(1, weight=1)   # 变更队列：吃掉剩余空间
        self.tool_frame.columnconfigure(0, weight=1)

        edit = ttk.LabelFrame(self.tool_frame, text="行编辑（改动先进变更队列，点「回写编辑器」才写入）",
                              padding=(12, 6, 12, 8))
        edit.grid(row=0, column=0, sticky="ew", pady=(0, 6))
        self._edit_frame = edit
        edit.columnconfigure(1, weight=1)
        edit.rowconfigure(1, weight=1)

        ttk.Label(edit, text="行名：").grid(row=0, column=0, sticky="w")
        self.row_name_var = tk.StringVar()
        self.row_name_entry = ttk.Entry(edit, textvariable=self.row_name_var, width=42,
                                        font=("Consolas", 10))
        self.row_name_entry.grid(row=0, column=1, sticky="ew")

        self.value_vars = {}
        self.value_widgets = {}
        # 字段区放进可滚动容器：字段多/名称长时内部滚动，不再溢出遮挡下方按钮
        self.edit_fields_outer, self.edit_fields_frame, self._refresh_edit_bars = \
            self._make_scrolled_frame(edit, height=EDIT_FIELDS_H, key="edit")
        self.edit_fields_outer.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=(6, 0))

        btn_bar = ttk.Frame(edit)
        btn_bar.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(8, 0))
        self.btn_apply = ttk.Button(btn_bar, text="加入/更新变更", command=self.on_apply_edit)
        self.btn_delete = ttk.Button(btn_bar, text="删除该行", command=self.on_delete_row)
        self.btn_clear = ttk.Button(btn_bar, text="清空变更", command=self.on_clear_pending)
        self.btn_write = ttk.Button(btn_bar, text="回写编辑器", command=self.on_write)
        self.btn_export = ttk.Button(btn_bar, text="导出 JSON 备份", command=self.on_export)
        self.btn_import = ttk.Button(btn_bar, text="从 JSON 导入", command=self.on_import)
        self.btn_abort = ttk.Button(btn_bar, text="中止", command=self.on_abort)
        for btn in (self.btn_apply, self.btn_delete, self.btn_clear, self.btn_write,
                    self.btn_export, self.btn_import, self.btn_abort):
            btn.pack(side="left", padx=3)

        # ---- 变更队列 ----
        pend = ttk.LabelFrame(self.tool_frame, text="待回写变更", padding=(12, 4, 12, 6))
        pend.grid(row=1, column=0, sticky="nsew")
        self._pend_frame = pend
        pend.rowconfigure(0, weight=1)
        pend.columnconfigure(0, weight=1)
        self.pending_tree = ttk.Treeview(pend, columns=("op", "detail"),
                                         show="headings", height=3)
        self.pending_tree.grid(row=0, column=0, sticky="nsew")
        self.pending_tree.heading("op", text="操作")
        self.pending_tree.heading("detail", text="内容")
        # stretch=False + 固定列宽：列不会被压扁，宽度超视口时横向滚动条出现
        self.pending_tree.column("op", width=80, anchor="w", stretch=False)
        self.pending_tree.column("detail", width=1200, anchor="w", stretch=False)
        self._refresh_pend_bars = self._attach_scrollbars(pend, self.pending_tree, "pend")

        # ---- 状态栏（窗口最底部，不参与分栏，永远可见） ----
        self._status_label = ttk.Label(self, textvariable=self.status_var, font=FONT_SMALL,
                                       foreground="#4a5560", anchor="w",
                                       padding=(12, 6, 12, 8))
        self._status_label.pack(fill="x")

        self.action_buttons = [self.btn_connect, self.btn_pick, self.btn_read,
                               self.btn_apply, self.btn_delete, self.btn_clear,
                               self.btn_write, self.btn_export, self.btn_import]

    # ---------------- 滚动容器 ----------------
    def _attach_scrollbars(self, parent, widget, key="", row=0, column=0):
        """给 widget 挂横/纵滚动条，并按内容自动显隐；返回手动刷新函数。"""
        vsb = ttk.Scrollbar(parent, orient="vertical", command=widget.yview)
        hsb = ttk.Scrollbar(parent, orient="horizontal", command=widget.xview)
        widget.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        vsb.grid(row=row, column=column + 1, sticky="ns")
        hsb.grid(row=row + 1, column=column, sticky="ew")
        vsb.grid_remove()
        hsb.grid_remove()
        if key:
            self._bars_map[key] = (hsb, vsb)
        refresh = self._auto_scrollbars(widget, hsb, vsb, row, column)
        parent.bind("<Configure>", refresh, add="+")
        return refresh

    def _init_sash(self):
        """初始 sash 位置：工具区按其自然高度，剩余空间全给数据区。"""
        try:
            total = self.paned.winfo_height()
            if total <= 1:
                return False
            sash_w = int(self.paned.cget("sashwidth"))
            natural = self.tool_frame.winfo_reqheight() or TOOL_MIN_H
            upper = max(TOOL_MIN_H, total - DATA_MIN_H - sash_w)
            want = max(TOOL_MIN_H, min(TOOL_MAX_H, natural, upper))
            self.paned.sash_place(0, 0, int(total - want - sash_w))
            return True
        except Exception:
            return False

    def _clamp_sash(self, _event=None):
        """把工具区高度夹在 [TOOL_MIN_H, TOOL_MAX_H]，并保住数据区最小高度。

        Tk 的 panedwindow pane 只支持 -minsize，没有 -maxsize，所以上限在这里兜：
        拖拽或窗口缩放后重算，越界就把 sash 拉回合法位置。
        """
        if getattr(self, "_clamping", False):
            return
        try:
            total = self.paned.winfo_height()
            if total <= 1:
                return
            # 首帧高度常为 1（after_idle 太早），所以等第一次真正布局时再定初始位置
            if not getattr(self, "_sash_inited", False):
                if self._init_sash():
                    self._sash_inited = True
            sash_w = int(self.paned.cget("sashwidth"))
            # 注意：tkinter 的 PanedWindow 没有 sashpos()，要用 sash_coord/sash_place
            data_h = int(self.paned.sash_coord(0)[1])
            tool_h = total - data_h - sash_w
            # 上限：用户拖过 sash 就用 TOOL_MAX_H；没拖过就只给到「自然高度」，
            # 这样窗口变大时多出来的空间归数据区，而不是被工具区吃掉。
            limit = TOOL_MAX_H
            if not self._sash_user_moved:
                natural = self.tool_frame.winfo_reqheight() or TOOL_MIN_H
                limit = max(TOOL_MIN_H, min(TOOL_MAX_H, natural))
            max_tool = max(TOOL_MIN_H, min(limit, total - DATA_MIN_H - sash_w))
            want = min(max(tool_h, TOOL_MIN_H), max_tool)
            if abs(want - tool_h) <= 1:
                return
            self._clamping = True
            try:
                self.paned.sash_place(0, 0, int(total - want - sash_w))
            finally:
                self._clamping = False
            # 缩放后 Tk 会在 <Configure> 之后再自行重算一次 pane 分配，把 sash 推回去；
            # 而 sash_place 不改变 paned 自身几何、不会触发新的 <Configure>，
            # 所以主动安排一次复查，直到 sash 稳定在合法区间（稳定后上面就 return 了）。
            if not getattr(self, "_recheck_scheduled", False):
                self._recheck_scheduled = True
                try:
                    self.after(120, self._recheck_sash)
                except Exception:
                    self._recheck_scheduled = False
        except Exception:
            self._clamping = False

    def _recheck_sash(self):
        """sash 夹紧后的复查回调，收敛后自然停止。"""
        self._recheck_scheduled = False
        try:
            if self.winfo_exists():
                self._clamp_sash()
        except Exception:
            pass

    # ---- 识别用户是否手动拖过 sash：拖过之后不再自动收窄工具区 ----
    def _on_sash_press(self, event):
        try:
            sash_y = int(self.paned.sash_coord(0)[1])
            sw = int(self.paned.cget("sashwidth"))
            self._press_on_sash = abs(event.y - sash_y) <= max(4, sw)
            self._press_sash_y = sash_y
        except Exception:
            self._press_on_sash = False

    def _on_sash_release(self, _event=None):
        try:
            if self._press_on_sash and \
                    int(self.paned.sash_coord(0)[1]) != self._press_sash_y:
                self._sash_user_moved = True
        except Exception:
            pass

    def _tree_scrollbars(self):
        """数据区滚动条 (横向, 纵向)。"""
        return self._bars_map.get("tree", (None, None))

    def _edit_scrollbars(self):
        """行编辑字段区滚动条 (横向, 纵向)。"""
        return self._bars_map.get("edit", (None, None))

    def _pend_scrollbars(self):
        """变更队列滚动条 (横向, 纵向)。"""
        return self._bars_map.get("pend", (None, None))

    @staticmethod
    def _auto_scrollbars(widget, hsb, vsb, row=0, column=0):
        """内容放不下就显示滚动条，放得下就隐藏（after_idle 合并，避免布局递归）。"""

        state = {"h": False, "v": False, "sched": False}

        def apply():
            state["sched"] = False
            try:
                lo, hi = widget.xview()
                need_h = (hi - lo) < 0.999
            except Exception:
                need_h = False
            try:
                lo2, hi2 = widget.yview()
                need_v = (hi2 - lo2) < 0.999
            except Exception:
                need_v = False
            if need_h != state["h"]:
                state["h"] = need_h
                if need_h:
                    hsb.grid(row=row + 1, column=column, sticky="ew")
                else:
                    hsb.grid_remove()
            if need_v != state["v"]:
                state["v"] = need_v
                if need_v:
                    vsb.grid(row=row, column=column + 1, sticky="ns")
                else:
                    vsb.grid_remove()

        def refresh(_event=None):
            if state["sched"]:
                return
            state["sched"] = True
            try:
                widget.after_idle(apply)
            except Exception:
                state["sched"] = False
        return refresh

    def _make_scrolled_frame(self, parent, height=EDIT_FIELDS_H, key=""):
        """建一个可横/纵滚动的内容容器，返回 (外层, 内层, 刷新函数)。

        内层放真正的内容；容器不够大时自动出滚动条，内容不会溢出到别的区域。
        """
        outer = ttk.Frame(parent)
        outer.rowconfigure(0, weight=1)
        outer.columnconfigure(0, weight=1)
        canvas = tk.Canvas(outer, height=height, highlightthickness=0, borderwidth=0)
        canvas.grid(row=0, column=0, sticky="nsew")
        inner = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=inner, anchor="nw")
        refresh = [None]

        def on_inner(_event=None):
            try:
                canvas.configure(scrollregion=canvas.bbox("all"))
            except Exception:
                pass
            if refresh[0]:
                refresh[0]()

        inner.bind("<Configure>", on_inner)
        refresh[0] = self._attach_scrollbars(outer, canvas, key=key)
        return outer, inner, refresh[0]

    def _rebuild_edit_fields(self):
        for widget in self.value_widgets.values():
            try:
                widget.destroy()
            except Exception:
                pass
        self.value_vars = {}
        self.value_widgets = {}
        for idx, field in enumerate(self.fields):
            name = field["name"]
            label = field.get("friendly") or name
            var = tk.StringVar()
            ttk.Label(self.edit_fields_frame, text="%s(%s)：" % (label, name)).grid(
                row=idx // 2, column=(idx % 2) * 2, sticky="w", padx=(0, 4), pady=2)
            entry = ttk.Entry(self.edit_fields_frame, textvariable=var, width=46,
                              font=("Consolas", 9))
            entry.grid(row=idx // 2, column=(idx % 2) * 2 + 1, sticky="w", pady=2)
            self.value_vars[name] = var
            self.value_widgets[name] = entry
        # 字段数量变化会改变内容尺寸，重算滚动条显隐
        if getattr(self, "_refresh_edit_bars", None):
            self._refresh_edit_bars()

    def _rebuild_columns(self):
        columns = [f["name"] for f in self.fields]
        self.tree.configure(columns=columns)
        self.tree.heading("#0", text="行名", anchor="w")
        self.tree.column("#0", width=300, stretch=False)
        for name in columns:
            self.tree.heading(name, text=name, anchor="w")
            # stretch=False：列保持设定宽度，总宽超视口时横向滚动条自动出现
            self.tree.column(name, width=190, stretch=False)
        if getattr(self, "_refresh_tree_bars", None):
            self._refresh_tree_bars()

    # ---------------- 异步执行 ----------------
    def _run_async(self, func, on_done=None, busy_text="", ticker=True):
        """在后台线程执行，并在等待期间持续刷新状态栏秒数。

        背景：MCP 调用受编辑器状态影响（PIE 启动、编译、保存都会排队），
        只显示一句「正在…」会让人以为界面卡死；这里给出已等待秒数与中止入口。

        任务代次（_task_seq）：每次发起任务自增；回调只在代次一致时生效，
        这样「中止」或新任务发起后，在途的旧回调会被丢弃，不会中途弹错框。
        """
        self._task_seq = getattr(self, "_task_seq", 0) + 1
        seq = self._task_seq
        self._task_start = time.time()
        self._ticker_id = None
        self._last_progress = ""

        def worker():
            try:
                result = func()
            except Exception as exc:
                result = {"__error__": exc, "__trace__": traceback.format_exc()}

            def finish():
                if seq != self._task_seq:
                    return  # 已被「中止」或新任务取代，丢弃本次结果
                self._stop_ticker()
                # 统一兜底复位：任何 done 回调漏写 _busy(False) 都会让按钮永久禁用、
                # 界面看起来「卡死」，所以复位必须由这里保证，不能只靠各回调自觉。
                self._busy(False)
                if on_done:
                    on_done(result)
            # 关键：必须经 _ui_post 回主线程，工作线程直接 after 会抛
            # RuntimeError('main thread is not in main loop') 并静默结束线程。
            self._ui_post(finish)

        self._busy(True, busy_text)
        threading.Thread(target=worker, daemon=True).start()
        if ticker:
            self._ticker_base = busy_text or "处理中"
            self._tick()

    def _tick(self):
        """每秒刷新等待时长；任务结束由 _stop_ticker 取消。"""
        if not self.busy:
            return
        secs = int(time.time() - getattr(self, "_task_start", time.time()))
        base = getattr(self, "_last_progress", "") or self._ticker_base
        try:
            self.status_var.set(_short("%s ｜ 已等待 %d 秒，编辑器繁忙（PIE 启动 / 编译 / 保存）"
                                       "时会排队，长时间无结果可点「中止」" % (base, secs)))
        except Exception:
            pass
        self._ticker_id = self.after(1000, self._tick)

    def _stop_ticker(self):
        tid = getattr(self, "_ticker_id", None)
        if tid:
            try:
                self.after_cancel(tid)
            except Exception:
                pass
            self._ticker_id = None

    def on_abort(self):
        """中止当前 MCP 操作：断开 SSE 让阻塞的调用返回，并立即恢复界面。"""
        if not self.busy:
            self._set_status("当前没有进行中的操作；「中止」只用于打断正在等待的 MCP 调用。")
            return
        # 代次自增：在途任务的回调随后会被判定为过期直接丢弃
        self._task_seq = getattr(self, "_task_seq", 0) + 1
        try:
            self.service.client.close()
        except Exception:
            pass
        self._stop_ticker()
        self._busy(False)
        self._set_status("已中止：连接已断开。重新点「连接编辑器」后可继续"
                         "（编辑器繁忙时建议等 PIE 启动完成再试）。")

    def _show_error(self, title, exc):
        detail = str(exc)
        self._log("[错误] %s：%s" % (title, detail))
        try:
            messagebox.showerror(title, detail[:1500], parent=self)
        except Exception:
            pass

    # ---------------- 动作：连接 / 定位 / 读取 ----------------
    def on_connect(self):
        def task():
            self.service.ensure_connected()
            return True

        def done(result):
            self._busy(False)
            if isinstance(result, dict) and "__error__" in result:
                self._show_error("连接失败", result["__error__"])
                self._set_status("连接失败：%s" % result["__error__"])
                return
            self._set_status("已连接 UGCAskQ MCP（端口 %s）" % self.service.client.port)
            self.after(50, self._check_pie_state)

        self._run_async(task, done, "正在连接编辑器 MCP…")

    def _check_pie_state(self):
        """连接后提示 PIE 状态：PIE 运行中改表不会生效，需要停 PIE 后重新 PIE。"""

        def task():
            res = self.service.client.call_tool("ue_read", {"queries": ["ctx:"]}, timeout=15)
            return (res.get("text") or "")

        def done(result):
            if isinstance(result, dict) and "__error__" in result:
                return
            text = result or ""
            playing = '"is_debug_playing": true' in text or "is_debug_playing\\\\\": true" in text
            if playing:
                self._set_status("注意：编辑器正在 PIE 调试中，表格改动不会热生效，需停止 PIE 后重新 PIE。")

        self._run_async(task, done, "正在检查编辑器状态…")

    def on_pick_table(self):
        def task():
            return self.service.list_tables()

        def done(result):
            self._busy(False)
            if isinstance(result, dict) and "__error__" in result:
                self._show_error("列举表格失败", result["__error__"])
                return
            tables = result or []
            if not tables:
                messagebox.showinfo("无表格", "未在 Asset/Data 下发现 DataTable 资产。", parent=self)
                return
            TablePicker(self, tables)

        self._run_async(task, done, "正在列举项目表格…")

    def on_read(self):
        raw = self.path_var.get().strip()
        if not raw:
            messagebox.showwarning("未指定表格", "请填写表格资产路径或表名。", parent=self)
            return

        def task():
            resolved = self.service.resolve(raw)
            data = self.service.read_table(resolved["path"], limit=0)
            return {"resolved": resolved, "data": data}

        def done(result):
            self._busy(False)
            if isinstance(result, dict) and "__error__" in result:
                self._show_error("读取失败", result["__error__"])
                self._set_status("读取失败：%s" % result["__error__"])
                return
            resolved, data = result["resolved"], result["data"]
            self.path_var.set(resolved["path"])
            self.fields = data.get("fields") or []
            self.rows = data.get("rows") or {}
            self._rebuild_columns()
            self._rebuild_edit_fields()
            self.render_rows()
            msg = "已读取 %s：%d 行 / %d 列（定位方式：%s）" % (
                resolved["path"], len(self.rows), len(self.fields), resolved.get("source", "?"))
            if data.get("truncated"):
                msg += " · 结果被截断，导出 JSON 可看全量"
            self._set_status(msg)

        self._run_async(task, done, "正在读取表格数据…")

    # ---------------- 动作：渲染 / 选中 ----------------
    def render_rows(self):
        try:
            self.tree.delete(*self.tree.get_children())
        except Exception:
            return
        keyword = self.filter_var.get().strip().lower()
        for row_name in sorted(self.rows.keys()):
            values = self.rows.get(row_name) or {}
            if keyword:
                blob = (row_name + " " + " ".join(str(v) for v in values.values())).lower()
                if keyword not in blob:
                    continue
            self.tree.insert("", "end", iid=row_name, text=row_name,
                             values=[self._fmt(values.get(f["name"])) for f in self.fields])
        # 行数变化后重算滚动条（行多到超出视口时才显示纵向条）
        if getattr(self, "_refresh_tree_bars", None):
            self._refresh_tree_bars()

    @staticmethod
    def _fmt(value):
        if value is None:
            return ""
        if isinstance(value, bool):
            return "true" if value else "false"
        return str(value)

    def on_select_row(self, _event=None):
        sel = self.tree.selection()
        if not sel:
            return
        row_name = sel[0]
        values = self.rows.get(row_name) or {}
        self.row_name_var.set(row_name)
        for field in self.fields:
            var = self.value_vars.get(field["name"])
            if var is not None:
                var.set(self._fmt(values.get(field["name"])))

    # ---------------- 动作：编辑变更 ----------------
    def on_apply_edit(self):
        row_name = self.row_name_var.get().strip()
        ok, msg = validate_row_name(row_name)
        if not ok:
            messagebox.showwarning("行名不合法", msg, parent=self)
            return
        if not self.fields:
            messagebox.showwarning("未读取表格", "请先读取表格再编辑。", parent=self)
            return

        fields = {}
        for field in self.fields:
            var = self.value_vars.get(field["name"])
            fields[field["name"]] = var.get() if var is not None else ""

        vtype = fields.get("ValueType")
        if vtype is not None and "Value" in fields:
            ok, msg = validate_value(vtype, fields["Value"])
            if not ok:
                messagebox.showwarning("值校验不通过", msg, parent=self)
                return

        merged = dict(self.pending["upsert"].get(row_name) or {})
        merged.update(fields)
        self.pending["upsert"][row_name] = merged
        if row_name in self.pending["delete"]:
            self.pending["delete"].remove(row_name)
        self.render_pending()
        self._set_status("已加入变更：%s（尚未写入编辑器）" % row_name)

    def on_delete_row(self):
        row_name = self.row_name_var.get().strip()
        if not row_name:
            messagebox.showwarning("未选择行", "请先在上方选择或填写要删除的行名。", parent=self)
            return
        if row_name in self.pending["upsert"]:
            del self.pending["upsert"][row_name]
        if row_name not in self.pending["delete"]:
            self.pending["delete"].append(row_name)
        self.render_pending()
        self._set_status("已加入删除：%s（尚未写入编辑器）" % row_name)

    def on_clear_pending(self):
        self.pending = {"upsert": {}, "delete": []}
        self.render_pending()
        self._set_status("已清空变更队列")

    def render_pending(self):
        try:
            self.pending_tree.delete(*self.pending_tree.get_children())
        except Exception:
            return
        for row_name, fields in self.pending["upsert"].items():
            detail = "；".join("%s=%s" % (k, _short(v, 40)) for k, v in fields.items())
            op = "新增" if row_name not in self.rows else "修改"
            self.pending_tree.insert("", "end", values=(op, "%s → %s" % (row_name, detail)))
        for row_name in self.pending["delete"]:
            self.pending_tree.insert("", "end", values=("删除", row_name))
        # 变更条目变化后重算滚动条
        if getattr(self, "_refresh_pend_bars", None):
            self._refresh_pend_bars()

    # ---------------- 动作：回写 ----------------
    def on_write(self):
        if not self.pending["upsert"] and not self.pending["delete"]:
            messagebox.showinfo("无变更", "变更队列为空。", parent=self)
            return
        path = self.path_var.get().strip()
        if not path:
            messagebox.showwarning("未指定表格", "请先读取表格。", parent=self)
            return

        confirm = "即将回写 %s：\n新增/修改 %d 行，删除 %d 行。\n\n写入前会自动备份到知识库备份目录，写入后回读校验。\n确定继续？" % (
            path, len(self.pending["upsert"]), len(self.pending["delete"]))
        if not messagebox.askyesno("确认回写", confirm, parent=self):
            return

        changes = {"upsert": dict(self.pending["upsert"]), "delete": list(self.pending["delete"])}

        def task():
            return self.service.write_table(path, changes, do_backup=True)

        def done(result):
            self._busy(False)
            if isinstance(result, dict) and "__error__" in result:
                self._show_error("回写失败", result["__error__"])
                return
            if not result.get("ok"):
                parts = []
                if result.get("errors"):
                    parts.append("校验/执行错误：\n" + "\n".join(
                        "· %s：%s" % (a, b) for a, b in result["errors"]))
                if result.get("diffs"):
                    parts.append("回读差异：\n" + "\n".join(
                        "· %s：%s" % (a, b) for a, b in result["diffs"]))
                messagebox.showerror("回写未完成", "\n\n".join(parts) or "未知原因", parent=self)
                self._set_status("回写未通过：%s" % result.get("message", ""))
                return

            self.pending = {"upsert": {}, "delete": []}
            self.render_pending()
            notes = []
            if result.get("backup"):
                notes.append("备份：%s" % result["backup"])
            if result.get("notes"):
                notes.extend("· %s：%s" % (a, b) for a, b in result["notes"])
            if result.get("warnings"):
                notes.extend("· 提示 %s：%s" % (a, b) for a, b in result["warnings"])
            messagebox.showinfo("回写成功",
                                "%s\n\n%s\n\n注意：配置表改动需重新 PIE 生效。"
                                % (result.get("message", ""), "\n".join(notes)), parent=self)
            self._set_status("回写成功：%s" % result.get("message", ""))
            self.on_read()

        self._run_async(task, done, "正在回写并回读校验…")

    # ---------------- 动作：导出 / 导入 ----------------
    def on_export(self):
        path = self.path_var.get().strip()
        if not path:
            messagebox.showwarning("未指定表格", "请先读取表格。", parent=self)
            return
        target = filedialog.askdirectory(
            title="选择备份目录（默认知识库备份目录）",
            initialdir=os.path.join(BACKUP_ROOT, self.project_name or ""), parent=self)
        if not target:
            return

        def task():
            return self.service.export_table(path, target)

        def done(result):
            self._busy(False)
            if isinstance(result, dict) and "__error__" in result:
                self._show_error("导出失败", result["__error__"])
                return
            self._set_status("已导出：%s" % result)
            messagebox.showinfo("导出成功", "已导出：\n%s" % result, parent=self)

        self._run_async(task, done, "正在导出 JSON 备份…")

    def on_import(self):
        path = self.path_var.get().strip()
        if not path:
            messagebox.showwarning("未指定表格", "请先读取或填写表格路径。", parent=self)
            return
        src = filedialog.askopenfilename(
            title="选择要导入的表格 JSON", filetypes=[("JSON 文件", "*.json"), ("所有文件", "*.*")],
            parent=self)
        if not src:
            return
        try:
            with open(src, "r", encoding="utf-8") as fp:
                payload = json.load(fp)
        except Exception as exc:
            messagebox.showerror("读取失败", "无法解析 JSON：%s" % exc, parent=self)
            return

        rows = payload.get("rows") if isinstance(payload, dict) else None
        if not isinstance(rows, dict) or not rows:
            messagebox.showerror("格式错误",
                                 "JSON 需包含 {\"rows\": {行名: {字段: 值}}} 结构。", parent=self)
            return

        changes = {"upsert": {}, "delete": []}
        for row_name, fields in rows.items():
            if not isinstance(fields, dict):
                continue
            ok, msg = validate_row_name(row_name)
            if not ok:
                messagebox.showerror("行名不合法", "%s：%s" % (row_name, msg), parent=self)
                return
            vtype, value = fields.get("ValueType"), fields.get("Value")
            if vtype is not None and value is not None:
                ok, msg = validate_value(vtype, value)
                if not ok:
                    messagebox.showerror("值校验不通过", "%s：%s" % (row_name, msg), parent=self)
                    return
            changes["upsert"][row_name] = {str(k): ("" if v is None else str(v))
                                           for k, v in fields.items()}

        if not messagebox.askyesno("确认导入",
                                   "将把 %d 行写入 %s（已存在则覆盖字段）。\n继续？"
                                   % (len(changes["upsert"]), path), parent=self):
            return

        def task():
            return self.service.write_table(path, changes, do_backup=True)

        def done(result):
            self._busy(False)
            if isinstance(result, dict) and "__error__" in result:
                self._show_error("导入失败", result["__error__"])
                return
            if not result.get("ok"):
                parts = []
                if result.get("errors"):
                    parts.append("\n".join("· %s：%s" % (a, b) for a, b in result["errors"]))
                if result.get("diffs"):
                    parts.append("\n".join("· %s：%s" % (a, b) for a, b in result["diffs"]))
                messagebox.showerror("导入未完成", "\n".join(parts) or "未知原因", parent=self)
                return
            messagebox.showinfo("导入成功",
                                "%s\n备份：%s\n\n配置表改动需重新 PIE 生效。"
                                % (result.get("message", ""), result.get("backup", "无")),
                                parent=self)
            self.on_read()

        self._run_async(task, done, "正在导入并回写…")


class TablePicker(tk.Toplevel):
    """表格选择对话框。"""

    def __init__(self, master, tables):
        tk.Toplevel.__init__(self, master)
        self.title("选择表格")
        self.geometry("760x420")
        self.tables = tables
        self.master_window = master

        frame = ttk.Frame(self, padding=10)
        frame.pack(fill="both", expand=True)
        self.tree = ttk.Treeview(frame, columns=("cls", "path"), show="headings")
        self.tree.heading("cls", text="类型")
        self.tree.heading("path", text="资产路径")
        self.tree.column("cls", width=120, anchor="w")
        self.tree.column("path", width=580, anchor="w")
        self.tree.pack(fill="both", expand=True)
        for item in tables:
            self.tree.insert("", "end", values=(item.get("asset_class", ""),
                                                item.get("load_path", "")))
        self.tree.bind("<Double-1>", self.on_pick)
        ttk.Button(frame, text="使用选中表格", command=self.on_pick).pack(pady=(8, 0))

    def on_pick(self, _event=None):
        sel = self.tree.selection()
        if not sel:
            return
        values = self.tree.item(sel[0], "values")
        self.master_window.path_var.set(values[1])
        self.destroy()
        self.master_window.on_read()
