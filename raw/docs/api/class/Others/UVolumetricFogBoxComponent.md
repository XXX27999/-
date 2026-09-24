# UVolumetricFogBoxComponent

Used to create local volumetric fog.

## Parents

- [UBoxComponent](./UBoxComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| VolumetricFogAlbedo | [FColor](../../cppstruct/F/FC/FColor.md) | The height fog particle reflectiveness used by volumetric fog.<br>	  Water particles in air have an albedo near white, while dust has slightly darker value. |
| VolumetricFogEmissive | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | Light emitted by height fog.  This is a density so more light is emitted the further you are looking through the fog.<br>	  In most cases skylight is a better choice, however right now volumetric fog does not support precomputed lighting,<br>	  So stationary skylights are unshadowed and static skylights don't affect volumetric fog at all. |
| VolumetricFogExtinctionScale | `float` | Scales the height fog particle extinction amount used by volumetric fog.  Values larger than 1 cause fog particles everywhere absorb more light. |

## Functions

### SetVolumetricFogExtinctionScale

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewValue | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetVolumetricFogAlbedo

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewValue | [FColor](../../cppstruct/F/FC/FColor.md) |  |

**Return**

- Type: 
- Description: _None_

### SetVolumetricFogEmissive

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewValue | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
