# UInterpData

Interpolation data, containing keyframe tracks, event tracks etc.
  This does not contain any  AActor  references or state, so can safely be stored in
  packages, shared between multiple MatineeActors etc.

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| InterpLength | `float` | Duration of interpolation sequence - in seconds. |
| PathBuildTime | `float` | Position in Interp to move things to for path-building in editor. |
| InterpGroups | `TArray < UInterpGroup * >` | Actual interpolation data. Groups of InterpTracks. |
| CurveEdSetup | `UInterpCurveEdSetup *` | Used for curve editor to remember curve-editing setup. Only loaded in editor. |
| EdSectionStart | `float` | Used in editor for defining sections to loop, stretch etc. |
| EdSectionEnd | `float` | Used in editor for defining sections to loop, stretch etc. |
| bShouldBakeAndPrune | `uint32` | If true, then the matinee should be baked and pruned at cook time. |
| CachedDirectorGroup | `UInterpGroupDirector *` | Cached version of the director group, if any, for easy access while in game |
| AllEventNames | `TArray < FName >` | Unique names of all events contained across all event tracks |
| InterpFilters | `TArray < UInterpFilter * >` | Used for filtering which tracks are currently visible. |
| SelectedFilter | `UInterpFilter *` | The currently selected filter. |
| DefaultFilters | `TArray < UInterpFilter * >` | Array of default filters. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
