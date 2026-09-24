# UGCCommonDragDropItem

拖拽控件

## Parents

_None_

## Variables

_None_

## Functions

### SetDragWidget

设置拖拽时的控件

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | `UUserWidget\|Class` | 拖拽时的控件实例 或 类 |
| bCreate | `boolean` | 是否创建控件，传入Class则创建控件实例 |

**Return**

_None_

### SetDragDirectionMode

设置拖拽方向模式

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DirectionMode | [EDragDirectionMode](../../cppenum/E/ED/EDragDirectionMode.md) | 拖拽方向模式 |

**Return**

_None_

### SetDragDropMode

设置拖拽模式

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DragDropMode | [EDragDropMode](../../cppenum/E/ED/EDragDropMode.md) | 拖拽模式 |

**Return**

_None_

### RegisterDragDropData

注册拖拽(入口), 仅执行一次有效

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DragDropData | `table` | 拖拽数据，在拖拽响应事件中传递 |
| DragDropMode | [EDragDropMode](../../cppenum/E/ED/EDragDropMode.md) | 拖拽模式 |
| InDragWidgetClass | `FSoftClassPath\|string` | 可选，自定义拖拽控件类 |

**Return**

_None_

### SetData

设置拖拽数据

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Data | `table` | 拖拽数据 |

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua
