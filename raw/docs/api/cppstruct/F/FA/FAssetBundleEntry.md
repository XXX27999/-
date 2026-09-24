# FAssetBundleEntry

A struct representing a single AssetBundle

## Fields

| Name | Type | Description |
| --- | --- | --- |
| BundleScope | [FPrimaryAssetId](../FP/FPrimaryAssetId.md) | Asset this bundle is saved within. This is empty for global bundles, or in the saved bundle info |
| BundleName | `FName` | Specific name of this bundle, should be unique for a given scope |
| BundleAssets | `TArray < FSoftObjectPath >` | List of string assets contained in this bundle |
