# UAnimSingleNodeInstance

## Parents

- [UAnimInstance](./UAnimInstance.md)

## Variables

_None_

## Functions

### SetLooping

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bIsLooping | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetPlayRate

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPlayRate | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetReverse

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInReverse | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetPosition

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPosition | `float` |  |
| bFireNotifies | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetPositionWithPreviousTime

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPosition | `float` |  |
| InPreviousTime | `float` |  |
| bFireNotifies | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetBlendSpaceInput

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBlendInput | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### SetPlaying

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bIsPlaying | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetLength

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### PlayAnim

For AnimSequence specific

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bIsLooping | `bool` |  |
| InPlayRate | `float` |  |
| InStartPosition | `float` |  |

**Return**

- Type: 
- Description: _None_

### StopAnim

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetAnimationAsset

Set New Asset - calls InitializeAnimation, for now we need MeshComponent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewAsset | `UAnimationAsset *` |  |
| bIsLooping | `bool` |  |
| InPlayRate | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetAnimationAsset

Get the currently used asset

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetPreviewCurveOverride

Set pose value

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PoseName | `FName &` |  |
| Value | `float` |  |
| bRemoveIfZero | `bool` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| PostEvaluateAnimEvent |  |  |
| OnAnimSinglePlayAnim |  |  |

## Language

cpp
