# UWrapBox

Arranges widgets left-to-right.  When the widgets exceed the Width it will place widgets on the next line.

   Many Children
   Flows
   Wraps

## Parents

- [UPanelWidget](./UPanelWidget.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| InnerSlotPadding | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | The inner slot padding goes between slots sharing borders |
| WrapWidth | `float` | When this width is exceeded, elements will start appearing on the next line. |
| bExplicitWrapWidth | `bool` | Use explicit wrap width whenever possible. It greatly simplifies layout calculations and reduces likelihood of "wiggling UI" |

## Functions

### SetInnerSlotPadding

Sets the inner slot padding goes between slots sharing borders

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPadding | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### AddChildWrapBox

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Content | `UWidget *` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
