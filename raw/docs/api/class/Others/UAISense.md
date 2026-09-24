# UAISense

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| DefaultExpirationAge | `float` | age past which stimulus of this sense are "forgotten" |
| NotifyType | [EAISenseNotifyType](../../cppenum/E/EA/EAISenseNotifyType.md) |  |
| bWantsNewPawnNotification | `uint32` | whether this sense is interested in getting notified about new Pawns being spawned<br>	 	this can be used for example for automated sense sources registration |
| bAutoRegisterAllPawnsAsSources | `uint32` | If true all newly spawned pawns will get auto registered as source for this sense. |
| PerceptionSystemInstance | `UAIPerceptionSystem *` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
