# 运行卡死闪退：线索动效 Tween 共享句柄重复 KillTween 触发引擎断言

> 类型：项目事实 / PIE 崩溃日志分析（客户端 appError）
> 主题：`Assertion failed: Pair != nullptr [Map.h:586]`、`UGCTweenSystem.KillTween` 重复调用、`AuctionUIMotionService` 共享句柄
> 适用范围：`IslandAuctionKing` 项目；客户端侧 Tween 封装 `AuctionUIMotionService` / `AuctionClueFeedbackService`
> 证据状态：项目实测（客户端 FullLog 硬证据 + 源码行号对齐）；修复已写入 `AuctionUIMotionService.lua` 并通过 luaparser 语法校验与行号回读；**2026-09-20 双人 PIE 已复现：同一断言在修复代码在位的情况下仍发生**（见下「复现」节），定位到 09-16 修复**未覆盖**的 `PlayClueFlashPhase` 完成回调路径
> 来源：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\Saved\Logs\IslandAuctionKing\Clientlog\FullLog\2026.09.16-15.49.26_client__dkck7plomtzdy8_1.log`（L121763 / L121790 / L121792 / L122254）；`Script/Function/AuctionUIMotionService.lua`；`Script/Function/AuctionClueFeedbackService.lua`；`Script/Function/AuctionTestUIService.lua`；`Content/LuaHelper/Source/Lua/ugc/UGCAPI/UGCTweenSystem.lua`（@meta 声明）。复现证据：`Saved\Crashes\UE4CC-Windows-FD0CFA6049AB26EE643D58B61D7172E6_0000\2026.09.20-11.01.07_client__dkck7pp6wwoo9p_1.log`（L120180 / L120184 / L120819）与 `…1C0AC94041F4D3A6C73ABDA9BEA8E702_0000\…_2.log`（L127277 / L127281 / L133483）
> 更新时间：2026-09-18（增补 2026-09-20 双人 PIE 复现与未覆盖路径定位）
> 关联主题：[绿洲 UI 动效与 Tween](../../知识/通用/UI与交互/绿洲UI动效与Tween.md)、[2026-09-15 AuctionTestUI WidgetOuter 断言修复](./2026-09-15_AuctionTestUI_WidgetOuter断言修复.md)、[2026-09-14 编辑器连续闪退日志分析](./2026-09-14_编辑器连续闪退日志分析.md)、[2026-09-18_装扮主题双人PIE双界面验证](./2026-09-18_装扮主题双人PIE双界面验证.md)
> 排除范围：本页不把引擎 Tween 子系统内部实现写成官方确认；不证明 Lua 侧 `pcall` 能拦住该断言（实测拦不住）；不覆盖 DS 侧任何崩溃
> 官方依据：本地 `raw/docs/api/class/Others/UGCTweenSystem.md` 只列出 `KillTween(Handle)`/`IsTweenValid(Handle)` 签名，未记录重复调用语义，也未记录 `Map.h:586` 断言

## 现象

用户反馈「运行卡死闪退」。工程根 `log.txt`（2 行）与 `error.log`（空）无内容，真实日志位于
`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\Saved\Logs\IslandAuctionKing\`。

时间线（客户端会话 `2026.09.16-15.49.26_client__dkck7plomtzdy8`）：

| 时刻 | 事件 |
| --- | --- |
| 15:53:06.776 | `LogScriptPlugin: Warning: [LuaException] OnLogLuaStack: Assertion failed:Pair != nullptr,:` |
| 15:53:06.778 | `LogUGCAlertDialog->Show sync dialog [Type=Engine, Category=Assert, Title=Assertion Failed ...]`（弹框，界面卡住） |
| 15:53:11.655 | `LogSlate: Request Window 'Assertion Failed' being destroyed`（约 5 秒后弹框被关闭） |
| 15:53:11.667 | `LogWindows: Error: appError called: Assertion failed: Pair != nullptr ...`（进程崩溃闪退） |

同一时刻 DS 侧（`2026.09.16-15.52.09_ds__dkck7plomtzdy9_realtime.log`）**没有任何 `LogWindows: Error`/`Fatal`**，且文件仍在持续写入 —— 客户端已崩、DS 仍悬挂，这是「卡死」体感的重要来源，排查时不要先去怀疑 DS。

## 硬证据

### 引擎断言签名（客户端 FullLog L121792、L122254）

```text
Assertion failed: Pair != nullptr [File:D:\CG038\UE4181\Engine\Source\Runtime\Core\Public\Containers/Map.h] [Line: 586]
```

`Map.h:586` 的 `Pair != nullptr` 断言在引擎侧的含义是「在 TMap 中按 key 查找条目时找不到」——即传入的句柄在 Tween 子系统的映射表里已经没有对应条目。

### Lua 崩溃栈（L121766-121789）

```text
stack traceback:
	[C]: in field '?'                                  -- UnrealTweenBlueprintLibrary.KillTween
	ugc/ugc_env.lua:12: in function <ugc/ugc_env.lua:11>
	(...tail calls...)
	ugc/UGCAPI/UGCTweenSystem.lua:228
	[C]: in function 'pcall'
	Script/Function/AuctionUIMotionService.lua:120      KillHandle
	Script/Function/AuctionUIMotionService.lua:624      StopClueMotion
	Script/Function/AuctionUIMotionService.lua:872      PlayClueWaveMotion 的完成回调
	Script/Function/AuctionUIMotionService.lua:193      BindCompleted 包装
	ugc/UGCAPI/UGCTweenSystem.lua:251                   官方完成回调分发
	Script/Function/AuctionUIMotionService.lua:827      PlayClueWaveMotion
	Script/Function/AuctionClueFeedbackService.lua:288  PlayOutlineClue
	Script/Function/AuctionClueFeedbackService.lua:377  ObserveSkillIntel
	Script/Function/AuctionTestUIService.lua:1267       RefreshPrivateState
	Script/Function/AuctionTestUIService.lua:2458 → Script/Blueprint/CF_FWDRPC.lua:102/306 → Script/Blueprint/UGCPlayerController.lua:66
```

最内层是引擎函数 `KillTween`；`KillHandle`（L114-128）已经用 `pcall(UGCTweenSystem.IsTweenValid, handle)` 做过有效性校验，但依然没能拦住。

### 触发时序（同帧 15:53:06 内三步）

| 时刻 | 日志 | 含义 |
| --- | --- | --- |
| 15:53:06.696 | `【AuctionUIMotionService+PlayClueWaveMotion】关键数据 handle=ud_struct[TweenHandle @0000000241876B20] bindOK=true targetCount=36 tweenCount=1 reason=PublicIntelClue:ItemCount:PublicIntelSequence1` | 36 个控件状态**共享同一个句柄 A** |
| 15:53:06.735 | `... handle=ud_struct[TweenHandle @000000024187FAE0] ... targetCount=1 ... reason=OutlineClue:Shape:SkillIntel` | 新建句柄 B；同时 L827 循环里对旧目标调 `StopClueMotion` |
| 15:53:06.743 | `【AuctionUIMotionService+PlayClueWaveMotion】分支 波浪完成并复位 targetCount=36` | 句柄 A 的完成回调触发，回调内 for 36 个 entry 调 `StopClueMotion` |
| 15:53:06.776 | 断言 | 回调内第 2 次 `KillTween(A)` |

源码对应关系：

- `AuctionUIMotionService.lua:866-868`：`for _, entry in ipairs(states) do entry.State.ClueHandle = handleOrError end` —— 注释原文即「共享同一句柄便于随时 kill」，**36 个 state 持有同一个句柄**。
- `AuctionUIMotionService.lua:869-876`：完成回调里对每个 entry 调 `AuctionUIMotionService.StopClueMotion(entry.Target, settings)`。
- `AuctionUIMotionService.lua:614-635`：`StopClueMotion` 每次都对 `state.ClueHandle` 走 `KillHandle`。

即：**同一个句柄被 36 个持有者逐个 kill，第 2 次即崩溃**。

## 根因

1. 同一 `FTweenHandle` 被多个控件状态共享持有，而销毁路径按持有者逐个执行 → 同一句柄被 `KillTween` ≥2 次。
2. `UGCTweenSystem.IsTweenValid` 在句柄已被 Kill 之后仍返回 `true`（`KillHandle` L118-119 的防线失效），拦不住重复 Kill。
3. 引擎 Tween 子系统内部 TMap 已移除该句柄 → `FindPair` 返回 null → `Pair != nullptr` 断言失败 → 弹出 Assert 同步对话框（引擎判定应用不可继续）→ 数秒后 `appError` 崩溃。
4. 完成回调（tween 已自然结束）里再次 Kill 自身句柄，是本次的直接触发形态。

## 修复（2026-09-16 已落地）

改动文件：`Script/Function/AuctionUIMotionService.lua`（唯一改动文件，共 4 处）。

| 位置 | 改动 |
| --- | --- |
| 新增 L133-152 `KillSharedClueHandle(state)` | 从 state 取出 `ClueHandle` + `ClueGroup`，先清引用；若共享组已 `Killed == true` 则跳过 `KillTween`，否则置 `Killed = true` 后调 `KillHandle` 真正销毁。保证**一个句柄只 KillTween 一次**。 |
| L648 `StopClueMotion` | `KillHandle(state.ClueHandle)` + `state.ClueHandle = nil` 两行替换为 `KillSharedClueHandle(state)`。 |
| 新增 L662-684 `AuctionUIMotionService.ResetClueVisual(target, options)` | 只做视觉复位（`ApplyRenderScale(1.0)` / `ApplyOpacity(1.0)` / `ApplyRenderTranslation(0,0)` / 可选 `RestoreColor`）并清空 `ClueHandle`/`ClueGroup`/缓存，**不做 KillTween**。 |
| L915-923 `PlayClueWaveMotion` | 创建共享组 `waveGroup = { Handle = handleOrError, Killed = false }`，随句柄一并写入各 `entry.State.ClueGroup`；完成回调由 `StopClueMotion` 改调 `ResetClueVisual`（Tween 已完成，引擎自行回收）。 |

验证：

- luaparser `ast.parse` 语法校验通过（脚本 `check_lua_syntax.py` 落在备份目录，未进工程）。
- 行号回读确认 4 处改动均已落盘（L135 / L648 / L664 / L915-923）。
- 备份：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260916_线索动效Tween重复Kill修复\before\AuctionUIMotionService.lua`（52,335 B）。
- 生效方式：只改普通 Lua 函数体 → 可热更新（reloadlua）；崩溃复现验证建议重新 PIE。
- 预估成功日志：`【AuctionUIMotionService+KillSharedClueHandle】分支 共享句柄已销毁，跳过重复Kill`；`【AuctionUIMotionService+ResetClueVisual】出口`。

未覆盖：若后续再出现「同一句柄被多处共享」的新路径，仍需同样成组建组；`PlayClueFeedbackMotion` 等单目标路径无共享，继续走 `KillHandle`。

## 复现（2026-09-20 双人 PIE）：09-16 的修复没盖住 `PlayClueFlashPhase`

### 关键事实

1. **同一断言再次发生**：DebugID `_dkck7pp6wwoo9p` 的两个客户端分别在 `11:04:48.162` / `11:04:48.956` 报
   `LogScriptPlugin: Warning: [LuaException] OnLogLuaStack: Assertion failed:Pair != nullptr,:`，
   紧接 `LogUGCAlertDialog->Show sync dialog [Type=Engine, Category=Assert, Title=Assertion Failed …]`，
   约 1.5 分钟后（`11:06:20.954` / `11:06:22.424`）在用户点 Ignore 后 `appError called` 崩溃。**两个客户端同时中招**。
2. **修复代码确实在位**：崩溃前的 TagLog 里能看到 09-16 新增的两个函数在运行 ——
   `【AuctionUIMotionService+KillSharedClueHandle】关键数据 handle=… shared=false`、
   以及大量 `【AuctionUIMotionService+ResetClueVisual】入口/出口`。所以这不是「旧版代码没生效」。
3. **本次 Lua 栈为空**：09-20 日志的 `>> LuaException Lua Stack:` 后面是空的 `stack traceback:`（无帧），
   与 09-16 有完整帧（`KillHandle` ← `StopClueMotion` ← callback）不同 → **无法直接指认 Lua 调用行**，只能靠上下文推定。

### 上下文推定（断言前 1ms 的 TagLog 序列）

```text
L120162 11:04:48.160  【AuctionUIMotionService+BindCompleted】分支 动画完成 … handle=ud_struct[TweenHandle @…24EDFA5F0]
L120163 11:04:48.160  【AuctionUIMotionService+StopClueMotion】入口 target=…AuctionTestUI_C_0.WidgetTree_0.CollectibleImage04 hasRestoreColor=false
L120164 11:04:48.160  【AuctionUIMotionService+KillSharedClueHandle】关键数据 handle=ud_struct[TweenHandle @…27D799610] shared=false   ← 去重防线未生效
L120165 11:04:48.160  【AuctionUIMotionService+BindCompleted】分支 动画完成 … handle=…24EDFCA10
L120166 11:04:48.160  【AuctionUIMotionService+PlayClueFlashPhase】分支 闪烁完成但令牌已失效，跳过复位 token=1
L120167 11:04:48.161  【AuctionUIMotionService+StopClueMotion】出口
L120168 11:04:48.161  【AuctionUIMotionService+PlayClueFlashPhase】分支 线索闪烁完成并复位 target=…CollectibleImage04 token=1
L120180 11:04:48.162  [LuaException] OnLogLuaStack: Assertion failed:Pair != nullptr   ← 1ms 后
```

### 定位到的未覆盖路径

`AuctionUIMotionService.lua` 的 `PlayClueFlashPhase`（`L774-833`）：

- `L821`：`state.ClueHandle = handleOrError` —— **只写句柄，没有写 `state.ClueGroup`**；
- `L822-829`：完成回调里仍是 `AuctionUIMotionService.StopClueMotion(target, safeSettings)`（**不是** `ResetClueVisual`）；
- `L827 → StopClueMotion(L638) → KillSharedClueHandle(L135)`：因为 `ClueGroup` 不是 table，日志打 `shared=false`，
  **绕过 09-16 的共享组去重**，直接 `KillHandle(handle)` → `pcall(UGCTweenSystem.IsTweenValid / KillTween, handle)`。

即：**09-16 只把 `PlayClueWaveMotion` 的完成回调改成了 `ResetClueVisual`（不 Kill），却漏改了 `PlayClueFlashPhase` 的同型回调** ——
而这里 Kill 的正是**刚刚自然完成**的那个 tween（回调本身就是它的完成回调），引擎 Tween 子系统已把它移出映射表 → `Map.h:586` 断言。

`StopClueMotion` 之后仍打印 `出口`，且**没有** `【AuctionUIMotionService+KillHandle】错误 KillTween失败` 行 —— 与「断言发生在 `KillHandle` 内的 `pcall` 里、被 Lua 侧 pcall 吞掉、但引擎侧同步对话框已经弹出」完全一致（与 09-16 页「Lua 侧 pcall 拦不住该断言」的结论一致）。

### 建议修复（未实施，1 行，与 09-16 既有范式一致）

`AuctionUIMotionService.lua` L827：`AuctionUIMotionService.StopClueMotion(target, safeSettings)` → `AuctionUIMotionService.ResetClueVisual(target, safeSettings)`，
并在 `L821` 之后补 `state.ClueGroup = nil`（保持与 `PlayClueWaveMotion` 的字段一致性）。
改完后 `PlayClueFlashPhase` 的完成回调不再 Kill 自身句柄，与 `PlayClueWaveMotion` 的处理方式统一。
**注意**：本轮未改该文件；改前须按 `[调试备份存放](../../知识/通用/工具与流程/调试备份存放.md)` 备份，改后必须重新 PIE 复现验证。

## 已验证 / 未验证

- 已验证：断言签名、崩溃时刻、Lua 崩溃栈（09-16）、36 句柄共享、DS 侧无错；修复已在 `AuctionUIMotionService.lua` 落盘，luaparser 语法通过 + 行号回读一致。
- 已验证（2026-09-20 新增）：**修复后该断言**在双人 PIE 中**仍然复现**，且修复函数确实在运行；复现路径指向 09-16 未覆盖的 `PlayClueFlashPhase` 完成回调（`shared=false`，绕过去重）。
- 未验证：上述「1 行修复」是否彻底消除；`PlayClueFeedbackMotion` 等其他单目标路径是否需要同样处理（该路径无共享组，同样存在「完成回调里 Kill 自身句柄」的形态风险）。


## 排查经验（可复用）

- 崩溃先看客户端 FullLog 的 `LogWindows: Error: appError`，再往上看最近的 `[LuaException]` 与 Lua 栈。
- `ugc-log-bug-analyzer` 按 DebugID 取「最新会话」时可能选到 DS 侧（本例客户端 `dkck7plomtzdy8` / DS `dkck7plomtzdy9` 配对不一致），会报 `missing_sides=[client]`；此时改为直接查客户端 FullLog。
- 弹 Assert 框到 `appError` 之间有数秒空档，日志会出现大段无关刷屏（如 `UGCLuaConsoleMsgHandlerComponent: In ProcessMessage`），不要被这段带偏。
- **客户端日志 0 字节 ≠ 这一轮没有客户端日志**：UE 在客户端崩溃时会把该会话日志随崩溃报告搬进 `Saved\Crashes\UE4CC-Windows-<ID>_0000\`，原路径文件被截成 0 B。查客户端证据应先去 `Saved\Crashes\`。次生判据：PIE 会话资源可能仍报 `phase=running`（DS 侧还活着），此时 `Get-Process | ? { $_.ProcessName -match "ShadowTrackerExtra" }` 看 `MainWindowTitle` 会显示 `Assertion Failed` 或 `Responding=False`。
- **`LastExtraMaterialInfo` 里的 `LastTex` / `LastMaterialName` 是环境快照，不是断言原因**：本例同一断言在 09-16 附带的是游戏自带 `/Game/Arts/UI/NoAtlas/OB/Icon_OB_Img_Crit`（材质 `_Layer1_0`），在 09-20 附带的是当时刚加载的 `Dress/DefaultGray/PropUsePanel`（材质 `WorldGridMaterial`）——两次完全不同却是同一断言。**不要**据该字段把最近加载过贴图的功能（如装扮主题）判为元凶；正确做法是拿它对时间点、再用 Lua 栈或 TagLog 上下文找真正调用点。
- **注意日志时间戳是 `HH.MM.SS:mmm`**（毫秒前是**冒号**），按时间窗切日志时正则别写成 `段.毫秒`，否则窗口会取空、误判「这段时间什么都没发生」。
- **判断一次修复是否真的覆盖全部同类路径**：09-16 修了 `PlayClueWaveMotion` 的完成回调却漏了结构几乎相同的 `PlayClueFlashPhase`。修这类「同一形态多处出现」的问题时，必须把所有调用同一危险函数的站点列出来逐个核对（本例危险函数是 `StopClueMotion` / `KillHandle`；正确替代是 `ResetClueVisual`）。

