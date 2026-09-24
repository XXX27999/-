# AuctionTestUI 第二张参照图对齐

> 类型：项目 UI 蓝图修改与 PIE 复测证据
> 主题：AuctionTestUI 空白框架参照图对齐
> 适用范围：IslandAuctionKing，客户端 `AuctionTestUI`，PIE
> 证据状态：项目实测；MCP 写入与回读、FlaUI 截图、客户端 Lua 日志已完成
> 来源：用户提供的第二张参照图、UGCAskQ MCP 计划与回读、项目 Lua、PIE 客户端日志
> 更新时间：2026-09-01
> 关联主题：竞拍 UI 贴图、UIConfigTable、AuctionTestUIService、底部按钮布局、PIE 启动黑屏
> 排除范围：本页不修改玩法数据、服务端出价、角色技能面板逻辑；系统反作弊水印和编辑器/引擎资源 MissingFile 告警不属于 UI 参照图内容
> 官方依据：`D:\oasis-skill-plus\docs\api\class\Others\UBorder.md`、`D:\oasis-skill-plus\docs\api\cppstruct\F\FS\FSlateBrush.md`

## 目标与处理结果

第二张参照图仅保留灰色背景、橙色边框、四组左侧玩家卡片、中间空白面板、右侧空白仓库框和底部竞价框。竞拍 UI 本体不显示运行时文字、仓库格覆盖层、情报卡和藏品图片；附件只作为视觉参照，不作为额外操作指令。

本次通过配置开关实现“参照图空白态”，不删除业务控件和数据：

- `UI.ReferenceBlankMode=true`：初始化仓库后折叠 `CellButton01..36`、`CellLabel01..36`、藏品图片/按钮/标签，并保留仓库数据与控件树。
- 通过 MCP 清理主界面动态文字和中间情报覆盖层；弹窗静态文本 56 项已恢复，避免说明、表情等弹窗失去内容。
- 通过 MCP 将竞拍 UI 本体的 `TitleText`、`BrandEyebrowText` 持久化为 `Collapsed`；控件树回读确认位置分别为 `(95,48,179,26)`、`(95,31,179,14)`。
- 通过运行时 `AuctionUITextureReplacementService` 应用 8 组 UBorder 画刷纹理；`FooterPanel` 改用 `AuctionUI_TopBottomBar`，与参照图底部整条框架一致。
- 底部三个保留入口回读位置与尺寸：`OpenPropPanelButton` `(68,880,112,75)`、`OpenEmotePanelButton` `(190,880,112,75)`、`OpenHelpPanelButton` `(312,880,112,75)`。
- 顶部计时器、阶段、参赛、锁定和金币背景设置为深色半透明，匹配参照图的空白芯片样式。
- 角色技能入口删除记录见 [AuctionTestUI 删除角色技能入口](./2026-09-01_AuctionTestUI_删除角色技能入口.md)。

## MCP 修改记录

目标资产：`/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/AuctionTestUI`

配置表：`/IslandAuctionKing/Asset/Data/Table/Customized/UI/UIConfigTable`

写入前备份：

- `D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\_Backup\2026-09-01_AuctionTestUI_ReferenceBlank\AuctionTestUI_before_ReferenceBlank.uasset`
- `D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\_Backup\2026-09-01_AuctionTestUI_ReferenceBlank\AuctionTestUIService_before_ReferenceBlankMode.lua`
- `D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\_Backup\2026-09-01_AuctionTestUI_ReferenceBlank\AuctionUITexturePathService_before_ConfigFallback.lua`

已执行并回读的计划：

- `plan_16783570_d003642e`：清理主界面普通状态文字，隐藏刷新、清空和锁定等参照图不显示控件，并恢复弹窗静态文本。
- `plan_16784044_27196188`：设置主面板画刷颜色、折叠中间动态层、仓库格/藏品动态层和主界面文字按钮覆盖层。
- `plan_16784215_f9949c32`：修正 `UI.TextureBinding.FooterPanel` 为 `AuctionUI_TopBottomBar`。
- `plan_16785280_2343d5c8`：新增并回读 `UI.ReferenceBlankMode`，类型 `bool`，值 `true`。
- `plan_16785838_bd56c11a`：底部三个入口位置和尺寸回读一致。
- `plan_16786080_a2614607`：顶部芯片背景颜色写入并保存。
- `plan_16787052_c64191fa`：隐藏 `TitleText`、`BrandEyebrowText`，编译保存后 MCP 回读均为 `Visibility: Collapsed`。

说明：尝试直接向 UBorder 的 `FSlateBrush.ResourceObject` 写入 Texture2D 后，MCP 回读仍为 `None`，因此没有把该尝试当作蓝图纹理写入成功。最终以已存在的运行时贴图替换服务和 UIConfigTable 路径为生效依据。

## Lua 与配置变更

- `Script/Function/AuctionTestUIService.lua:100` 在运行时函数内读取 `AuctionConfig.GetBoolean("UI.ReferenceBlankMode", false)`；`RefreshWarehouse` 在开关开启时折叠动态覆盖层并记录入口、分支、出口日志。
- `Script/Function/AuctionUITextureReplacementService.lua:26` 将底部框架回退资源改为 `AuctionUI_TopBottomBar`。
- `Script/Function/AuctionUITexturePathService.lua:60` 起改为从配置表/回退路径读取，避免启动阶段对 `AuctionUITexturePaths` 结构体写入造成 Lua 取值错误；显式运行时 `SetPath` 入口仍保留。
- `Asset/Data/Table/Customized/UI/UIConfigTable.uasset` 新增 `UI.ReferenceBlankMode` 行，修改后需要重新 PIE。

## PIE 与截图验证

复测 DebugID：`_dkck7sbwdrxkk7`

客户端 Lua 日志：

`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\Saved\Logs\IslandAuctionKing\Clientlog\LuaLog\2026.09.01-12.50.25_client__dkck7sbwdrxkk7_1.log`

全量客户端日志：

`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\Saved\Logs\IslandAuctionKing\Clientlog\FullLog\2026.09.01-12.50.25_client__dkck7sbwdrxkk7_1.log`

最新 FlaUI 截图：

`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Screenshots\FlaUI\20260901_AuctionTestUI_final_ReferenceBlankMode_NoBrand.png`

截图 PNG 校验通过，尺寸 `1296x759`。目视结果为灰色/橙色主框架、四组左侧卡片、中间空白区、右侧空白仓库区、底部三按钮和竞价框；未出现黑屏。截图左上角仍有外层 `MainWidget` 的 `MainUI_SutraIsland_Kill_184_C_0` 系统 HUD 标识，以及引擎反作弊水印；两者不属于 `AuctionTestUI`，本次未改动。

关键日志证据：

- `UI.ReferenceBlankMode valueType=bool value=true setOK=true`
- `side=client appliedCount=21 invalidCount=0`，配置加载 `success=true`
- `RefreshWarehouse ... referenceBlankMode=true`，出口 `visibleCount=0`
- `TitleText`、`BrandEyebrowText` 蓝图回读均为 `Visibility: Collapsed`
- `AuctionTestUIService+CreateAndShow` 已存在且初始化完成
- 日志筛查：`LuaExtend_GetStructPropertyValue Failed`、`Fatal error`、`SIGABRT`、`DSGameMode is null` 均为 0 次

## 检索轨迹

检索主文档：`D:\知识库\和平精英绿洲起源\raw\知识\通用\UI与交互\MCP-UI编辑与高保真还原知识库.md`、`D:\知识库\和平精英绿洲起源\raw\IslandAuctionKing\000_项目索引.md`。

补充依赖：`D:\知识库\和平精英绿洲起源\raw\知识\通用\UI与交互\绿洲通用UI编辑规范与排错.md`、[竞拍 UI 布局与按钮画刷修复](./2026-08-31_竞拍UI布局与按钮画刷修复.md)、[竞拍 UI 贴图导入与运行时替换](../资产清单/2026-08-31_竞拍UI贴图导入与运行时替换.md)。

证据复核：官方 `UBorder`/`FSlateBrush` API 文档、上述 MCP 计划回读、项目 Lua 和 PIE/FlaUI 产物。

知识库未覆盖：用户提供的参照图没有提供原始控件尺寸、字体或纹理源文件，因此本页只记录项目实际回读和截图结果，不推断图片之外的设计参数。
