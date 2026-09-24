# UPhysicalMaterial

Physical materials are used to define the response of a physical object when interacting dynamically with the world.

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Friction | `float` | Friction value of surface, controls how easily things can slide on this surface (0 is frictionless, higher values increase the amount of friction) |
| FrictionCombineMode | `TEnumAsByte < EFrictionCombineMode :: Type >` | Friction combine mode, controls how friction is computed for multiple materials. |
| bOverrideFrictionCombineMode | `bool` | If set we will use the FrictionCombineMode of this material, instead of the FrictionCombineMode found in the project settings. |
| Restitution | `float` | Restitution or 'bounciness' of this surface, between 0 (no bounce) and 1 (outgoing velocity is same as incoming). |
| RestitutionCombineMode | `TEnumAsByte < EFrictionCombineMode :: Type >` | Restitution combine mode, controls how restitution is computed for multiple materials. |
| bOverrideRestitutionCombineMode | `bool` | If set we will use the RestitutionCombineMode of this material, instead of the RestitutionCombineMode found in the project settings. |
| Density | `float` | Used with the shape of the object to calculate its mass properties. The higher the number, the heavier the object. g per cubic cm. |
| RaiseMassToPower | `float` | Used to adjust the way that mass increases as objects get larger. This is applied to the mass as calculated based on a 'solid' object.<br>	 	In actuality, larger objects do not tend to be solid, and become more like 'shells' (e.g. a car is not a solid piece of metal).<br>	 	Values are clamped to 1 or less. |
| DestructibleDamageThresholdScale | `float` | How much to scale the damage threshold by on any destructible we are applied to |
| PhysicalMaterialProperty | `UDEPRECATED_PhysicalMaterialPropertyBase *` | UPROPERTY(deprecated) |
| SurfaceType | `TEnumAsByte < EPhysicalSurface >` | To edit surface type for your project, use ProjectSettingsPhysicsPhysicalSurface section |
| TireFrictionScale | `float` | DEPRECATED - Overall tire friction scalar for every type of tire. This value is multiplied against our parents' values. |
| TireFrictionScales | `TArray < FTireFrictionScalePair >` | DEPRECATED - Tire friction scales for specific types of tires. These values are multiplied against our parents' values. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
