# UParticleModuleLocationPrimitiveCylinder

## Parents

- [UParticleModuleLocationPrimitiveBase](./UParticleModuleLocationPrimitiveBase.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| RadialVelocity | `uint32` | If true, get the particle velocity form the radial distance inside the primitive. |
| StartRadius | [FRawDistributionFloat](../../cppstruct/F/FR/FRawDistributionFloat.md) | The radius of the cylinder. |
| StartHeight | [FRawDistributionFloat](../../cppstruct/F/FR/FRawDistributionFloat.md) | The height of the cylinder, centered about the location. |
| HeightAxis | `TEnumAsByte < enum CylinderHeightAxis >` | Determine particle particle system axis that should represent the height of the cylinder.<br>	  Can be one of the following:<br>	    PMLPC_HEIGHTAXIS_X - Orient the height along the particle system X-axis.<br>	    PMLPC_HEIGHTAXIS_Y - Orient the height along the particle system Y-axis.<br>	    PMLPC_HEIGHTAXIS_Z - Orient the height along the particle system Z-axis. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
