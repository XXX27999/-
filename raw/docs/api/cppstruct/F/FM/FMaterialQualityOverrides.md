# FMaterialQualityOverrides

## Fields

| Name | Type | Description |
| --- | --- | --- |
| bEnableOverride | `bool` |  |
| bForceFullyRough | `bool` |  |
| bForceNonMetal | `bool` |  |
| bForceDisableLMDirectionality | `bool` |  |
| bForceLQReflections | `bool` |  |
| bHighDeviceSkipForceFullyRough | `bool` | 仅在 ENABLE_DEVICE_LEVEL_SHADER_VARIANT 开启时生效 |
| bHighDeviceSkipForceNonMetal | `bool` | 仅在 ENABLE_DEVICE_LEVEL_SHADER_VARIANT 开启时生效 |
| MobileCSMQuality | [EMobileCSMQuality](../../../cppenum/E/EM/EMobileCSMQuality.md) |  |
| MobilePointLightShadowQuality | [EMobileCSMQuality](../../../cppenum/E/EM/EMobileCSMQuality.md) |  |
| MobilePhotonShadowQuality | [EMobileCSMQuality](../../../cppenum/E/EM/EMobileCSMQuality.md) | #if WITH_PHOTON_SHADOW |
