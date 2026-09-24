# UParticleModuleKillBox

## Parents

- UParticleModuleKillBase

## Variables

| Name | Type | Description |
| --- | --- | --- |
| LowerLeftCorner | [FRawDistributionVector](../../cppstruct/F/FR/FRawDistributionVector.md) | The lower left corner of the box. |
| UpperRightCorner | [FRawDistributionVector](../../cppstruct/F/FR/FRawDistributionVector.md) | The upper right corner of the box. |
| bAbsolute | `uint32` | If true, the box coordinates are in world space. |
| bKillInside | `uint32` | If true, particles INSIDE the box will be killed.<br>	 	If false (the default), particles OUTSIDE the box will be killed. |
| bAxisAlignedAndFixedSize | `uint32` | If true, the box will always be axis aligned and non-scalable. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
