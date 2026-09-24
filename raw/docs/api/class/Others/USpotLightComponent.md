# USpotLightComponent

A spot light component emits a directional cone shaped light (Eg a Torch).

## Parents

- [UPointLightComponent](./UPointLightComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| InnerConeAngle | `float` | Degrees. |
| OuterConeAngle | `float` | Degrees. |
| bCastPhotonShadow | `uint32` | #if WITH_PHOTON_SHADOW<br>	 Whether the light should cast photon shadow for character<br>	 #endif |
| NearPlaneOffset | `float` |  |
| FarPlaneOffset | `float` |  |
| LightShaftConeAngle | `float` | Degrees.<br>	UPROPERTY(EditAnywhere, BlueprintReadOnly, Category=LightShaft, meta=(UIMin = "1.0", UIMax = "180.0")) |

## Functions

### SetInnerConeAngle

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewInnerConeAngle | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetOuterConeAngle

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewOuterConeAngle | `float` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
