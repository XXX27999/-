# 2026-09-09 AuctionCharacterSelectUI 切图绑定

> 类型：项目蓝图与 UI 记录
> 主题：AuctionCharacterSelectUI 按用户确认参考图绑定人物选择切图
> 适用范围：IslandAuctionKing 的 `/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/AuctionCharacterSelectUI`、`Script/Function/AuctionCharacterSelectUIService.lua`、`UIConfigTable` 的 `UI.CharacterSelect.*` 行、贴图目录 `/IslandAuctionKing/Asset/TuPian/AuctionUI/CharacterSelect`
> 证据状态：项目实测（UGCAskQ MCP 写入 + 回读）+ 官方 API 依据；FlaUI 枚举不到编辑器窗口，未截设计态；未启动 PIE
> 来源：用户参考图与切图 `C:\Users\Administrator\Desktop\素材\竞拍\人物选择`；UGCAskQ MCP `ue_plan_submit` / `ue_py`
> 更新时间：2026-09-09
> 关联主题：[2026-09-07_AuctionCharacterSelectUI_对齐网页预览](./2026-09-07_AuctionCharacterSelectUI_对齐网页预览.md)、[2026-09-09_AuctionPropSelectUI_切图绑定与拥有态](./2026-09-09_AuctionPropSelectUI_切图绑定与拥有态.md)、[资源导入与路径规范](../../知识/通用/配置与数据/资源导入与路径规范.md)
> 排除范围：未改 AuctionHouseSelectUI / AuctionPropSelectUI / AuctionTestUI / ZhuJieMian
> 官方依据：`D:\oasis-skill-plus\docs\wiki\新手入门\资源管理与编辑\277_资源导入.md`（PNG 导入）；`D:\oasis-skill-plus\docs\api\class\Others\UBorder.md`（`SetBrushFromTexture`）；`D:\oasis-skill-plus\docs\api\class\Others\UImage.md`（`SetBrushFromTexture`）

## 一、写前备份

`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260909_CharacterSelectArt\`

含 `AuctionCharacterSelectUI.uasset`、`AuctionCharacterSelectUI.lua`、`AuctionCharacterSelectUIService.lua`、`UIConfigTable.uasset`、英文切图副本、MCP 计划与 Python 载荷。

## 二、贴图导入

plan_id：`plan_16801684_9ba01067`（Import CharacterSelect UI PNG）

8 张 PNG 导入到 `/IslandAuctionKing/Asset/TuPian/AuctionUI/CharacterSelect`。回读全部 `Texture2D`，五项属性 `(LODGroup, MipGenSettings, CompressionSettings, CompressionQuality, SRGB) = (16, 13, 0, 5, True)`。

| 资产 | 尺寸 |
| --- | --- |
| CharacterSelectPanel | 1685x778 |
| CharacterSelectPortraitFrame | 293x285 |
| CharacterSelectClose | 68x69 |
| CharacterSelectPosBox | 630x155 |
| CharacterSelectSkillBox | 630x196 |
| CharacterSelectNameBar | 242x40 |
| CharacterSelectSkillTitle | 426x40 |
| CharacterSelectConfirm | 334x76 |

参考图 `参考图.png` 为 1870x841，底图在参考图内 bbox `(93,17)`，落到 1920x1080 画布为 `SheetX=118, SheetY=151`。

## 三、蓝图绑定

plan_id：`plan_16802180_3d7ac159`（used_count=2）

新增并回读存在：`CharacterNameBar`、`CharacterSkillTitleBar`、`CharacterFrame01-06`。底板 `SheetBorder` 绑 `CharacterSelectPanel`，关闭钮绑 `CharacterSelectClose`，确认钮绑 `CharacterSelectConfirm`。

plan_id：`plan_16803707_d7a05958` 将 `ScreenBackground` 设为 `0,0 / 1920x1080`。回读 `p=[0,0] s=[1920,1080] vis=0`。

最终回读：

- `SheetBorder` 118,151 / 1685x778
- `CharacterFrame01` 167,269 / 293x285
- `CharacterFrame06` 797,570 / 293x285
- `CharacterPosBox` 1130,335 / 630x155
- `CharacterSkillBox` 1136,547 / 630x196
- `ConfirmButton` 1281,798 / 334x76
- `CloseButton` 1700,163 / 68x69

## 四、配置表

plan_id：`plan_16802538_8b056f32`（WriteCharacterSelectConfigRows）

`UIConfigTable` 回读：`SheetWidth=1685`、`CardWidth=293`、`ConfirmX=1281`、`UI.CharacterSelect.Texture.Panel=Asset/TuPian/AuctionUI/CharacterSelect/CharacterSelectPanel.CharacterSelectPanel`。

## 五、Lua

`AuctionCharacterSelectUIService.lua`：函数内读 `UI.CharacterSelect.*`；`ApplyLayout` 按切图像素摆放并 `SetBrushFromTexture`；确认钮保持白色乘色，避免盖住切图。`luaparser` SYNTAX OK。

## 六、待查证

- FlaUI `--list` 未枚举到 `ShadowTrackerExtraUGCEditor`，设计态截图未完成。已打开的 UI 编辑器页签需要关闭后重新打开才能看到切图。
- 未启动 PIE，运行态选中、锁定盖章与确认钮文字需重新调试 PIE 验证。
- 角色立绘仍无素材，卡内 `CharacterArt` 用灰色占位，不盗用其他游戏素材。
