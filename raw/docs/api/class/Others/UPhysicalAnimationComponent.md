# UPhysicalAnimationComponent

## Parents

- [UActorComponent](./UActorComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| StrengthMultiplyer | `float` | Multiplies the strength of any active motors. (can blend from 0-1 for example) |
| SkeletalMeshComponent | `USkeletalMeshComponent *` |  |

## Functions

### SetSkeletalMeshComponent

Sets the skeletal mesh we are driving through physical animation. Will erase any existing physical animation data.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSkeletalMeshComponent | `USkeletalMeshComponent *` |  |

**Return**

- Type: 
- Description: _None_

### ApplyPhysicalAnimationSettings

Applies the physical animation settings to the body given.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BodyName | `FName` |  |
| PhysicalAnimationData | `FPhysicalAnimationData &` |  |

**Return**

- Type: 
- Description: _None_

### ApplyPhysicalAnimationSettingsBelow

Applies the physical animation settings to the body given and all bodies below.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BodyName | `FName` |  |
| PhysicalAnimationData | `FPhysicalAnimationData &` |  |
| bIncludeSelf | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetStrengthMultiplyer

Updates strength multiplyer and any active motors

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InStrengthMultiplyer | `float` |  |

**Return**

- Type: 
- Description: _None_

### ApplyPhysicalAnimationProfileBelow

Applies the physical animation profile to the body given and all bodies below.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BodyName | `FName` | The body from which we'd like to start applying the physical animation profile. Finds all bodies below in the skeleton hierarchy. None implies all bodies |
| ProfileName | `FName` | The physical animation profile we'd like to apply. For each body in the physics asset we search for physical animation settings with this name. |
| bIncludeSelf | `bool` | Whether to include the provided body name in the list of bodies we act on (useful to ignore for cases where a root has multiple children) |
| bClearNotFound | `bool` | If true, bodies without the given profile name will have any existing physical animation settings cleared. If false, bodies without the given profile name are left untouched. |

**Return**

- Type: 
- Description: _None_

### GetBodyTargetTransform

Returns the target transform for the given body. If physical animation component is not controlling this body, returns its current transform.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BodyName | `FName` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
