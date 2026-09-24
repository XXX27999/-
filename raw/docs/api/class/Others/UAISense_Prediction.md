# UAISense_Prediction

## Parents

- [UAISense](./UAISense.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| RegisteredEvents | `TArray < FAIPredictionEvent >` |  |

## Functions

### RequestControllerPredictionEvent

Asks perception system to supply Requestor with PredictedActor's predicted location in PredictionTime seconds
	 	Location is being predicted based on PredicterActor's current location and velocity

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Requestor | `AAIController *` |  |
| PredictedActor | `AActor *` |  |
| PredictionTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### RequestPawnPredictionEvent

Asks perception system to supply Requestor with PredictedActor's predicted location in PredictionTime seconds
	 	Location is being predicted based on PredicterActor's current location and velocity

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Requestor | `APawn *` |  |
| PredictedActor | `AActor *` |  |
| PredictionTime | `float` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
