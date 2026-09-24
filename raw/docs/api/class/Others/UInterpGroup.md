# UInterpGroup

## Parents

- [UObject](./UObject.md)
- FInterpEdInputInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| InterpTracks | `TArray < UInterpTrack * >` |  |
| GroupName | `FName` | Within an InterpData, all GroupNames must be unique.<br>	 	Used for naming Variable connectors on the Action in Kismet and finding each groups object. |
| GroupColor | [FColor](../../cppstruct/F/FC/FColor.md) | Colour used for drawing tracks etc. related to this group. |
| bCollapsed | `uint32` | Whether or not this group is folded away in the editor. |
| bVisible | `uint32` | Whether or not this group is visible in the editor. |
| bIsFolder | `uint32` | When enabled, this group is treated like a folder in the editor, which should only be used for organization.  Folders are never associated with actors and don't have a presence in the Kismet graph. |
| bIsParented | `uint32` | When true, this group is considered a 'visual child' of another group.  This doesn't at all affect the behavior of the group, it's only for visual organization.  Also, it's implied that the parent is the next prior group in the array that doesn't have a parent. |
| bIsSelected | `uint32` | When enabled, this group will be selected in the interp editor. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
