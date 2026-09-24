# FPrimaryAssetTypeInfo

Structure with publicly exposed information about an asset type. These can be loaded out of a config file.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| PrimaryAssetType | `FName` | The logical name for this type of Primary Asset |
| AssetBaseClass | `TSoftClassPtr < UObject >` | Base Class of all assets of this type |
| AssetBaseClassLoaded | `UClass *` | Base Class of all assets of this type |
| bHasBlueprintClasses | `bool` | True if the assets loaded are blueprints classes, false if they are normal UObjects |
| bIsEditorOnly | `bool` | True if this type is editor only |
| Directories | `TArray < FDirectoryPath >` | Directories to search for this asset type |
| SpecificAssets | `TArray < FSoftObjectPath >` | Individual assets to scan |
| Rules | [FPrimaryAssetRules](./FPrimaryAssetRules.md) | Default management rules for this type, individual assets can be overridden |
| AssetScanPaths | `TArray < FString >` | Combination of directories and individual assets to search for this asset type. Will have the Directories and Assets added to it |
| bIsDynamicAsset | `bool` | True if this is an asset created at runtime that has no on disk representation. Cannot be set in config |
| NumberOfAssets | `int32` | Number of tracked assets of that type |
