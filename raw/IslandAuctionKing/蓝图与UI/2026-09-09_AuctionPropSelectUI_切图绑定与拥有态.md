# 2026-09-09 AuctionPropSelectUI 切图绑定与拥有态

> 类型：项目蓝图与 UI 记录
> 主题：AuctionPropSelectUI 按确认后的网页预览绑定技能道具切图，底栏显示价格与购买/补全/已拥有，右侧道具行按拥有态切图
> 适用范围：IslandAuctionKing 的 `/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/AuctionPropSelectUI`、`Script/Function/AuctionPropSelectUIService.lua`、`UIConfigTable` 的 `UI.PropSelect.*` 行、贴图目录 `/IslandAuctionKing/Asset/TuPian/AuctionUI/PropSelect`
> 证据状态：项目实测（UGCAskQ MCP 写入 + 回读）+ 官方 API 依据；未启动 PIE，运行态未验证
> 来源：用户确认网页预览 `C:\Users\Administrator\.codex\visualizations\2026\09\08\01a0804a-03db-77f3-be02-f5fda55713eb\index.html`；桌面切图 `C:\Users\Administrator\Desktop\素材\竞拍\技能道具UI`；UGCAskQ MCP `ue_plan_submit` / `ue_py`
> 更新时间：2026-09-09
> 关联主题：[绿洲编辑器控件位置与尺寸准确性](../../知识/通用/UI与交互/绿洲编辑器控件位置与尺寸准确性.md)、[资源导入与路径规范](../../知识/通用/配置与数据/资源导入与路径规范.md)、[2026-09-07_AuctionPropSelectUI_对齐网页预览仪器组合层](./2026-09-07_AuctionPropSelectUI_对齐网页预览仪器组合层.md)
> 后续：[2026-09-09_AuctionPropSelectUI_道具行状态底与道具图](./2026-09-09_AuctionPropSelectUI_道具行状态底与道具图.md)
> 排除范围：未改 AuctionCharacterSelectUI / AuctionHouseSelectUI / ZhuJieMian / AuctionHubUIService / AuctionGameService；商店扣费 RPC 本轮未实现
> 官方依据：`D:\oasis-skill-plus\docs\wiki\新手入门\资源管理与编辑\277_资源导入.md`（PNG 导入）；`D:\oasis-skill-plus\docs\api\class\Others\UBorder.md`（`SetBrushFromTexture`）；`D:\oasis-skill-plus\docs\api\class\Others\UWidget.md`（`SetIsEnabled` / `SetVisibility`）

## 一、写前备份

`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260909_PropSelectArt\`

含 `AuctionPropSelectUI.uasset`、`AuctionPropSelectUI.lua`、`AuctionPropSelectUIService.lua`、`UIConfigTable.uasset`、英文切图副本、MCP 计划与 Python 载荷。

## 二、贴图导入

plan_id：`plan_16782227_96e060da`（`ImportPropSelectArt`）

15 张 PNG 导入到 `/IslandAuctionKing/Asset/TuPian/AuctionUI/PropSelect`。回读全部 `Texture2D`，五项属性 `(LODGroup, MipGenSettings, CompressionSettings, CompressionQuality, SRGB) = (16, 13, 0, 5, True)`。抽样尺寸：`PropSelectPanel=1372x1089`、`PropSelectFooter=715x105`、`PropSelectConfirm=366x102`、`PropSelectItemUnowned=719x139`。

## 三、蓝图绑定

plan_id：`plan_16784601_48ef66c0`（`BindPropSelectArt`）

新增并回读存在：`RightPanel`、`ActionButton`、`ActionLabel`、`ItemStatus01-06`。底板 `SheetPanel` 绑 `PropSelectPanel`，底栏 `GoldChipBorder` 绑 `PropSelectFooter`，确认钮绑 `PropSelectConfirm`，关闭钮绑 `PropSelectClose`。组卡 `GroupTop01-05` 默认绑低级底，运行时按品质/选中切换。

## 四、配置表

plan_id：`plan_16786676_5498b120`（`WritePropSelectConfigRows`）

`UIConfigTable` 回读：`SheetWidth=1372`、`BuyText=购买道具组`、`CompleteText=补全道具组`、`OwnedText=已拥有道具组`、`ItemOwnedText=已拥有`、`ItemUnownedText=未拥有`。贴图路径行 `UI.PropSelect.Texture.*` 已写入。

## 五、Lua

`AuctionPropSelectUIService.lua`：函数内读 `UI.PropSelect.*`；`Refresh` 把底栏 `GoldChipText` 写成当前组价格；组内全无则「购买道具组」，缺件则「补全道具组」，齐了或 `PropGroups[组名]>0` 则「已拥有道具组」并 `SetIsEnabled(false)`。右侧行按拥有态切 `PropSelectItemOwned/Unowned`，状态字「已拥有/未拥有」。`HandleAction` 仅打日志，商店 RPC 未实现。

## 六、待查证

- 未启动 PIE，运行态拥有态依赖 `AuctionPrivateState.OwnedProps/Props` 或 `PropGroups`；当前存档只有组库存，没有单件库存字段。
- 商店购买/补全扣费与写库存尚未有官方或项目 RPC，不能宣称已购买成功。
- 已打开的 UI 编辑器页签需要关闭后重新打开才能看到设计态切图。
