# AuctionTestUI WidgetTree Outer 断言修复

> 类型：项目事实 / 编辑器 UMG ensure 修复
> 主题：`Ensure condition failed: Widget->GetOuter() == Blueprint->WidgetTree`、`AuctionTestUI` 控件树对象归属
> 适用范围：`IslandAuctionKing` 项目，`AuctionTestUI` UI 蓝图
> 证据状态：MCP 实测；写前快照、MCP Execute、编译保存、重新加载回读和 UI 全树回归均完成；PIE 上传验证通过，但后端调试服务请求失败，未生成 client/DS/DebugID
> 来源：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\Saved\Logs\ShadowTrackerExtra.log`、UGCAskQ MCP `ue_read`/`ue_py`、项目蓝图与 Lua
> 更新时间：2026-09-15
> 关联主题：[2026-09-14 编辑器连续闪退日志分析](./2026-09-14_编辑器连续闪退日志分析.md)、[2026-09-01 AuctionTestUI 轮次详情素材导入与对齐](../蓝图与UI/2026-09-01_AuctionTestUI_轮次详情素材导入与对齐.md)、[MCP UI 编辑与高保真还原知识库](../../知识/通用/UI与交互/MCP-UI编辑与高保真还原知识库.md)
> 排除范围：本页不证明编辑器安装资源、AIGC 地形缓存或 Lua 是本次 ensure 根因；不把本轮 PIE 后端服务失败归因于 WidgetTree 修复
> 官方依据：本地官方 API/Wiki 未直接确认该 `WidgetBlueprint.cpp` 断言；控件树读写流程参考 `D:\知识库\和平精英绿洲起源\raw\知识\通用\UI与交互\MCP-UI编辑与高保真还原知识库.md`

## 现象

2026-09-15 10:18:05，编辑器在 `UGCProjectBrowserBridge.OpenProject` 项目打开流程中报告：

```text
Ensure condition failed: Widget->GetOuter() == Blueprint->WidgetTree
[File:D:\CG038\Survive\Plugins\UGCEditor\Source\UGCUMGEditor\Private\WidgetBlueprint.cpp]
[Line: 682]
```

异常前完成了多个 UI 蓝图编译。项目配置还显示 `CleanShutdown=False`，自动恢复资产为 `ZhuJieMian`。

## MCP 定位

使用 `ue_py` 从各自 `WidgetTree.RootWidget` 递归 `Slots.Content` 检查 10 个 UI 蓝图。只有 `AuctionTestUI` 存在 Outer 异常：

| 控件 | 类型 | 错误 Outer | 父级 | Slot |
| --- | --- | --- | --- | --- |
| `Image_0` | Image | `RoundDetailContent` | `RoundDetailContent` | `56,318 / 145x50`, Z=-5 |
| `Image_1` | Image | `RoundDetailContent` | `RoundDetailContent` | `42,355 / 204x72`, Z=-10 |
| `TextBlock_0` | TextBlock | `RoundDetailContent` | `RoundDetailContent` | `56,326 / 145x32`, Z=5 |
| `Image_2` | Image | `RoundDetailContent` | `RoundDetailContent` | `56,432 / 145x50`, Z=-5 |
| `Image_3` | Image | `RoundDetailContent` | `RoundDetailContent` | `42,469 / 204x100`, Z=-10 |
| `TextBlock_1` | TextBlock | `RoundDetailContent` | `RoundDetailContent` | `56,440 / 145x32`, Z=5 |

这 6 个控件的层级看似正确，但对象 Outer 指向父 `CanvasPanel`，不满足编辑器断言；其余 9 个 UI 蓝图及 `AuctionTestUI` 其他节点均为 `Outer=WidgetTree`。

## 修复

写入前备份：

`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260915_AuctionTestUI_WidgetOuter修复\AuctionTestUI_before_WidgetOuterFix.uasset`

备份 SHA-256：`0EF05C93BA68EF7B816CFCABF97296EC4355058F7BB3B2C7E6EA63BA3C9E4682`。

使用 UGCAskQ MCP `Resolve → Plan → Execute`，计划号 `plan_16780590_12ea74be`，目标资产 `/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/AuctionTestUI`：

1. 删除 6 个游离节点。
2. 使用 `widget_add(wbp, type, name, "RoundDetailContent")` 按原类型、名称、父级重建。
3. 恢复原 `Brush`、`Text`、`Font`、`ColorAndOpacity`、`Visibility`、Canvas `Offsets` 和 `ZOrder`。
4. 编译并保存蓝图。

第一次事务因使用旧 Slot 句柄失败，MCP 自动回滚；第二次从 `RoundDetailContent.Slots.Content` 获取新句柄，并通过 `LayoutData.Offsets` 恢复布局，执行成功。

## 验证

- 6 个节点重新加载后均为 `Outer=WidgetTree`。
- 6 个节点父级均为 `RoundDetailContent`，类型、Visibility、Offsets、ZOrder 与写前快照一致。
- `AuctionTestUI` 全树 469 个节点，`outer_bad=[]`；另外 9 个 UI 蓝图也全部 `outer_bad=[]`。
- `ue.objed_open_asset("AuctionTestUI", "UI")` 返回成功；编辑器回读为已编译、无未保存修改。
- 修复后日志没有新增该 WidgetTree ensure；旧日志中的两条 10:18:05 记录保留为历史。

## PIE 边界

本轮单人 PIE 已通过上传文件验证、上传文件名验证和 Lua 文件验证；随后日志报告 `PIE debug failed: start debug request failed`，没有 client、DS 或 DebugID。会话已停止并回读为 `phase=stopped`。因此编辑器资产级和打开级修复已验证，完整运行时 UI 行为仍需后端调试服务恢复后重新 PIE。

## 证据分类

- 项目实测：6 个节点的 Outer 错误、MCP 重建、编译保存、回读和全 UI 回归。
- 官方未确认：本地官方 API/Wiki 未直接记录 `WidgetBlueprint.cpp:682` 的断言语义。
- 推断：该类错误与 UI 控件通过错误对象创建/重挂载路径产生游离 Outer 有关；本推断不升格为官方通用机制。
- MCP 状态：`ue_read`、`ue_plan_submit`、`ue_py` 已调用；计划执行成功，写后回读通过。
