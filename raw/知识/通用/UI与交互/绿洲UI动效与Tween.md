# 绿洲 UI 动效与 Tween

> 类型：通用知识
> 主题：UI / Tween / UGCTweenSystem / WidgetAnimation
> 适用范围：全局通用（绿洲 UMG 客户端动效）
> 证据状态：官方确认 + 冲突 + 知识库未覆盖
> 来源：[Tween 动画使用指南](../../../docs/wiki/通用功能/20351_Tween功能.md)、[UGCTweenSystem](../../../docs/api/class/Others/UGCTweenSystem.md)、[EEasingType](../../../docs/api/cppenum/E/EE/EEasingType.md)、[UWidget](../../../docs/api/class/Others/UWidget.md)、[UUserWidget](../../../docs/api/class/Others/UUserWidget.md)、[2026-09-10 UI 动效与 Tween](../来源记录/2026-09-10_UI动效与Tween.md)
> 更新时间：2026-09-18
> 关联主题：UGCTweenSystem、EEasingType、UWidget.SetRenderOpacity、UWidget.SetRenderScale、UGCWidgetManagerSystem.SlotAsCanvasSlot、UI页面切换与Widget生命周期、绿洲通用UI编辑规范与排错、Tween 句柄生命周期
> 排除范围：不覆盖骨骼/怪物动画蓝图、技能 Task 动画、3D 角色预览动画；不把 IslandAuctionKing 未 PIE 的运行观感写成已验证；不把 `UUserWidget.PlayAnimation` 写成已验证的 Lua 入口
> 官方依据：`D:\知识库\和平精英绿洲起源\raw\docs\wiki\通用功能\20351_Tween功能.md`；`D:\知识库\和平精英绿洲起源\raw\docs\api\class\Others\UGCTweenSystem.md`；`D:\知识库\和平精英绿洲起源\raw\docs\api\cppenum\E\EE\EEasingType.md`；`D:\知识库\和平精英绿洲起源\raw\docs\api\class\Others\UWidget.md`；`D:\知识库\和平精英绿洲起源\raw\docs\wiki\版本日志\20361_1.36 Release Notes.md`

## 来源与官方依据

| 证据 | 状态 | 结论边界 |
| --- | --- | --- |
| Wiki `20351_Tween功能.md` | 官方确认 | Tween 明确适用于按钮缩放、淡入淡出、颜色变化、进度条/数值计数、UI 元素移动；创建后默认自动执行。 |
| Wiki 文首注意 | 官方确认 | 「Tween动画只在客户端生效，相关的接口也只能在客户端调用。」 |
| API `UGCTweenSystem` | 官方确认 | Lua 接口库。函数页标注「生效范围：服务器&客户端」。与 Wiki 客户端限制冲突，不得静默覆盖。 |
| 1.36 Release Notes | 官方确认 | 「新增Tween动画系统，支持位置、旋转、颜色等数值的平滑过渡，适用于UI动效与场景变换」。 |
| `UWidget.SetRenderOpacity` / `SetRenderScale` / `SetRenderTranslation` | 官方确认 | Tween 回调可写的 Widget 渲染属性。 |
| `UWidget.SetRenderAngle` | 官方确认 | 旋转用 `SetRenderAngle(float)`。本地 API 目录中**查无 `SetRenderTransformAngle`**（2026-09-17 全库检索），沿用旧写法会调用到 nil。 |
| `UGCWidgetManagerSystem.SlotAsCanvasSlot` | 官方确认 | 获取 Canvas 插槽；生效范围：客户端。 |
| `UCanvasPanelSlot.SetPosition` | 官方确认 | 参数 `InPosition: FVector2D`。 |
| `EEasingType` | 官方确认 | 枚举值为 `Linear`、`QuadIn`、`QuadOut`、`QuadInOut` 等，没有 `EaseOutQuad`。 |
| Wiki 示例 `EEasingType.EaseOutQuad` | 冲突 | 与 API 枚举名不一致。代码优先写 API 名 `QuadOut`；`EaseOutQuad` 是否别名未在本地 API 确认。 |
| `UUserWidget.PlayAnimation` / `UWidgetAnimation` | 官方确认存在，Lua 可调性未覆盖 | API Language 为 `cpp`。官方 UI 系统 Wiki 无操作页。1.29 只证明编辑器曾修复「UI动画和序列动画轨道编辑」。 |
| IslandAuctionKing AuctionUIMotionService and UIConfigTable UI.Motion rows | 项目实测 | 2026-09-10 已落地客户端 Tween 封装，并由测试页/拖拽测试 UI 调用；配置行见项目页 [2026-09-10_UIConfigTable_UIMotion行](../../IslandAuctionKing/配置表/2026-09-10_UIConfigTable_UIMotion行.md)。未启动 PIE，不把运行观感写成已验证。 |

## 核心结论

Wiki 能给 UI 加动效。官方推荐入口是客户端 Lua 的 `UGCTweenSystem`，不是另做一套 Tick 插值，也不是未验证的 UMG 时间线 Lua 调用。

可做的反馈与平滑切换：

1. **点击反馈**：`TweenFloatValue` 改缩放，回调里 `Widget:SetRenderScale(UGCMathUtility.MakeVector2D(Value, Value))`，`MakeConfig(0, 0, true, 0)` 做一次放大再回弹。
2. **页面/面板出现**：先把透明度设为 0，再用 `TweenFloatValue` 回调 `SetRenderOpacity` 淡入。
3. **位置滑动**：`TweenVectorValue` + `UGCWidgetManagerSystem.SlotAsCanvasSlot(Widget):SetPosition(UGCMathUtility.MakeVector2D(Value.X, Value.Y))`。
4. **颜色变化**：`TweenColorValue` + `SetColorAndOpacity`。
5. **数值滚动**：`TweenFloatValue` 驱动文本/进度，适合结算估值累加这类展示。
6. **多步切换**：`ChainTween` 把淡入、位移、缩放串起来。

硬约束：

- UI 动效只在客户端跑。服务端金币、仓库、出价仍走权威逻辑，禁止用 Tween 改权威数据。
- 同一属性不要并行两个 Tween；换动画先 `KillTween` 或 `ChainTween`。
- `KillTween` 会把对象拉回起始值；只要停在当前值用 `PauseTween`。
- `RepeatCount` 必须显式传：`0` 播一次，`-1` 无限。不要依赖 `MakeConfig` 默认值 `1`。
- 回调签名是 `function(Object, Value)`。`Object` 是占位，当前值在第二个参数。不要在回调里再创建 Tween。
- 时长、缩放倍率、透明度起止值属于可调参数，项目落地时进对应功能 DataTable，禁止硬编码后当最终值。

## 可执行步骤

客户端 Widget 脚本里，在点击、打开页面或切换面板时创建 Tween。创建后默认播放，不需要先 Pause 再 Resume。

```lua
-- 点击缩放反馈。只在客户端调用。
function SomeUI:OnClickButton()
    ugcprint("【SomeUI+OnClickButton】入口")
    local Button = self.ClickButton
    if Button == nil then
        ugcprint("【SomeUI+OnClickButton】错误 Button 为空")
        return
    end

    local Callback = function(Object, Value)
        Button:SetRenderScale(UGCMathUtility.MakeVector2D(Value, Value))
    end
    local Config = UGCTweenSystem.MakeConfig(0, 0, true, 0)
    self.ClickTweenHandle = UGCTweenSystem.TweenFloatValue(
        1.0,
        1.2,
        0.2,
        EEasingType.QuadOut,
        Callback,
        Config
    )
    ugcprint("【SomeUI+OnClickButton】出口 已创建点击缩放 Tween")
end
```

```lua
-- 面板淡入。打开前先把透明度置 0。
function SomeUI:PlayFadeIn(Widget)
    ugcprint("【SomeUI+PlayFadeIn】入口")
    if Widget == nil then
        ugcprint("【SomeUI+PlayFadeIn】错误 Widget 为空")
        return
    end
    Widget:SetRenderOpacity(0.0)
    local Callback = function(Object, Value)
        Widget:SetRenderOpacity(Value)
    end
    local Config = UGCTweenSystem.MakeConfig(0, 0, false, 0)
    self.FadeTweenHandle = UGCTweenSystem.TweenFloatValue(
        0.0,
        1.0,
        0.25,
        EEasingType.QuadOut,
        Callback,
        Config
    )
    ugcprint("【SomeUI+PlayFadeIn】出口")
end
```

官方组合序列是淡入 -> 位移 -> 缩放，用 `UGCTweenSystem.ChainTween(FadeHandler, MoveHandler)` 再 `ChainTween(MoveHandler, ScaleHandler)`。完成时用 `BindCompletedDelegate` 再切页面或显示下一张卡。

pet_paradise 已把上述规则固化成可复用库 `Script/Common/UI/UIMotionKit.lua`：6 档动效令牌 + 6 态状态矩阵 + 句柄组（防二次 Kill）+ 同属性不并行分键 + 服务端拦截 + 减弱动效降级；接入示例与实测校验见 [2026-09-17_UI动效方案与Tween落地](../../pet_paradise/蓝图与UI/2026-09-17_UI动效方案与Tween落地.md)。

缓动优先用 API 枚举：点击反馈 `QuadOut`，出现 `QuadOut`/`SineOut`，强调回弹才用 `BackOut`/`ElasticOut`。Wiki 示例里的 `EEasingType.EaseOutQuad` 与 API `QuadOut` 冲突，未验证前不要抄示例名。

## 句柄生命周期：同一句柄禁止重复 KillTween

> 证据状态：项目实测（2026-09-16，IslandAuctionKing 客户端 PIE 崩溃现场）。官方 API 未记录 `KillTween` 的重复调用语义，也未记录该断言，故本条只保证「重复 KillTween 会崩」这一现象，不推断引擎内部实现必然如此。

现象与硬证据：

```text
[15.53.06:776] LogScriptPlugin: Warning: [LuaException] OnLogLuaStack: Assertion failed:Pair != nullptr,
Assertion failed: Pair != nullptr [File:<Engine>/Source/Runtime/Core/Public/Containers/Map.h] [Line: 586]
[15.53.11:667] LogWindows: Error: appError called: Assertion failed: Pair != nullptr ...
```

崩溃前的 Lua 栈（`UnrealTweenBlueprintLibrary.KillTween` 为最内层）：

```text
[C]: in field '?'                                 -- KillTween
ugc/UGCAPI/UGCTweenSystem.lua:228
Script/Function/<项目服务>.lua:120                -- KillHandle 里的 pcall(KillTween)
Script/Function/<项目服务>.lua:624                -- StopClueMotion
Script/Function/<项目服务>.lua:872                -- Tween 完成回调内再次 Stop
ugc/UGCAPI/UGCTweenSystem.lua:251                 -- 官方完成回调分发
```

结论与硬约束：

1. **一个 `FTweenHandle` 只允许 `KillTween` 一次。** 同一个句柄被多个控件/多个状态对象共享持有、逐个 kill 时，第 2 次 `KillTween` 会触发 `Map.h:586` 断言（`Pair != nullptr`），引擎弹 Assert 同步对话框并判定应用不可继续，数秒后 `appError` 崩溃闪退。
2. **`IsTweenValid` 不能当作重复 kill 的唯一防线。** 实测在句柄已被 Kill 之后它仍可能返回 `true`，于是「先 `IsTweenValid`，有效则 `KillTween`」的写法拦不住第二次 kill。必须自己记录「该句柄已销毁」。
3. **不要在 Tween 的完成回调里 Kill 自己。** 完成回调触发时该 Tween 已结束，回调里应只做视觉复位与清空句柄引用，不要再走 Kill 路径。
4. 共享句柄的正确写法是「一次创建、一次销毁、引用者只清引用」：创建时把句柄挂在一个共享「组」对象上（如 `{ Handle = H, Killed = false }`），销毁时先判组是否已销毁，销毁后只把各持有者的字段置 nil；或改用已销毁标记表按句柄去重。
5. 崩溃表现容易误判：客户端弹「Assertion Failed」框**卡住数秒**，点掉后进程退出；同一时刻 DS 侧日志无错且仍在写，容易被误读成「DS 卡死」。排查时先看客户端 FullLog 的 `LogWindows: Error: appError` 与它上方的 Lua 栈。

## 常见错误

- 在 `HasAuthority()==true` 的服务端路径调 Tween，或用 Tween 改金币/仓库。Wiki 明确只在客户端生效。
- 模块加载时创建 Tween。Widget 尚未 Construct，回调目标为空。
- 同一按钮连点创建多个缩放 Tween。先 `IsTweenValid`，有效则 `KillTween`；但 `IsTweenValid` 在句柄已销毁后仍可能返回 `true`，不能作为唯一防线。
- 多个控件共享同一句柄后各自 `KillTween`。第 2 次调用触发 `Map.h:586 Pair != nullptr` 断言，客户端卡住数秒后 `appError` 闪退。
- 在 Tween 的完成回调里 Kill 自己。完成回调触发时 Tween 已结束，只做视觉复位与清空引用。
- 把 `UUserWidget.PlayAnimation` 当 Lua 标准入口。该页 Language 是 `cpp`，官方 UI Wiki 无用法。
- 把 `SetRenderTransformAngle` 当旋转入口。本地 API 无此方法，应用 `SetRenderAngle(float)`（2026-09-17 检索结论）。
- 以为有现成「页面切换过渡」API。本地 Wiki 检索「页面切换」未命中 UI 过渡接口，要自己对旧页淡出、新页淡入。
- **把面板自身背景当引导遮罩**（`PlayGuideSpotlight` 的 `Options.MaskWidget` 传面板背景图）。该函数会对遮罩 `PlayFade(0 → MaskOpacity, 默认 0.6)` 且不再复位，结果是整个面板永久停在 60% 不透明度（pet_paradise 2026-09-18 实测）。引导遮罩必须是独立的遮罩控件，显示前还要显式复位 `SetRenderOpacity(1.0)`。
- **把业务文本当数值滚动文本**（`PlayLoadingProgress` 的第一个文本参数）。内部走 `PlayNumberRoll`，按 `%d%%` 逐帧 `SetText` 覆盖原文，且收尾对文本控件做强调缩放；「第 1 / 8 步」会被写成「0%」→「1%」（pet_paradise 2026-09-18 实测）。只有真正的百分比/数值文本才能接数值滚动；进度类动效的终值必须由业务数据驱动，且 `ToPercent` 要按真实百分比传（传 1 会把进度条缩到 1%）。

## 相关页面

- [绿洲通用 UI 编辑规范与排错](./绿洲通用UI编辑规范与排错.md)
- [UI 页面切换与 Widget 生命周期](./UI页面切换与Widget生命周期.md)
- [2026-09-10 UI 动效与 Tween](../来源记录/2026-09-10_UI动效与Tween.md)
- [IslandAuctionKing 线索动效 Tween 重复 Kill 断言闪退（项目证据）](../../IslandAuctionKing/日志证据/2026-09-16_线索动效Tween重复Kill断言闪退.md)
- [pet_paradise UI 动效方案与 Tween 落地（含可复用库 UIMotionKit 参考实现）](../../pet_paradise/蓝图与UI/2026-09-17_UI动效方案与Tween落地.md)
- [pet_paradise 新手教程三缺陷：遮罩误用背景 / 数值滚动覆盖步骤文本 / 传送坐标出触发盒](../../pet_paradise/开发记录/2026-09-18_新手教程面板半透明与步骤文本与清洗区按钮.md)

## 待查证

- `UGCTweenSystem` 在服务端调用是直接失败、无效果，还是会改非 UI 对象。Wiki 与 API 生效范围冲突。
- `EEasingType.EaseOutQuad` 是否为 `QuadOut` 别名。
- 绿洲 UI 编辑器时间线做出的 `UWidgetAnimation`，能否从当前 Lua 运行时拿到并调用 `PlayAnimation`。
- IslandAuctionKing 测试页与拖拽测试 UI 已接 AuctionUIMotionService；大厅/选择层/竞拍主界面/图鉴/结算是否已接不在本页展开。本轮未 PIE。
