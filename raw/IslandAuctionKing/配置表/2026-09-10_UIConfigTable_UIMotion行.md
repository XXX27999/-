> 类型：项目证据
> 主题：配置表 / UI 动效
> 适用范围：IslandAuctionKing 的 `/IslandAuctionKing/Asset/Data/Table/Customized/UI/UIConfigTable`
> 证据状态：项目实测
> 来源：UGCAskQ MCP `ue_read` / `ue_plan_submit` / `ue_py`；`data_table_find_row` 回读；工程文件 `Asset/Data/Table/Customized/UI/UIConfigTable.uasset`、`Script/Function/CharacterPropSelectTestUIService.lua`、`Script/Function/DragTestUIService.lua`
> 更新时间：2026-09-10
> 关联主题：AuctionUIMotionService、UGCTweenSystem、EEasingType、AuctionUIConfigTableService
> 排除范围：不覆盖大厅、选择层、竞拍主界面、图鉴、结算业务脚本；不把本轮未启动的 PIE 写成已验证运行效果
> 官方依据：`D:\知识库\和平精英绿洲起源\raw\docs\api\class\Others\UGCTweenSystem.md`；`D:\知识库\和平精英绿洲起源\raw\docs\api\cppenum\E\EE\EEasingType.md`；`D:\知识库\和平精英绿洲起源\raw\docs\wiki\通用功能\20351_Tween功能.md`

# UIConfigTable UI.Motion 行

## 写前备份

`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260910_UIMotion\`

含 `UIConfigTable.uasset`、`UIConfigTable_before_UIMotion.uasset`、PRV plan 与 `ue_py` 回读 JSON。禁止把备份放进 UGC 工程 Backup/。

## MCP 流程

1. Resolve：`ue_read` 查询 `ctx:`、`py:data_table_add_row`、`py:data_table_empty_row`、`py:data_table_find_row`、`py:data_table_modify_row`、`py:guide datatable`。
2. Plan：`ue_plan_submit` 得到 `plan_id=plan_16796695_640bc434`，`asset_path=/IslandAuctionKing/Asset/Data/Table/Customized/UI/UIConfigTable`，`plan_valid=true`。
3. Execute：`ue_py` 事务 `WriteUIConfigTableMotionRows`。`data_table_add_row` 返回 `None`，不以返回值判定成功。
4. 独立回读：再次 `ue_py` 对 6 行执行 `data_table_find_row`，`missing=[]`。

写前只读：表已有 268 行，`UI.Motion.*` 为空，列名为 `ValueType` / `Value` / `Description` / `ModificationNotes`。

## 回读值

| 行名 | ValueType | Value |
| --- | --- | --- |
| `UI.Motion.Enabled` | bool | true |
| `UI.Motion.PressScale` | float | 1.08 |
| `UI.Motion.PressDuration` | float | 0.16 |
| `UI.Motion.FadeInDuration` | float | 0.22 |
| `UI.Motion.FadeOutDuration` | float | 0.16 |
| `UI.Motion.PanelDuration` | float | 0.18 |

`Description` 与 `ModificationNotes` 含用途、边界和“生效：重新 PIE”。MCP JSON 控制台中文会乱码；工程 `.uasset` 以 UTF-16LE 保存，可检索到 `AuctionUIMotionService`、`PlayPress`、`PrepareFadeIn`、`PlayFadeIn`、`PlayFadeOutThen`、`PlayPanelOpen` 和“生效”。

落盘后 `UIConfigTable.uasset` 从 83763 字节变为 86686 字节，时间 2026-09-10 15:52:32。

## Lua 接入（本轮允许文件）

- `CharacterPropSelectTestUIService.CreateAndShow`：`PrepareFadeIn` 后 `AddToViewport`，再 `PlayFadeIn`。
- `CharacterPropSelectTestUIService.BindEvents`：角色/道具槽、翻页、重置、确认、关闭按钮包装 `PlayPress`，回调写入 `CharacterPropCharacterCallbacks` / `CharacterPropGroupCallbacks` / `CharacterProp*PressCallback`。
- `CharacterPropSelectTestUIService.Shutdown`：解绑同一函数后把 `PressCallback` 置空。
- `DragTestUIService.CreateAndShow`：打开淡入。`CloseButton` 走 `_CloseButtonCallback` 的 `PlayPress`；拖拽位移逻辑未改。
- `CharacterPropSelectTestUI.lua`：`Construct` / `Destruct` 仍只委托功能模块，无额外业务。

`AuctionConfig.UIConfigTablePath` 已注册为 `Data/Table/Customized/UI/UIConfigTable`，无需改 `AuctionConfig`。`AuctionUIMotionService` API 形状本轮未改。

## 验证

- Lua 语法：`luaparser` 解析 3 个允许脚本通过。
- 本轮未启动 PIE。配置表修改必须重新调试 PIE 才生效。

## 后续追加（2026-09-16）

- 新增 7 行 `UI.Motion.WarehouseFeedback.*`（品质/道具仓库反馈动效），详见 [2026-09-15_仓库反馈动效](..\开发记录\2026-09-15_仓库反馈动效_高亮闪烁渐显弹出.md)。
- 新增 19 行 `UI.Motion.ClueFeedback.*`（全部线索类型反馈动效，含开局线索）：`Enabled`、`PopScale`(1.45)、`PopDuration`(0.18)、`FadeFromOpacity`(0.30)、`FlashCount`(4)、`FlashDuration`(0.13)、`FlashMinOpacity`(0.28)、`FlyInOffsetX`(0)、`FlyInOffsetY`(-36)、`WaveDuration`(0.78)、`WaveStaggerRatio`(0.45)、`MaxTargets`(36)、`ReplayOnFirstObserve`(true)、`IntelCardFlashEnabled`(true)、`HighlightColor`/`SkillHighlightColor`/`PublicIntelHighlightColor`/`OutlineHighlightColor`/`AggregateHighlightColor`（R,G,B,A 字符串）。
  - plan_id `plan_16792454_89042d0f`；`data_table_add_row` 返回 `None` 不以返回值判定，独立回读 `missing=[]`。
  - 消费方：`AuctionUIMotionService` + 新增 `AuctionClueFeedbackService`。
  - 详见 [2026-09-16_竞拍仓库藏品线索动效全覆盖](..\开发记录\2026-09-16_竞拍仓库藏品线索动效全覆盖.md)。
- 经验：`data_table_get_all_rows()` 返回 **list of UScriptStruct**（无行名），要按行名取用 `data_table_as_dict()` 或 `data_table_find_row(名)`。

## 待查证

1. PIE 中 `AuctionUIConfigTableService.LoadAndApplyConfig` 是否把 6 行 `UI.Motion.*` 写进 `AuctionConfig`。
2. 测试页与拖拽测试 UI 的实际 Tween 观感，需 PIE 日志确认。
3. `UI.Motion.ClueFeedback.*` 在 PIE 中是否按预期加载（`SetRenderTranslation` 是否对 `UButton`/`UImage` 生效）。
