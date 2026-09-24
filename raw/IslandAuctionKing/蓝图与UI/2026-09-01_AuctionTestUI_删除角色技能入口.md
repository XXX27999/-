# AuctionTestUI 删除角色技能入口

> 类型：项目 UI 蓝图修改与 PIE 复测证据
> 主题：AuctionTestUI 底部按钮与参照图对齐，删除角色技能入口
> 适用范围：IslandAuctionKing，`AuctionTestUI`
> 证据状态：项目实测；MCP 写入、蓝图回读、Lua 语法检查和 PIE 初始化已完成
> 来源：用户参照图、UGCAskQ MCP Resolve/Plan/Execute、项目 Lua 与 PIE 日志
> 更新时间：2026-09-01
> 关联主题：UI 控件树、底部按钮、AuctionTestUIService、角色技能 UI
> 排除范围：仅删除角色技能入口按钮；角色技能面板、服务端角色技能计算和历史情报展示逻辑保留；未修改说明、表情、侦察仪器和藏品图鉴按钮
> 官方依据：`D:\知识库\和平精英绿洲起源\raw\知识\通用\UI与交互\绿洲通用UI编辑规范与排错.md`

## 参照与目标

用户提供的参照图底部入口不包含“角色技能”按钮。本项目原控件树中对应控件为：

- `OpenSkillPanelButton`：角色技能入口按钮
- `OpenSkillPanelLabel`：按钮文本

相邻且保留的控件为 `OpenPropPanelButton`、`OpenHelpPanelButton`、`OpenEmotePanelButton` 和 `OpenCollectibleCodexButton`。

## MCP 修改记录

目标资产：`/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/AuctionTestUI`

写入前备份：

`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\_Backup\2026-09-01_AuctionTestUI_RemoveSkillButton\AuctionTestUI_before_RemoveSkillButton.uasset`

通过 UGCAskQ MCP 执行计划 `plan_16782183_53ca0a65`：

1. `ue.widget_remove(wbp, "OpenSkillPanelButton")`
2. `ue.compile_blueprint(wbp)`
3. `wbp.save_package()`

回读确认：

- `OpenSkillPanelButton` 不存在
- `OpenSkillPanelLabel` 不存在
- `SkillPanel` 面板仍存在
- `OpenPropPanelButton`、`OpenHelpPanelButton`、`OpenEmotePanelButton`、`OpenCollectibleCodexButton` 均存在

## Lua 配套清理

为避免已删除控件被贴图替换服务计为失败，移除：

- `Script/Function/AuctionUITextureReplacementService.lua` 中 `OpenSkillPanelButton` 的按钮贴图绑定
- `Script/Blueprint/Prefabs/UI/AuctionTestUI.lua` 中已删除按钮的字段声明

角色技能服务仍保留，但 `AuctionTestUIService.ValidateCharacterSkillWidgetContract` 会在入口缺失时将角色技能 UI 标记为不可用并继续初始化主竞拍 UI，不会阻断主界面。

## PIE 复测

复测 DebugID：`dkck7sbwdrugxk`

客户端日志：

`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\Saved\Logs\IslandAuctionKing\Clientlog\FullLog\2026.09.01-11.31.04_client__dkck7sbwdrugxk_1.log`

DS 日志：

`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\Saved\Logs\IslandAuctionKing\DSlog\FullLog\2026.09.01-11.32.00_ds__dkck7sbwdrugxk_realtime.log`

验证结果：

- PIE 会话为 `running`。
- `UGCPlayerController+ReceiveBeginPlay`、`AuctionTestUIService+CreateAndShow`、`AuctionTestUIService+Initialize` 和 `AuctionTestUI+Construct` 均执行。
- UI 主初始化成功，图片替换成功。
- Lua 语法检查通过：`AuctionUITextureReplacementService.lua`、`AuctionTestUI.lua`。
- 未再发现 `OpenSkillPanelButton` 或 `OpenSkillPanelLabel` 的项目脚本残留绑定。
- 日志中的 `ValidateCharacterSkillWidgetContract` 将已删除的 `OpenSkillPanelButton` 列入缺失控件，是入口删除后的预期诊断；角色技能面板保留为可选控件，主竞拍 UI 仍继续初始化。

编辑器视觉复核截图：

`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Screenshots\FlaUI\20260901_AuctionTestUI_after_RemoveSkillButton.png`

FlaUI 复核结果：PNG 有效，尺寸 `1936x1056`，目标 UI 编辑器窗口可见且无遮挡；底部左侧入口只保留侦察仪器、说明、表情三组，角色技能入口已消失。

当前仍存在的系统资源/nil 告警属于既有非本次按钮删除范围的问题，未将其归因于本次 UI 修改。
