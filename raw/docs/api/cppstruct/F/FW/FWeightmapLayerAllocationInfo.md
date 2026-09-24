# FWeightmapLayerAllocationInfo

Stores information about which weightmap texture and channel each layer is stored

## Fields

| Name | Type | Description |
| --- | --- | --- |
| LayerInfo | `ULandscapeLayerInfoObject *` |  |
| WeightmapTextureIndex | `uint8` |  |
| WeightmapTextureChannel | `uint8` |  |
| bUseForWeightmapPCOnly | `TEnumAsByte < ELandscapeWeightmapUsage >` |  |
| WeightmapTextureIndex_ForPC | `uint8` |  |
| WeightmapTextureChannel_ForPC | `uint8` |  |
| CustomWeightName | `FName` |  |
| CustomWeightChannelCount | `int32` |  |
