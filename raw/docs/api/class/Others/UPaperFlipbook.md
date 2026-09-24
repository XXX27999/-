# UPaperFlipbook

Contains an animation sequence of sprite frames

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| FramesPerSecond | `float` |  |
| KeyFrames | `TArray < FPaperFlipbookKeyFrame >` |  |
| DefaultMaterial | `UMaterialInterface *` |  |
| CollisionSource | `TEnumAsByte < EFlipbookCollisionMode :: Type >` |  |

## Functions

### GetNumFrames

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetTotalDuration

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetKeyFrameIndexAtTime

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Time | `float` |  |
| bClampToEnds | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetSpriteAtTime

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Time | `float` |  |
| bClampToEnds | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetSpriteAtFrame

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| FrameIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetNumKeyFrames

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsValidKeyFrameIndex

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Index | `int32` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
