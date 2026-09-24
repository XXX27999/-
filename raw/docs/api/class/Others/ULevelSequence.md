# ULevelSequence

Movie scene animation for Actors.

## Parents

- [UMovieSceneSequence](./UMovieSceneSequence.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| MovieScene | `UMovieScene *` | Pointer to the movie scene that controls this animation. |
| ObjectReferences | `FLevelSequenceObjectReferenceMap` | Legacy object references - should be read-only. Not deprecated because they need to still be saved |
| BindingReferences | [FLevelSequenceBindingReferences](../../cppstruct/F/FL/FLevelSequenceBindingReferences.md) | References to bound objects. |
| PossessedObjects_DEPRECATED | `TMap < FString , FLevelSequenceObject >` | Deprecated property housing old possessed object bindings |
| DirectorClass | `UClass *` | The class that is used to spawn this level sequence's director instance.<br>	  Director instances are allocated on-demand one per sequence during evaluation and are used by event tracks for triggering events. |
| DirectorBlueprint | `UBlueprint *` | A pointer to the director blueprint that generates this sequence's DirectorClass. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
