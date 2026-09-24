# 3D UI 挂载方案记录

本文记录项目可用的两种 3D UI 挂载方法：

1. `UGCWidgetManagerSystem.AddObjectPositionUI`：对象位置 UI，实际显示在屏幕 UI 层。
2. `UWidgetComponent` 且 `Space = World`：世界空间 UI，实际参与三维场景渲染。

结论先行：需要严格符合透视规律、随距离自然变小的 UI，使用方案二。需要始终清晰、尺寸基本不受距离影响的头顶信息，使用方案一。

## 一、方案一：AddObjectPositionUI 对象位置 UI

### 1. 原理

`AddObjectPositionUI` 接收一个世界中的 `Actor`，把 Actor 的世界位置投影到屏幕，再在屏幕 UI 层显示对应控件。它看起来跟随三维对象，但不是放在世界中的真实平面。

官方定义称其为“对象位置 UI、头顶 UI（类似血条、玩家名）”，并要求控件继承 `UObjectPositionWidget`。

### 2. 标准挂载

```lua
-- 目标角色：UI 要跟随的世界 Actor
local targetActor = self
-- 控件路径：必须指向继承 UObjectPositionWidget 的控件类
local widgetClassPath = UGCGameSystem.GetUGCResourcesFullPath(UIPath)
-- 世界偏移：相对目标 Actor 的投影点偏移
local offset = { X = 0, Y = 0, Z = 150 }
-- 实例索引：用于后续查询和移除；官方文档未标注返回类型，运行时必须判空并以 PIE 验证
local instanceIndex = UGCWidgetManagerSystem.AddObjectPositionUI(
    targetActor,
    widgetClassPath,
    offset,
    true,  -- SizeAutoContent
    true,  -- OutViewHide
    true,  -- BeOcclusionHide
    true   -- ShowSelf
)
```

移除时保存并传回 `InstanceIndex`：

```lua
UGCWidgetManagerSystem.RemoveObjectPositionUI(targetActor, instanceIndex)
```

`GetObjectPositionUI` 只在客户端生效，而且官方明确说明 Add 后不能保证立刻取到，控件可能仍在加载。因此不能在 Add 后无等待地假设 Widget 已存在。

### 3. 视觉特征

- UI 位于屏幕空间，通常保持接近固定的屏幕像素尺寸。
- 摄像机远离 Actor 时，Actor 在画面中变小，但 UI 不按同样比例缩小，因此相对 Actor 会显得越来越大。
- 不应使用“距离越远，控件缩放越大”的反向补偿。它会进一步放大违背透视的观感。
- `OutViewHide`、`BeOcclusionHide`、`ShowSelf` 是挂载时直接提供的便捷策略。
- 适合作为 HUD 式信息，不适合表达真实世界尺寸。

### 4. 适用场景

- 玩家名、队友标识、血条、任务目标标记。
- 无论远近都必须清楚辨认的提示。
- 希望直接使用出屏隐藏、遮挡隐藏、自身显示等对象位置 UI 管理能力。
- UI 数量和生命周期需要由 `UGCWidgetManagerSystem` 统一管理。

### 5. 不适用场景

- 招牌、机器面板、宠物头顶铭牌等需要近大远小的场景物件。
- 需要让 UI 像世界中的实体平面一样被观察。
- 对透视比例和空间尺度有严格要求的 UI。

## 二、方案二：UWidgetComponent + Space = World

### 1. 原理

`UWidgetComponent` 把 `UUserWidget` 先渲染到 RenderTarget，再把该 RenderTarget 显示在三维环境中的组件表面。设置 `Space = World` 后，它具有真实世界位置、旋转和缩放，经过摄像机透视投影，因此距离越远，屏幕占用尺寸自然越小。

官方枚举值：

- `EWidgetSpace.World = 0`
- `EWidgetSpace.Screen = 1`

本方案必须使用 `World`。如果 WidgetComponent 仍设为 `Screen`，仍然不是本项目要求的真实世界透视效果。

### 2. 蓝图挂载步骤

1. 在需要承载 UI 的 Actor 蓝图中添加 `WidgetComponent`。
2. 将 `WidgetClass` 指向对应 `UUserWidget` 控件类。
3. 将 `Space` 设置为 `World`。
4. 设置组件相对位置，使其位于角色头顶或物体表面。
5. 使用 `DrawSize`，或仅在布局尺寸稳定时启用 `bDrawAtDesiredSize`。
6. 根据是否允许背面观察设置 `bIsTwoSided`。
7. 用组件 Transform 的世界缩放确定 UI 的真实世界尺寸，不再按摄像机距离反向缩放。

注意：蓝图组件和资源结构必须通过 UGCAskQ MCP 按 Resolve → Plan → Execute 修改，写入后立即回读；`_JsonOutput` 只能读取和校验，禁止直接编辑。

### 3. 获取和绑定 Widget 实例

官方提供 `UWidgetComponent:GetUserWidgetObject()`，用它获取组件内部创建的 Widget 实例，再更新文本或注入业务目标。

```lua
-- 世界 UI 组件：由 Actor 蓝图预先挂载
local widgetComponent = self.WorldTitle3D
-- 控件实例：组件加载完成后由 GetUserWidgetObject 获取
local widget = widgetComponent and widgetComponent:GetUserWidgetObject() or nil

if widget then
    -- 目标角色：项目约定字段，不是官方自动提供的 Owner 关系
    widget.WorldWidgetTargetActor = self
end
```

绑定边界必须明确：

- `GetUserWidgetObject()` 是官方 API。
- `WorldWidgetTargetActor` 是项目自定义约定，不是官方字段。
- 不要猜测 Widget 能自动反查其挂载 Actor。需要业务 Actor 时，应在 Actor 侧显式注入。
- 组件或 Widget 可能尚未初始化，获取后必须判空；必要时在已确认的生命周期或定时重试中绑定。

### 4. 朝向摄像机

世界空间 UI 不会自动保证正面朝向玩家。公告牌式 UI 需要周期性计算朝向。社区实践建议使用 `FindLookAtRotation`，并在玩家进入有效范围后开启 Timer，离开范围后清除 Timer，以减少常驻 Tick 成本。

具体正反方向受 WidgetComponent 本地朝向和资产 Transform 影响，必须在 PIE 中确认是否需要附加 180 度旋转，不能只凭静态代码断定。

如果 UI 固定在门牌、机器屏幕或广告牌表面，应保持物体自身朝向，不使用始终面向摄像机的逻辑。

### 5. 尺寸与刷新

- 世界尺寸由组件 Transform、`DrawSize` 和 Widget 内容共同决定。
- `DrawSize` 表示世界中显示 Quad 的绘制尺寸。
- `bDrawAtDesiredSize` 会让 RenderTarget 自动匹配期望尺寸；官方警告每帧改变会非常昂贵。
- 启用 `bManuallyRedraw` 后，内容改变需要调用 `RequestRedraw()`；`RedrawTime` 可限制最大重绘频率。
- 社区资料也反馈动态文本可能需要 `RequestRedraw()`，但是否必须取决于组件重绘配置，应以本项目 PIE 行为为准。
- 不要同时使用世界透视和按距离增加 `SetWorldScale3D` 的补偿，否则会抵消自然的近大远小。

### 6. 遮挡与交互

- World 模式作为场景表面渲染，遮挡表现与屏幕 UI 不同，应按场景实际材质和深度关系进行 PIE 验证。
- 官方 `bHideIfOccluded` 说明为“仅 Screen Space 有效”，不能把它当作 World 模式的通用遮挡开关。
- `bIsTwoSided` 只控制背面是否可见，不等于忽略场景遮挡。
- `bReceiveHardwareInput` 会注册视口硬件输入并可能抢占焦点。官方建议需要玩家继续操控世界并与 3D UI 交互时使用 `WidgetInteractionComponent`，而不是简单开启该字段。

### 7. 适用场景

- 宠物名称、专属称号、战力、工作进度等需要符合透视的头顶 UI。
- 场景区域名称、设施标牌、机器面板、门牌和广告牌。
- 需要真实世界位置、旋转、缩放和遮挡关系的界面。
- UI 需要作为 Actor 组件随 Actor 生命周期一起存在。

### 8. 不适用场景

- 远距离仍必须保持固定可读尺寸的玩家名或任务标记。
- 需要完全按 HUD 层级显示、不能被三维场景影响的提示。
- 数量极多且持续高频重绘的 UI；RenderTarget、Tick 和朝向更新成本需要评估。

## 三、核心差异对照

| 对比项 | AddObjectPositionUI | UWidgetComponent + World |
| --- | --- | --- |
| 实际渲染空间 | 屏幕 UI 层 | 三维世界中的组件表面 |
| 透视规律 | 不保证随距离自然缩小 | 符合摄像机透视，近大远小 |
| 控件基类 | 必须继承 `UObjectPositionWidget` | `WidgetClass` 为 `UUserWidget` 子类 |
| 挂载方式 | Lua 调管理器动态创建 | Actor 蓝图预挂组件，或经已验证流程添加组件 |
| 目标绑定 | Add 时直接传 Actor | Actor 持有组件；业务目标建议显式注入 Widget |
| 生命周期句柄 | 保存 `InstanceIndex`，调用 Remove | 跟随组件/Actor；通过组件控制显示和内容 |
| 朝向摄像机 | 屏幕层天然面向视口 | World 模式通常需自行做 Billboard |
| 出屏/遮挡参数 | Add 时提供专用参数 | 依赖组件和场景行为；`bHideIfOccluded` 仅 Screen 有效 |
| 尺寸控制 | 屏幕布局和对象位置 UI 参数 | DrawSize、内容尺寸、组件世界缩放 |
| 动态内容入口 | 异步取得 ObjectPositionWidget 实例 | `GetUserWidgetObject()` |
| 更新成本 | 由对象位置 UI 系统管理 | 需关注 RenderTarget、Redraw、Tick 和 Billboard 成本 |
| 推荐用途 | 血条、玩家名、远距标记 | 场景标牌、宠物头顶信息、真实空间面板 |

## 四、项目选型规则

按以下顺序判断：

1. UI 是否必须符合真实透视？是：使用 `UWidgetComponent + World`。
2. UI 是否必须远距离仍保持固定可读大小？是：使用 `AddObjectPositionUI`。
3. UI 是否是世界物件的一部分并应被空间关系影响？是：使用 `UWidgetComponent + World`。
4. UI 是否只是把 Actor 位置投影到 HUD 上？是：使用 `AddObjectPositionUI`。
5. 需求同时包含“真实透视”和“远距离恒定可读”时，两者冲突，必须由设计明确优先级，不能用反向距离缩放同时满足。

本项目当前需求“摄像机越远，3D UI 应越小”统一选择 `UWidgetComponent` 且 `Space = World`。

## 五、常见错误

### 错误 1：把屏幕投影 UI 当作世界 UI

`AddObjectPositionUI` 虽然跟随世界 Actor，但它的屏幕尺寸不会自动体现 Actor 的真实世界比例。这正是“距离越远，3D UI 相对显得越大”的根本原因。

### 错误 2：WidgetComponent 使用 Space = Screen

组件存在并不代表已经是世界 UI。必须核对 `Space = World (0)`。

### 错误 3：按距离反向放大世界组件

World 模式本来就具有透视缩小。距离越远越放大组件会抵消透视，重新产生大小异常。

### 错误 4：假定 Widget 自动知道目标 Actor

组件创建 Widget，不代表业务 Widget 自动拥有挂载 Actor 引用。通过 `GetUserWidgetObject()` 获取实例后显式注入，或使用项目中已验证的绑定接口。

### 错误 5：频繁改变 bDrawAtDesiredSize 或无条件每帧重绘

官方明确警告每帧改变期望尺寸代价很高。动态数据应限制刷新频率，并避免对不可见或远距离 UI 继续做高频更新。

## 六、实施与验证清单

### AddObjectPositionUI

- 控件继承 `UObjectPositionWidget`。
- 保存 `InstanceIndex`，销毁时调用 `RemoveObjectPositionUI`。
- 客户端异步获取 Widget 时处理“尚未加载”。
- 明确 `OutViewHide`、`BeOcclusionHide`、`ShowSelf`。
- 不使用反向距离缩放制造伪透视。

### UWidgetComponent + World

- 蓝图回读确认组件存在、`WidgetClass` 正确、`Space = 0`。
- 确认相对位置、Pivot、DrawSize、世界缩放和双面设置。
- 通过 `GetUserWidgetObject()` 取得实例并显式绑定业务 Actor。
- PIE 检查近大远小、正反面、Billboard 朝向和遮挡。
- PIE 检查动态文本是否需要 `RequestRedraw()`。
- 对宠物成长体型、坐骑附着、传送和销毁重生分别验证偏移与生命周期。
- 性能检查关注组件数量、RenderTarget 尺寸、更新频率和朝向 Timer。

## 七、依据与证据边界

### 官方 API 文档

- `D:\oasis-skill-plus\docs\api\class\Others\UWidgetComponent.md`
- `D:\oasis-skill-plus\docs\api\cppenum\E\EW\EWidgetSpace.md`
- `D:\oasis-skill-plus\docs\api\class\和平全局接口\UI 界面\UGCWidgetManagerSystem.md`

官方文档确认了组件渲染原理、`Space`、`WidgetClass`、`DrawSize`、重绘字段、`GetUserWidgetObject()`、`RequestRedraw()`，以及对象位置 UI 的参数与端侧范围。

### 社区补充资料

- `C:\Users\Administrator\.codex\skills\sq-skill\docs\community\replies\1762.md`
- `C:\Users\Administrator\.codex\skills\sq-skill\docs\community\replies\1950.md`
- `C:\Users\Administrator\.codex\skills\sq-skill\docs\community\replies\1240.md`
- 社区归档快照时间：2026-05-31。

社区资料补充了 World 模式下定时朝向摄像机、通过 `GetUserWidgetObject()` 修改内容，以及手动重绘的实践。它们不是 API 存在性或端侧约束的权威依据，最终行为必须通过当前编辑器版本 PIE 验证。

### 暂未由官方文档确认

- `AddObjectPositionUI` 返回值的明确类型；项目按现有实践保存为 `InstanceIndex`，但必须以运行结果验证。
- World 模式在当前项目材质和移动端画质下的具体遮挡、排序和性能表现。
- 不同 Widget 资产的正面朝向是否统一需要额外 180 度旋转。

