# UDemoNetDriver

Simulated network driver for recording and playing back game sessions.

## Parents

- [UNetDriver](./UNetDriver.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| RollbackNetStartupActors | `TMap < FString , FRollbackNetStartupActorInfo >` | Net startup actors that need to be rolled back during scrubbing by being destroyed and re-spawned<br>	  NOTE - DeletedNetStartupActors will take precedence here, and destroy the actor instead |
| CheckpointSaveMaxMSPerFrame | `float` | Maximum time allowed each frame to spend on saving a checkpoint. If 0, it will save the checkpoint in a single frame, regardless of how long it takes.<br>	  See also demo.CheckpointSaveMaxMSPerFrameOverride. |
| bIsLocalReplay | `bool` |  |
| GameInstance | `UGameInstance *` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
