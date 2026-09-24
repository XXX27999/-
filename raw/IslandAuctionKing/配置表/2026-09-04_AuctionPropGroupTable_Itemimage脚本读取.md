> 类型：项目证据
> 主题：配置表
> 适用范围：IslandAuctionKing
> 证据状态：项目实测
> 来源：UGCAskQ MCP `ue_py` 回读 `/IslandAuctionKing/Asset/Data/Table/Customized/AuctionPropGroupTable` 与 `UGCTemplateRowStruct_AuctionPropGroupTable`；脚本修改 `Script/Function/AuctionPropConfigService.lua`、`AuctionTestUIService.lua`、`AuctionPropSelectionUIService.lua`、`AuctionRoundHistoryUIService.lua`、`CharacterPropSelectTestUIService.lua`
> 更新时间：2026-09-04
> 关联主题：配置表与结构体的MCP编辑, GetTableData, 图鉴藏品数据与详情打开修复
> 排除范围：不覆盖向两张表再次新增列；不把已填的两张藏品底图当成全部道具正式图标
> 官方依据：`D:\知识库\和平精英绿洲起源\raw\docs\api\class\和平全局接口\基础功能\UGCGameSystem.md` 的 `GetTableData`；`D:\知识库\和平精英绿洲起源\raw\docs\api\class\Others\UImage.md` 的 `SetBrushFromTexture`

# AuctionPropGroupTable Itemimage 脚本读取

## MCP 回读

- 表路径：`/IslandAuctionKing/Asset/Data/Table/Customized/AuctionPropGroupTable`
- 结构体：`UGCTemplateRowStruct_AuctionPropGroupTable`
- 列：`FriendlyName=Itemimage`，内部名 `Itemimage_3_50AE95F24A04FF034A7E73BF7E690DDC`，`Category=object`，`ToolTip=道具图片`
- 行数：17
- 2026-09-04 回读时 17 行该列均为空（`null`）

同日稍后回读更正：`AuctionPropTable` 才是道具表。原 `Image` bool 列已改为 `FriendlyName=Itemimage`，内部名 `Itemimage_5_2D98C1A944084D63E95683A030EBB23D`，`Category=object`，`ToolTip=道具图片`。40 行中 2 行已填贴图：`特殊估值仪器`、`至尊鉴定仪器`。`AuctionPropGroupTable` 是道具组表，17 行 `Itemimage` 仍为空。

脚本优先级：道具列表/轮次图先读道具表 `Itemimage`（`ItemimageSource=PropTable`）；仅当该道具为空时才回退道具组 `Itemimage`（`GroupFallback`）；两组都空才用品质占位图。

## 脚本

`AuctionPropConfigService.GetRowTexture` 按 `Itemimage` / `Texture` / `Image` 显示名读取，再扫描 `Itemimage*`、`Image*` GUID 后缀，并排除 bool/数字/空值。

加载点：

- 服务端 `AuctionPropConfigService:LoadGroups` 缓存 `Itemimage`
- 客户端 `AuctionTestUIService.LoadPropTables`、`AuctionRoundHistoryUIService.LoadPropRows`、`CharacterPropSelectTestUIService.LoadData`

`ApplyGroupItemimageFallback` 把组图回填到尚无独立贴图的组成员。道具列表与轮次详情图优先用表格贴图，空值时回退原品质占位图。

## 待查证
0. 运行时 `GetTableData` 对道具表返回的是 `Itemimage` 还是仅 `Itemimage_5_2D98C1A944084D63E95683A030EBB23D`，需 PIE 日志 `itemimageField` 确认。


1. `GetTableData` 运行时字段名是 `Itemimage` 还是仅 GUID 后缀，需 PIE 日志确认。
2. 组表填入 Texture2D 后，`SetBrushFromTexture` 是否直接接受该对象。