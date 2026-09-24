# APlayerStart

This class indicates a location where a player can spawn when the game begins

## Parents

- [ANavigationObjectBase](./ANavigationObjectBase.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| PlayerStartTag | `FName` | ~ To take more control over PlayerStart selection, you can override the virtual AGameModeBase::FindPlayerStart and AGameModeBase::ChoosePlayerStart functions.<br>	 Used when searching for which playerstart to use. |
| ArrowComponent | `UArrowComponent *` | Arrow component to indicate forward direction of start |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
