# UTimelineComponent

TimelineComponent holds a series of events, floats, vectors or colors with associated keyframes.
  Events can be triggered at keyframes along the timeline.
  Floats, vectors, and colors are interpolated between keyframes along the timeline.

## Parents

- [UActorComponent](./UActorComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| TheTimeline | [FTimeline](../../cppstruct/F/FT/FTimeline.md) | The actual timeline structure |
| bIgnoreTimeDilation | `uint32` | True if global time dilation should be ignored by this timeline, false otherwise. |

## Functions

### Play

Start playback of timeline

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### PlayFromStart

Start playback of timeline from the start

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Reverse

Start playback of timeline in reverse

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ReverseFromEnd

Start playback of timeline in reverse from the end

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Stop

Stop playback of timeline

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsPlaying

Get whether this timeline is playing or not.

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

### SetPlaybackPosition

Jump to a position in the timeline.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewPosition | `float` |  |
| bFireEvents | `bool` | If true, event functions that are between current position and new playback position will fire. |
| bFireUpdate | `bool` | If true, the update output exec will fire after setting the new playback position. |

**Return**

- Type: 
- Description: _None_

### GetPlaybackPosition

Get the current playback position of the Timeline

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetLooping

true means we would loop, false means we should not.

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

Sets the new play rate for this timeline

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewRate | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetPlayRate

Get the current play rate for this timeline

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

### GetTimelineLength

Get length of the timeline

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetTimelineLength

Set length of the timeline

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewLength | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetTimelineLengthMode

Sets the length mode of the timeline

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewLengthMode | [ETimelineLengthMode](../../cppenum/E/ET/ETimelineLengthMode.md) |  |

**Return**

- Type: 
- Description: _None_

### SetIgnoreTimeDilation

Set whether to ignore time dilation.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewIgnoreTimeDilation | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetIgnoreTimeDilation

Get whether to ignore time dilation.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetFloatCurve

Update a certain float track's curve

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewFloatCurve | `UCurveFloat *` |  |
| FloatTrackName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### SetVectorCurve

Update a certain vector track's curve

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewVectorCurve | `UCurveVector *` |  |
| VectorTrackName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### SetLinearColorCurve

Update a certain linear color track's curve

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewLinearColorCurve | `UCurveLinearColor *` |  |
| LinearColorTrackName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### OnRep_Timeline

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
