# UGCWidgetUtility

UI控件工具接口库

## Parents

_None_

## Variables

_None_

## Functions

### CreateWidgetAsync

异步创建一个控件，返回控件实例

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WidgetClassPath | `string\|FSoftObjectPath` | 控件类路径 |
| OnCreatedCallback | `fun(Widget:UUserWidget)` | 创建完成回调 |

**Return**

_None_

### CreateWidget

创建一个控件，返回控件实例

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WidgetClass | `UClass` | 控件蓝图类 |

**Return**

- Type: 
- Description: _None_

### DestroyWidget

销毁一个控件

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](./UUserWidget.md) | 控件实例 |

**Return**

_None_

### SetWidgetLayout

异步加载并设置当前的 WidgetLayout，同时只能设置一个，旧的 WidgetLayout 会被卸载。传入 “Default” 可卸载 WidgetLayout 回到默认状态。（主要用于可视化屏蔽玩法中不需要的和平 UI，UI 会强制隐藏）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| LayoutPath | `string` | WidgetLayout 引用路径 |

**Return**

_None_

### GetUserWidgetByWidgetLayout

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

### AddToSlot

添加一个控件到指定 UI 挂点槽位

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](./UUserWidget.md) | 控件实例 |
| SlotName | `string` | 控件槽位名称，默认为 UI.UISlot.MainUISlot_Low |
| ZOrder | `number` | 控件层级，默认为 0 |
| AnchorData | [FAnchorData](../../cppstruct/F/FA/FAnchorData.md) | 控件锚点，默认为 { Anchors = { Minimum = Vector2D.New(0, 0), Maximum = Vector2D.New(1, 1) } } |

**Return**

_None_

### RemoveFromSlot

从 UI 挂点槽位移除控件

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](./UUserWidget.md) | 控件实例 |

**Return**

_None_

### IsWidgetAddedToSlot

判断一个控件是否已经挂载在 UI 挂点上

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](./UUserWidget.md) | 控件实例 |

**Return**

- Type: 
- Description: _None_

### ShowWidget

显示一个控件，需要控件已经挂载到挂点槽上

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](./UUserWidget.md) | 控件实例 |

**Return**

_None_

### HideWidget

隐藏一个控件

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](./UUserWidget.md) | 控件实例 |

**Return**

_None_

### SetWidgetVisible

设置控件的显示或隐藏状态
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](./UUserWidget.md) | 控件实例 |
| bVisible | `boolean` | 是否可见 |

**Return**

_None_

### IsWidgetVisible

判断一个控件是否可见

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](./UUserWidget.md) | 控件实例 |

**Return**

- Type: 
- Description: _None_

### GetSubWidget

获取子控件，可用于获取 UMG 蓝图里的子控件

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](./UUserWidget.md) | 控件实例 |
| SubWidgetName | `string` | 子控件名称 |

**Return**

- Type: 
- Description: _None_

### GetAllWidgetsOfClass

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

### AddChildToTochButton

把自定义 UI 挂到和平 UI 上并应用自定义布局
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | `UserWidget` |  |

**Return**

_None_

### ProjectWorldLocationToWidgetPosition

将世界坐标转换为控件坐标
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldLocation | [FVector](../../cppstruct/F/FV/FVector.md) | 世界坐标 |

**Return**

- Type: 
- Description: _None_

### SlotAsCanvasSlot

获取 Canvas 插槽
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](./UUserWidget.md) | 控件实例 |

**Return**

- Type: 
- Description: _None_

### SlotAsOverlaySlot

获取 Overlay 插槽
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](./UUserWidget.md) | 控件实例 |

**Return**

- Type: 
- Description: _None_

### SlotAsVerticalBoxSlot

获取 HorizontalBox 插槽
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](./UUserWidget.md) | 控件实例 |

**Return**

- Type: 
- Description: _None_

### GetViewportScale

获取视口缩放比例
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetViewportSize

获取视口尺寸
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetViewportWidgetGeometry

获取视口 Widget 几何信息
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetWidgetGeometry

获取控件的几何信息（可用于坐标转换等）
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](./UUserWidget.md) | 控件实例 |

**Return**

- Type: 
- Description: _None_

### AbsoluteToLocal

绝对坐标转本地坐标
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Geometry | `FGeometry` | 控件几何信息 |
| AbsoluteCoordinate | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | 绝对坐标 |

**Return**

- Type: 
- Description: _None_

### LocalToAbsolute

本地坐标转绝对坐标
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Geometry | `FGeometry` | 控件几何信息 |
| LocalCoordinate | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | 本地坐标 |

**Return**

- Type: 
- Description: _None_

### GetLocalSize

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

获取控件的绝对位置
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Geometry | `FGeometry` | 控件几何信息 |

**Return**

- Type: 
- Description: _None_

### SetWidgetOpacity

设置控件的不透明度
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](./UUserWidget.md) | 控件实例 |
| Opacity | `number` | 不透明度(0全透明~1不透明) |

**Return**

_None_

### GetWidgetOpacity

获取控件当前不透明度
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](./UUserWidget.md) | 控件实例 |

**Return**

- Type: 
- Description: _None_

### SetWidgetColor

设置控件的颜色和透明度（颜色与不透明度组合设置）
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](./UUserWidget.md) | 控件实例 |
| HexString | `string` | 设置字符串色值sRGB（含Alpha通道控制透明度），例：FB5AF9FF |

**Return**

_None_

### AddChildWidget

添加子控件到指定Panel父控件上（非Panel控件无效）
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ParentWidget | [UPanelWidget](./UPanelWidget.md) | Panel父控件 |
| ChildWidget | [UUserWidget](./UUserWidget.md) | 要添加的子控件 |

**Return**

_None_

### RemoveChildWidget

从Panel父控件移除指定子控件（非Panel控件无效）
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ParentWidget | [UPanelWidget](./UPanelWidget.md) | Panel父控件 |
| ChildWidget | [UUserWidget](./UUserWidget.md) | 需要移除的子控件 |

**Return**

_None_

### RemoveAllChildWidgets

清空Panel父控件下所有子控件（非Panel控件无效）
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ParentWidget | [UPanelWidget](./UPanelWidget.md) | Panel父控件 |

**Return**

_None_

### SetWidgetSlotPosition

设置控件在slot上的位置（相对于父控件）
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](./UUserWidget.md) | 控件实例 |
| Position | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | slot坐标位置 |

**Return**

_None_

### GetWidgetSlotPosition

获取控件当前slot位置（相对于父控件）
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](./UUserWidget.md) | 控件实例 |

**Return**

- Type: 
- Description: _None_

### SetWidgetSlotSize

设置控件的slot尺寸
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](./UUserWidget.md) | 控件实例 |
| Size | `Vector2D` | 尺寸（宽度，高度） |

**Return**

_None_

### GetWidgetSlotSize

获取控件slot尺寸
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](./UUserWidget.md) |  |

**Return**

- Type: 
- Description: _None_

### SetActiveWidgetIndex

设置容器控件（如 WidgetSwitcher）当前显示的页面索引
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Container | [UUserWidget](./UUserWidget.md) | 容器控件（需为WidgetSwitcher或类似） |
| Index | `integer` | 页面索引（从1开始） |

**Return**

_None_

### GetActiveWidgetIndex

获取容器当前显示的页面索引（从1开始）
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Container | [UUserWidget](./UUserWidget.md) |  |

**Return**

- Type: 
- Description: _None_

### GetActiveWidget

获取容器当前显示的页面控件
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetWidgetEnabled

设置控件是否可交互（启用/禁用输入）
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UUserWidget](./UUserWidget.md) | 控件实例 |
| bEnabled | `boolean` | 是否启用 |

**Return**

_None_

### SetCheckBoxChecked

设置复选框的勾选状态
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bChecked | `boolean` | 是否勾选 |

**Return**

_None_

### IsCheckBoxChecked

查询复选框是否勾选
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CheckBoxWidget | [UUserWidget](./UUserWidget.md) | 复选框控件 |

**Return**

- Type: 
- Description: _None_

### SetComboBoxSelectedOption

设置下拉菜单当前选中的选项
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ComboBoxWidget | [UUserWidget](./UUserWidget.md) | 下拉菜单控件实例 |
| Option | `string` | 选项文本 |

**Return**

_None_

### GetComboBoxSelectedOption

获取下拉菜单当前选中的选项文本
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ComboBoxWidget | [UUserWidget](./UUserWidget.md) | 下拉菜单控件实例 |

**Return**

- Type: 
- Description: _None_

### GetComboBoxOptionAtIndex

获取下拉菜单指定索引的选项文本
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ComboBoxWidget | [UUserWidget](./UUserWidget.md) | 下拉菜单控件实例 |
| Index | `integer` | 选项索引 |

**Return**

- Type: 
- Description: _None_

### SetWidgetProgress

设置进度条控件的当前进度值
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ProgressWidget | [UUserWidget](./UUserWidget.md) |  |
| Percent | `number` |  |

**Return**

- Type: 
- Description: _None_

### SetImageTexture

设置Image控件的图像/纹理（通过资源路径）
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Image | [UImage](./UImage.md) | 图像控件 |
| TexturePath | `string` | 纹理资源引用路径 |

**Return**

_None_

### ScrollBoxToEnd

滚动容器内容到底部
生效范围：客户端

**Parameters**

_None_

**Return**

_None_

### SetWidgetText

设置控件（文本控件）的显示文本
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UWidget](./UWidget.md) | 控件实例 |
| Text | `string` | 文本内容 |

**Return**

_None_

### GetWidgetText

获取控件（文本控件）的显示文本
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | [UWidget](./UWidget.md) | 文本控件 |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua
