# UTimelineTemplate

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| TimelineLength | `float` | Length of this timeline |
| LengthMode | `TEnumAsByte < ETimelineLengthMode >` | How we want the timeline to determine its own length (e.g. specified length, last keyframe) |
| bAutoPlay | `uint32` | If we want the timeline to auto-play |
| bLoop | `uint32` | If we want the timeline to loop |
| bReplicated | `uint32` | If we want the timeline to loop |
| bValidatedAsWired | `uint32` | Compiler Validated As Wired up |
| bIgnoreTimeDilation | `uint32` | If we want the timeline to ignore global time dilation |
| EventTracks | `TArray < struct FTTEventTrack >` | Set of event tracks |
| FloatTracks | `TArray < struct FTTFloatTrack >` | Set of float interpolation tracks |
| VectorTracks | `TArray < struct FTTVectorTrack >` | Set of vector interpolation tracks |
| LinearColorTracks | `TArray < struct FTTLinearColorTrack >` | Set of linear color interpolation tracks |
| MetaDataArray | `TArray < struct FBPVariableMetaDataEntry >` | Metadata information for this timeline |
| TimelineGuid | [FGuid](../../cppstruct/F/FG/FGuid.md) |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
