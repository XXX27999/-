# ACullDistanceVolume

## Parents

- [AVolume](./AVolume.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| CullDistances | `TArray < struct FCullDistanceSizePair >` | Array of size and cull distance pairs. The code will calculate the sphere diameter of a primitive's BB and look for a best<br>	  fit in this array to determine which cull distance to use. |
| bEnabled | `uint32` | Whether the volume is currently enabled or not. |
| bEnabledDeviceScale | `uint32` |  |
| VeryLowScale | `float` |  |
| LowScale | `float` |  |
| MidScale | `float` |  |
| HighScale | `float` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
