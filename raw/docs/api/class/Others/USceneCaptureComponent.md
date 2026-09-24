# USceneCaptureComponent

## Parents

- [USceneComponent](./USceneComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| PrimitiveRenderMode | [ESceneCapturePrimitiveRenderMode](../../cppenum/E/ES/ESceneCapturePrimitiveRenderMode.md) | Controls what primitives get rendered into the scene capture. |
| HiddenComponents | `TArray < TWeakObjectPtr < UPrimitiveComponent > >` | The components won't rendered by current component. |
| HiddenActors | `TArray < AActor * >` | The actors to hide in the scene capture. |
| ShowOnlyComponents | `TArray < TWeakObjectPtr < UPrimitiveComponent > >` | The only components to be rendered by this scene capture, if PrimitiveRenderMode is set to UseShowOnlyList. |
| bShowAttachedActor | `bool` |  |
| ShowOnlyActors | `TArray < AActor * >` | The only actors to be rendered by this scene capture, if PrimitiveRenderMode is set to UseShowOnlyList. |
| bCaptureEveryFrame | `bool` | Whether to update the capture's contents every frame.  If disabled, the component will render once on load and then only when moved. |
| bCaptureOnMovement | `bool` | Whether to update the capture's contents on movement.  Disable if you are going to capture manually from blueprint. |
| bAlwaysPersistRenderingState | `bool` | Whether to persist the rendering state even if bCaptureEveryFrame==false.  This allows velocities for Motion Blur and Temporal AA to be computed. |
| LODDistanceFactor | `float` | Scales the distance used by LOD. Set to values greater than 1 to cause the scene capture to use lower LODs than the main view to speed up the scene capture pass. |
| MaxViewDistanceOverride | `float` | if > 0, sets a maximum render distance override.  Can be used to cull distant objects from a reflection if the reflecting plane is in an enclosed area like a hallway or room |
| CaptureSortPriority | `int32` | Capture priority within the frame to sort scene capture on GPU to resolve interdependencies between multiple capture components. Highest come first. |
| ShowFlagSettings | `TArray < struct FEngineShowFlagsSetting >` | ShowFlags for the SceneCapture's ViewFamily, to control rendering settings for this view. Hidden but accessible through details customization |
| LightingChannels | [FLightingChannels](../../cppstruct/F/FL/FLightingChannels.md) |  |
| bUseLightingChannels | `bool` |  |

## Functions

### HideComponent

Adds the component to our list of hidden components.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InComponent | `UPrimitiveComponent *` |  |

**Return**

- Type: 
- Description: _None_

### HideActorComponents

Adds all primitive components in the actor to our list of hidden components.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InActor | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### ShowOnlyComponent

Adds the component to our list of show-only components.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InComponent | `UPrimitiveComponent *` |  |

**Return**

- Type: 
- Description: _None_

### ShowOnlyActorComponents

Adds all primitive components in the actor to our list of show-only components.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InActor | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### RemoveShowOnlyComponent

Removes a component from the Show Only list.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InComponent | `UPrimitiveComponent *` |  |

**Return**

- Type: 
- Description: _None_

### RemoveShowOnlyActorComponents

Removes a actor's components from the Show Only list.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InActor | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### ClearShowOnlyComponents

Clears the Show Only list.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ClearHiddenComponents

Clears the hidden list.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetCaptureSortPriority

Changes the value of TranslucentSortPriority.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewCaptureSortPriority | `int32` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
