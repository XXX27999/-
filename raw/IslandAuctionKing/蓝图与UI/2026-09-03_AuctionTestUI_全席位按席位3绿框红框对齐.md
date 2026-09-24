# 2026-09-03 AuctionTestUI 全席位按席位3绿框红框对齐

> 类型：项目证据
> 主题：蓝图与 UI / AuctionTestUI 四席名称报价与槽位
> 适用范围：IslandAuctionKing
> 证据状态：项目实测
> 来源：用户对照图 P3/P4、UGCAskQ MCP 回读写入、FlaUI 设计态截图、源图左侧玩家席位.png
> 更新时间：2026-09-03
> 关联主题：2026-09-03_AuctionTestUI_席位3绿框红框对齐、UCanvasPanelSlot
> 排除范围：不覆盖 Lua、配置表、RPC、PIE 运行态；未绘制彩色参考框
> 官方依据：D:\\oasis-skill-plus\\docs\\api\\class\\Others\\UCanvasPanelSlot.md；知识库未覆盖绿框/红框到 UMG 的官方换算公式

## 问题

用户反馈：席位3的玩家名称、报价与其他席位不一致；道具图片和点击触发区域此前只改了席位3，其余席位仍是旧大框。

## 官方确认

Canvas 槽位通过 UCanvasPanelSlot.SetPosition / SetSize 写入；compile_blueprint 官方返回 None。

## 项目实测

源图 478x767 四席暗槽 Y：P1=101、P2=277、P3=452、P4=628；单格约 63x61。LeftPlayerPanel=(10.667,131.246,545.185,800.824)。

按席位3已验证模板复制到四席：

- 绿框/图片贴暗槽，约 71.855x63.690
- 红框/点击区约 74.849x127.380，覆盖序号、图片、出价
- 标题保留在各席卡头：P1 y=192、P2 y=378.167、P3 y=558.479、P4 y=744
- P3 标题从 546.117 下移到 558.479，使 title-to-image 间距与 P1 同为 44.7

20 组点击区回读均覆盖序号、图片、出价。

截图：D:\\WeGameApps\\rail_apps\\OasisEraEditor(2001776)\\ShadowTrackerExtra\\UGCProjects\\IslandAuctionKing\\Screenshots\\20260903_AuctionTestUI_AllSeatsP3Template_titles.png

备份：D:\\WeGameApps\\rail_apps\\OasisEraEditor(2001776)\\ShadowTrackerExtra\\UGCProjects\\IslandAuctionKing\\_Backup\\2026-09-03_AuctionTestUI_AllSeatsP3Template\\AuctionTestUI_before_AllSeatsP3Template.uasset
