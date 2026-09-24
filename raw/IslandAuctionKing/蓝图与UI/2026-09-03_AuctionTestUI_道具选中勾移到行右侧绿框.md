# 2026-09-03 AuctionTestUI 道具选中勾移到行右侧绿框

> 类型：项目证据
> 主题：蓝图与 UI / AuctionTestUI PropSelectedMark
> 适用范围：IslandAuctionKing
> 证据状态：项目实测（MCP 回读）
> 来源：UGCAskQ MCP plan_16806760_4261f3f3、AuctionTestUI PropRow01-08 回读
> 更新时间：2026-09-03
> 关联主题：绿洲编辑器控件位置与尺寸准确性、AuctionTestUI 道具栏顶部详情绑定 SkillBar
> 排除范围：未改道具图片、按钮点击区、席位或仓库几何；未启动 PIE
> 官方依据：D:\oasis-skill-plus\docs\api\class\Others\UCanvasPanelSlot.md（SetPosition/SetSize）。知识库未覆盖用户绿框到画布的官方换算公式。

## 问题

用户绿框圈住道具行右侧空白。当时 `PropSelectedMark01-08` 铺满整行 227.51x116.483，左对齐，勾出现在左侧图标旁。

## 写入

备份：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\_Backup\2026-09-03_AuctionTestUI_MovePropSelectedMark\`

MCP：`plan_16806760_4261f3f3`

相对 `PropRow`：左侧图标 `(8.387,28.886,58.712x58.712)`，右侧勾镜像为 `(160.411,28.886,58.712x58.712)`，居中对齐，`inside=true`。8 个标记全部回读一致。

Lua：`AuctionPropSelectionUIService.RefreshSlot` 选中时改为 `HitTestInvisible` 显示勾，未选中仍 `Collapsed`。
