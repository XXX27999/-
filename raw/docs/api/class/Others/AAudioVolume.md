# AAudioVolume

## Parents

- [AVolume](./AVolume.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Priority | `float` | Priority of this volume. In the case of overlapping volumes the one with the highest priority<br>	  is chosen. The order is undefined if two or more overlapping volumes have the same priority. |
| bEnabled | `uint32` | whether this volume is currently enabled and able to affect sounds |
| Settings | [FReverbSettings](../../cppstruct/F/FR/FReverbSettings.md) | Reverb settings to use for this volume. |
| AmbientZoneSettings | [FInteriorSettings](../../cppstruct/F/FI/FInteriorSettings.md) | Interior settings used for this volume |

## Functions

### SetPriority

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewPriority | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetEnabled

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewEnabled | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetReverbSettings

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewReverbSettings | `FReverbSettings &` |  |

**Return**

- Type: 
- Description: _None_

### SetInteriorSettings

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewInteriorSettings | `FInteriorSettings &` |  |

**Return**

- Type: 
- Description: _None_

### OnRep_bEnabled

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
