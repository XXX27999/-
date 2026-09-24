# UGCMapMarkManagerSystem

地图标记管理器系统接口库

## Parents

_None_

## Variables

_None_

## Functions

### AddCustomMark

添加一个自定义 Mark，需要自行管理位置（Widget 需继承自 MapUIMarkBaseWidget）
必须先调用一次 UpdateMarkLocation，调用 GetMarkLocation 才有效（Rotation 同理）
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WidgetClassPath | `string` | 控件类路径，Widget 需继承自 MapUIMarkBaseWidget |
| RangeType | [EMarkDispatchRange](../../../cppenum/E/EM/EMarkDispatchRange.md) | 标记同步范围 |
| RangeRad | `number` | 标记显示范围，超出范围不会显示标记（目标实际距离，单位：cm） |
| OwnerPlayerState | `PlayerState` | 同步相关性 PlayerState，主要用于仅同步自身或者队友同步，非必传 |

**Return**

- Type: 
- Description: _None_

### AddLocalCustomMark

添加一个自定义 Mark，需要自行管理位置（Widget 需继承自 MapUIMarkBaseWidget）
必须先调用一次 UpdateMarkLocation，调用 GetMarkLocation 才有效（Rotation 同理）
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WidgetClassPath | `string` | 控件类路径，Widget 需继承自 MapUIMarkBaseWidget |
| RangeRad | `number` | 标记显示范围，超出范围不会显示标记（目标实际距离，单位：cm） |

**Return**

- Type: 
- Description: _None_

### AddPlayerMark

添加一个玩家 Mark，会根据玩家位置实时更新位置。（Widget 需继承自 UGCMapUIMarkDynamicWidget）
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WidgetClassPath | `string` | 控件类路径，Widget 需继承自 UGCMapUIMarkDynamicWidget |
| RangeType | [EMarkDispatchRange](../../../cppenum/E/EM/EMarkDispatchRange.md) | 标记同步范围 |
| RangeRad | `number` | 标记显示范围，超出范围不会显示标记（目标实际距离，单位：cm） |
| OwnerPlayerState | `PlayerState` | 标记目标 PlayerState |

**Return**

- Type: 
- Description: _None_

### AddLocalPlayerMark

添加一个玩家Mark，会根据玩家位置实时更新位置。（Widget 需继承自 UGCMapUIMarkDynamicWidget）
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WidgetClassPath | `string` | 控件类路径，Widget 需继承自 UGCMapUIMarkDynamicWidget |
| OwnerPlayerState | `PlayerState` | 标记目标 PlayerState |
| RangeRad | `number` | 标记显示范围，超出范围不会显示标记（目标实际距离，单位：cm） |

**Return**

- Type: 
- Description: _None_

### RemoveMark

移除一个标记，此接口的调用者同传入的 InstanceID 匹配。
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstanceID | `number` | 标记 ID |

**Return**

_None_

### UpdateMarkLocation

更新标记位置，此接口的调用者同传入的 InstanceID 匹配。
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstanceID | `number` | 标记 ID |
| MarkLocation | `Vector` | 新 Location |
| bNeedPrintLog | `boolean` | 是否输出日志 |

**Return**

_None_

### UpdateMarkRotation

更新标记旋转，此接口的调用者同传入的 InstanceID 匹配。
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstanceID | `number` | 标记 ID |
| NewRotation | `Rotator` | 新 Rotator 可使用 Rotator.New(Roll,Pitch,Yaw) 创建，结构 {Roll=Roll, Pitch=Pitch, Yaw=Yaw} |

**Return**

_None_

### GetMarkLocation

获取标记位置，此接口的调用者同传入的 InstanceID 匹配。
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstanceID | `number` | 标记 ID |

**Return**

- Type: 
- Description: _None_

### GetMarkRotation

获取标记旋转，此接口的调用者同传入的 InstanceID 匹配。
调用此接口来更新通过 UGCMapMarkManagerSystem.Add[Local]CustomMark 创建的小地图标记控件时，须确保该控件的 Rotate Widget to Angle 选项已勾选。
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstanceID | `number` | 标记 ID |

**Return**

- Type: 
- Description: _None_

### GetMarkOwner

获取标记 Owner，此接口的调用者同传入的 InstanceID 匹配。
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstanceID | `number` | 标记 ID |

**Return**

- Type: 
- Description: _None_

### MakeMapMarkGraph

在地图上画图
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldCorners | `FVector[]` | 世界坐标点，按顺序绘制，1个点画圆，2个点画直线，3个点或以上画多边形 |
| MarkColor | [FColor](../../../cppstruct/F/FC/FColor.md) | 图像颜色 |
| RadiusOrLineWidth | `number` | 半径或直线宽度 |
| bRecolorOrBlending | `boolean` | 覆盖颜色或Alpha混合 |
| AddMarkFlag | [EAddMarkFlag](../../../cppenum/E/EA/EAddMarkFlag.md) | 生效地图类型 |

**Return**

_None_

### ClearMapMarkGraph

清除地图上的图案
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ClearMarkFlag | [EAddMarkFlag](../../../cppenum/E/EA/EAddMarkFlag.md) | 生效地图类型 |

**Return**

_None_

### SetVoiceVisualization

开关小地图上的指定类型音效图标
生效范围：服务端&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InFlag | [EVoiceVisualizationFlag](../../../cppenum/E/EV/EVoiceVisualizationFlag.md) | 指定音效类型 |
| bIsEnable | `boolean` | 开关控制 |

**Return**

_None_

### IsVoiceVisualizationFlagEnable

获取小地图上指定类型音效图标的开关状态
生效范围：服务端&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InFlag | [EVoiceVisualizationFlag](../../../cppenum/E/EV/EVoiceVisualizationFlag.md) | 指定音效类型 |

**Return**

- Type: 
- Description: _None_

### GetMapMarkLocation

获取和平原生小地图标点位置
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerState | `ASTExtraPlayerState` | 玩家状态 |

**Return**

- Type: 
- Description: _None_

### ChangeMapByMapID

根据地图ID修改右上角地图
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MapID | `number` | 地图ID |

**Return**

_None_

### DrawGuidePathToTarget

请求绘制引导线
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Params | `FGuidePathDrawParams` | 绘制参数 |
| OnResult | `FOnGuidePathResult` | 结果回调 |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua
