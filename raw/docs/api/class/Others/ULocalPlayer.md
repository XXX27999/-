# ULocalPlayer

Each player that is active on the current client has a LocalPlayer. It stays active across maps
 	There may be several spawned in the case of splitscreencoop.
 	There may be 0 spawned on servers.

## Parents

- [UPlayer](./UPlayer.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| ViewportClient | `UGameViewportClient *` | The master viewport containing this player's view. |
| AspectRatioAxisConstraint | `TEnumAsByte < enum EAspectRatioAxisConstraint >` | How to constrain perspective viewport FOV |
| PendingLevelPlayerControllerClass | `TSubclassOf < APlayerController >` | The class of PlayerController to spawn for players logging in. |
| bSentSplitJoin | `uint32` | set when we've sent a split join request |
| ControllerId | `int32` | The controller ID which this player accepts input from. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
