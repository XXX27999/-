# UMovieSceneSequence

Abstract base class for movie scene animations (C++ version).

## Parents

- [UMovieSceneSignedObject](./UMovieSceneSignedObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| EvaluationTemplate | `FCachedMovieSceneEvaluationTemplate` |  |
| TemplateParameters | [FMovieSceneTrackCompilationParams](../../cppstruct/F/FM/FMovieSceneTrackCompilationParams.md) |  |
| InstancedSubSequenceEvaluationTemplates | `TMap < UObject * , FCachedMovieSceneEvaluationTemplate >` |  |
| bParentContextsAreSignificant | `bool` | true if the result of GetParentObject is significant in object resolution for LocateBoundObjects.<br>	  When true, if GetParentObject returns nullptr, the PlaybackContext will be used for LocateBoundObjects, other wise the object's parent will be used<br>	  When false, the PlaybackContext will always be used for LocateBoundObjects |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
