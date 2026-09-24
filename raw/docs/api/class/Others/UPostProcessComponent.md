# UPostProcessComponent

PostProcessComponent. Enables Post process controls for blueprints.
 	Will use a parent UShapeComponent to provide volume data if available.

## Parents

- [USceneComponent](./USceneComponent.md)
- IInterface_PostProcessVolume

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Settings | [FPostProcessSettings](../../cppstruct/F/FP/FPostProcessSettings.md) | Post process settings to use for this volume. |
| Priority | `float` | Priority of this volume. In the case of overlapping volumes the one with the highest priority<br>	  overrides the lower priority ones. The order is undefined if two or more overlapping volumes have the same priority. |
| BlendRadius | `float` | World space radius around the volume that is used for blending (only if not unbound). |
| BlendWeight | `float` | 0:no effect, 1:full effect |
| bEnabled | `uint32` | Whether this volume is enabled or not. |
| bUnbound | `uint32` | set this to false to use the parent shape component as volume bounds. True affects the whole world regardless. |

## Functions

### AddOrUpdateBlendable

Adds an Blendable (implements IBlendableInterface) to the array of Blendables (if it doesn't exist) and update the weight

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBlendableObject | `TScriptInterface < IBlendableInterface >` |  |
| InWeight | `float` |  |

**Return**

- Type: 
- Description: _None_

### AddWeatherCompTag

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ClearCustomGIFallbackSH

Clear all Custom GI Fallback SH coefficients (reset to zero)

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GenerateCustomGIFallbackSH

Generate Custom GI Fallback SH coefficients from directional colors using Monte Carlo integration

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GenerateCustomGIFallbackSHFromCubeMap

Generate Spherical Harmonics coefficients from CubeMap texture using Monte Carlo sampling

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
