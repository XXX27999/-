# UPawnNoiseEmitterComponent

PawnNoiseEmitterComponent tracks noise event data used by SensingComponents to hear a Pawn.
  This component is intended to exist on either a Pawn or its Controller. It does nothing on network clients.

## Parents

- [UActorComponent](./UActorComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| bAIPerceptionSystemCompatibilityMode | `uint32` |  |
| LastRemoteNoisePosition | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| NoiseLifetime | `float` |  |
| LastRemoteNoiseVolume | `float` |  |
| LastRemoteNoiseTime | `float` |  |
| LastLocalNoiseVolume | `float` |  |
| LastLocalNoiseTime | `float` |  |

## Functions

### MakeNoise

Cache noises instigated by the owning pawn for AI sensing

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NoiseMaker | `AActor *` | - is the actual actor which made the noise |
| Loudness | `float` | - is the relative loudness of the noise (0.0 to 1.0) |
| NoiseLocation | `FVector &` | - is the position of the noise |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
