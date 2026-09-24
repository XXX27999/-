# UInheritableComponentHandler

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Records | `TArray < FComponentOverrideRecord >` | All component records |
| UnnecessaryComponents | `TArray < UActorComponent * >` | List of components that were marked unnecessary, need to keep these around so it doesn't regenerate them when a child asks for one |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
