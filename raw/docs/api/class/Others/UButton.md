# UButton

The button is a click-able primitive widget to enable basic interaction, you
  can place any other widget inside a button to make a more complex and
  interesting click-able element in your UI.

   Single Child
   Clickable

## Parents

- [UContentWidget](./UContentWidget.md)
- IWidgetSkinInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Style_DEPRECATED | `USlateWidgetStyleAsset *` | The template style asset, used to seed the mutable instance of the style. |
| WidgetStyle | [FButtonStyle](../../cppstruct/F/FB/FButtonStyle.md) | The button style used at runtime |
| ColorAndOpacity | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | The color multiplier for the button content |
| BackgroundColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | The color multiplier for the button background |
| ClickMethod | `TEnumAsByte < EButtonClickMethod :: Type >` | The type of mouse action required by the user to trigger the buttons 'Click' |
| TouchMethod | `TEnumAsByte < EButtonTouchMethod :: Type >` | The type of touch action required by the user to trigger the buttons 'Click' |
| ListenEscMethod | `TEnumAsByte < EListenEscMethod :: Type >` | 通过命名识别关闭按钮，识别忽略大小写下划线，推荐命名(Button_Close,NewButton_Close...) |
| ListenActions | `TArray < FButtonListenAction >` | 通过监听Action，来统一模拟按键点击，扩展Esc模拟点击功能 |
| IsTipsBgBtn | `bool` | 是否为Tips背景按钮 |
| IsFocusable | `bool` | Sometimes a button should only be mouse-clickable and never keyboard focusable. |
| IsPassMouseEvent | `bool` |  |
| IsImgAlphaBtn | `bool` |  |
| bUseCustomSettings | `bool` |  |
| CustomHitAreaTexture | `UTexture2D *` |  |
| CustomHitAreaAlpha | `int` |  |
| bIsShowHover | `bool` |  |
| bIsLayerPlus | `bool` |  |
| OnMouseButtonDownEvent | `FOnPointerEvent` |  |
| OnMouseButtonUpEvent | `FOnPointerEvent` |  |
| OnMouseMoveEvent | `FOnPointerEvent` |  |
| InputActionBindings | [FButtonInputActionBindingsStruct](../../cppstruct/F/FB/FButtonInputActionBindingsStruct.md) |  |
| EscRespondSetting | [FEscRespondSetting](../../cppstruct/F/FE/FEscRespondSetting.md) |  |
| IsThisFrameClicked | `bool` |  |

## Functions

### SetStyle

Sets the color multiplier for the button background

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InStyle | `FButtonStyle &` |  |

**Return**

- Type: 
- Description: _None_

### SetColorAndOpacity

Sets the color multiplier for the button content

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InColorAndOpacity | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_

### SetBackgroundColor

Sets the color multiplier for the button background

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBackgroundColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_

### IsPressed

Returns true if the user is actively pressing the button.  Do not use this for detecting 'Clicks', use the OnClicked event instead.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Release

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetClickMethod

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InClickMethod | `EButtonClickMethod :: Type` |  |

**Return**

- Type: 
- Description: _None_

### SetTouchMethod

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTouchMethod | `EButtonTouchMethod :: Type` |  |

**Return**

- Type: 
- Description: _None_

### GetReleasedReason

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetListenEscMethod

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InListenEscMethod | `EListenEscMethod :: Type` |  |

**Return**

- Type: 
- Description: _None_

### GetListenEscMethod

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetShowHover

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InShowHover | `bool` |  |

**Return**

- Type: 
- Description: _None_

### AddListenAction

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InActionName | `FName` |  |
| InType | `EButtonListenActionEvent :: Type` |  |

**Return**

- Type: 
- Description: _None_

### RemoveListenAction

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InActionName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### ClearListenActions

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetCacheLayerId

return CacheLayerId only windows

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### RespondEscape

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetButtonsFromAction

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OutButtons | `TArray < UButton * > &` |  |
| InAction | `FName` |  |

**Return**

- Type: 
- Description: _None_

### ClearInvalidForListenActions

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetButtonsFromTipsBg

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetButtonClickedGlobalEvent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InEvent | `FOnButtonClickedGlobalEvent` |  |

**Return**

- Type: 
- Description: _None_

### ClearButtonClickedGlobalEvent

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetIsFocusable

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InFocusable | `bool` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnClicked |  | Called when the button is clicked |
| OnPressed |  | Called when the button is pressed |
| OnReleased |  | Called when the button is released |
| OnHovered |  |  |
| OnUnhovered |  |  |
| OnPressedParam |  |  |
| OnReleasedParam |  |  |
| OnReplayRecordNotify |  |  |

## Language

cpp
