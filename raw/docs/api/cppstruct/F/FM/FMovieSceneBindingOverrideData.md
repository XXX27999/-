# FMovieSceneBindingOverrideData

Movie scene binding override data

## Fields

| Name | Type | Description |
| --- | --- | --- |
| ObjectBindingId | [FMovieSceneObjectBindingID](./FMovieSceneObjectBindingID.md) | Specifies the object binding to override. |
| Object | `TWeakObjectPtr < UObject >` | Specifies the object to override the binding with. |
| bOverridesDefault | `bool` | Specifies whether the default assignment should remain bound (false) or if this should completely override the default binding (false). |
