# UDefaultLevelSequenceInstanceData

Default instance data class that level sequences understand. Implements IMovieSceneTransformOrigin.

## Parents

- [UObject](./UObject.md)
- IMovieSceneTransformOrigin

## Variables

| Name | Type | Description |
| --- | --- | --- |
| TransformOriginActor | `AActor *` | When set, this actor's world position will be used as the transform origin for all absolute transform sections |
| TransformOrigin | [FTransform](../../cppstruct/F/FT/FTransform.md) | Specifies a transform that offsets all absolute transform sections in this sequence. Will compound with attach tracks. Scale is ignored. Not applied to Relative or Additive sections. |
| ShouldIgnoreScale | `bool` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
