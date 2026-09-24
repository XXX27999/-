# FFoliageTypeObject

A wrapper struct used to allow the use of either FoliageType assets or FoliageType blueprint classes

## Fields

| Name | Type | Description |
| --- | --- | --- |
| FoliageTypeObject | `UObject *` | The foliage type that will be spawned by the procedural foliage simulation |
| TypeInstance | `UFoliageType *` | The actual instance of the foliage type that is used for spawning |
| bIsAsset | `bool` | Whether this contains an asset object (as opposed to a BP class) |
| Type_DEPRECATED | `TSubclassOf < UFoliageType_InstancedStaticMesh >` |  |
