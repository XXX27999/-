# UScrollBox

An arbitrary scrollable collection of widgets.  Great for presenting 10-100 widgets in a list.  Doesn't support virtualization.

## Parents

- [UPanelWidget](./UPanelWidget.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| WidgetStyle | [FScrollBoxStyle](../../cppstruct/F/FS/FScrollBoxStyle.md) | The style |
| WidgetBarStyle | [FScrollBarStyle](../../cppstruct/F/FS/FScrollBarStyle.md) | The bar style |
| OverscrollLooseness | `float` | Overscroll Looseness |
| Style_DEPRECATED | `USlateWidgetStyleAsset *` |  |
| BarStyle_DEPRECATED | `USlateWidgetStyleAsset *` |  |
| Orientation | `TEnumAsByte < EOrientation >` | The orientation of the scrolling and stacking in the box. |
| ScrollBarVisibility | [ESlateVisibility](../../cppenum/E/ES/ESlateVisibility.md) | Visibility |
| ConsumeMouseWheel | [EConsumeMouseWheel](../../cppenum/E/EC/EConsumeMouseWheel.md) | Enable to always consume mouse wheel event, even when scrolling is not possible |
| ScrollbarThickness | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |
| AlwaysShowScrollbar | `bool` |  |
| AllowOverscroll | `bool` | Disable to stop scrollbars from activating inertial overscrolling |
| NavigationDestination | [EDescendantScrollDestination](../../cppenum/E/ED/EDescendantScrollDestination.md) |  |
| NavigationScrollPadding | `float` | The amount of padding to ensure exists between the item being navigated to, at the edge of the<br>	  scrollbox.  Use this if you want to ensure there's a preview of the next item the user could scroll to. |
| bAllowRightClickDragScrolling | `bool` | Option to disable right-click-drag scrolling |
| bScrollEnabled | `bool` | 启用滑动 |
| bScrollDisableHandled | `bool` | 启用滑动 |
| bPreciseScroll | `bool` | 启用精准滑动 |
| bDisableDragListScroll | `bool` | 依旧可以通过拖拽bar或者鼠标滚轮滑动, 仅PC版生效 |
| bScrollFocus | `bool` | 滑动时获得焦点 |

## Functions

### SetOrientation

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewOrientation | [EOrientation](../../cppenum/E/EO/EOrientation.md) |  |

**Return**

- Type: 
- Description: _None_

### SetScrollBarVisibility

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewScrollBarVisibility | [ESlateVisibility](../../cppenum/E/ES/ESlateVisibility.md) |  |

**Return**

- Type: 
- Description: _None_

### SetScrollbarThickness

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewScrollbarThickness | `FVector2D &` |  |

**Return**

- Type: 
- Description: _None_

### SetAlwaysShowScrollbar

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewAlwaysShowScrollbar | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetAllowOverscroll

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewAllowOverscroll | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetCacheOverscrollOffset

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetOverscrollLooseness

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| v | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetScrollEnabled

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InScrollEnabled | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetScrollDisableHandled

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InScrollDisableHandled | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetScrollPrecise

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InScrollPrecise | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetScrollFocus

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InScrollFocus | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetDragListScrollEnabled

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InDragListScrollEnabled | `bool` |  |

**Return**

- Type: 
- Description: _None_

### IsReachEnd

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsLargerThanContentSize

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetScrollOffset

Updates the scroll offset of the scrollbox.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewScrollOffset | `float` | is in Slate Units. |

**Return**

- Type: 
- Description: _None_

### GetScrollOffset

Gets the scroll offset of the scrollbox in Slate Units.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ScrollToStart

Scrolls the ScrollBox to the top instantly

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ScrollToEnd

Scrolls the ScrollBox to the bottom instantly during the next layout pass.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### StopScroll

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ScrollWidgetIntoView

Scrolls the ScrollBox to the widget during the next layout pass.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WidgetToFind | `UWidget *` |  |
| AnimateScroll | `bool` |  |
| ScrollDestination | [EDescendantScrollDestination](../../cppenum/E/ED/EDescendantScrollDestination.md) |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnUserScrolled |  | Called when the scroll has changed |
| OnUserScrolledUnused |  | Called when the scroll has changed,the value is mouse movement in another direction -zhenzhai |
| OnTouchFinish |  | Called when the touch has end |

## Language

cpp
