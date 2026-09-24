# 绿洲 UMG 文字、透明点击层与贴边锚点摆放

> 类型：通用知识
> 主题：UI / CanvasPanelSlot 文字与贴边摆放
> 适用范围：全局通用（绿洲 UMG 编辑器，固定布局 CanvasPanel）
> 证据状态：官方确认 + 项目实测归纳
> 来源：UCanvasPanelSlot / FAnchorData / FAnchors / FMargin 官方 API；20269_UI自适应屏幕；IslandAuctionKing ZhuJieMian 用户手动摆正后 MCP 只读回读
> 更新时间：2026-09-11
> 关联主题：UCanvasPanelSlot、Anchors、Alignment、透明 UButton、TextBlock、网页预览双轨等价
> 排除范围：不覆盖玩法数据刷新、头像/名称/金币运行时加载、事件绑定；不把某一张主界面的具体像素当成所有项目默认值
> 官方依据：D:\oasis-skill-plus\docs\api\class\Others\UCanvasPanelSlot.md；D:\oasis-skill-plus\docs\api\cppstruct\F\FA\FAnchorData.md；D:\oasis-skill-plus\docs\api\cppstruct\F\FA\FAnchors.md；D:\oasis-skill-plus\docs\api\cppstruct\F\FM\FMargin.md；D:\知识库\和平精英绿洲起源\raw\docs\wiki\进阶内容\UI系统\20269_UI自适应屏幕.md。知识库未覆盖“网页 CSS 绝对像素到 UMG Offsets”的官方换算公式。

## 结论

给已有底图补可点区域或补字时，必须按底图的锚点系摆放，不能按网页预览的 `left/top` 硬写成左上角绝对坐标。用户一旦在设计器里手动摆正，MCP 回读到的 `LayoutData` 就是新基线，禁止再用上一轮估算值覆盖。

可执行规则只有五条：

1. **先回读底图，再放文字。** 目标控件的 `Slot.GetAnchors()`、`LayoutData.Offsets`、`GetPosition`、`GetSize`、`GetAlignment`、`GetZOrder` 全部读完，确认文字落在底图内容区，而不是预览 HTML 的绝对像素。
2. **透明点击层和文字是两层。** `UButton` 可以盖住整张底图负责点击；`TextBlock` 必须独立，对齐底图标题/内容区，不要对齐按钮几何中心。
3. **贴边控件抄底图锚点。** 右上金币、右下工具、左下头像这类贴边件，底图若是 `Min=Max=(1,0)/(1,1)/(0,1)`，覆盖上去的按钮和文字必须用同一组锚点；不要用左上角绝对坐标去追假定的 1920×1080。
4. **MCP 写完立刻回读；已打开的设计器页签要关掉再开。** 写入 API 成功也返回 `None`。`GetPosition` 的含义随锚点变化，回读时以 `LayoutData.Offsets + GetAnchors` 为准。
5. **用户手动摆正后，禁止回滚估算值。** 新基线以这一次 MCP 回读为准。运行时 Lua 若仍 `SetPosition/SetSize` 旧配置，会把设计态摆正结果盖掉；发现后只记录风险，未授权不得改玩法脚本。

## 官方锚点语义（必须先读再解释坐标）

官方确认：`UCanvasPanelSlot.GetOffsets` 的说明是 “could be position and size, or margins depending on the anchor points”。`FAnchorData.Alignment` 是控件枢轴，`(0,0)` 左上、`(1,1)` 右下。`FAnchors.Minimum` 是左+上，`Maximum` 是右+下。

因此回读时按下面解释，不能把所有 `GetPosition` 都当成画布左上角像素：

| Anchors.Min == Max | Offsets / GetPosition 含义 | 典型用途 |
| --- | --- | --- |
| `(0,0)` | 相对父级左上角的 `(X,Y,W,H)` | 顶部页签、中部固定卡 |
| `(1,0)` | 相对父级右上角；X 常为负 | 右上金币条 |
| `(0,1)` | 相对父级左下角；Y 常为负 | 左下头像框 |
| `(1,1)` | 相对父级右下角；X、Y 常为负 | 右下帮助/奖励/保底金 |
| `(1,0.5)` | 相对父级右边缘 + 垂直中线；X 常为负，Y 可正可负 | 夹在顶栏与底栏之间的右侧中部卡 |
| Min=`(0,0)` 且 Max=`(1,1)` | 四边留白；`GetSize()` 可能是 `(0,0)` | 铺满参考图 |

项目实测：对 `Min=Max=(0,1)` 的控件，单独调用 `GetOffsets()` 可能把 `Top/Right/Bottom` 读成 `0`，但 `LayoutData.Offsets` 与 `GetPosition/GetSize` 仍完整。回读清单必须包含 `LayoutData`，不能只打一次 `GetOffsets()`。

## 推荐操作顺序

1. `ue.load_object` 目标 WidgetBlueprint，从 `WidgetTree.RootWidget` 递归子控件。
2. 先读底图 Image：`GetAnchors`、`LayoutData.Offsets`、`GetAlignment`、`GetZOrder`、`Visibility`。
3. 量底图内容区（标题条、图标内框、按钮斜切后的文字带），不要用量整张含透明边的贴图像素。
4. 透明 `UButton`：锚点复制底图；尺寸可以略大于内容区以方便点击；`BackgroundColor` alpha=0；`bIsVariable=true`；ZOrder 高于底图、低于或等于文字。
5. 独立 `TextBlock`：锚点同样复制底图；Position/Size 对准内容区；`HitTestInvisible`；ZOrder 高于按钮。
6. `compile_blueprint` + `save_package` 后重新 `load_object`，再读 Position/Size/Anchors/Alignment/ZOrder。
7. 关闭已打开的“编辑 Xxx”页签再打开，设计器才会显示新控件。FlaUI/截图只能证明当前打开的页签，不能证明磁盘上的旧页签缓存。
8. 若用户已经在设计器里拖过控件：以这一次回读为基线，停止用网页预览或配置表旧值回写。

网页预览仍可用于结构、文案和相对关系。预览坐标只有在同时满足下面三条时，才能直接当 `SetPosition/SetSize` 入参：舞台 1920×1080、HTML `id` 与控件同名、预览没有对主界面做非等比 `transform: scale()`。主界面 HUD、贴边条、斜切页签通常不满足，必须改走“回读底图再放字”。

## 透明点击层与文字的分层

同一视觉按钮最少三层，必须分开量：

| 层 | 职责 | 对齐对象 |
| --- | --- | --- |
| 底图 Image | 视觉 | 素材内容区 |
| 透明 UButton | 点击 | 可点热区，可略大于字 |
| TextBlock | 文案 | 底图标题/内容，而不是按钮中心 |

禁止把文字做成 Button 的子控件后指望它自动居中。绿洲 Canvas 下 Button 子文本仍走自己的 Slot；按按钮 `Size/2` 估中心，斜切页签和异形底图都会把字挤出内容带。

ZOrder 建议：底图 0 或更低，点击层高于底图，文字再高一层。文字必须 `HitTestInvisible`，否则会挡住按钮。

## 贴边锚点，不要用左上角追 1920×1080

官方自适应方案把设计舞台锁在 1920×1080，但那是外层 `ScaleBox + SizeBox` 的职责，不是把所有贴边件改写成左上角绝对坐标的理由。

| 视觉位置 | 底图应使用的锚点 | 错误写法 |
| --- | --- | --- |
| 右上金币 | `Min=Max=(1,0)` | `SetPosition(1920-宽, 顶)` |
| 右侧中部卡 | `Min=Max=(1,0.5)` | 抄金币条 `(1,0)` 或右下工具 `(1,1)` |
| 右下工具 | `Min=Max=(1,1)` | `SetPosition(1487, 900)` 这类换算值 |
| 左下头像 | `Min=Max=(0,1)` | `SetPosition(47, 1080-高)` |
| 顶部页签 | 与顶栏底图一致，常见 `(0,0)` | 按 CSS `left: 86/214/342...` 一排硬写 |

覆盖层（透明按钮、金币数字、工具文字）必须复制底图锚点，再用同一坐标系写 Offsets。把 `(1,1)` 底图的 `GetPosition` 和 `(0,0)` 按钮的 `GetPosition` 直接相减，得到的不是画布距离。

`Alignment` 保持与底图一致。现有贴边件常见 `Alignment=(0,0)` 配负 Offsets；未回读前不要改成 `(1,1)`，否则控件会绕锚点跳开。

## MCP 回读与设计器页签

- 位置尺寸只走 `Slot.SetPosition` / `SetSize` / `SetAnchors` / `SetAlignment` / `SetZOrder`。`widget_slot` 实测不能写 Position/Size。
- 纯查询不需要 PRV plan。查询代码不得 `save_package`、`compile_blueprint`、`setattr` 可变资产。
- 回读字段最少：`GetPosition`、`GetSize`、`GetAnchors`、`GetAlignment`、`GetZOrder`、`LayoutData.Offsets`。
- 设计器已打开的页签要关了再开。用户手动拖过的结果只存在当前打开的蓝图工作副本里时，必须先确认用户已保存，再 MCP 回读。
- 用户摆正并保存后，配置表和 Lua 里的旧 `UI.*.X/Y` 都视为过期。下一轮若要改布局，先用回读值更新配置，再决定是否让运行时 `ApplyLayout` 继续写 Slot。

## 常见错误

- 按网页 CSS `position:absolute; left:792px; top:668px` 给 `MatchLabel` 写绝对坐标，字落到底图外。
- 透明按钮和文字共用同一个 Rect，字被按钮几何中心带到斜切页签的空白区。
- 底图已经是右下锚点，新按钮仍用左上角 `(1487,900)` 去“换算”1920×1080，换分辨率或父级尺寸一变就漂。
- 会场这类夹在顶底之间的右侧中部卡，只因为靠近右上就抄金币条 `(1,0)`；父级变高后簇跟着顶边走，和底栏间距失调。正确是 `Min=Max=(1,0.5)`，先回读用户摆正结果。
- 只回读 `GetPosition`，把 `(1,1)` 的负数和 `(0,0)` 的正数放进同一张差值表。
- MCP 写入后不关设计器页签，截到的仍是旧布局。
- 用户已经摆正，下一轮又用配置表默认值 `792,100,448x420` 回写，把验收结果覆盖掉。
- 运行时 `ApplyLayout` 在 `Initialize` 里无条件 `SetPosition/SetSize`，设计态基线与 PIE 显示不一致。

## 相关页面

- [绿洲编辑器控件位置与尺寸准确性](./绿洲编辑器控件位置与尺寸准确性.md)
- [绿洲通用 UI 编辑规范与排错](./绿洲通用UI编辑规范与排错.md)
- [MCP UI 编辑与高保真还原知识库](./MCP-UI编辑与高保真还原知识库.md)
- [绿洲 UMG 文本自动包裹与换行](./绿洲UMG文本自动包裹与换行.md)
- [绿洲 UMG 设计态缩放裁剪与白块排错](./绿洲UMG设计态缩放裁剪与白块排错.md)
- 项目证据（数值不可当全局默认）：[2026-09-08 ZhuJieMian 用户摆正后布局回读](../../../IslandAuctionKing/蓝图与UI/2026-09-08_ZhuJieMian用户摆正后布局回读.md)
- 项目证据（会场簇垂直中线锚点，像素不可当默认）：[2026-09-11 ZhuJieMian 会场匹配区用户修正锚点](../../../IslandAuctionKing/蓝图与UI/2026-09-11_ZhuJieMian会场匹配区用户修正锚点.md)

## 待查证

- 官方文档未给出“网页预览 CSS 像素 → UMG Offsets”公式；本页禁止把预览坐标直接当结论。
- `GetOffsets()` 在 `Min=Max=(0,1)` 时返回不完整，是否为绿洲 Python 绑定问题，尚未用最小复现工程验证。
- 贴边件 `Alignment=(0,0)+负 Offsets` 与 `Alignment=(1,1)+正 Offsets` 的运行时等价性，未做 PIE 对照。
