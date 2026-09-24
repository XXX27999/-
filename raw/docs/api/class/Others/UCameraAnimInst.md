# UCameraAnimInst

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| CamAnim | `UCameraAnim *` | which CameraAnim this is an instance of |
| InterpGroupInst | `UInterpGroupInst *` | the UInterpGroupInst used to do the interpolation |
| PlayRate | `float` | Multiplier for playback rate.  1.0 = normal. |
| MoveTrack | `UInterpTrackMove *` | cached movement track from the currently playing anim so we don't have to go find it every frame |
| MoveInst | `UInterpTrackInstMove *` |  |
| PlaySpace | `TEnumAsByte < ECameraAnimPlaySpace :: Type >` |  |

## Functions

### SetCurrentTime

Jumps he camera anim to the given (unscaled) time.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### Stop

Stops this instance playing whatever animation it is playing.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bImmediate | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetDuration

Changes the running duration of this active anim, while maintaining playback position.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewDuration | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetScale

Changes the scale of the animation while playing.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewDuration | `float` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
