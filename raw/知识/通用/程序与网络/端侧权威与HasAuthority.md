# 端侧权威与 HasAuthority

> 来源：`raw/docs/ai/2026-07-13_RPC编码规范标准文档.md`、`raw/docs/ai/2026-08-03_GM私有实体碰撞血条伤害隔离.md`、`raw/docs/ai/2026-07-13_跳楼机多人座椅与宠物朝向修复记录.md`、`raw/docs/ai/2026-07-20_跳楼机本地玩家宠物附着与客户端座位同步修复记录.md`  
> 官方依据：`raw/docs/wiki/进阶内容/352_绿洲启元玩法开发框架介绍.md`、`raw/docs/wiki/进阶内容/203_网络同步系统介绍.md`、`raw/docs/api/class/Others/AActor.md`

---

## 一、基本原则

服务端（DS）持有权威状态，客户端只做表现与输入。判断当前执行端统一使用 `self:HasAuthority()`。

| 端 | `HasAuthority()` | 职责 |
| --- | --- | --- |
| 服务端 | `true` | 属性写入、Actor 生成、伤害判定、存档、位置权威 |
| 客户端 | `false` | UI、特效、本地表现、输入采集 |

---

## 二、必须双分支且双端打印日志

```lua
if self:HasAuthority() == true then
    ugcprint("【CF_KHDRPC+ServerRPC_Foo】分支: 服务端执行逻辑")
    -- 服务端业务逻辑
else
    ugcprint("【CF_KHDRPC+ServerRPC_Foo】分支: 客户端收到 RPC 调用，不执行服务端逻辑")
end
```

**禁止静默跳过**：

```lua
-- ❌ 客户端静默返回，排查时完全没有痕迹
if not self:HasAuthority() then return end
```

KHDRPC 期望 `HasAuthority() == true`，FWDRPC 期望 `false`；出现在异常端时必须打印错误日志，而不是安静退出。

---

## 三、API 端侧分类（项目经验，最终以官方文档「生效范围」为准）

| API | 调用端 |
| --- | --- |
| `UGCAttributeSystem.*` | 双端（服务端写、客户端只读） |
| `UGCGameSystem.*` | 双端查询 |
| `UGCActorComponentUtility.SpawnActor` | 服务端 |
| `UGCWidgetManagerSystem.*`、`UserWidget.*` | 客户端 |
| `UGCPersistEffectSystem.*`、`UGCBackpackSystemV2.*` | 服务端 |
| `SpawnEmitterAttached` | 客户端 |
| `SetIgnoreMoveInput` | 服务端 |
| `K2_SetActorLocation` | 双端 |

越界调用的典型错误：客户端 `SpawnActor`、服务端 `AddToViewport`、客户端写 `SetGameAttributeValue`。

不确定时先查 `raw/docs/api` 对应条目的「生效范围」标注，禁止猜测。

---

## 四、六个独立系统必须分别处理

来自私有实体隔离实战（`2026-08-03`）的重要结论——下列行为互不等价：

1. Actor 隐藏
2. Mesh 隐藏
3. 组件碰撞（`SetCollisionEnabled`）
4. 服务端移动碰撞（`IgnoreActorWhenMoving`）
5. 伤害判定（服务端权威过滤）
6. 血条显示（每客户端 Actor 实例级设置）

要点：

- 客户端关闭碰撞只影响本地表现，不能代替服务端权威伤害过滤。
- `IgnoreActorWhenMoving` 是移动忽略关系，不等于全局关闭碰撞；按玩家隔离时需在实体组件和玩家移动组件两侧都设置。
- 私有血条不能改蓝图 CDO 全局关闭，应按 OwnerKey 在每个客户端实例上设置。
- 伤害过滤尽量在父类扣血前完成，同时在公式覆盖与后置事件保留防线和日志。
- 攻击来源 `EventInstigator = nil` 时默认拒绝，避免环境伤害绕过归属校验。

---

## 五、附着与移动的权威顺序

来自跳楼机两篇修复记录：

1. 解除旧父级 → 关闭碰撞 → 设置世界位置与世界旋转 → 冻结 `CharacterMovement`（`SetMovementMode(0)`、`GravityScale = 0`、`bOrientRotationToMovement = false`）→ `K2_AttachToActor(..., true)` 保持世界位姿。
2. 服务端建立权威附着后，通过 FWDRPC 让客户端对本地 Pawn 显式附着，并用 `GetAttachParentActor` 回读验证。
3. 下车时恢复移动模式、重力、朝向和碰撞。

经验规则：

- Attach 优于逐帧手动同步世界坐标。
- 移动复制、客户端预测、服务端强制同步不能同时控制同一个 Actor。
- 先定世界姿态再附着，比附着后修正更可靠。
- `SetIgnoreLookInput` 是计数栈，需要用 `ResetIgnoreLookInput` 重置。

### 5.1 几何读数（Actor 位置 / 包围盒）的端侧可信度可能不同

**2026-09-17 实测（pet_paradise，季卡打工特效贴脚底）**：同一个宠物 Actor，同一时刻：

| 端 | 读数 | 可信度 |
| --- | --- | --- |
| 服务端 `StartWork`（在 `PreserveBottomAtZ` 落点对齐之后） | `GetActorBounds` 推出的脚底世界 Z ≈ `103.97`，与实际打工区地面一致 | **可信** |
| 客户端 `RPC_StartWork` 回调时机 | `K2_GetActorLocation().Z = -1178.12`、`GetActorBounds` 推出脚底 `-1558.12` | **不可信（无效常量）** |

判定"无效常量"的依据：这两个数值在**不同体型宠物（chicken / nuilai1）、不同时段、不同会话**中完全一致，
而真实落点是 ≈104，偏差 1600+ cm。体型差异极大的两个 Actor 不可能返回同一包围盒。

**可复用规则**

1. 客户端在"刚收到 RPC、Actor 可能尚未完成本地同步/初始化"的时机读取位置与包围盒，**结果可能是常量而非真实几何**；
   这类读数只用于日志观察，**不得直接驱动挂点、吸附、放置**。
2. 需要几何量（脚底高度、包围盒中心、尺寸）时，**由服务端权威端计算，再把标量结果经 RPC 下发给客户端**。
   下发**相对偏移**（如"脚底相对根组件原点的 Z"）比下发世界坐标更稳：相对量是模型几何常量，与两端坐标/插值误差无关。
3. 数值跨端下发前先做**合理性钳制 + 降级回退**（示例：偏移绝对值 > 250 cm 即判不可信 → 回退配置固定值并告警），
   避免一次异常读数把表现扔到看不见的地方（本例曾把特效挂到地下 1660 cm）。
4. 挂点位置不要写死为 `0`：**根组件原点常在身体偏上处**，固定偏移为 0 会表现为"特效在头顶"。
   同工程既有写法可作量级参考（跟随宠物特效用 `Z = -120`）。
5. RPC 数值参数可能以**字符串**到达（同工程 `RPC_StartWork("true")` 即传字符串布尔），
   接收端一律先 `tonumber(...)` 再判空，不要假设类型已正确。
6. 两端 RPC 的**到达顺序不保证**。若客户端要用的权威值由另一条 RPC 携带，接收方必须处理"先渲染、后拿值"：
   拿到值后对已生成的组件做一次**重挂/重设**（本例为销毁重挂），而不是只在下一次生成时生效。

---

## 六、相关页面

- [RPC 分发架构](RPC分发架构.md)
- [日志与错误保护规范](../工具与流程/日志与错误保护规范.md)
- [存档与数据持久化](存档与数据持久化.md)
- [PIE 调试与热更新边界](../工具与流程/PIE调试与热更新边界.md)
- [绿洲蓝图变量与玩家数据存储](绿洲蓝图变量与玩家数据存储.md)
- 来源：[2026-08-26 raw 资料入库总结](../来源记录/2026-08-26_raw资料入库总结.md)

---

## 七、待查证

`TakeDamage` 的完整 Lua 覆写签名与 `PreOverrideDamageValue` 精确语义未在本地官方文档完整列出，现有实现依据编辑器反射与 LuaHelper 签名，使用前需在 PIE 验证。
