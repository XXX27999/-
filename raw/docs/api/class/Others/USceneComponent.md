# USceneComponent

A SceneComponent has a transform and supports attachment, but has no rendering or collision capabilities.
  Useful as a 'dummy' component in the hierarchy to offset others.

## Parents

- [UActorComponent](./UActorComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| PhysicsVolume | `TWeakObjectPtr < APhysicsVolume >` | Physics Volume in which this SceneComponent is located |
| AttachParent | `USceneComponent *` | What we are currently attached to. If valid, RelativeLocation etc. are used relative to this object |
| AttachSocketName | `FName` | Optional socket name on AttachParent that we are attached to. |
| AttachChildren | `TArray < USceneComponent * >` | List of child SceneComponents that are attached to us. |
| ClientAttachedChildren | `TArray < USceneComponent * >` | Set of attached SceneComponents that were attached by the client so we can fix up AttachChildren when it is replicated to us. |
| RelativeLocation | [FVector](../../cppstruct/F/FV/FVector.md) | Location of the component relative to its parent |
| RelativeRotation | [FRotator](../../cppstruct/F/FR/FRotator.md) | Rotation of the component relative to its parent |
| RelativeScale3D | [FVector](../../cppstruct/F/FV/FVector.md) | Non-uniform scaling of the component relative to its parent.<br>		Note that scaling is always applied in local space (no shearing etc) |
| ComponentToWorld | [FTransform](../../cppstruct/F/FT/FTransform.md) | Current transform of the component, relative to the world |
| ComponentVelocity | [FVector](../../cppstruct/F/FV/FVector.md) | Velocity of the component.<br>	 @see GetComponentVelocity() |
| bComponentToWorldUpdated | `uint8` | True if we have ever updated ComponentToWorld based on RelativeLocationRotationScale. Used at startup to make sure it is initialized. |
| bAbsoluteLocation | `uint8` | If RelativeLocation should be considered relative to the world, rather than the parent |
| bAbsoluteRotation | `uint8` | If RelativeRotation should be considered relative to the world, rather than the parent |
| bAbsoluteScale | `uint8` | If RelativeScale3D should be considered relative to the world, rather than the parent |
| bVisible | `uint8` | Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow. |
| bHiddenInGame | `uint8` | Whether to hide the primitive in game, if the primitive is Visible. |
| bShouldUpdatePhysicsVolume | `uint8` | Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.<br>	  @see GetPhysicsVolume() |
| bBoundsChangeTriggersStreamingDataRebuild | `uint8` | If true, a change in the bounds of the component will call trigger a streaming data rebuild |
| bUseAttachParentBound | `uint8` | If true, this component uses its parents bounds when attached.<br>	   This can be a significant optimization with many components attached together. |
| bShouldUpdateOverLaps | `uint8` |  |
| bForceUpdateChildCompTransform | `uint8` |  |
| bEnableUpdateTransformOption | `uint8` |  |
| bUpdateTransformOptionConsiderAbsolute | `uint8` |  |
| bOpenServerOptLite | `uint8` | Simplify server move<br>		by zoranouyang |
| bShouldUseTeleportMove | `uint8` |  |
| bForceFrameInterpolate | `uint8` |  |
| bEnableParallelMove | `uint8` |  |
| Mobility | `TEnumAsByte < EComponentMobility :: Type >` | How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor. |
| DetailMode | `TEnumAsByte < enum EDetailMode >` | If detail mode is >= system detail mode, primitive won't be rendered. |
| UpdateTransformOption | [EUpdateTransformOption](../../cppenum/E/EU/EUpdateTransformOption.md) |  |
| bIsFppLayerRecursive | `uint8` |  |
| bDisableFppLayerRecursive | `uint8` |  |
| bAbsoluteTranslation_DEPRECATED | `uint8` |  |
| bVisualizeComponent | `uint8` |  |
| bVisibilityMayChange | `uint8` | Let Editor tool, like pvs, to know whether visibility may change |
| RelativeTranslation_DEPRECATED | [FVector](../../cppstruct/F/FV/FVector.md) |  |

## Functions

### GetBoundsOirgin

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetBoundsBoxExtent

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRep_Transform

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRep_AttachParent

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRep_AttachChildren

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRep_AttachSocketName

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRep_Visibility

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OldValue | `bool` |  |

**Return**

- Type: 
- Description: _None_

### K2_SetRelativeLocation

Set the location of the component relative to its parent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewLocation | `FVector` | New location of the component relative to its parent. |
| bSweep | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| SweepHitResult | `FHitResult &` | Hit result from any impact if sweep is true. |
| bTeleport | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Return**

- Type: 
- Description: _None_

### K2_SetRelativeRotation

Set the rotation of the component relative to its parent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewRotation | `FRotator` | New rotation of the component relative to its parent |
| bSweep | `bool` | Whether we sweep to the destination (currently not supported for rotation). |
| SweepHitResult | `FHitResult &` | Hit result from any impact if sweep is true. |
| bTeleport | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Return**

- Type: 
- Description: _None_

### K2_SetRelativeTransform

Set the transform of the component relative to its parent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewTransform | `FTransform &` | New transform of the component relative to its parent. |
| bSweep | `bool` | Whether we sweep to the destination (currently not supported for rotation). |
| SweepHitResult | `FHitResult &` | Hit result from any impact if sweep is true. |
| bTeleport | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Return**

- Type: 
- Description: _None_

### GetRelativeTransform

Returns the transform of the component relative to its parent

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ResetRelativeTransform

Reset the transform of the component relative to its parent. Sets relative location to zero, relative rotation to no rotation, and Scale to 1.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetRelativeScale3D

Set the non-uniform scale of the component relative to its parent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewScale3D | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### K2_AddRelativeLocation

Adds a delta to the translation of the component relative to its parent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DeltaLocation | `FVector` | Change in location of the component relative to its parent |
| bSweep | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| SweepHitResult | `FHitResult &` | Hit result from any impact if sweep is true. |
| bTeleport | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Return**

- Type: 
- Description: _None_

### K2_AddRelativeRotation

Adds a delta the rotation of the component relative to its parent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DeltaRotation | `FRotator` | Change in rotation of the component relative to is parent. |
| bSweep | `bool` | Whether we sweep to the destination (currently not supported for rotation). |
| SweepHitResult | `FHitResult &` | Hit result from any impact if sweep is true. |
| bTeleport | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Return**

- Type: 
- Description: _None_

### K2_AddLocalOffset

Adds a delta to the location of the component in its local reference frame

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DeltaLocation | `FVector` | Change in location of the component in its local reference frame. |
| bSweep | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| SweepHitResult | `FHitResult &` | Hit result from any impact if sweep is true. |
| bTeleport | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Return**

- Type: 
- Description: _None_

### K2_AddLocalRotation

Adds a delta to the rotation of the component in its local reference frame

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DeltaRotation | `FRotator` | Change in rotation of the component in its local reference frame. |
| bSweep | `bool` | Whether we sweep to the destination (currently not supported for rotation). |
| SweepHitResult | `FHitResult &` | Hit result from any impact if sweep is true. |
| bTeleport | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Return**

- Type: 
- Description: _None_

### K2_AddLocalTransform

Adds a delta to the transform of the component in its local reference frame. Scale is unchanged.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DeltaTransform | `FTransform &` | Change in transform of the component in its local reference frame. Scale is unchanged. |
| bSweep | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| SweepHitResult | `FHitResult &` | Hit result from any impact if sweep is true. |
| bTeleport | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Return**

- Type: 
- Description: _None_

### K2_SetWorldLocation

Put this component at the specified location in world space. Updates relative location to achieve the final world location.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewLocation | `FVector` | New location in world space for the component. |
| bSweep | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| SweepHitResult | `FHitResult &` | Hit result from any impact if sweep is true. |
| bTeleport | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Return**

- Type: 
- Description: _None_

### K2_SetWorldRotation

Put this component at the specified rotation in world space. Updates relative rotation to achieve the final world rotation.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewRotation | `FRotator` | New rotation in world space for the component. |
| bSweep | `bool` | Whether we sweep to the destination (currently not supported for rotation). |
| SweepHitResult | `FHitResult &` | Hit result from any impact if sweep is true. |
| bTeleport | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Return**

- Type: 
- Description: _None_

### SetWorldScale3D

Set the relative scale of the component to put it at the supplied scale in world space.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewScale | [FVector](../../cppstruct/F/FV/FVector.md) | New scale in world space for this component. |

**Return**

- Type: 
- Description: _None_

### K2_SetWorldTransform

Set the transform of the component in world space.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewTransform | `FTransform &` | New transform in world space for the component. |
| bSweep | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| SweepHitResult | `FHitResult &` | Hit result from any impact if sweep is true. |
| bTeleport | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Return**

- Type: 
- Description: _None_

### K2_AddWorldOffset

Adds a delta to the location of the component in world space.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DeltaLocation | `FVector` | Change in location in world space for the component. |
| bSweep | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| SweepHitResult | `FHitResult &` | Hit result from any impact if sweep is true. |
| bTeleport | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Return**

- Type: 
- Description: _None_

### K2_AddWorldRotation

Adds a delta to the rotation of the component in world space.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DeltaRotation | `FRotator` | Change in rotation in world space for the component. |
| bSweep | `bool` | Whether we sweep to the destination (currently not supported for rotation). |
| SweepHitResult | `FHitResult &` | Hit result from any impact if sweep is true. |
| bTeleport | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Return**

- Type: 
- Description: _None_

### K2_AddWorldTransform

Adds a delta to the transform of the component in world space. Scale is unchanged.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DeltaTransform | `FTransform &` | Change in transform in world space for the component. Scale is unchanged. |
| bSweep | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| SweepHitResult | `FHitResult &` | Hit result from any impact if sweep is true. |
| bTeleport | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Return**

- Type: 
- Description: _None_

### K2_GetComponentLocation

Return location of the component, in world space

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### K2_GetComponentRotation

Returns rotation of the component, in world space.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### K2_GetComponentScale

Returns scale of the component, in world space.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### K2_GetComponentToWorld

Get the current component-to-world transform for this component

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetForwardVector

Get the forward (X) unit direction vector from this component, in world space.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetUpVector

Get the up (Z) unit direction vector from this component, in world space.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetRightVector

Get the right (Y) unit direction vector from this component, in world space.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsSimulatingPhysics

Returns whether the specified body is currently using physics simulation

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BoneName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### IsAnySimulatingPhysics

Returns whether the specified body is currently using physics simulation

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetAttachParent

Get the SceneComponent we are attached to.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetAttachSocketName

Get the socket we are attached to.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetParentComponents

Gets all parent components up to and including the root component

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Parents | `TArray < USceneComponent * > &` |  |

**Return**

- Type: 
- Description: _None_

### GetNumChildrenComponents

Gets the number of attached children components

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetChildComponent

Gets the attached child component at the specified location

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ChildIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetChildrenComponents

Gets all the attached child components

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bIncludeAllDescendants | `bool` | Whether to include all descendants in the list of children (i.e. grandchildren, great grandchildren, etc.) |
| Children | `TArray < USceneComponent * > &` | The list of attached child components |

**Return**

- Type: 
- Description: _None_

### K2_AttachTo

Attach this component to another scene component, optionally at a named socket. It is valid to call this on components whether or not they have been Registered.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InParent | `USceneComponent *` | Parent to attach to. |
| InSocketName | `FName` | Optional socket to attach to on the parent. |
| AttachType | `EAttachLocation :: Type` | How to handle transform when attaching (Keep relative offset, keep world position, etc). |
| bWeldSimulatedBodies | `bool` | Whether to weld together simulated physics bodies. |

**Return**

- Type: 
- Description: _None_

### K2_AttachToComponent

Attach this component to another scene component, optionally at a named socket. It is valid to call this on components whether or not they have been Registered.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Parent | `USceneComponent *` | Parent to attach to. |
| SocketName | `FName` | Optional socket to attach to on the parent. |
| LocationRule | `EAttachmentRule` | How to handle translation when attaching. |
| RotationRule | `EAttachmentRule` | How to handle rotation when attaching. |
| ScaleRule | `EAttachmentRule` | How to handle scale when attaching. |
| bWeldSimulatedBodies | `bool` | Whether to weld together simulated physics bodies. |

**Return**

- Type: 
- Description: _None_

### SnapTo

Zeroes out the relative transform of the component, and calls AttachTo(). Useful for attaching directly to a scene component or socket location

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InParent | `USceneComponent *` |  |
| InSocketName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### DetachFromParent

Detach this component from whatever it is attached to. Automatically unwelds components that are welded together (See WeldTo)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bMaintainWorldPosition | `bool` | If true, update the relative location of the component to keep its world position the same |
| bCallModify | `bool` | If true, call Modify() on the component and the current attach parent component |

**Return**

- Type: 
- Description: _None_

### K2_DetachFromComponent

Detach this component from whatever it is attached to. Automatically unwelds components that are welded together (See WeldTo)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| LocationRule | `EDetachmentRule` | How to handle translations when detaching. |
| RotationRule | `EDetachmentRule` | How to handle rotation when detaching. |
| ScaleRule | `EDetachmentRule` | How to handle scales when detaching. |
| bCallModify | `bool` | If true, call Modify() on the component and the current attach parent component |

**Return**

- Type: 
- Description: _None_

### GetAllSocketNames

Gets the names of all the sockets on the component.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetSocketTransform

Get world-space socket transform.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSocketName | `FName` | Name of the socket or the bone to get the transform |
| TransformSpace | [ERelativeTransformSpace](../../cppenum/E/ER/ERelativeTransformSpace.md) |  |

**Return**

- Type: 
- Description: _None_

### GetSocketLocation

Get world-space socket or bone location.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSocketName | `FName` | Name of the socket or the bone to get the transform |

**Return**

- Type: 
- Description: _None_

### GetSocketRotation

Get world-space socket or bone  FRotator rotation.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSocketName | `FName` | Name of the socket or the bone to get the transform |

**Return**

- Type: 
- Description: _None_

### GetSocketQuaternion

Get world-space socket or bone FQuat rotation.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSocketName | `FName` | Name of the socket or the bone to get the transform |

**Return**

- Type: 
- Description: _None_

### GetSocketScale

Get world-space socket or bone scale.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSocketName | `FName` | Name of the socket or the bone to get the scale |

**Return**

- Type: 
- Description: _None_

### DoesSocketExist

return true if socket with the given name exists

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSocketName | `FName` | Name of the socket or the bone to get the transform |

**Return**

- Type: 
- Description: _None_

### GetComponentVelocity

Get velocity of the component: either ComponentVelocity, or the velocity of the physics body if simulating physics.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsVisible

Is this component visible or not in game

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetVisibility

Set visibility of the component, if during game use this to turn onoff

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewVisibility | `bool` |  |
| bPropagateToChildren | `bool` |  |
| bForceNoPropagate | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ToggleVisibility

Toggle visibility of the component

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bPropagateToChildren | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetHiddenInGame

Changes the value of HiddenGame.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewHidden | `bool` | - The value to assign to HiddenGame. |
| bPropagateToChildren | `bool` |  |

**Return**

- Type: 
- Description: _None_

### IsForceFrameInterpolate

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetForceFrameInterpolate

set bForceDynamic

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InForceFrameInterpolate | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetComponentTransformViewTranslatedBP

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetComponentLocal

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| localTransform | `FTransform &` |  |

**Return**

- Type: 
- Description: _None_

### GetPhysicsVolume

Get the PhysicsVolume overlapping this component.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### K2_SetRelativeLocationAndRotation

Set the location and rotation of the component relative to its parent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewLocation | `FVector` | New location of the component relative to its parent. |
| NewRotation | `FRotator` | New rotation of the component relative to its parent. |
| bSweep | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| SweepHitResult | `FHitResult &` | Hit result from any impact if sweep is true. |
| bTeleport | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Return**

- Type: 
- Description: _None_

### SetAbsolute

Set which parts of the relative transform should be relative to parent, and which should be relative to world

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewAbsoluteLocation | `bool` |  |
| bNewAbsoluteRotation | `bool` |  |
| bNewAbsoluteScale | `bool` |  |

**Return**

- Type: 
- Description: _None_

### IsAbsoluteLocation

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ContainsParent | `bool` |  |

**Return**

- Type: 
- Description: _None_

### K2_SetWorldLocationAndRotation

Set the relative location and rotation of the component to put it at the supplied pose in world space.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewLocation | `FVector` | New location in world space for the component. |
| NewRotation | `FRotator` | New rotation in world space for the component. |
| bSweep | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| SweepHitResult | `FHitResult &` | Hit result from any impact if sweep is true. |
| bTeleport | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Return**

- Type: 
- Description: _None_

### K2_SetMobility

Set how often this component is allowed to move during runtime. Causes a component re-register if the component is already registered

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewMobility | `EComponentMobility :: Type` |  |

**Return**

- Type: 
- Description: _None_

### SetFppLayerRecursive

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InIsFppLayer | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetDisableFppLayerRecursive

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bDisable | `bool` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| PhysicsVolumeChangedDelegate |  | Delegate that will be called when PhysicsVolume has been changed |
| TransformUpdatedDynamic |  |  |

## Language

cpp
