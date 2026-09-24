# AEmitter

## Parents

- [AActor](./AActor.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| ParticleSystemComponent | `UParticleSystemComponent *` |  |
| bDestroyOnSystemFinish | `uint32` |  |
| bPostUpdateTickGroup | `uint32` |  |
| bCurrentlyActive | `uint32` | used to update status of toggleable level placed emitters on clients |

## Functions

### OnParticleSystemFinished

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| FinishedComponent | `UParticleSystemComponent *` |  |

**Return**

- Type: 
- Description: _None_

### OnRep_bCurrentlyActive

Replication Notification Callbacks

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Activate

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Deactivate

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ToggleActive

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsActive

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetTemplate

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewTemplate | `UParticleSystem *` |  |

**Return**

- Type: 
- Description: _None_

### SetFloatParameter

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ParameterName | `FName` |  |
| Param | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetVectorParameter

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ParameterName | `FName` |  |
| Param | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### SetColorParameter

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ParameterName | `FName` |  |
| Param | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_

### SetActorParameter

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ParameterName | `FName` |  |
| Param | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### SetMaterialParameter

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ParameterName | `FName` |  |
| Param | `UMaterialInterface *` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnParticleSpawn |  |  |
| OnParticleBurst |  |  |
| OnParticleDeath |  |  |
| OnParticleCollide |  |  |

## Language

cpp
