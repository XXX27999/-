# 2026-09-09 AuctionPropSelectUI 道具行状态底与道具图

> 类型：项目蓝图与 UI 记录
> 主题：AuctionPropSelectUI 右侧道具行按第二张参考图居中道具名，红框放道具图，蓝框已拥有/未拥有底下加 PropSelectStatus
> 适用范围：IslandAuctionKing 的 `/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/AuctionPropSelectUI`、`Script/Function/AuctionPropSelectUIService.lua`、`UIConfigTable` 的 `UI.PropSelect.Item*` 与 `UI.PropSelect.Texture.Status`
> 证据状态：项目实测（UGCAskQ MCP 写入 + 即时回读）+ 官方 API 依据；未启动 PIE，运行态道具图未验证
> 来源：用户参考图红框/蓝框；UGCAskQ MCP `ue_plan_submit` / `ue_py`；官方 `UBorder.SetBrushFromTexture`、`UImage.SetBrushFromTexture(texture, false)`、`UGCGameSystem.GetUGCResourcesFullPath`
> 更新时间：2026-09-09
> 关联主题：[2026-09-09_AuctionPropSelectUI_切图绑定与拥有态](./2026-09-09_AuctionPropSelectUI_切图绑定与拥有态.md)、[2026-09-09_AuctionPropSelectUI_滑动框与文字归位](./2026-09-09_AuctionPropSelectUI_滑动框与文字归位.md)
> 排除范围：未改 AuctionCharacterSelectUI / AuctionHouseSelectUI / ZhuJieMian；商店购买/补全 RPC 仍未实现
> 官方依据：`D:\oasis-skill-plus\docs\api\class\Others\UBorder.md`；`D:\oasis-skill-plus\docs\api\class\Others\UImage.md`；`D:\oasis-skill-plus\docs\api\class\和平全局接口\基础功能\UGCGameSystem.md`（`GetUGCResourcesFullPath`）；`D:\oasis-skill-plus\docs\api\class\Others\UTextBlock.md`（`SetJustification`）

## 一、写前备份

`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260909_PropSelectItemLayout\`

含 `AuctionPropSelectUI_beforeStatus.uasset`、`UIConfigTable_beforeStatus.uasset`、`AuctionPropSelectUIService_beforeStatus.lua`。

## 二、蓝图

plan_id：`plan_16803388_5b5d4b91`（`BindPropSelectItemStatusLayout`）

MCP 即时回读：`ItemStatusBg01-06` 全部 `Border`，父级 `ItemCard0n`，`bIsVariable=true`，`Visibility=3`。`ItemIconText01/02/04/05/06` 为 `Collapsed(1)`；`ItemIconText03` 当时 missing，运行时按空控件处理。状态底贴图路径 `/IslandAuctionKing/Asset/TuPian/AuctionUI/PropSelect/PropSelectStatus.PropSelectStatus`。

二次回读 plan_id：`plan_16805466_7a4cfaed`。父级、画刷、ZOrder、Justification 已持久化；`FVector2D` 无 `.X` 属性，坐标数值需以写入脚本为准。

设计态摆放：

- `ItemIcon` 18,14 / 111x111
- `ItemName` 红框名称区 140,16 / 430x36，字号 22，写 AuctionPropTable.Name
- `ItemDesc` 灰条详细作用 140,62 / 410x44，字号 18，AutoWrapText=true，写 AuctionPropTable.Description
- `ItemStatusBg` + `ItemStatus` 587,14 / 116x39

## 三、配置表

plan_id：`plan_16804243_0659ba30`（`WritePropSelectItemStatusConfig`）

回读：

- `UI.PropSelect.ItemIconSize=111`
- `UI.PropSelect.ItemNameX=140`
- `UI.PropSelect.ItemStatusX=575`
- `UI.PropSelect.Texture.Status=Asset/TuPian/AuctionUI/PropSelect/PropSelectStatus.PropSelectStatus`

## 四、Lua

`AuctionPropSelectUIService.lua`：

- 函数内读上述布局行。
- `ApplyLayout` 只摆卡内图标/名字/状态底，不再把道具行绝对铺到舞台。
- `ItemIconText` 折叠。
- 客户端自己读 `AuctionPropTable`，用 `AuctionPropConfigService.GetRowTexture` 给 `ItemIcon` 上道具图；缺图回退 `PropSelectItemIcon`。
- 状态底运行时再绑一次 `GetUGCResourcesFullPath('Asset/TuPian/AuctionUI/PropSelect/PropSelectStatus.PropSelectStatus')`。
- 购买/补全/已拥有逻辑未改：全无买、缺件补全、齐了或 `PropGroups[name]>0` 已拥有并禁用。`HandleAction` 仍只打日志。

未调用服务端专用 `AuctionPropConfigService:GetGroupProps`。

## 五、待查证

- 未启动 PIE，道具表 `Itemimage` 是否每行都有对象贴图未验证。
- 已打开的「编辑 AuctionPropSelectUI」页签需关闭后重开才能看到 `ItemStatusBg`。
- 商店扣费与写库存仍无 RPC。
