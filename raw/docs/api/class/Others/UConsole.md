# UConsole

A basic command line console that accepts most commands.

## Parents

- [UObject](./UObject.md)
- FOutputDevice

## Variables

| Name | Type | Description |
| --- | --- | --- |
| ConsoleTargetPlayer | `ULocalPlayer *` | The player which the next console command should be executed in the context of.  If nullptr, execute in the viewport. |
| DefaultTexture_Black | `UTexture2D *` |  |
| DefaultTexture_White | `UTexture2D *` |  |
| HistoryBuffer | `TArray < FString >` | Holds the history buffer, order is old to new |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
