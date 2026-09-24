# 2026-09-16 FolderTreeTranslator 表格窗口布局与交互修复

> 类型：来源记录 / 工具与流程
> 日期：2026-09-16
> 范围：知识库工具 `D:\知识库\和平精英绿洲起源\工具\FolderTreeTranslator`（版本 1.5.1 → 1.5.2）
> 项目：通用工具（不依赖具体地图项目；验证不连编辑器，service 用桩替换）
> 证据状态：本机 Tk 8.6 行为实测 + 源码验证 + 冻结版 exe 冒烟
> 正文：[FolderTreeTranslator 表格蓝图 MCP 读写](../工具与流程/FolderTreeTranslator表格蓝图MCP读写.md) 第八·补三节

---

## 一、报障

用户三条，前两条为主：

1. 「**工具区域无法通过上下拖拽调整高度**（拖拽手柄失效或拖动无响应）」。
2. 「**部分内容区域既不能横向滚动也不能纵向滚动**，导致内容超出容器边界后被裁剪或溢出遮挡其他区域」。
   验收要求：可拖拽且有合理最小/最大高度；空间不足时自动出滚动条；任何窗口尺寸与缩放比例下都不溢出、不遮挡；保持现有功能与界面风格。
3. 附带两条：「**不能多开表格蓝图数据**」「**表格的行名不受文件命名规则影响**」。

附带发现（用户截图里的一条日志）：`[MCP] SSE 读线程结束：'int' object has no attribute 'get'`。

## 二、改动清单

| 文件 | 改动 |
| --- | --- |
| `oasis_table_ui.py` | 主改：`PanedWindow` 分栏 + sash 夹紧/复查、三区自动滚动条、编辑字段滚动容器、窗口 `minsize` 跟随内容 |
| `FolderTreeTranslator.py` | 表格窗口单例（复用存活实例 + `<Destroy>` 清引用）；`APP_VERSION` 1.5.1 → **1.5.2** |
| `oasis_datatable.py` | `validate_row_name` 放宽为「只校验非空」，废弃 `ROW_NAME_RE` |
| `oasis_mcp_client.py` | `_reader_loop` 对非 dict 的 JSON 负载 `continue`，不再打死读线程 |

## 三、关键坑（本机 Tk 8.6 实测）

| # | 坑 | 表现 | 解法 |
| --- | --- | --- | --- |
| 1 | pane 没有 `-maxsize` | `paned.add(f, minsize=…, maxsize=…)` 抛 `TclError: unknown option "-maxsize"` | 上限自己用 `sash_place` 夹 |
| 2 | 没有 `sashpos()` | `AttributeError: 'PanedWindow' object has no attribute 'sashpos'` | 用 `sash_coord(0)[1]` 读、`sash_place(0, x, y)` 写 |
| 3 | `sash_place` 不触发 `<Configure>` | 窗口缩放后 Tk 自行重分配把 sash 推回，只在 `<Configure>` 里夹一次会被覆盖（工具区停在 441px，自然高度 383px） | 夹紧后 `after(120)` 复查（`_recheck_sash`），收敛即停；启动再补 `(80,200,400,700)` 四次复查 |
| 4 | `winfo_reqheight()` 随分配变化 | 内部 `weight=1` 子容器吸收空间，工具区被拉到 440 后 `reqheight` 也从 383 涨到 440，形成正反馈 | 上限用常量或布局前测一次，不每次动态取 |
| 5 | PanedWindow 没请求高度 | 空间不足时 `pack(expand=True)` 无法压缩它，底部状态栏被挤出窗口（620px 高时状态栏消失） | 构造时给 `height=DATA_MIN_H+TOOL_MIN_H`，并 `_fit_min_height()` 按 `winfo_reqheight()` 设 `minsize` |
| 6 | 验证窗口未映射 | `withdraw()` 下子控件不参与布局，`winfo_height()` 恒为 1，什么都测不出 | 脚本里 `root.deiconify()` + `win.deiconify()` + `geometry(...)` |
| 7 | `pans.bind()` 无参返回元组 | `"%s" % pans.bind()` 抛 `TypeError: not all arguments converted` | 用 `%r` 且加逗号：`"%r" % (pans.bind(),)` |

## 四、行名规则的更正（重要，涉及既有结论）

1.5.1 及之前，行名按 `^[A-Za-z][A-Za-z0-9_]*(\.[A-Za-z0-9_]+)*$` 校验（禁空格、禁中文）。
**这是错的**：行名是 DataTable 的 **FName 行键**，不是文件名，不受「UGC 工程文件名必须以英文字母开头、
不得含 `.` / `-`」那套规则约束——后者约束的是 **PIE 上传时会被递归扫描的脚本与工程文件**。
写入链路走 `ue_py` 的 base64 + JSON 参数，任意字符都能安全传输。

1.5.2 起只校验非空。实测 9 例全通过：英文点号、纯数字 `1001`、长名下划线、
中文 `武器.伤害.基础值`、含空格、含连字符 `A-B_C`、首尾空白（strip），空串与纯空白拒绝。

> 影响面：存量中文行名的表（如 `AuctionCharacterSkillTable`）现在可以直接新增中文行名。
> 旧知识库里「新增行必须满足英文点号规范」的结论已同步标注废弃。

## 五、SSE 非 dict 负载（附带修复）

服务端偶尔推裸数字心跳（`data: 3`），`json.loads` 得 `int`，原代码直接 `msg.get("id")` →
`AttributeError: 'int' object has no attribute 'get'`，**整个 SSE 读线程被打死**，
之后所有 MCP 响应无人接收（外观又是「卡住」）。修法：`if not isinstance(msg, dict): continue`。

## 六、验证

| 套件 | 覆盖 | 结果 |
| --- | --- | --- |
| `verify_layout.py` | 拖拽改变高度 / min 300 / max 580 / 数据区 min 120 / 宽表出横条 / 多行出纵条 / 编辑区滚动 / 队列横条 / 窄内容自动隐藏 ×2 / 5 尺寸无越界遮挡 | **12/12** |
| `verify_changes.py` | 行名 9 例 + SSE 3 例 + 单例 7 例 | **19/19** |
| `verify_final.py` | 4 个 `.py` 编译 + 自然高度上限 + 增量归数据区 + 拖拽后保持 | **9/9** |

合计 **40/40**。定位第 3 条坑用的诊断脚本是 `probe_clamp.py`：手工调 `_clamp_sash()`
工具区立刻从 441 收回 382，证明夹紧逻辑本身正确，问题只是「没机会执行」。

多尺寸实测（`problems=[]`）：960×620 / 1180×760 / 1600×1000 / 1024×700 / 960×560 下，
状态栏均在窗口内，编辑区与变更队列无重叠、无越界。

## 七、产物

- exe：`D:\知识库\和平精英绿洲起源\工具\FolderTreeTranslator\dist\FolderTreeTranslator.exe`
- **12.00 MB**，SHA256 `a31abf0f98793a89c7d642e7dabc04848f99722da68eaf53019a7182df50712d`
- 冒烟：主窗口标题 `绿洲起源 · 文件夹结构整理工具  v1.5.2`，启动存活、正常终止
- 构建脚本：`备份\FolderTreeTranslator\20260916_表格窗口布局与单例\build_exe.py`
- 生效方式：**替换 exe 后重新打开工具即可**（本次为纯工具改动，不涉及 UGC 工程，无需 PIE）

## 八、可复用结论

1. tkinter 要「可拖拽 + 有上下限」的分栏：`PanedWindow` + 自己夹 sash，别指望 `-maxsize`。
2. **夹 sash 必须配复查回调**——Tk 的自动重分配发生在 `<Configure>` 之后，且 `sash_place` 不触发新事件。
3. 滚动条自动显隐用 `xview()`/`yview()` 的 fraction 判断 + `grid_remove`，比常驻省空间。
4. 任何「按内容自然尺寸做上限」的逻辑，先确认该尺寸不随分配变化，否则会正反馈放大。
5. 子窗口默认应做单例：复用存活实例 + `<Destroy>` 清引用，避免重复打开多个相同窗口。
6. 网络读线程对**任何**非预期负载都要跳过而不是解析，否则一次异常心跳就打死整条接收链路。

## 九、未验证

1. 多显示器、不同 DPI 缩放（125% / 150%）下的布局未实测；当前常量按 100% 缩放下 960×620 ~ 1600×1000 验证。
2. 1.5.2 未做冻结环境下的真实 MCP 往返验证（布局验证全部用桩 service，不连编辑器）。
3. `_recheck_sash` 是收敛式复查（120ms 一次）；极端高频连续拖拽/缩放下的最大收敛次数未测，
   实测在 5 种尺寸切换下均能 1~2 次内收敛。
