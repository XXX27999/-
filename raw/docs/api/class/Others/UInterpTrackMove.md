# UInterpTrackMove

Track containing data for moving an actor around over time.

## Parents

- [UInterpTrack](./UInterpTrack.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| PosTrack | [FInterpCurveVector](../../cppstruct/F/FI/FInterpCurveVector.md) | Actual position keyframe data. |
| EulerTrack | [FInterpCurveVector](../../cppstruct/F/FI/FInterpCurveVector.md) | Actual rotation keyframe data, stored as Euler angles in degrees, for easy editing on curve. |
| LookupTrack | [FInterpLookupTrack](../../cppstruct/F/FI/FInterpLookupTrack.md) |  |
| LookAtGroupName | `FName` | When using IMR_LookAtGroup, specifies the Group which this track should always point its actor at. |
| LinCurveTension | `float` | Controls the tightness of the curve for the translation path. |
| AngCurveTension | `float` | Controls the tightness of the curve for the rotation path. |
| bUseQuatInterpolation | `uint32` | Use a Quaternion linear interpolation between keys.<br>	 	This is robust and will find the 'shortest' distance between keys, but does not support ease inout. |
| bShowArrowAtKeys | `uint32` | In the editor, show a small arrow at each keyframe indicating the rotation at that key. |
| bDisableMovement | `uint32` | Disable previewing of this track - will always position  AActor  at Time=0.0. Useful when keyframing an object relative to this group. |
| bShowTranslationOnCurveEd | `uint32` | If false, when this track is displayed on the Curve Editor in Matinee, do not show the Translation tracks. |
| bShowRotationOnCurveEd | `uint32` | If false, when this track is displayed on the Curve Editor in Matinee, do not show the Rotation tracks. |
| bHide3DTrack | `uint32` | If true, 3D representation of this track in the 3D viewport is disabled. |
| RotMode | `TEnumAsByte < enum EInterpTrackMoveRotMode >` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
