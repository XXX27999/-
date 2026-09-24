# UWindDirectionalSourceComponent

Component that provides a directional wind source. Only affects SpeedTree assets.

## Parents

- [USceneComponent](./USceneComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Strength | `float` |  |
| Speed | `float` |  |
| MinGustAmount | `float` |  |
| MaxGustAmount | `float` |  |
| Radius | `float` |  |
| bPointWind | `uint32` |  |

## Functions

### SetStrength

Because the actual data used to query wind is stored on the render thread in
	  an instance of FWindSourceSceneProxy all of our properties are read only.
	  The data can be manipulated with the following functions which will queue
	  a render thread update for this component

	 Sets the strength of the generated wind

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InNewStrength | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetSpeed

Sets the windspeed of the generated wind

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InNewSpeed | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetMinimumGustAmount

Set minimum deviation for wind gusts

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InNewMinGust | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetMaximumGustAmount

Set maximum deviation for wind gusts

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InNewMaxGust | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetRadius

Set the effect radius for point wind

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InNewRadius | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetWindType

Set the type of wind generator to use

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InNewType | [EWindSourceType](../../cppenum/E/EW/EWindSourceType.md) |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
