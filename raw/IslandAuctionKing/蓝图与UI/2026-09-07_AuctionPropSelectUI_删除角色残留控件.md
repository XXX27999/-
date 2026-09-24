# AuctionPropSelectUI 顶部/左侧方块排查与角色残留控件删除

> 类型：项目 UI 蓝图修改与回读证据
> 主题：编辑器设计器里 Collapsed 无贴图 UBorder 渲染成实心方块；复制残留控件清理
> 适用范围：IslandAuctionKing，`AuctionPropSelectUI`（道具选择界面，2026-09-07 由 `CharacterPropSelectTestUI` 复制新建）
> 证据状态：项目实测；UGCAskQ MCP 实时回读 + PRV 写入 + 回读验证已完成
> 来源：用户编辑器截图（`codex-clipboard-a4121e9a-*.png`，1928x1040）、UGCAskQ MCP `ue_py` / `ue_plan_submit`、工程 Lua
> 更新时间：2026-09-07
> 关联主题：控件树复制残留、UBorder 画刷、编辑器设计器可见性表现、widget_remove 清理流程
> 排除范围：未处理 `PropGroupPanel`（右侧）与 `FooterPanel`（底部）两个仍为 Collapsed 且无贴图的 UBorder；未修改 `AuctionCharacterSelectUI` / `AuctionHouseSelectUI`（后者仍复用 `CharacterButton01..06` 作为 `HouseButton*`）；未处理编辑器窗口自带的顶部黑条（非工程资产）
> 官方依据：[绿洲通用 UI 编辑规范与排错](../../知识/通用/UI与交互/绿洲通用UI编辑规范与排错.md)、[UGCAskQ-MCP 能力矩阵](../../知识/通用/工具与流程/UGCAskQ-MCP能力矩阵.md)

## 现象与定位

用户在绿洲 UI 编辑器里打开当天新建的道具选择界面，反馈"左上角有方块和黑点"。本会话收到的图像只能做像素分析，取证方式：

1. 截图尺寸 1928x1040，内容区约 (4,32) 起、1920x1000。
2. 用纯色连通域检测定位到设计画布：原点约 (292,176)，缩放约 0.6708（1288x724 ≈ 1920x1080）。
3. 画布内纯色块换算回控件坐标后，与 `AuctionPropSelectUI` 控件树一一对上：

| 画布实测（控件坐标） | rgb | 对应控件 | 运行时 Visibility |
| --- | --- | --- | --- |
| L=27 T=125 W=823 H=787 | 72,92,118 | `CharacterPanel`（Border，32,128,820x786） | Collapsed(1) |
| L=872 T=125 W=1020 H=787 | 72,92,118 | `PropGroupPanel`（Border，872,128,1016x786） | Collapsed(1) |
| L=27 T=935 W=1865 H=112 | 67,84,112 | `FooterPanel`（Border，32,930,1856x118） | Collapsed(1) |
| L=318 T=161 W=1284 H=58 | 68,85,113 | `TopPanel`（Border，320,160,1280x64） | Visible(0) |
| L=58 / L=456，T≈219~648 的成排小块 | 87~107 | `CharacterButton01..06` 及其 `CharacterLabel*` | Collapsed(1) |

结论：**编辑器设计器会把 Visibility=Collapsed 且 `Brush.ResourceObject=None` 的 UBorder/Button 照常画成实心色块**，因此从 `CharacterPropSelectTestUI` 复制来的角色选择一整套残留控件在道具选择界面里显示为方块。`AuctionUITextureReplacementService` 只对 `AuctionTestUI` 的面板键（HUDBackgroundPanel/TopBarPanel/…）做运行时贴图绑定，新界面的这几个 Border 没有任何绑定来源。

## 修改记录

目标资产：`/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/AuctionPropSelectUI`

写前备份（知识库备份目录）：

`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260907_HUDTopLeftCheck\uasset_before\AuctionPropSelectUI_before_remove_character_leftovers.uasset`

PRV 计划：`ue_plan_submit` → `plan_id = plan_16788216_6d421b4b`（intent：Remove collapsed character-select leftover widgets from AuctionPropSelectUI）

执行（`ue_py` 带 plan_id，事务名 `RemovePropSelectCharacterLeftovers`）：

```python
bp = ue.load_object(Blueprint, '/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/AuctionPropSelectUI')
for name in ['CharacterPanel','CharacterHeadingText','CharacterCounterText','CharacterDetailText',
             'CharacterButton01','CharacterButton02','CharacterButton03','CharacterButton04',
             'CharacterButton05','CharacterButton06']:
    ue.widget_remove(bp, name)
ue.compile_blueprint(bp); bp.save_package()
```

PRV 返回：`decision=pass`、`plan_valid=true`、`resolved_via_plan_id=true`、`has_mutation=true`、`writes_to_cdo=false`。

回读确认（`ue_py` 纯查询，事务名 `VerifyPropSelectUIRemoval`）：

- 控件数 38（修改前 48 顶层+子级），`character_leftover = []`
- `CharacterLabel01..06` 已随按钮一并移除
- 仍保留：`ScreenBackground`、`TopPanel`、`PropGroupPanel`、`FooterPanel`、`TitleText`、`SubtitleText`、`CloseButton`、`PropHeadingText`、`PropCounterText`、`PropButton01..06` + `PropLabel01..06`、`PropDetailText`、`PrevPageButton`、`PageText`、`NextPageButton`、`SummaryText`、`StatusText`、`ResetButton`、`ConfirmButton`

## Lua 配套清理

`Script/Blueprint/Prefabs/UI/AuctionPropSelectUI.lua`：删除已失效的 `---@field CharacterButton01..06`、`CharacterDetailText`、`CharacterLabel01..06` 共 13 行声明。

引用面检查：`AuctionPropSelectUIService.lua` 只引用 `PropButton%02d` 与道具详情文本，不引用任何 `Character*`；`AuctionCharacterSelectUIService.lua` / `AuctionCharacterSkillUIService.lua` 的 `CharacterButton%02d` 属于 `AuctionCharacterSelectUI`，`AuctionHouseSelectUI.lua` 仍把 `CharacterButton01..03` 别名成 `HouseButton*`，均不受本次删除影响。

## 待办与风险

- 剩余两个 Collapsed 无贴图 Border（`PropGroupPanel` 872,128,1016x786；`FooterPanel` 32,930,1856x118）在编辑器里仍是色块；要么删除，要么补运行时贴图绑定，待用户确认。
- 编辑器已打开的设计器页签不会自动刷新，需要关闭后重新打开 `AuctionPropSelectUI` 才能看到清理结果。
- 蓝图结构变更，生效方式为**重新调试 PIE**（非热更新）。

## 相关页面

- [AuctionTestUI 删除角色技能入口](./2026-09-01_AuctionTestUI_删除角色技能入口.md) — 同样的 `widget_remove` + 回读 + Lua 字段清理流程
- [绿洲通用 UI 编辑规范与排错](../../知识/通用/UI与交互/绿洲通用UI编辑规范与排错.md)
- [UGCAskQ-MCP 能力矩阵](../../知识/通用/工具与流程/UGCAskQ-MCP能力矩阵.md)
