# UGCPlayerController 竞拍 UI 图片路径结构体

> 类型：项目证据 / 蓝图与 UI / Lua 运行时入口
> 主题：UGCPlayerController、UserDefinedStruct、竞拍 UI 图片路径、局内样式切换
> 适用范围：`IslandAuctionKing`
> 证据状态：项目实测；MCP 资产写入、VarGuid 与 PropertyFlags 修复及回读已通过，编辑器变量面板可见性和完整客户端 PIE 初始化待查证
> 来源：UGCAskQ MCP Resolve/Plan/Execute、同步后的只读 JSON、项目 Lua 文件、PIE DebugID `_dkck7sb0t9khh8` 及客户端握手日志；2026-09-01 VarGuid/PropertyFlags 修复回读
> 更新时间：2026-09-01
> 关联主题：[竞拍 UI 贴图导入与运行时替换](../资产清单/2026-08-31_竞拍UI贴图导入与运行时替换.md)、[IslandAuctionKing 项目资料索引](../000_项目索引.md)
> 关联主题：[竞拍 UI 贴图导入与运行时替换](../资产清单/2026-08-31_竞拍UI贴图导入与运行时替换.md)、[IslandAuctionKing 项目资料索引](../000_项目索引.md)、[绿洲蓝图变量与玩家数据存储](../../知识/通用/程序与网络/绿洲蓝图变量与玩家数据存储.md)
> 排除范围：本页不证明 CDO 内嵌结构体字段默认值已持久化，不覆盖 `AuctionTestUI.uasset` 的控件结构修改，也不把 PIE 握手失败归因于本功能代码
> 官方依据：`D:\oasis-skill-plus\docs\api\class\Others\UUserDefinedStruct.md`、`D:\oasis-skill-plus\docs\api\cppstruct\F\FB\FBPVariableDescription.md`；UGCAskQ `py:guide blueprint`、`py:guide asset` 和项目本地 MCP 能力记录。官方资料未直接定义本项目字段名及本次 MCP 组合写入过程。

## 一、MCP 写入结果

### 1. 路径结构体

已创建并保存独立 UserDefinedStruct：

`/IslandAuctionKing/Asset/Data/Table/Customized/UI/AuctionUITexturePathSet.AuctionUITexturePathSet`

MCP `schema:AuctionUITexturePathSet` 回读确认 11 个字段均为 `FString`：

`Background`、`TopBottomBar`、`PlayerSeats`、`CenterPanel`、`WarehousePanel`、`FooterBid`、`BottomButton`、`BidKeypad`、`NameLabelFrame`、`DescriptionPanel`、`Reference`。

### 2. UGCPlayerController 成员

已在以下蓝图资产下新增并保存结构体成员：

`/IslandAuctionKing/Asset/Blueprint/UGCPlayerController.UGCPlayerController`

成员名：`AuctionUITexturePaths`

最终 MCP 回读：

`schema:UGCPlayerController_C?filter=AuctionUITexturePaths` 返回 `AuctionUITexturePaths : FAuctionUITexturePathSet [Edit, BPVisible]`，PinCategory 为 `struct`，PinSubCategoryObject 为 `AuctionUITexturePathSet` UserDefinedStruct。

写入前备份：

`/IslandAuctionKing/Asset/Blueprint/UGCPlayerController_AuctionUIPaths_Backup.UGCPlayerController_AuctionUIPaths_Backup`

### 3. 变量面板不显示的修复

2026-09-01 复核发现：正式蓝图的 `NewVariables` 中虽然存在唯一的 `AuctionUITexturePaths`，但其 `FBPVariableDescription.VarGuid` 的 `A/B/C/D` 均为 `0`。这与官方 `FBPVariableDescription` 对 `VarGuid` 持久变量标识的定义不符，推断为 UE 4.18 蓝图编辑器“我的蓝图”变量列表不显示的原因。

已使用 UGCAskQ MCP 计划 `plan_16781123_1e6f9404` 修复现有变量的 `VarGuid`，未新增同名变量；正式资产写入前备份为：

`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\_Backup\2026-09-01_AuctionUITexturePaths_VarGuidRepair\UGCPlayerController_before_VarGuidRepair.uasset`

修复后 MCP 重载与回读确认：`NewVariables` 数量为 `1`，变量名仍为 `AuctionUITexturePaths`，类型仍为 `FAuctionUITexturePathSet`，分类仍为 `UI`，`VarGuid` 已为非零值 `{813527461,172905384,1482395076,691250327}`。同步脚本转换正式蓝图成功，未编辑 JSON。

VarGuid 修复后变量面板仍为空。2026-09-01 再次通过 MCP 纯读取发现该变量的 `PropertyFlags` 为 `1`，即仅有 `CPF_Edit`；对比同一蓝图中可见的 `MainUIClass`、`WaitingUI` 等变量，其属性标记包含 `CPF_BlueprintVisible`。因此在保留原变量名、类型、分类和 VarGuid 的前提下，使用 MCP 计划 `plan_16782000_21d11f44` 将现有变量的 `PropertyFlags` 从 `1` 改为 `5`（`CPF_Edit | CPF_BlueprintVisible`），随后编译、保存、重载并回读。

本次写入前备份为：

`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\_Backup\2026-09-01_AuctionUITexturePaths_PropertyFlagsRepair\UGCPlayerController_before_PropertyFlagsRepair.uasset`

最终 MCP 回读确认：唯一变量 `AuctionUITexturePaths` 的 `PropertyFlags=5`、分类为 `UI`、PinCategory 为 `struct`，PinSubCategoryObject 为 `AuctionUITexturePathSet` UserDefinedStruct，VarGuid 保持非零；schema 现在明确显示 `[Edit, BPVisible]`。同步后的只读 JSON 在 `D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\_JsonOutput\Asset\Blueprint\UGCPlayerController.json` 中显示 `PropertyFlags` 值为 `5`，转换统计 `Failed: 0`。这证明资产数据和反射层已修复，但截图中的“我的蓝图”面板仍需重新打开目标资产后人工确认。

关键 MCP 计划：蓝图备份 `plan_16804163_dff32e1d`；结构体创建与字段定义 `plan_16804181_81ef598b`、`plan_16804218_2b33884a`、`plan_16804248_c3ebbd22`；正式蓝图成员写入 `plan_16805063_4052f095`。

## 二、Lua 读取与切换入口

新增：

`Script/Function/AuctionUITexturePathService.lua`

职责：

- 客户端 `Initialize(playerController)` 从 `UIConfigTable` 读取 11 个 `UI.Texture.*` 路径，写入 `playerController.AuctionUITexturePaths` 并逐项回读。
- `GetPath(playerController, textureKey)` 优先读取控制器结构体字段，结构体字段为空时才回退到 `UIConfigTable` 和代码默认路径。
- `SetPath(playerController, textureKey, newPath)` 提供客户端局内替换单张图片路径的入口，写入后回读校验。

更新：

`Script/Function/AuctionUITextureReplacementService.lua`

8 个已确认 `UBorder` 绑定现在通过 `AuctionUITexturePathService.GetPath` 取路径。初始化完成后可调用 `Refresh(widget)`，重新从控制器结构体读取路径并应用画刷。

推荐调用顺序：

```lua
local changed = AuctionUITexturePathService.SetPath(playerController, "AuctionUI_Background", newPath)
if changed then
    AuctionUITextureReplacementService.Refresh(widget)
end
```

## 三、边界与验证状态

### 项目实测

- 编辑器 MCP 资产查询可按完整对象路径加载 11 张 `Texture2D`；图片资产清单见关联页面。
- 蓝图和结构体 schema 回读通过，证明成员是结构体属性，不是早期错误生成的整数属性。
- Lua 文件已被编辑器加载器读取，未出现本功能文件的语法加载错误。

### 待查证

- 当前 UGCAskQ 反射接口无法持久化写入 CDO 内嵌 UDS 的子字段；因此图片路径由客户端 UI 初始化函数在运行时写入控制器结构体，而不是声称已写入蓝图默认值。
- 两次 PIE 运行均未完成客户端 Lua 控制台注册。最新 DebugID `_dkck7sb0t9khh8` 的客户端日志出现 `Initial handshake packet timeout` 和 `LongTimeNoReceived`，未产生 `AuctionUITexturePathService+Initialize` 运行时日志。完整的字段赋值、UI 刷新和贴图加载仍需在 PIE 客户端连接成功后复测。

### 生效方式

蓝图成员和 UserDefinedStruct 变更必须重新调试 PIE；普通 Lua 函数体变更可在客户端连接成功的 PIE 中使用 `reloadlua`，但修改图片路径后仍需调用 `Refresh(widget)` 才会更新已经显示的控件画刷。
