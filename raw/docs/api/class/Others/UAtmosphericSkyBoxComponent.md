# UAtmosphericSkyBoxComponent

## Parents

- [USceneComponent](./USceneComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| RenderDynamicSky | `bool` |  |
| Material | `UMaterialInterface *` |  |
| NoiseTexture | `UTexture2D *` |  |
| StaticMesh | `UStaticMesh *` |  |
| RadiusScale | `float` |  |
| MeshRotation | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |
| RainyDegree | `float` |  |
| Atmosphere | [FTOD_AtmosphereParameters](../../cppstruct/F/FT/FTOD_AtmosphereParameters.md) |  |
| Day | [FTOD_DayParameters](../../cppstruct/F/FT/FTOD_DayParameters.md) |  |
| Light | [FTOD_LightParameters](../../cppstruct/F/FT/FTOD_LightParameters.md) |  |
| CloudsPbr | [FTOD_CloudPBRParameters](../../cppstruct/F/FT/FTOD_CloudPBRParameters.md) |  |
| World | [FTOD_WorldParameters](../../cppstruct/F/FT/FTOD_WorldParameters.md) |  |
| Cycle | [FTOD_CycleParameters](../../cppstruct/F/FT/FTOD_CycleParameters.md) |  |
| TodTime | [FTOD_Time](../../cppstruct/F/FT/FTOD_Time.md) |  |
| TodAnimation | [FTOD_Animation](../../cppstruct/F/FT/FTOD_Animation.md) |  |
| TodSunParams | [FTOD_Sun](../../cppstruct/F/FT/FTOD_Sun.md) |  |
| TodMoonParams | [FTOD_Moon](../../cppstruct/F/FT/FTOD_Moon.md) |  |
| TodSunAndMoonParams | [FTOD_SunAndMoon](../../cppstruct/F/FT/FTOD_SunAndMoon.md) |  |
| TodStarsParams | [FTOD_Stars](../../cppstruct/F/FT/FTOD_Stars.md) |  |
| TodSpecialSkyParams | [FTOD_SpecialSky](../../cppstruct/F/FT/FTOD_SpecialSky.md) |  |
| SunActor | `AActor *` |  |
| MoonActor | `AActor *` |  |
| LightingChannels | [FLightingChannels](../../cppstruct/F/FL/FLightingChannels.md) |  |
| MaterialInstancesDynamic | `UMaterialInstanceDynamic *` |  |
| bIsMaterialInstanceDirty | `bool` |  |
| FixedTimeOfDay | `bool` |  |
| FixedCurrTime | `float` |  |
| bNeedUpdate | `bool` |  |

## Functions

### SetFixedCurrTime

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| time | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetFixedTimeOfDay

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| IsFiexd | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetNeedUpdate

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NeedUpdate | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetMaterialInstancesDynamic

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
