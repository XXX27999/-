# UPhysicsSpringComponent

Note: this component is still work in progress. Uses raycast springs for simple vehicle forces
 	Used with objects that have physics to create a spring down the X direction
 	ie. point X in the direction you want generate spring.

## Parents

- [USceneComponent](./USceneComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| SpringStiffness | `float` | Specifies how much strength the spring has. The higher the SpringStiffness the more force the spring can push on a body with. |
| SpringDamping | `float` | Specifies how quickly the spring can absorb energy of a body. The higher the damping the less oscillation |
| SpringLengthAtRest | `float` | Determines how long the spring will be along the X-axis at rest. The spring will apply 0 force on a body when it's at rest. |
| SpringRadius | `float` | Determines the radius of the spring. |
| SpringChannel | `TEnumAsByte < enum ECollisionChannel >` | Strength of thrust force applied to the base object. |
| bIgnoreSelf | `bool` | If true, the spring will ignore all components in its own actor |
| SpringCompression | `float` | The current compression of the spring. A spring at rest will have SpringCompression 0. |

## Functions

### GetNormalizedCompressionScalar

Returns the spring compression as a normalized scalar along spring direction.
	   0 implies spring is at rest
	   1 implies fully compressed

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetSpringRestingPoint

Returns the spring resting point in world space.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetSpringCurrentEndPoint

Returns the spring current end point in world space.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetSpringDirection

Returns the spring direction from start to resting point

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
