# UPhysicsHandleComponent

Utility object for moving physics objects around.

## Parents

- [UActorComponent](./UActorComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| GrabbedComponent | `UPrimitiveComponent *` | Component we are currently holding |
| bSoftAngularConstraint | `uint32` |  |
| bSoftLinearConstraint | `uint32` |  |
| bInterpolateTarget | `uint32` |  |
| LinearDamping | `float` | Linear damping of the handle spring. |
| LinearStiffness | `float` | Linear stiffness of the handle spring |
| AngularDamping | `float` | Angular stiffness of the handle spring |
| AngularStiffness | `float` | Angular stiffness of the handle spring |
| InterpolationSpeed | `float` | How quickly we interpolate the physics target transform |

## Functions

### GrabComponent

Grab the specified component

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Component | `UPrimitiveComponent *` |  |
| InBoneName | `FName` |  |
| GrabLocation | `FVector` |  |
| bConstrainRotation | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GrabComponentAtLocation

Grab the specified component at a given location. Does NOT constraint rotation which means the handle will pivot about GrabLocation.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Component | `UPrimitiveComponent *` |  |
| InBoneName | `FName` |  |
| GrabLocation | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### GrabComponentAtLocationWithRotation

Grab the specified component at a given location and rotation. Constrains rotation.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Component | `UPrimitiveComponent *` |  |
| InBoneName | `FName` |  |
| Location | `FVector` |  |
| Rotation | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |

**Return**

- Type: 
- Description: _None_

### ReleaseComponent

Release the currently held component

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetGrabbedComponent

Returns the currently grabbed component, or null if nothing is grabbed.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetTargetLocation

Set the target location

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewLocation | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### SetTargetRotation

Set the target rotation

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewRotation | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |

**Return**

- Type: 
- Description: _None_

### SetTargetLocationAndRotation

Set target location and rotation

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewLocation | `FVector` |  |
| NewRotation | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |

**Return**

- Type: 
- Description: _None_

### GetTargetLocationAndRotation

Get the current location and rotation

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetLocation | `FVector &` |  |
| TargetRotation | `FRotator &` |  |

**Return**

- Type: 
- Description: _None_

### SetLinearDamping

Set linear damping

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewLinearDamping | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetLinearStiffness

Set linear stiffness

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewLinearStiffness | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetAngularDamping

Set angular damping

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewAngularDamping | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetAngularStiffness

Set angular stiffness

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewAngularStiffness | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetInterpolationSpeed

Set interpolation speed

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewInterpolationSpeed | `float` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
