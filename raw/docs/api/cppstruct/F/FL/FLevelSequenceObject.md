# FLevelSequenceObject

Structure for animated Actor objects.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| ObjectOrOwner | `TLazyObjectPtr < UObject >` | The object or the owner of the object being possessed. |
| ComponentName | `FString` | Optional name of an ActorComponent. |
| CachedComponent | `TWeakObjectPtr < UObject >` | Cached pointer to the Actor component (only if ComponentName is set). |
