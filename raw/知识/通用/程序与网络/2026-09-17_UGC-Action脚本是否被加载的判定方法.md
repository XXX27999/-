# 2026-09-17 UGC Action 脚本是否被加载的判定方法（`Script/gamemode/*.lua`）

- **类型**：通用知识 / 调试排错
- **主题**：判断一个放在 `Script/gamemode/` 下的 Action 脚本（如 `PlayerGetMSCard.lua`）在关卡里**是否真的执行**
- **适用范围**：绿洲起源所有 UGC 工程
- **证据状态**：项目实测（`pet_paradise`，2026-08-28 与 2026-09-17 全部会话日志）
- **来源**：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\Saved\Logs\pet_paradise\`
- **更新时间**：2026-09-17
- **关联主题**：[PIE 调试与热更新边界](./PIE调试与热更新边界.md)·[日志与错误保护规范](./日志与错误保护规范.md)
- **排除范围**：不是「Lua 语法错误导致模块加载失败」的排查（那种会有 `LuaException` 报错）；本页解决的是**语法正确、文件存在，但整段逻辑从来不跑**的静默失效
- **官方依据**：无（结论来自运行时日志实证）

---

## 一、问题模式

`Script/gamemode/` 是关卡「Action」脚本目录。文件**放在目录里 ≠ 会执行**：只有被挂入关卡动作表的模块才会在运行时被加载并回调 `Execute`。

典型后果（静默失效，无任何报错）：

- 该脚本里的每日/周期逻辑完全不跑；
- 相关功能只在本脚本里实现时，表现为「功能整体不存在」，例如季卡天数永不递减、每日奖励永不发放；
- 排查时容易误判成业务代码写错，因为**日志里连一条错误都没有**。

## 二、三步判定法（按可靠性排序）

1. **查运行时模块加载清单（最硬的证据）**
   日志里搜索 `battlemodulerequire <模块路径> load success`，例如：

   ```text
   LuaLog: battlemodulerequire Script.gamemode.PlayerGetMSCard load success
   ```

   把一次会话内该清单去重列出。绿洲 2026-09-17 实测约 149 个模块；其中 `Script.gamemode.*` 只加载了
   `ControllerExitGame / ExpLevelUp / PetActorDic / PlayerExitGame / PlayerGetMSCard / PlayerLogin / StatusChange`。
   **清单里没有 = 该 Action 没挂入关卡**。

2. **查该脚本自身 `Execute` 的入口打印次数**
   脚本首行就写 `ugcprint("【脚本名+Execute】入口: ...")` 的规范在此时直接变现：
   每个会话各出现 1 次 = 正常；全量日志 **0 次** = 从未执行。
   注意有些 Action 的 `Execute` 在关卡开始后约 **50s** 才触发（延迟注册/登录回调），别只看开局前 10 秒。

3. **反证检查：不要用 `can't find correspond Bluepirint` 作依据**
   `LogBasic: Warning: Actor Lua file .../<任意>.lua can't find correspond Bluepirint` 这条 warning
   在每次启动时对**工程内所有 Lua 文件各打一次**（实测 274 个文件 → 274 条）。
   因此它对某个具体脚本出现**不代表该脚本有问题或缺蓝图**，不能用来判定「未挂载」。

## 三、修复选择

| 方案 | 做法 | 适用 |
| --- | --- | --- |
| A. 把逻辑迁到已加载的 Action | 把周期逻辑移到已确认加载的 Action（如 `PlayerGetMSCard:Execute`） | 不想改关卡资产、要立刻拿到可验证结果 |
| B. 正式挂入关卡动作表 | 在编辑器里把该 Action 加入关卡动作列表 | 该 Action 是独立业务、需要独立生命周期 |

**迁移安全**：若两个 Action 都实现同一份每日逻辑，必须在同一份存档字段上做**日期互斥**
（如 `SeasonalCardGetTime` 与当前日期比较），使两处**同时启用也不会重复发放/重复扣天**；
迁移后把原脚本页首标注「已迁移，保留仅为兼容」，避免后来者重复接线。

## 四、复现用脚本思路

对目标会话日志扫描：

```python
# 1) 模块加载清单
re.search(r"battlemodulerequire Script\.([A-Za-z0-9_.]+?) load success", line)
# 2) Execute 入口计数
line.count("【<脚本名>+Execute】入口")
# 3) 通用 warning 计数（用于排除误判）
re.search(r"Actor Lua file (.+?) can't find correspond", line)
```

## 五、实测案例

`pet_paradise` 2026-09-17：`MonthlyCardAndSeasonCard.lua` 是季卡每日权益与天数扣减的**唯一**实现，
但不在 `battlemodulerequire` 清单内，全量日志 `【MonthlyCardAndSeasonCard+Execute】` 为 **0** 次 →
季卡天数永不递减、每日完美打工卡与每日离线托管时长永不发放。
处理：按方案 A 迁移到 `PlayerGetMSCard:Execute`，并用 `SeasonalCardGetTime` 与原脚本保持互斥。

详见 `raw/pet_paradise/开发记录/2026-09-17_月卡季卡持续时间与每日奖励修复.md`。
