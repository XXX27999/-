# 3D UI 挂载方案

> 来源：`raw/docs/ai/3D_UI_MOUNTING_GUIDE.md`、`raw/docs/ai/2026-06-24_称号3DUI架构重构.md`、`raw/docs/ai/2026-07-15_打工区3DUI挂载与显示距离修复.md`  
> 官方依据：`raw/docs/api/class/和平全局接口/UI 界面/UGCWidgetManagerSystem.md`、`raw/docs/api/class/Others/UWidgetComponent.md`

---

## 一、两种方案

| 方案 | 实际渲染空间 | 透视表现 |
| --- | --- | --- |
| `UGCWidgetManagerSystem.AddObjectPositionUI` | 屏幕 UI 层（投影 Actor 世界位置） | 尺寸基本不随距离变化，远距离仍清晰 |
| `UWidgetComponent` 且 `Space = World` | 三维场景中的组件表面 | 符合摄像机透视，近大远小 |

官方枚举：`EWidgetSpace.World = 0`、`EWidgetSpace.Screen = 1`。

---

## 二、方案一：对象位置 UI

官方定义为「对象位置 UI、头顶 UI（类似血条、玩家名）」，生效范围服务器&客户端，控件必须继承 `UObjectPositionWidget`。

```lua
local instanceIndex = UGCWidgetManagerSystem.AddObjectPositionUI(
    targetActor,
    UGCGameSystem.GetUGCResourcesFullPath(UIPath),
    { X = 0, Y = 0, Z = 150 },
    true,  -- SizeAutoContent
    true,  -- OutViewHide
    true,  -- BeOcclusionHide
    true   -- ShowSelf
)
-- 卸载需要回传 instanceIndex
UGCWidgetManagerSystem.RemoveObjectPositionUI(targetActor, instanceIndex)
```

要点：

- `GetObjectPositionUI` 仅客户端生效，且 Add 之后不保证立刻取到，Widget 可能仍在加载，必须判空或延后绑定。
- 还有 `AddObjectPositionUI_Custom` 提供更多参数配置。
- 显示距离由 `ObjectPositionWidget.ParamInfo.MaxShowDistance` 控制（打工区实战中设为 3000，即 30 米）。
- 文本刷新走 `Event_InitParamEnd` + `SetText`，不依赖 `BindingProperty`；可用低频 Tick 补刷，但不要手动 `SetVisibility`。

### 实战踩坑

- **必须挂在 Actor 本体**，挂到独立标记物会导致文本不更新、并与本体链路叠加出双 UI；旧链路要显式停用。
- **只在本地有 `PlayerController` 的端挂载**，避免纯服务器重复挂载；同时做 Actor 级防重复。
- **远程 Pawn 脱离网络相关性后 Widget 会被引擎清理且不会自动重建**。称号系统的解法是客户端 5 秒定时器遍历全局选中表强制重挂。
- 称号缩放曾出现「越远越大」，根因是屏幕投影 UI 本身不随距离缩小，再叠加反向距离缩放就会异常。

---

## 三、方案二：World 空间 Widget 组件

`UWidgetComponent` 先把 `UUserWidget` 渲染到 RenderTarget，再以三维组件表面呈现，因此具备真实世界位置、旋转、缩放与透视。

蓝图挂载步骤：添加 `WidgetComponent` → `WidgetClass` 指向控件类 → `Space = World` → 设相对位置 → 设 `DrawSize`（或在布局稳定时用 `bDrawAtDesiredSize`）→ 按需设 `bIsTwoSided` → 用组件世界缩放决定真实尺寸。

获取实例用官方 `GetUserWidgetObject()`：

```lua
local widgetComponent = self.WorldTitle3D
local widget = widgetComponent and widgetComponent:GetUserWidgetObject() or nil
if widget then
    widget.WorldWidgetTargetActor = self  -- 项目自定义约定字段，非官方
end
```

注意：

- 世界空间 UI 不会自动朝向玩家，公告牌式 UI 需周期性 `FindLookAtRotation`；建议玩家进入范围才开 Timer，离开即清除。正反方向受组件本地朝向与资产 Transform 影响，须 PIE 确认是否需要额外 180 度。
- `bDrawAtDesiredSize` 每帧改变代价极高（官方警告）；启用 `bManuallyRedraw` 后内容变化需 `RequestRedraw()`，`RedrawTime` 可限制重绘频率。
- `bHideIfOccluded` 官方说明仅 Screen Space 有效，不能当作 World 模式遮挡开关；`bIsTwoSided` 只控制背面可见性。
- 需要玩家同时操控世界并与 3D UI 交互时，官方建议用 `WidgetInteractionComponent`，而不是直接开 `bReceiveHardwareInput`（会注册视口硬件输入并可能抢焦点）。

---

## 四、选型规则

1. 必须符合真实透视 → `UWidgetComponent + World`。
2. 必须远距离保持固定可读 → `AddObjectPositionUI`。
3. UI 是世界物件的一部分、应受空间关系影响 → `UWidgetComponent + World`。
4. UI 只是把 Actor 位置投影到 HUD → `AddObjectPositionUI`。
5. 两个需求同时出现时相互冲突，必须由设计决定优先级，**不能用反向距离缩放同时满足**。

---

## 五、五个常见错误

1. 把屏幕投影 UI 当世界 UI，误以为它会体现真实世界比例。
2. `WidgetComponent` 留在 `Space = Screen`，组件存在不等于已是世界 UI。
3. 对 World 模式按距离反向放大，抵消透视又制造新的尺寸异常。
4. 假定 Widget 自动知道挂载 Actor，实际需显式注入。
5. 频繁改 `bDrawAtDesiredSize` 或无条件每帧重绘。

---

## 六、相关页面

- [UI 页面切换与 Widget 生命周期](../UI与交互/UI页面切换与Widget生命周期.md)
- [模型渲染与缩放问题](../UI与交互/模型渲染与缩放问题.md)
- [资源导入与路径规范](../配置与数据/资源导入与路径规范.md)
- [蓝图与 MCP 写入流程](../工具与流程/蓝图与MCP写入流程.md)
- [MCP UI 编辑与高保真还原知识库](../UI与交互/MCP-UI编辑与高保真还原知识库.md)
- 来源：[2026-08-26 raw 资料入库总结](../来源记录/2026-08-26_raw资料入库总结.md)

---

## 七、待查证

- `AddObjectPositionUI` 的返回值类型官方文档未标注，运行时必须判空并以 PIE 验证。
- `WorldWidgetTargetActor` 为项目自定义字段。
- World 模式动态文本是否必须 `RequestRedraw()`，取决于组件重绘配置，需按项目 PIE 行为确认。
