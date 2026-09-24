# UPaperFlipbookComponent

## Parents

- [UMeshComponent](./UMeshComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| SourceFlipbook | `UPaperFlipbook *` | Flipbook currently being played |
| Material_DEPRECATED | `UMaterialInterface *` |  |
| PlayRate | `float` | Current play rate of the flipbook |
| bLooping | `uint32` | Whether the flipbook should loop when it reaches the end, or stop |
| bReversePlayback | `uint32` | If playback should move the current position backwards instead of forwards |
| bPlaying | `uint32` | Are we currently playing (moving Position) |
| AccumulatedTime | `float` | Current position in the timeline |
| CachedFrameIndex | `int32` | Last frame index calculated |
| SpriteColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | Vertex color to apply to the frames |
| CachedBodySetup | `UBodySetup *` | The cached body setup |

## Functions

### SetFlipbook

Change the flipbook used by this instance (will reset the play time to 0 if it is a new flipbook).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewFlipbook | `UPaperFlipbook *` |  |

**Return**

- Type: 
- Description: _None_

### GetFlipbook

Gets the flipbook used by this instance.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetSpriteColor

Set color of the sprite

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_

### Play

Start playback of flipbook

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### PlayFromStart

Start playback of flipbook from the start

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Reverse

Start playback of flipbook in reverse

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ReverseFromEnd

Start playback of flipbook in reverse from the end

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Stop

Stop playback of flipbook

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsPlaying

Get whether this flipbook is playing or not.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsReversing

Get whether we are reversing or not

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetPlaybackPositionInFrames

Jump to a position in the flipbook (expressed in frames). If bFireEvents is true, event functions will fire, otherwise they will not.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewFramePosition | `int32` |  |
| bFireEvents | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetPlaybackPositionInFrames

Get the current playback position (in frames) of the flipbook

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetPlaybackPosition

Jump to a position in the flipbook (expressed in seconds). If bFireEvents is true, event functions will fire, otherwise they will not.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewPosition | `float` |  |
| bFireEvents | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetPlaybackPosition

Get the current playback position (in seconds) of the flipbook

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetLooping

true means we should loop, false means we should not.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewLooping | `bool` |  |

**Return**

- Type: 
- Description: _None_

### IsLooping

Get whether we are looping or not

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetPlayRate

Sets the new play rate for this flipbook

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewRate | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetPlayRate

Get the current play rate for this flipbook

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetNewTime

Set the new playback position time to use

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetFlipbookLength

Get length of the flipbook (in seconds)

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetFlipbookLengthInFrames

Get length of the flipbook (in frames)

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetFlipbookFramerate

Get the nominal framerate that the flipbook will be played back at (ignoring PlayRate), in frames per second

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRep_SourceFlipbook

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OldFlipbook | `UPaperFlipbook *` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnFinishedPlaying |  | Event called whenever a non-looping flipbook finishes playing (either reaching the beginning or the end, depending on the play direction) |

## Language

cpp
