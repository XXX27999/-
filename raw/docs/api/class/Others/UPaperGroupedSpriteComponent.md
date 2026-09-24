# UPaperGroupedSpriteComponent

A component that handles rendering and collision for many instances of one or more UPaperSprite assets.

  @see UPrimitiveComponent, UPaperSprite

## Parents

- [UMeshComponent](./UMeshComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| InstanceMaterials | `TArray < UMaterialInterface * >` | Array of materials used by the instances |
| PerInstanceSpriteData | `TArray < FSpriteInstanceData >` | Array of instances |

## Functions

### AddInstance

Add an instance to this component. Transform can be given either in the local space of this component or world space.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Transform | `FTransform &` |  |
| Sprite | `UPaperSprite *` |  |
| bWorldSpace | `bool` |  |
| Color | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_

### GetInstanceTransform

Get the transform for the instance specified. Instance is returned in local space of this component unless bWorldSpace is set.  Returns True on success.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstanceIndex | `int32` |  |
| OutInstanceTransform | `FTransform &` |  |
| bWorldSpace | `bool` |  |

**Return**

- Type: 
- Description: _None_

### UpdateInstanceTransform

Update the transform for the instance specified. Instance is given in local space of this component unless bWorldSpace is set.  Returns True on success.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstanceIndex | `int32` |  |
| NewInstanceTransform | `FTransform &` |  |
| bWorldSpace | `bool` |  |
| bMarkRenderStateDirty | `bool` |  |
| bTeleport | `bool` |  |

**Return**

- Type: 
- Description: _None_

### UpdateInstanceColor

Update the color for the instance specified. Returns True on success.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstanceIndex | `int32` |  |
| NewInstanceColor | `FLinearColor` |  |
| bMarkRenderStateDirty | `bool` |  |

**Return**

- Type: 
- Description: _None_

### RemoveInstance

Remove the instance specified. Returns True on success.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstanceIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### ClearInstances

Clear all instances being rendered by this component

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetInstanceCount

Get the number of instances in this component

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SortInstancesAlongAxis

Sort all instances by their world space position along the specified axis

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldSpaceSortAxis | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
