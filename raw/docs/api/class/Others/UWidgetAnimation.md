# UWidgetAnimation

## Parents

- [UMovieSceneSequence](./UMovieSceneSequence.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| MovieScene | `UMovieScene *` | Pointer to the movie scene that controls this animation. |
| AnimationBindings | `TArray < FWidgetAnimationBinding >` |  |

## Functions

### GetStartTime

Get the start time of this animation.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetEndTime

Get the end time of this animation.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### BindToAnimationStarted

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | `UUserWidget *` |  |
| Delegate | `FWidgetAnimationDynamicEvent` |  |

**Return**

- Type: 
- Description: _None_

### UnbindFromAnimationStarted

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | `UUserWidget *` |  |
| Delegate | `FWidgetAnimationDynamicEvent` |  |

**Return**

- Type: 
- Description: _None_

### UnbindAllFromAnimationStarted

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | `UUserWidget *` |  |

**Return**

- Type: 
- Description: _None_

### BindToAnimationFinished

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | `UUserWidget *` |  |
| Delegate | `FWidgetAnimationDynamicEvent` |  |

**Return**

- Type: 
- Description: _None_

### UnbindFromAnimationFinished

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | `UUserWidget *` |  |
| Delegate | `FWidgetAnimationDynamicEvent` |  |

**Return**

- Type: 
- Description: _None_

### UnbindAllFromAnimationFinished

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | `UUserWidget *` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnAnimationStarted |  | Fires when the widget animation starts playing. compatible for lua, to be deleted |
| OnAnimationFinished |  | Fires when the widget animation is finished. compatible for lua, to be deleted |

## Language

cpp
