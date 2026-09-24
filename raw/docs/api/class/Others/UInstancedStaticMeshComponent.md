# UInstancedStaticMeshComponent

A component that efficiently renders multiple instances of the same StaticMesh.

## Parents

- [UStaticMeshComponent](./UStaticMeshComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| PerInstanceSMData | `TArray < FInstancedStaticMeshInstanceData >` | Array of instances, bulk serialized. |
| InstancingRandomSeed | `int32` | Value used to seed the random number stream that generates random numbers for each of this mesh's instances.<br>		this is set to zero (default), it will be populated automatically by the editor. |
| InstanceStartCullDistance | `int32` | Distance from camera at which each instance begins to fade out. |
| InstanceEndCullDistance | `int32` | Distance from camera at which each instance completely fades out. |
| InstanceNearCullDistance | `int32` | Distance from camera at which each instance. |
| bIsFlyType | `bool` |  |
| bIsFoliage | `bool` |  |
| bIsPCFoliage | `bool` |  |
| InstanceReorderTable | `TArray < int32 >` | Mapping from PerInstanceSMData order to instance render buffer order. If empty, the PerInstanceSMData order is used. |
| RemovedInstances | `TArray < int32 >` |  |
| InstanceVisibilityMapping | `TMap < int32 , FInstanceVisibilityData >` |  |
| UseDynamicInstanceBuffer | `bool` | Set to true to permit updating the vertex buffer used in the instance buffer without recreating it completely. This should be used if you plan on dynamically changing the instances at run-time. |
| KeepInstanceBufferCPUAccess | `bool` | Set to true to keep instance buffer accessible by the CPU, otherwise it's discarded and considered never changing, only GPU has a copy of the data. |
| DynamicInstancingParametersValue | `TArray < FVector4 >` |  |
| PerInstanceDynamicInstancingParameterCount | `int32` | PerInstanceDynamicInstancingParameterCount |
| PhysicsSerializer | `UPhysicsSerializer *` | Serialization of all the InstanceBodies. Helps speed up physics creation time. |
| StashInstanceTransform | `TMap < int32 , FMatrix >` |  |
| NumPendingLightmaps | `int32` | Number of pending lightmaps still to be calculated (Apply()'d). |
| CachedMappings | `TArray < FInstancedStaticMeshMappingInfo >` | The mappings for all the instances of this component. |

## Functions

### AddInstance

Add an instance to this component. Transform is given in local space of this component.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstanceTransform | `FTransform &` |  |

**Return**

- Type: 
- Description: _None_

### AddInstanceWorldSpace

Add an instance to this component. Transform is given in world space.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldTransform | `FTransform &` |  |

**Return**

- Type: 
- Description: _None_

### SetInstanceDIP

Set a DIP value on one instance for the given material slot.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstanceIndex | `int32` |  |
| MaterialIndex | `int32` |  |
| Name | `FString &` |  |
| Value | `FVector4 &` |  |

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

Update the transform for the instance specified.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstanceIndex | `int32` | The index of the instance to update |
| NewInstanceTransform | `FTransform &` | The new transform |
| bWorldSpace | `bool` | If true, the new transform interpreted as a World Space transform, otherwise it is interpreted as Local Space |
| bMarkRenderStateDirty | `bool` | If true, the change should be visible immediately. If you are updating many instances you should only set this to true for the last instance. |
| bTeleport | `bool` | Whether or not the instance's physics should be moved normally, or teleported (moved instantly, ignoring velocity). |

**Return**

- Type: 
- Description: _None_

### RemoveInstance

Remove the instance specified. Returns True on success. Note that this will leave the array in order, but may shrink it.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstanceIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### ClearInstances

Clear all instances being rendered by this component.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetInstanceCount

Get the number of instances in this component.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetCullDistances

Sets the fading start and culling end distances for this component.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| StartCullDistance | `int32` |  |
| EndCullDistance | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetNearCullDistance

Sets the cull near distance for this component.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CullDistance | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetInstancesOverlappingSphere

Returns the instances with instance bounds overlapping the specified sphere. The return value is an array of instance indices.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Center | `FVector &` |  |
| Radius | `float` |  |
| bSphereInWorldSpace | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetInstancesOverlappingBox

Returns the instances with instance bounds overlapping the specified box. The return value is an array of instance indices.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Box | `FBox &` |  |
| bBoxInWorldSpace | `bool` |  |

**Return**

- Type: 
- Description: _None_

### HideInstance

Update the transform for the instance specified.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstanceIndices | `TArray < int32 > &` |  |

**Return**

- Type: 
- Description: _None_

### ShowInstance

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstanceIndices | `TArray < int32 > &` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
