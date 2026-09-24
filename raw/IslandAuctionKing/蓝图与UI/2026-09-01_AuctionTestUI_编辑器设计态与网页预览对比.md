# AuctionTestUI 编辑器设计态与网页预览对比

> 类型：项目事实 / 蓝图与 UI / 截图验证
> 主题：`AuctionTestUI` 设计态主框架画刷、已删除旧控件与网页预览对比
> 适用范围：`IslandAuctionKing` 项目
> 证据状态：UGCAskQ MCP 实测 + FlaUI 编辑器截图 + 浏览器截图；本轮未启动 PIE；最终按展示范围收敛并再次回读
> 来源：UGCAskQ MCP PRV 计划与回读、项目网页预览、编辑器截图、项目 Lua、官方 UMG API 文档
> 更新时间：2026-09-01
> 关联主题：[素材导入与网页预览对齐](./2026-09-01_AuctionTestUI_素材导入与网页预览对齐.md)、[第二张参照图对齐](./2026-09-01_AuctionTestUI_第二张参照图对齐.md)、[MCP UI 编辑与高保真还原知识库](../../知识/通用/UI与交互/MCP-UI编辑与高保真还原知识库.md)
> 排除范围：本页不证明 PIE 运行态像素与事件链已复测；编辑器截图包含编辑器工具栏、视口缩放线和项目既有水印叠加；网页截图的动态金额与藏品图片是预览样例，不是蓝图固定数据。
> 官方依据：`D:\oasis-skill-plus\docs\api\class\Others\UBorder.md`、`D:\oasis-skill-plus\docs\api\cppstruct\F\FS\FSlateBrush.md`、`D:\知识库\和平精英绿洲起源\raw\知识\通用\UI与交互\MCP-UI编辑与高保真还原知识库.md`

## 本轮结果

目标蓝图：`/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/AuctionTestUI`

### 主框架画刷

使用 MCP 计划 `plan_16800035_e8f8cbd8`，通过 Python 复制现有 `FSlateBrush` 后设置 `ResourceObject`，再编译、保存并回读。以下 7 个 UBorder 的 `Background.ResourceObject` 均回读为 `Texture2D`，`DrawAs=3`：

| 控件 | 贴图 |
| --- | --- |
| `HUDBackgroundPanel` | `AuctionUI_Background` |
| `TopBarPanel`、`FooterPanel` | `AuctionUI_TopBottomBar` |
| `LeftPlayerPanel` | `AuctionUI_PlayerSeats` |
| `RightDetailPanel` | `AuctionUI_CenterPanel` |
| `WarehousePanel` | `AuctionUI_WarehousePanel` |
| `FooterBidControlPanel` | `AuctionUI_FooterBid` |

这次实际写入成功与旧记录中的“通用 `widget_set_property`/旧路径未回读到贴图”是不同证据，旧记录保留不覆盖；当前结论限定为本项目本资产、当前 MCP Python 直接克隆画刷路径实测成功。

### 旧控件删除

使用 MCP 计划 `plan_16800469_b8e01aca`，删除 `RefreshButton` 与 `ClearBidButton` 两个父控件。回读确认父控件删除时其子标签一并删除，重新加载蓝图后：

`FINAL_LEGACY_MATCHES=[]`

项目 Lua 中同步移除两个按钮的必需控件声明、点击绑定、关闭清理绑定和贴图绑定；`rg` 对 `RefreshButton`、`RefreshLabel`、`ClearBidButton`、`ClearBidLabel` 的结果为无引用。轮次历史的 20 个 `RoundIndexTextP01R01` 至 `RoundIndexTextP04R05` 控件仍为 `Visible`，网页预览中的实际金额继续由运行时历史服务填充。

### 截图证据

- 网页基准：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Screenshots\AuctionFunctionalPreview_reference.jpg`，`1620x971`，JPEG 签名与尺寸校验通过。
- 编辑器设计态：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Screenshots\AuctionTestUI_editor_final_clean.png`，`1592x925`，PNG 校验通过；为完整编辑器窗口截图，已取消控件选中状态。

两张图均确认存在：顶部栏、当前拍卖场名称、阶段/倒计时/参赛与金币信息；四个玩家卡片；中部竞拍情报面板；右侧唯一仓库；底部侦察仪器、说明、表情、当前报价与锁定暗标。编辑器截图中不再显示网页基准里的刷新/清空旧控件。外层尺寸不同是截图对象不同：网页截图为 1620×971 舞台，编辑器截图包含窗口 chrome 与缩放后的设计视口。

## 全屏修复

用户截图显示内容超出红框展示范围。MCP 回读确认中间状态曾为 `ScaleBox_0.Stretch=1 (Fill)`，而现有网页设计基准为 `SizeBox_0=1620x971`，两者组合会把固定业务布局拉伸到展示范围外。

写入前备份：

`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\_Backup\2026-09-01_AuctionTestUI_FullScreenScale\AuctionTestUI_before_FullScreenScale.uasset`

曾使用 `plan_16801822_b6941057` 与 `plan_16802008_23b9a13c` 试验全屏组合；截图比对确认扩大尺寸框和 Fill 会破坏既有网页坐标契约。最终使用 `plan_16803161_fa2f94b8`、`plan_16803952_4c96543e` 与 `plan_16804310_a7553cf9` 收敛展示范围；内层 `RenderTransform.Scale` 的直接结构写入经 MCP 回读确认未持久化，使用 `plan_16803087_aedadce8` 将 Pivot 恢复为中性值。

- `ScaleBox_0.Stretch=2 (ScaleToFit)`
- `ScaleBox_0.UsePcParams=False`
- `ScaleBox_0.StretchPc=1`（未启用 PC 参数接管）
- `ScaleBox_0.StretchDirectionPc=0`
- `SizeBox_0.bOverride_WidthOverride=True`、`bOverride_HeightOverride=True`
- `SizeBox_0.WidthOverride=1620`、`HeightOverride=971`，保持网页预览坐标契约

重新按 `Blueprint` 类型加载并打开设计器后回读值仍一致；最终截图为 `Screenshots\AuctionTestUI_editor_contained_final.png`，有效 PNG，`1592x925`（完整编辑器窗口尺寸）。`ScaleToFit + 1620x971` 已将完整 UI 收敛在展示范围内；截图中的外层黑色网格属于编辑器视口，不属于 UI。设计器仍可显示缩放比例，因此不能用编辑器外层网格判断运行时是否有留白。

### 最新铺满展示区修正

用户后续反馈目标改为“图片铺满展示画面”。官方 `EStretch` API 枚举回读确认：`Fill=1` 为非等比填充整个可用区域，`ScaleToFit=2` 会保持比例并产生留白。当前设计舞台为 `1620x971`，展示区域为 16:9，比例不同是之前左右留白的直接原因。

写入前备份：

`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\_Backup\2026-09-01_AuctionTestUI_FillDisplay\AuctionTestUI_before_FillDisplay.uasset`

使用 MCP 计划 `plan_16806940_841beda3` 写入、编译并保存后，重新加载蓝图回读确认：

- `ScaleBox_0.Stretch=1 (Fill)`
- `ScaleBox_0.UsePcParams=False`
- `ScaleBox_0.StretchPc=1`
- `ScaleBox_0.StretchDirectionPc=0`
- `SizeBox_0.WidthOverride=1620`、`HeightOverride=971`，业务坐标未改变

本次 `Fill` 是针对“铺满展示画面”的明确取舍，可能造成轻微非等比拉伸；未启动 PIE，因此本页只证明编辑器资产写入与 MCP 回读成功，不证明运行态像素结果。

本轮只读截图：D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Screenshots\AuctionTestUI_fill_display_editor.png，1592x925，PNG 校验通过。截图可见 UI 设计器中的完整控件，但编辑器当前视口缩放为“缩放-6”，因此不能把视口网格和 UI 外接矩形当作运行态铺满结论。

## 验证与生效

- `npx --yes luaparse --quiet --file .\Script\Function\AuctionTestUIService.lua`：通过。
- `npx --yes luaparse --quiet --file .\Script\Function\AuctionUITextureReplacementService.lua`：通过。
- `node --check .\Preview\previewServer.js`：通过。
- 未调用 `ue_pie`；按需求只完成编辑器设计态，不启动 PIE。
- 由于本轮修改涉及蓝图画刷和控件结构，后续正式运行需重新调试 PIE；不能以本页编辑器截图替代运行态验证。

## 底部栏贴图纠正

2026-09-01，用户明确指定整条底部栏使用：
`UGCGameSystem.GetUGCResourcesFullPath("Asset/TuPian/AuctionUI/AuctionUI_TopBottomBar.AuctionUI_TopBottomBar")`。

写入前备份：
`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\_Backup\2026-09-01_AuctionTestUI_FooterTopBottomBar\AuctionTestUI_before_FooterTopBottomBar.uasset`

使用 MCP 计划 `plan_16805986_a1575018` 写入并编译保存后，重新加载蓝图回读：

- `FooterPanel.Background.ResourceObject` = `AuctionUI_TopBottomBar`，`DrawAs=3`
- `FooterBidControlPanel.Background.ResourceObject` = `AuctionUI_FooterBid`，`DrawAs=3`

结论限定为当前 `AuctionTestUI` 蓝图设计态：整条底栏使用 `AuctionUI_TopBottomBar`，中间报价区域仍使用独立的 `AuctionUI_FooterBid`，与网页预览 `.footer` 和 `.bid-area` 两层结构一致。首次直接修改 FSlateBrush 字段未持久化，改用 `UScriptStruct.set_field` + `UObject.set_property` 后回读成功；该陷阱不作为成功写入依据。

本轮未启动 PIE。FlaUI 截图尝试因编辑器资源树未展开到 `Asset` 返回路径导航失败（StatusCode=12），未生成有效截图证据。

## 预估成功日志

以下为下次重新 PIE 时应观察的预估日志，不是本轮实际运行日志：

```text
【AuctionTestUIService+Initialize】关键数据 竞拍界面图片替换成功 appliedCount=... failureCount=0
【AuctionTestUIService+RefreshPublicState】关键数据 playerCount=4 roundCount=5 warehouseSlotCount=36
```

## 2026-09-01 严格网页 UI 对齐补充（MCP 实测）

- 类型：项目实测 / 蓝图与 Lua UI 变更。
- 适用范围：`IslandAuctionKing` 的 `AuctionTestUI` 设计态；本节不证明 PIE 运行态。
- 证据状态：MCP Resolve/Plan/Execute 已写入并保存，随后通过 `ue.widget_inspect` 回读；网页预览已打开说明和道具二级 UI 做视觉对照；FlaUI 已生成有效编辑器宿主窗口截图。
- MCP 计划：`plan_16808925_edd9712c`；写入前备份：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\_Backup\2026-09-01_AuctionTestUI_WebReplica\AuctionTestUI_before_WebReplica.uasset`。
- 主界面坐标契约：`TopBarPanel=(9,8,1600,102)`、`LeftPlayerPanel=(9,118,460,720)`、`RightDetailPanel=(482,118,620,720)`、`WarehousePanel=(1116,118,493,720)`、`FooterPanel=(9,852,1600,96)`；底部道具、说明、表情、报价和锁定暗标按钮已按网页预览坐标写入。
- 道具二级 UI：`PropPanel=(550,156,520,660)`，默认 `Collapsed`；两列八行槽位、道具图片、选中标记和 `确定使用` 按钮已按网页结构写入。运行服务隐藏选中绿框/“已选定”文字，保留点击选择和确认使用逻辑。
- 报价键盘二级 UI：`BidKeypadPanel=(558.5,213,503,545)`，默认 `Collapsed`；数字、`00`、`000`、删除、倍数、上轮出价、清除和确定报价控件已按网页布局写入，新增控件通过 `GetWidgetFromName` 查找并绑定。
- 说明二级 UI：`HelpPanel=(550,258,520,455)`，默认 `Collapsed`；上一页、下一页和页码控件已写入，Lua 提供三页说明内容及翻页回调。
- 相关代码：`Script\Function\AuctionTestUIService.lua`、`Script\Function\AuctionPropSelectionUIService.lua`、`Script\Function\AuctionRoundHistoryUIService.lua`、`Script\Function\AuctionUITextureReplacementService.lua`、`Script\Blueprint\Prefabs\UI\AuctionTestUI.lua`。
- 截图证据：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Screenshots\AuctionTestUI_main_web_compare_final.png`，PNG 有效，`1592x925`。FlaUI 可稳定捕获编辑器宿主窗口；`UI编辑器` 子窗口未被捕获工具按标题匹配，因此不把宿主截图冒充为二级子窗口截图。
- 验证：MCP 回读确认主界面控件、二级面板默认显隐及新增按钮几何；`git diff --check` 无本轮新增空白错误；本机未发现可用 `lua/luac/luajit/luacheck`，且本轮未启动 PIE。
- 最终 MCP 只读回读（2026-09-01）：`TopBarPanel`、`LeftPlayerPanel`、`RightDetailPanel`、`WarehousePanel`、`FooterPanel` 均为 `Visible`；`PropPanel=(550,156,520,660)`、`BidKeypadPanel=(558,213,503,545)`、`HelpPanel=(550,258,520,455)` 均为 `Collapsed`。`BidKeyButtonDoubleZero=(135,329,86,86)`、`BidKeyButtonTripleZero=(243,329,86,86)`、`BidKeyMultiplierButton=(351,133,126,86)`、`BidKeyPreviousButton=(351,231,126,86)`、`ClearBidButton=(351,329,126,86)`、`HelpPrevButton=(163,389,58,48)`、`HelpNextButton=(299,389,58,48)`、`HelpPageNumber=(190,397,140,28)`、`UseSelectedPropButton=(174,577,170,58)` 均回读成功且为 `Visible`。
- 生效方式：重新打开/刷新 UI 设计器查看蓝图持久化结果；涉及蓝图结构、控件初始化和 Lua 绑定，正式运行必须重新调试 PIE。
- 官方依据：`D:\oasis-skill-plus\docs\api\class\Others\UScaleBox.md`；通用操作依据：`D:\知识库\和平精英绿洲起源\raw\知识\通用\UI与交互\MCP-UI编辑与高保真还原知识库.md`、`D:\知识库\和平精英绿洲起源\raw\知识\通用\UI与交互\绿洲通用UI编辑规范与排错.md`。
