# 绿洲 UI 动效与 Tween

> 类型：概念索引
> 来源：[绿洲 UI 动效与 Tween 正文](../../raw/知识/通用/UI与交互/绿洲UI动效与Tween.md)、[2026-09-10 UI 动效与 Tween](../../raw/知识/通用/来源记录/2026-09-10_UI动效与Tween.md)
> 官方依据：[Tween 动画使用指南](../../raw/docs/wiki/通用功能/20351_Tween功能.md)、[UGCTweenSystem](../../raw/docs/api/class/Others/UGCTweenSystem.md)、[EEasingType](../../raw/docs/api/cppenum/E/EE/EEasingType.md)、[UWidget](../../raw/docs/api/class/Others/UWidget.md)
> 最近更新：2026-09-16

## 索引摘要

本页只提供导航。官方给 UI 加反馈和平滑切换的入口是客户端 Lua `UGCTweenSystem`：缩放走 `SetRenderScale`，淡入走 `SetRenderOpacity`，位移走 Canvas Slot `SetPosition`，序列走 `ChainTween`。Tween 只在客户端生效；`PlayAnimation` 的 Lua 可调性未覆盖。

**句柄生命周期硬约束（2026-09-16 项目实测）**：一个 `FTweenHandle` 只允许 `KillTween` 一次；被多个控件共享后逐个 kill，第 2 次触发 `Map.h:586 Pair != nullptr` 断言，客户端卡数秒后 `appError` 闪退。`IsTweenValid` 不足以防重复 kill；也不要在完成回调里 Kill 自己。详见正文「句柄生命周期」一节。

- **Raw 正文**：[绿洲 UI 动效与 Tween 正文](../../raw/知识/通用/UI与交互/绿洲UI动效与Tween.md)
- **来源记录**：[2026-09-10 UI 动效与 Tween](../来源/2026-09-10_UI动效与Tween.md)
- **相关页面**：[绿洲通用 UI 编辑规范与排错](./绿洲通用UI编辑规范与排错.md)、[UI 页面切换与 Widget 生命周期](./UI页面切换与Widget生命周期.md)
