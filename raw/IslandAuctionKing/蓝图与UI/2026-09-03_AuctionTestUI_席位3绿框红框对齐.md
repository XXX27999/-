# 2026-09-03 AuctionTestUI 席位3绿框红框对齐

> 类型：项目证据
> 主题：蓝图与 UI / AuctionTestUI 席位3道具图与点击区
> 适用范围：IslandAuctionKing
> 证据状态：项目实测
> 来源：用户参照图绿框/红框、UGCAskQ MCP 回读写入、FlaUI 设计态截图、源图左侧玩家席位.png
> 更新时间：2026-09-03
> 关联主题：2026-09-03_AuctionTestUI_席位123对齐席位4、UCanvasPanelSlot
> 排除范围：不覆盖 Lua、配置表、RPC、PIE 运行态；未改 P1/P2/P4
> 官方依据：D:\\oasis-skill-plus\\docs\\api\\class\\Others\\UCanvasPanelSlot.md；知识库未覆盖绿框/红框像素到 UMG 的官方换算公式

## 问题

用户反馈席位3的道具图片和点击触发区域仍与参照图不一致。参照图以席位4第5格为例：绿色框为道具图片，红色框为点击触发区域；其余格子按该示例对齐。

## 官方确认

- Canvas 槽位位置/尺寸通过 UCanvasPanelSlot.SetPosition / SetSize 写入。
- compile_blueprint 官方返回 None。

## 项目实测

参照图像素（322x121）：

- 红框 bbox=249,28-298,117，约 50x90
- 绿框 bbox=250,42-297,86，约 48x45
- 红框几乎与绿框等宽，高度约为绿框的 2 倍，上沿覆盖序号、下沿覆盖出价

源图 左侧玩家席位.png 为 478x767。席位3五格暗槽约为：

- R1 x54-116 y452-512
- R2 x129-190 y452-512
- R3 x203-265 y452-512
- R4 x278-340 y452-512
- R5 x353-415 y452-512
- 单格约 63x61

LeftPlayerPanel 回读 (10.667,131.246,545.185,800.824)，按面板缩放后席位3暗槽约：

- R1 图片 (72.257,603.179,71.855,63.690)
- 点击区按红/绿比例 50/48 宽、90/45 高，为 (70.760,583.364,74.849,127.380)

写入后 MCP 回读五格点击区均覆盖序号、图片、出价；P4 几何未变。

截图：D:\\WeGameApps\\rail_apps\\OasisEraEditor(2001776)\\ShadowTrackerExtra\\UGCProjects\\IslandAuctionKing\\Screenshots\\20260903_AuctionTestUI_P3GreenRedSlot.png

备份：D:\\WeGameApps\\rail_apps\\OasisEraEditor(2001776)\\ShadowTrackerExtra\\UGCProjects\\IslandAuctionKing\\_Backup\\2026-09-03_AuctionTestUI_P3GreenRedSlot\\AuctionTestUI_before_P3GreenRedSlot.uasset

## 推断

绿/红框是位置大小参考，不是要在运行时绘制彩色装饰框。该换算基于源图像素和当前面板尺寸，不是官方 API 定义。\n\n后续全席位复制见 [2026-09-03_AuctionTestUI_全席位按席位3绿框红框对齐](./2026-09-03_AuctionTestUI_全席位按席位3绿框红框对齐.md)。\n