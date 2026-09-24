# UExpandableArea

## Parents

- [UWidget](./UWidget.md)
- INamedSlotInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Style | [FExpandableAreaStyle](../../cppstruct/F/FE/FExpandableAreaStyle.md) |  |
| BorderBrush | [FSlateBrush](../../cppstruct/F/FS/FSlateBrush.md) |  |
| BorderColor | [FSlateColor](../../cppstruct/F/FS/FSlateColor.md) |  |
| bIsExpanded | `bool` |  |
| MaxHeight | `float` | The maximum height of the area |
| HeaderPadding | [FMargin](../../cppstruct/F/FM/FMargin.md) |  |
| AreaPadding | [FMargin](../../cppstruct/F/FM/FMargin.md) |  |
| HeaderContent | `UWidget *` |  |
| BodyContent | `UWidget *` |  |

## Functions

### GetIsExpanded

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetIsExpanded

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| IsExpanded | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetIsExpanded_Animated

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| IsExpanded | `bool` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnExpansionChanged |  | A bindable delegate for the IsChecked. |

## Language

cpp
