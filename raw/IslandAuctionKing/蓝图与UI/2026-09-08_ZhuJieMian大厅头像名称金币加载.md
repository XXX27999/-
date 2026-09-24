# ZhuJieMian 大厅头像、名称、金币加载

> 类型：项目证据
> 主题：ZhuJieMian 红框三处：右上金币数字、左下头像框、玩家名称条
> 适用范围：IslandAuctionKing，`ZhuJieMian` 主界面大厅身份区
> 证据状态：项目实测；UGCAskQ MCP 写入后独立回读通过；Lua 结构检查通过；未启动 PIE
> 来源：用户截图 `D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260908_HubLayoutAvatarRematch\ZhuJieMian_redboxes.png`；UGCAskQ MCP `ue_plan_submit` / `ue_py`；`Script/Function/AuctionHubUIService.lua`、`Script/Blueprint/Prefabs/UI/ZhuJieMian.lua`
> 更新时间：2026-09-08
> 关联主题：AuctionHubUIService、ZhuJieMian、UIConfigTable、APlayerState.PlayerName
> 关联主题：AuctionHubUIService、ZhuJieMian、UIConfigTable、APlayerState.PlayerName、[主界面点击层与大厅功能接入](./2026-09-08_ZhuJieMian主界面点击层与大厅功能接入.md)
> 排除范围：不总结通用摆放知识；不做二次匹配；不改 AuctionHouseSelectUI / AuctionCharacterSelectUI / AuctionPropSelectUI / AuctionGameService / UGCPlayerController；不编造玩家头像 API
> 官方依据：[UTextBlock.SetText](D:\oasis-skill-plus\docs\api\class\Others\UTextBlock.md)、[UTextBlock.SetColorAndOpacity](D:\oasis-skill-plus\docs\api\class\Others\UTextBlock.md)、[UImage.SetBrushFromTexture](D:\oasis-skill-plus\docs\api\class\Others\UImage.md)、[UUserWidget.GetWidgetFromName](D:\oasis-skill-plus\docs\api\class\Others\UUserWidget.md)、[APlayerState.PlayerName](D:\oasis-skill-plus\docs\api\class\Others\APlayerState.md)、[UGCPawnAttrSystem.GetPlayerName 废弃](D:\oasis-skill-plus\docs\api\class\和平全局接口\角色系统\UGCPawnAttrSystem.md)

## 现象

用户截图红框三处：

1. 右上金币条几乎看不到数字，只剩金币图标。
2. 左下头像框是空框。
3. 玩家名称条仍显示贴图占位「玩家名称」。

## 查证

| 项 | 结论 | 证据状态 |
| --- | --- | --- |
| `UTextBlock.SetText` | 官方存在，Refresh 写金币/名称用它 | 官方确认 |
| `UTextBlock.SetColorAndOpacity` | 官方存在 | 官方确认 |
| `UImage.SetBrushFromTexture` / `SetBrushImageReference` | 官方存在，可用于贴图；本轮未用于玩家头像 | 官方确认 |
| `UGCPlayerControllerSystem` 玩家昵称/头像 | 无 `GetPlayerName` / Avatar / Profile | 官方未确认 |
| `UGCAttributeSystem` 玩家昵称 | 无 `GetPlayerName` | 官方未确认 |
| `UGCPawnAttrSystem.GetPlayerName` | 存在但标注【废弃】，参数是 `PlayerPawn`，大厅无 Pawn 时不能当昵称源 | 官方确认（废弃） |
| 玩家头像/肖像 API | `verify-api` / `search "头像"` 无玩家资料头像接口；Avatar 命中均为角色换装/展示 Actor | 知识库未覆盖 / 官方未确认 |
| `APlayerState.PlayerName` | 官方字段 `FString`，结算身份解析已用过 | 官方确认 |
| 私有状态 | `AuctionPlayerService.BuildPrivateState` 与 `CF_FWDRPC.ClientAuctionPrivateState` 有 `Gold` / `PlayerKey`，没有 `PlayerName` | 项目实测 |

MCP 写入前回读（事务 `ReadZhuJieMianAvatarNameGold`）：

| 控件 | Slot | Font | 文本 |
| --- | --- | --- | --- |
| `GoldValueText` | 右上锚点 `x=-250,y=36,w=200,h=44,z=20`，仍在金币条内 | `Size=0`，`FontObject=None` | `30,000` |
| `PlayerNameText` | 左上锚点 `x=191,y=588,w=303,h=40,z=20`，不在名称胶囊上 | `Size=0`，`FontObject=None` | `玩家名称` |
| `头像框` | 底左锚点 `x=47,y=-172.571,w=153.571,h=154.286` | 画刷 `ZJM5` | 空框素材 |

金币看不见不是坐标跑出条外，而是字号被写成 0。名称条上的「玩家名称」是 `玩家名称` Image 贴图字；动态 `PlayerNameText` 当时不在胶囊上。

## 修改

写前备份：

`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260908_HubLayoutAvatarRematch\AvatarNameGold\`

蓝图计划：`plan_16784395_1a4955b6`，事务 `FixZhuJieMianGoldNameFonts` / `FixZhuJieMianPlayerNameSlot`。

配置表计划：`plan_16784884_43f03715`，事务 `WriteHubGoldNameAvatarRows`。

1. `GoldValueText` 保持用户已摆正的右上 `x=-250,y=36`，只恢复 `Roboto Bold 22` 和白色。
2. `PlayerNameText` 改到底左锚点 `x=208,y=-112,w=310,h=40,z=20`，落到名称胶囊文字区；设计态清空贴图占位字。
3. `AuctionHubUIService.Refresh` 写真实 `privateState.Gold`；名称优先 `PlayerState.PlayerName`，否则 `PlayerKey` / `UID`，禁止静默「玩家名称」。
4. 头像框只绑定 `头像框` / `AvatarImage` 并保持空框。官方未确认玩家头像 API，未编造加载。
5. `UIConfigTable` 新增 `UI.Hub.Gold.Color*`、`UI.Hub.PlayerName.Color*`、`UI.Hub.Avatar.PlaceholderNote`。

独立回读（事务 `VerifyZhuJieMianAvatarNameGold`）`checks` 全为 true：

- `goldInsideBar=true`，`goldFont22=true`
- `nameBottomLeft=true`，`nameFont22=true`
- `avatarPresent=true`
- `tabsUnchanged=true`

顶部仓库/装扮/签到/商城/邮件按钮坐标未改。

## 待查证

1. PIE 运行时 `PlayerState.PlayerName` 在绿洲大厅是否有真实昵称，还是空串后回退 `PlayerKey`。
2. 是否存在未入库的玩家头像/肖像官方 API。当前保持空框。
