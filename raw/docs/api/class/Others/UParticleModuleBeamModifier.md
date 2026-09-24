# UParticleModuleBeamModifier

## Parents

- UParticleModuleBeamBase

## Variables

| Name | Type | Description |
| --- | --- | --- |
| ModifierType | `TEnumAsByte < enum BeamModifierType >` | Whether this module modifies the Source or the Target. |
| PositionOptions | [FBeamModifierOptions](../../cppstruct/F/FB/FBeamModifierOptions.md) | The options associated with the position. |
| Position | [FRawDistributionVector](../../cppstruct/F/FR/FRawDistributionVector.md) | The value to use when modifying the position. |
| TangentOptions | [FBeamModifierOptions](../../cppstruct/F/FB/FBeamModifierOptions.md) | The options associated with the Tangent. |
| Tangent | [FRawDistributionVector](../../cppstruct/F/FR/FRawDistributionVector.md) | The value to use when modifying the Tangent. |
| bAbsoluteTangent | `uint32` | If true, don't transform the tangent modifier into the tangent basis. |
| StrengthOptions | [FBeamModifierOptions](../../cppstruct/F/FB/FBeamModifierOptions.md) | The options associated with the Strength. |
| Strength | [FRawDistributionFloat](../../cppstruct/F/FR/FRawDistributionFloat.md) | The value to use when modifying the Strength. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
