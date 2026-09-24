# UGCWidgetManagerSystem

UI控件管理器系统接口库

## Parents

_None_

## Variables

_None_

## Functions

### CreateWidgetAsync

【废弃】请使用 UGCWidgetUtility.CreateWidgetAsync
异步创建一个控件，返回控件实例

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WidgetClassPath | `string\|FSoftObjectPath` | 控件类路径 |
| OnCreatedCallback | `fun(Widget:UUserWidget)` | 创建完成回调 |

**Return**

_None_

### CreateWidget

【废弃】请使用 UGCWidgetUtility.CreateWidget
创建一个控件，返回控件实例

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WidgetClass | `UClass` | 控件蓝图类 |

**Return**

- Type: 
- Description: _None_

### DestroyWidget

【废弃】请使用 UGCWidgetUtility.DestroyWidget
销毁一个控件

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](../../Others/UUserWidget.md) | 控件实例 |

**Return**

_None_

### AddToSlot

【废弃】请使用 UGCWidgetUtility.AddToSlot
添加一个控件到指定 UI 挂点槽位

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](../../Others/UUserWidget.md) | 控件实例 |
| SlotName | `string` | 控件槽位名称，默认为 UI.UISlot.MainUISlot_Low |
| ZOrder | `number` | 控件层级，默认为 0 |
| AnchorData | [FAnchorData](../../../cppstruct/F/FA/FAnchorData.md) | 控件锚点，默认为 { Anchors = { Minimum = Vector2D.New(0, 0), Maximum = Vector2D.New(1, 1) } } |

**Return**

_None_

### RemoveFromSlot

【废弃】请使用 UGCWidgetUtility.RemoveFromSlot
从 UI 挂点槽位移除控件

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](../../Others/UUserWidget.md) | 控件实例 |

**Return**

_None_

### SetWidgetLayout

【废弃】请使用 UGCWidgetUtility.SetWidgetLayout
异步加载并设置当前的 WidgetLayout，同时只能设置一个，旧的 WidgetLayout 会被卸载。传入 "Default" 可卸载 WidgetLayout 回到默认状态。（主要用于可视化屏蔽玩法中不需要的和平 UI，UI 会强制隐藏）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| LayoutPath | `string` | WidgetLayout 引用路径 |

**Return**

_None_

### ShowWidget

【废弃】请使用 UGCWidgetUtility.ShowWidget
显示一个控件，需要控件已经挂载到挂点槽上

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](../../Others/UUserWidget.md) | 控件实例 |

**Return**

_None_

### HideWidget

【废弃】请使用 UGCWidgetUtility.HideWidget
隐藏一个控件

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](../../Others/UUserWidget.md) | 控件实例 |

**Return**

_None_

### IsWidgetAddedToSlot

【废弃】请使用 UGCWidgetUtility.IsWidgetAddedToSlot
判断一个控件是否已经挂载在 UI 挂点上

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](../../Others/UUserWidget.md) | 控件实例 |

**Return**

- Type: 
- Description: _None_

### IsWidgetVisible

【废弃】请使用 UGCWidgetUtility.IsWidgetVisible
判断一个控件是否可见

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](../../Others/UUserWidget.md) | 控件实例 |

**Return**

- Type: 
- Description: _None_

### GetSubWidget

【废弃】请使用 UGCWidgetUtility.GetSubWidget
获取子控件，可用于获取 UMG 蓝图里的子控件

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](../../Others/UUserWidget.md) | 控件实例 |
| SubWidgetName | `string` | 子控件名称 |

**Return**

- Type: 
- Description: _None_

### GetAllWidgetsOfClass

【废弃】请使用 UGCWidgetUtility.GetAllWidgetsOfClass
获取指定类别的所有控件，可筛选只获取已被添加到挂点的控件
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WidgetClass | `UClass` | 控件类（UUserWidget） |
| bAddedToSlotOnly | `boolean` | 是否只获取已添加到挂点的控件 |

**Return**

- Type: 
- Description: _None_

### GetMainUI

获取主 UI 面板实例（MainControlPanelTochButton）
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetMainControlUI

获取主控制 UI 面板实例（MainControlBaseUI）
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetShootingUIPanel

获取射击相关UI面板实例（ShootingUIPanel）
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetSkillRootPanel

获取技能相关UI面板实例（SkillRootPanel_BP）
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetUserWidgetByWidgetLayout

【废弃】请使用 UGCWidgetUtility.GetUserWidgetByWidgetLayout
获取通过WidgetLayout加载的自定义UserWidget
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WidgetLayoutPath | `string` | 控件 ClassPath, 控件需继承自 UUserWidgetLayout |
| UserWidgetName | `string` | 控件 Name |

**Return**

- Type: 
- Description: _None_

### SubWidgetHiddenLayer

【废弃】请使用 UGCWidgetUtility.ShowWidget
SubWidgetHiddenLayer为控件减少隐藏层数（主要用于屏蔽玩法中不需要的和平 UI，HiddenLayer>=1，UI 会强制隐藏）
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | `UserWidget` |  |

**Return**

_None_

### SetVirtualJoystickVisibility

设置摇杆是否可见
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| IsVisibility | `boolean` | 是否可见（true 为显示，false 为隐藏） |

**Return**

_None_

### SetCrosshairVisibility

设置准星是否可见
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| IsVisibility | `boolean` | 是否可见（true 为显示，false 为隐藏，在没有被隐藏的情况下禁止将其显示） |

**Return**

_None_

### Share

弹出分享界面
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CloseCallBack | `function` | 关闭分享界面回调函数 |

**Return**

- Type: 
- Description: _None_

### AddChildToTochButton

【废弃】请使用 UGCWidgetUtility.AddChildToTochButton
把自定义 UI 挂到和平 UI 上并应用自定义布局
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | `UserWidget` |  |

**Return**

_None_

### LoadLobbyChatFrameUI

加载大厅聊天框 UI
生效范围：客户端

**Parameters**

_None_

**Return**

_None_

### AddObjectPositionUI

添加对象位置 UI,头顶 UI（类似血条，玩家名）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | `Actor` | 需要添加位置 UI 的 Actor 对象 |
| WidgetClassPath | `string` | 控件 ClassPath 控件需继承自 UObjectPositionWidget |
| Offset | [FVector](../../../cppstruct/F/FV/FVector.md) | 偏移量 |
| SizeAutoContent | `boolean` | 大小适配 |
| OutViewHide | `boolean` | 控件离开镜头后是否隐藏（比如在背后） |
| BeOcclusionHide | `boolean` | 被遮挡后是否隐藏 |
| ShowSelf | `boolean` | 是否显示自己的 |

**Return**

- Type: 
- Description: _None_

### AddObjectPositionUI_Custom

添加对象位置 UI,头顶 UI（类似血条，玩家名），自定义版本，提供更多参数配置。（ObjectPosUIInfo 可在蓝图中添加参数使用带有默认值的版本）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | `Actor` | 需要添加位置 UI 的 Actor 对象 |
| WidgetClassPath | `string` | 控件 ClassPath 控件需继承自 UObjectPositionWidget |
| ObjectPosUIInfo | `FObjectPosUIInfo` | 配置属性结构体，可以在蓝图中定义该变量传入 |

**Return**

- Type: 
- Description: _None_

### RemoveObjectPositionUI

移除对象位置 UI
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContent | [UObject](../../Others/UObject.md) | 世界中对象 |
| InstanceIndex | `number` | 实例 Index |

**Return**

_None_

### GetObjectPositionUI

根据 InstanceIndex 获取 Widget 实例（Add 之后不能立刻获取到，Widget 有可能还在加载）
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContent | [UObject](../../Others/UObject.md) | 世界中对象 |
| InstanceIndex | `number` | 实例 Index |

**Return**

- Type: 
- Description: _None_

### SetPlayerStateUIVisibility

设置玩家状态 UI 可见性
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bVisible | `boolean` | 是否显示（true 为显示，false 为隐藏） |

**Return**

- Type: 
- Description: _None_

### ShowTipsUI

在屏幕中间上方显示 Tips 内容
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TipsContent | `string` | Tips 文字内容 |

**Return**

_None_

### ShowTipsUIByServer

在屏幕中间上方显示 Tips 内容，从DS发起，在传入的PC所属的客户端显示
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TipsContent | `string` | Tips 文字内容 |
| PlayerController | `PlayerController` | 玩家控制器 |

**Return**

_None_

### ShowCustomTipsByIDWithPC

在屏幕中间上方用用户配置的UI显示 Tips 内容，从DS发起，在传入的PC所属的客户端显示
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ID | `number` | Tips Tips表里的ID |
| TipsContent | `string` | Tips 文字内容 |
| PlayerController | `PlayerController` | 玩家控制器 |

**Return**

_None_

### ShowCustomTipsByID

在屏幕中间上方显示用户配置的 Tips 内容
生效范围：客户端
  1. UUAEBlackboard 对象 — 直接使用
  2. table 数组（推荐）— 如 {{SelectedKeyName="Point",Type=EUAEBlackboardType.EBT_Int,Value=20}, ...}，内部自动构造 Blackboard 并按 Type 设置值
  3. nil/省略 — 不传额外参数

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ID | `number` | Tips Tips表里的ID |
| TipsContent | `string\|nil` | Tips 文字内容 |
| ExtraParam | `UUAEBlackboard\|table\|nil` | Tips 额外参数，支持三种传入方式： |

**Return**

_None_

### GetGlobalOBUI

获取全局观战 UI，仅全局观战模式下生效
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ChangeMap

修改右上角地图
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MapPath | `string` | 地图文件路径 |
| MapCentre | [FVector](../../../cppstruct/F/FV/FVector.md) | 地图中心点坐标 |
| MapSize | `number` | 地图实际大小 |
| MapScale | `number` | 地图缩放比 |

**Return**

_None_

### ChangeMapByMapID

根据地图ID修改右上角地图
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MapID | `number` | 地图ID |

**Return**

_None_

### ProjectWorldLocationToWidgetPosition

【废弃】请使用 UGCWidgetUtility.ProjectWorldLocationToWidgetPosition
将世界坐标转换为控件坐标
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldLocation | [FVector](../../../cppstruct/F/FV/FVector.md) | 世界坐标 |

**Return**

- Type: 
- Description: _None_

### SlotAsCanvasSlot

【废弃】请使用 UGCWidgetUtility.SlotAsCanvasSlot
获取 Canvas 插槽
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](../../Others/UUserWidget.md) | 控件实例 |

**Return**

- Type: 
- Description: _None_

### SlotAsOverlaySlot

【废弃】请使用 UGCWidgetUtility.SlotAsOverlaySlot
获取 Overlay 插槽
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](../../Others/UUserWidget.md) | 控件实例 |

**Return**

- Type: 
- Description: _None_

### SlotAsVerticalBoxSlot

【废弃】请使用 UGCWidgetUtility.SlotAsVerticalBoxSlot
获取 HorizontalBox 插槽
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](../../Others/UUserWidget.md) | 控件实例 |

**Return**

- Type: 
- Description: _None_

### GetViewportScale

【废弃】请使用 UGCWidgetUtility.GetViewportScale
获取视口缩放比例
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetViewportSize

【废弃】请使用 UGCWidgetUtility.GetViewportSize
获取视口尺寸
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetViewportWidgetGeometry

【废弃】请使用 UGCWidgetUtility.GetViewportWidgetGeometry
获取视口 Widget 几何信息
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### AbsoluteToLocal

【废弃】请使用 UGCWidgetUtility.AbsoluteToLocal
绝对坐标转本地坐标
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Geometry | `FGeometry` | 控件几何信息 |
| AbsoluteCoordinate | [FVector2D](../../../cppstruct/F/FV/FVector2D.md) | 绝对坐标 |

**Return**

- Type: 
- Description: _None_

### LocalToAbsolute

【废弃】请使用 UGCWidgetUtility.LocalToAbsolute
本地坐标转绝对坐标
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Geometry | `FGeometry` | 控件几何信息 |
| LocalCoordinate | [FVector2D](../../../cppstruct/F/FV/FVector2D.md) | 本地坐标 |

**Return**

- Type: 
- Description: _None_

### GetLocalSize

【废弃】请使用 UGCWidgetUtility.GetLocalSize
获取控件的本地尺寸
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Geometry | `FGeometry` | 控件几何信息 |

**Return**

- Type: 
- Description: _None_

### GetAbsoluteSize

【废弃】请使用 UGCWidgetUtility.GetAbsoluteSize
获取控件的绝对尺寸
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Geometry | `FGeometry` | 控件几何信息 |

**Return**

- Type: 
- Description: _None_

### GetAbsolutePosition

【废弃】请使用 UGCWidgetUtility.GetAbsolutePosition
获取控件的绝对位置
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Geometry | `FGeometry` | 控件几何信息 |

**Return**

- Type: 
- Description: _None_

### GetWidgetFromName

【废弃】请使用 UGCWidgetUtility.GetSubWidget
通过控件名获取某一控件的子控件
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | `UserWidget` |  |
| UserWidgetName | `string` | 控件 Name |

**Return**

- Type: 
- Description: _None_

### LoadMainUIWidgetLayoutByPath

【废弃】请使用 UGCWidgetUtility.SetWidgetLayout
可视化设置主 UI 控件是否可见（主要用于可视化屏蔽玩法中不需要的和平 UI，UI 会强制隐藏）
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WidgetLayoutPath | `string` | 控件 ClassPath, 控件需继承自 UUserWidgetLayout |

**Return**

_None_

### UnloadMainUIWidgetLayoutByPath

【废弃】请使用 UGCWidgetUtility.SetWidgetLayout
可视化设置主 UI 控件是否可见（主要用于可视化屏蔽玩法中不需要的和平 UI，UI 会强制隐藏）
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WidgetLayoutPath | `string` | 控件 ClassPath, 控件需继承自 UUserWidgetLayout |

**Return**

_None_

### AddChildToUISlotByPath

【废弃】请使用 UGCWidgetUtility.CreateWidgetAsync + UGCWidgetUtility.AddToSlot
把自定义 UI 挂到和平 UI 挂点上
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WidgetPath | `string` | 控件 ClassPath |
| UISlotName | `string` | 挂点标识 |
| ZOrder | `number` | 层级 |
| AnchorData | [FAnchorData](../../../cppstruct/F/FA/FAnchorData.md) | 控件布局信息 |

**Return**

- Type: 
- Description: _None_

### AddChildToUISlotByWidget

【废弃】请使用 UGCWidgetUtility.AddToSlot
把自定义 UI 挂到和平 UI 挂点上
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | `UserWidget` | UI |
| UISlotName | `string` | 挂点标识 |
| ZOrder | `number` | 层级 |
| AnchorData | [FAnchorData](../../../cppstruct/F/FA/FAnchorData.md) | 控件布局信息 |

**Return**

_None_

### AddWidgetHiddenLayer

【废弃】请使用 UGCWidgetUtility.HideWidget
为控件添加隐藏层数（主要用于屏蔽玩法中不需要的和平 UI，HiddenLayer>=1，UI 会强制隐藏）
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | `UserWidget` |  |

**Return**

_None_

### AddNewUI

【废弃】请使用 UGCWidgetUtility.CreateWidgetAsync + UGCWidgetUtility.AddToSlot
添加新 UI，将会自动完成 AddViewport 显示
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WidgetClassPath | `string` | Widget 路径 |
| IsAdaptation | `boolean` | 是否屏幕适配 |

**Return**

- Type: 
- Description: _None_

### CreateNewWidget

【废弃】请使用 UGCWidgetUtility.CreateWidgetAsync
创建新控件
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WidgetClassPath | `string` | Widget 路径 |

**Return**

- Type: 
- Description: _None_

### CreateNewWidgetAsync

【废弃】请使用 UGCWidgetUtility.CreateWidgetAsync
异步创建新控件，并绑定回调
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WidgetClassPath | `string` | Widget 路径 |
| InCreatedDelegate | [ULuaSingleDelegate](../../Others/ULuaSingleDelegate.md) | 回调 |

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua
