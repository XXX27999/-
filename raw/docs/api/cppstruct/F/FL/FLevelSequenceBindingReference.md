# FLevelSequenceBindingReference

An external reference to an level sequence object, resolvable through an arbitrary context.

  Bindings consist of an optional package name, and the path to the object within that package.
  Where package name is empty, the reference is a relative path from a specific outer (the context).
  Currently, the package name should only ever be empty for component references, which must remain relative bindings to work correctly with spawnables and reinstanced actors.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| PackageName_DEPRECATED | `FString` | Replaced by ExternalObjectPath |
| ExternalObjectPath | [FSoftObjectPath](../FS/FSoftObjectPath.md) | Path to a specific actorcomponent inside an external package |
| ObjectPath | `FString` | Object path relative to a passed in context object, this is used if ExternalObjectPath is invalid |
