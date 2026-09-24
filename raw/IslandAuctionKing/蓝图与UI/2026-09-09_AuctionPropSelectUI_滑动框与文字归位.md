# 2026-09-09 AuctionPropSelectUI 滑动框与文字归位

> 类型：项目蓝图与 UI 记录
> 主题：道具选择层补 GroupScrollBox/ItemScrollBox，组卡与道具行不再绝对铺出底栏；组名/剩余/道具名/状态收到卡内坐标
> 适用范围：IslandAuctionKing 的 `/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/AuctionPropSelectUI`、`Script/Function/AuctionPropSelectUIService.lua`、`UIConfigTable` 的 `UI.PropSelect.GroupSlotCount/GroupScrollHeight/ItemScrollHeight`
> 证据状态：项目实测（UGCAskQ MCP 写入 + 回读）+ 官方 API 依据；未启动 PIE
> 来源：用户设计态截图；官方 `UScrollBox`/`UPanelWidget.AddChild`；社区帖 2193
> 更新时间：2026-09-09
> 关联主题：[2026-09-09_AuctionPropSelectUI_切图绑定与拥有态](./2026-09-09_AuctionPropSelectUI_切图绑定与拥有态.md)
> 排除范围：未改购买 RPC、大厅、角色选择、拍卖场选择
> 官方依据：`D:\oasis-skill-plus\docs\api\class\Others\UScrollBox.md`、`UVerticalBox.md`、`USizeBox.md`、`UPanelWidget.md`（AddChild）

## 一、问题

设计器里 5 张组卡绝对摆在 AdaptiveCanvas 上，第五张压到底栏；组说明/道具说明仍叠在卡面。官方要求列表用 ScrollBox，子项走 AddChild。

## 二、写入

写前备份：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260909_PropSelectScroll\`

- 蓝图滑动框 plan_id：`plan_16789478_c325edb2`
- 配置 plan_id：`plan_16794304_61b2beb7`
- 删除残留说明 plan_id：`plan_16799290_33c27973`

回读：`GroupScrollBox` 316,146 / 448x776，父 AdaptiveCanvas；`GroupList` 父 GroupScrollBox；`GroupName01` 父 GroupCard01，本地 32,84；`ItemScrollBox` 818,170 / 719x740；`ItemName01` 父 ItemCard01，本地 148,44；`ItemStatus01` 581,18。`GroupDesc*`/`ItemDesc*`/`GroupBand*` 删除后 `stillPresent=[]`。

配置回读：`GroupSlotCount=17`、`GroupScrollHeight=776`、`ItemScrollHeight=740`。

## 三、Lua

`ApplyLayout` 只摆滑动框、底栏和卡内本地坐标，不再按画布 Y 把组卡推出底栏。Refresh 按 17 槽全局索引填组；空卡 `GroupCardSize`/`ItemCardSize` Collapsed。SelectGroup 用 slot 作为全局索引。

## 四、待查证

已打开的「编辑 AuctionPropSelectUI」页签需关闭后重开才能看到 ScrollBox。未启动 PIE，运行态滚动手感未验证。
