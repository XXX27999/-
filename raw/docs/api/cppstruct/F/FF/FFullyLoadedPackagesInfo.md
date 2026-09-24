# FFullyLoadedPackagesInfo

Struct to help hold information about packages needing to be fully-loaded for DLC, etc.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| FullyLoadType | `TEnumAsByte < enum EFullyLoadPackageType >` | When to load these packages |
| Tag | `FString` | When this map or gametype is loaded, the packages in the following array will be loaded and added to root, then removed from root when map is unloaded |
| PackagesToLoad | `TArray < FName >` | The list of packages that will be fully loaded when the above Map is loaded |
| LoadedObjects | `TArray < UObject * >` | List of objects that were loaded, for faster cleanup |
