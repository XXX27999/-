# 绿洲编辑器 UI 截图与验证

> 内容层：绿洲编辑器 UI 截图、目标区域裁剪与机器校验
> 来源：2026-08-27 FlaUI 安装与编辑器截图实测；2026-08-27 路径驱动截图实现；2026-08-28 自绘资产面板点击与红框裁剪实测；2026-08-26 UGCAskQ MCP 编辑器修改能力实测
> 官方依据：当前本地 `raw/docs/api` 与 `raw/docs/wiki` 未确认专用的 UMG 编辑器画布 PNG 导出 API；FlaUI 官方 README 与本地 FlaUI 实测记录确认 `UIA3Automation`、`Capture.Element` 和 FlaUI 输入 API 的可用范围。

## 核心结论

- `ue.editor_get_active_viewport_size()` 只能证明可读取活动视口尺寸，不能证明可导出 UMG 画布 PNG。
- 当前编辑器点击、窗口截图和截图裁剪均通过 FlaUI 完成；UGCAskQ 只用于识别资产或控件，不承担截图写入。
- 截图成功必须同时满足：PNG 存在且非空、尺寸有效、目标 UI 可见、目标区域未被弹窗或提示遮挡。
- 多截图场景不能只按 zIndex 选择，因为弹窗或提示可能覆盖目标窗口。
- 截图默认优先识别红色标注边界，其次识别选中 UMG 预览的浅色虚线边界并保留少量边距；未检测到边界时返回 `StatusCode=18`，不能把整窗截图冒充目标区域。
- 路径驱动截图的 UIA 节点需要先读取 `ExpandCollapse`/`Toggle` 状态，逐级展开目录；自绘资产面板没有完整 UIA 节点时，使用新鲜窗口帧识别页签、搜索框和唯一资产行，再执行输入、单击、双击并逐步验证。

## 可执行步骤

1. 使用 FlaUI helper 的 `--list` 唯一匹配可见绿洲编辑器窗口，记录完整标题并激活目标窗口。
2. 使用 `--capture-file /<ProjectName>/Asset/.../<file>` 定位资产；语义 UIA 树按父级展开，自绘资产页按截图识别后用鼠标和键盘完成操作。
3. 每次点击、输入和双击后重新捕获窗口帧，确认唯一结果、选中状态、编辑器表面和稳定帧。
4. 保存到绝对路径；优先裁剪红框或选中虚线区域，未识别边界时拒绝保存整窗结果为目标截图。
5. 校验字节数、PNG 签名、尺寸和非单色像素，并用图像查看器确认目标 UI 和遮挡状态。
6. FlaUI helper 构建使用 `dotnet restore`、`dotnet build -c Release --no-restore`；路径驱动流程的 Schema、状态码和示例见 `raw/知识/通用/来源记录/2026-08-27_FlaUI安装与编辑器截图.md`。

## 常见错误

- 把视口尺寸接口描述成截图导出接口。
- 使用旧观察的坐标、截图 ID、data URL 或包含旧进程号的窗口标题。
- 只按 zIndex 自动挑图，误保存弹窗或提示层。
- 只验证文件存在，不检查 PNG 签名、尺寸、非空内容和目标 UI 是否遮挡。
- 未实际裁剪却将完整编辑器窗口称为画布截图。
- 未检测红框或选中边界就直接保存整窗截图，导致输出包含资产栏、层级面板和属性面板。

## 已验证记录

- 2026-08-27，FlaUI.Core 5.0.0 与 FlaUI.UIA3 5.0.0 构建 helper；唯一匹配 `ShadowTrackerExtraUGCEditor`，生成过 `1936x1056` 的完整编辑器 PNG，并完成签名和视觉检查。
- 2026-08-28，`--capture-file /IslandAuctionKing/Asset/Blueprint/Prefabs/UI/CollectibleCodexUI` 完成自绘资产面板搜索、选择、双击激活和 `selection-frame-fallback` 裁剪，输出 `504x303` PNG，`StatusCode=0`、`NonUniformPixels=true`。
- 2026-08-27 的 Computer Use 窗口截图测试遇到 `SetIsBorderRequired failed: 不支持此接口 (0x80004002)`；该失败不能被描述为成功截图。

## 待查证

- 当前本地官方资料未确认绿洲编辑器提供稳定的 UMG 画布原生 PNG 导出接口。
- 截图接口运行时可能返回 JPEG data URL；保存为 PNG 时必须进行格式转换并再次验证 PNG 签名、尺寸和视觉内容。

## 相关页面

- [MCP UI 编辑与高保真还原知识库](./MCP-UI编辑与高保真还原知识库.md)
- [绿洲通用 UI 编辑规范与排错](./绿洲通用UI编辑规范与排错.md)
- [绿洲 UMG 设计态缩放裁剪与白块排错](./绿洲UMG设计态缩放裁剪与白块排错.md)
- [2026-08-27 FlaUI 安装与编辑器截图](../来源记录/2026-08-27_FlaUI安装与编辑器截图.md)

## 2026-09-07 补充：FlaUI 无法枚举提权的编辑器窗口

- 现象：`FlaUiCapture --list` 只返回 ChatGPT / 资源管理器，枚举不到 `ShadowTrackerExtraUGCEditor`；即使按 `--process-name` + `--title` 精确匹配也提示 `Expected exactly one target window, found 0`。
- 已核实：进程存在（`Get-Process` 能取到 MainWindowTitle）、`IsIconic` 为 False（未最小化）；非提权进程对该进程 `OpenProcessToken` 失败，判断为权限隔离导致 UIA 不可见。
- 兜底：可用 GDI `CopyFromScreen(GetWindowRect)` 截窗口矩形，但从非提权进程 `SetForegroundWindow` 到提权窗口不生效，截到的是当前顶层窗口；且 `ue.open_editor_for_asset` / `ue.objed_open_asset` 返回 True 也不会切换前台文档（`ctx:` 的 asset 仍是原资产）。
- 结论：需要设计态截图时，先由用户手动把目标资产页签切到前台再截图；不要把"截到了编辑器窗口"当作"截到了目标 UI"。

## 2026-09-14 补充：FlaUI 失效时的 GDI 直截可复现方案（已验证）

- 复现条件：编辑器 `ShadowTrackerExtraUGCEditor` 进程存在且有窗口标题（本例 pid=22064，标题 `ShadowTrackerExtra (64 位，PCD3D_SM5) 22064, Compiled: Sep  3 2026 17:31:26`），但 `FlaUiCapture --list` 仍只返回 ChatGPT / Edge / 微信，精确匹配报 `Expected exactly one target window, found 0` —— 与 2026-09-07 记录一致，属权限隔离。
- **新增可用路径（本轮实测成功）**：绕开 UIA，直接用 Win32 `GetWindowRect` 取窗口矩形，再 GDI `CopyFromScreen` 截该矩形。
  - 关键点 1：目标窗口句柄必须用 **`Get-Process -Name ShadowTrackerExtraUGCEditor` 的 `MainWindowHandle`** 取得；同一进程名下存在**两个进程**（本例 pid=12048 的 `MainWindowHandle=0` 且标题为空，pid=22064 才有真实句柄 463876），必须按句柄非 0 且标题非空筛选，否则截到黑图。
  - 关键点 2：即使 `SetForegroundWindow` 对提权窗口返回 False，**只要该编辑器窗口本来就是可见的前台窗口**（`IsWindowVisible=True`），`CopyFromScreen` 就能截到正确内容。本轮在编辑器处于前台且 `AuctionSettlementUI` 设计页签已打开的情况下，成功截到 1936×1048 的完整编辑器窗口，目标 UI 清晰可读，`StatusCode` 断言不再依赖 FlaUI。
  - 关键点 3：窗口矩形为 `L=-8 T=-8 R=1928 B=1040`（含 -8 阴影偏移），必须按 `R-L` / `B-T` 计算位图尺寸，不能直接取 `Right`/`Bottom`。
- **仍未被绕过的限制**：`SetForegroundWindow` 依然无法把提权编辑器窗口拉到前台，因此**编辑器必须由用户预先置于前台并已打开目标资产页签**；进程在后台或被遮挡时 GDI 截到的是遮挡方。
- 产物证据：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260914_SettlementUI参考图对齐\SettlementUI_现状截图_20260914.png`（1936×1048，934581 字节）。
- 适用范围：仅用于**设计态目视核对**，不构成 UMG 画布原生 PNG 导出能力的证据；也不要据此声称 FlaUI 路径可用。
