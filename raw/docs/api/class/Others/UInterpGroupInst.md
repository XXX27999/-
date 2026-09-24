# UInterpGroupInst

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Group | `UInterpGroup *` | An instance of an UInterpGroup for a particular Actor. There may be multiple InterpGroupInsts for a single<br>	  UInterpGroup in the InterpData, if multiple Actors are connected to the same UInterpGroup.<br>	  The Outer of an UInterpGroupInst is a MatineeActor<br><br>	 UInterpGroup within the InterpData that this is an instance of. |
| GroupActor | `AActor *` | Actor that this Group instance is acting upon.<br>	 	NB: that this may be set to NULL at any time as a result of the  AActor  being destroyed. |
| TrackInst | `TArray < UInterpTrackInst * >` | Array if InterpTrack instances. TrackInst.Num() == UInterpGroup.InterpTrack.Num() must be true. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
