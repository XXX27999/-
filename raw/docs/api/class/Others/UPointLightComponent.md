# UPointLightComponent

A light component which emits light from a single point equally in all directions.

## Parents

- [ULightComponent](./ULightComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Radius_DEPRECATED | `float` |  |
| AttenuationRadius | `float` | Bounds the light's visible influence.<br>	  This clamping of the light's influence is not physically correct but very important for performance, larger lights cost more. |
| bUseInverseSquaredFalloff | `uint32` | Whether to use physically based inverse squared distance falloff, where AttenuationRadius is only clamping the light's contribution.<br>	  Disabling inverse squared falloff can be useful when placing fill lights (don't want a super bright spot near the light).<br>	  When enabled, the light's Intensity is in units of lumens, where 1700 lumens is a 100W lightbulb.<br>	  When disabled, the light's Intensity is a brightness scale. |
| LightFalloffExponent | `float` | Controls the radial falloff of the light when UseInverseSquaredFalloff is disabled.<br>	  2 is almost linear and very unrealistic and around 8 it looks reasonable.<br>	  With large exponents, the light has contribution to only a small area of its influence radius but still costs the same as low exponents. |
| SourceRadius | `float` | Radius of light source shape.<br>	  Note that light sources shapes which intersect shadow casting geometry can cause shadowing artifacts. |
| SoftSourceRadius | `float` | Soft radius of light source shape.<br>	 Note that light sources shapes which intersect shadow casting geometry can cause shadowing artifacts. |
| SourceLength | `float` | Length of light source shape.<br>	  Note that light sources shapes which intersect shadow casting geometry can cause shadowing artifacts. |
| bSimulateRectLight | `uint32` | By luciuszhang: when in rect light mode, source radius is the rect light source width. |
| bSimulatePortalLight | `uint32` | By luciuszhang: Portal light will be used in lightmass for IdeaBake, it is just a flag for Rect Light. |
| RectLightSourceWidth | `float` | By luciuszhang: rect light source width. |
| RectLightSourceHeight | `float` | By luciuszhang: rect light source height. |
| bEnableForVertexPointLight | `uint32` |  |
| LightmassSettings | `FLightmassPointLightSettings` | The Lightmass settings for this object. |

## Functions

### SetAttenuationRadius

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewRadius | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetLightFalloffExponent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewLightFalloffExponent | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetSourceRadius

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewValue | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetSoftSourceRadius

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewValue | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetSourceLength

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewValue | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetSimulateRectLight

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| newValue | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetSimulatePortalLight

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| newValue | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetRectLightSourceWidth

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewValue | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetRectLightSourceHeight

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewValue | `float` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
