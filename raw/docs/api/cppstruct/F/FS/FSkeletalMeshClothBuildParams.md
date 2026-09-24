# FSkeletalMeshClothBuildParams

Struct holding parameters needed when creating a new clothing asset or sub asset (LOD)

## Fields

| Name | Type | Description |
| --- | --- | --- |
| TargetAsset | `TWeakObjectPtr < UClothingAssetBase >` |  |
| TargetLod | `int32` |  |
| bRemapParameters | `bool` |  |
| AssetName | `FString` |  |
| LodIndex | `int32` |  |
| SourceSection | `int32` |  |
| bRemoveFromMesh | `bool` |  |
| PhysicsAsset | `TSoftObjectPtr < UPhysicsAsset >` |  |
