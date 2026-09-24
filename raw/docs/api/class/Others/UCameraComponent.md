# UCameraComponent

Represents a camera viewpoint and settings, such as projection type, field of view, and post-process overrides.
   The default behavior for an actor used as the camera view target is to look for an attached camera component and use its location, rotation, and settings.

## Parents

- [USceneComponent](./USceneComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| FieldOfView | `float` | The horizontal field of view (in degrees) in perspective mode (ignored in Orthographic mode) |
| FirstPersonFieldOfView | `float` | The horizontal field of view (in degrees) used for primitives tagged as "IsFirstPerson". |
| FirstPersonScale | `float` | The scale to apply to primitives tagged as "IsFirstPerson". This is used to scale down primitives towards the camera such that they are small enough not to intersect with the scene. |
| FirstPersonScaleCurveNearValue | `float` |  |
| FirstPersonScaleMaxLength | `float` |  |
| FirstPersonScaleCurvePow | `float` |  |
| bEnableFirstPersonFieldOfView | `uint8` | True if the first person field of view should be used for primitives tagged as "IsFirstPerson". |
| bEnableFirstPersonScale | `uint8` | True if the first person scale should be used for primitives tagged as "IsFirstPerson". |
| OrthoWidth | `float` | The desired width (in world units) of the orthographic view (ignored in Perspective mode) |
| OrthoNearClipPlane | `float` | The near plane distance of the orthographic view (in world units) |
| OrthoFarClipPlane | `float` | The far plane distance of the orthographic view (in world units) |
| AspectRatio | `float` |  |
| WidthHeight | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |
| bConstrainAspectRatio | `uint32` |  |
| bUseFieldOfViewForLOD | `uint32` |  |
| bLockToHmd | `uint32` | True if the camera's orientation and position should be locked to the HMD |
| bUsePawnControlRotation | `uint32` | If this camera component is placed on a pawn, should it use the viewcontrol rotation of the pawn where possible?<br>	  @see APawn::GetViewRotation() |
| bEnableModifyAdditiveOffset | `uint32` |  |
| ProjectionMode | `TEnumAsByte < ECameraProjectionMode :: Type >` |  |
| PostProcessBlendWeight | `float` | Indicates if PostProcessSettings should be used when using this Camera to view through. |
| PostProcessSettings | [FPostProcessSettings](../../cppstruct/F/FP/FPostProcessSettings.md) | Post process settings to use for this camera. Don't forget to check the properties you want to override |
| bUseControllerViewRotation_DEPRECATED | `uint32` | DEPRECATED: use bUsePawnControlRotation instead |

## Functions

### SetFieldOfView

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InFieldOfView | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetFirstPersonFieldOfView

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InFirstPersonFieldOfView | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetFirstPersonScale

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InFirstPersonScale | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetFirstPersonScaleParams

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InFirstPersonScale | `float` |  |
| InFPScaleCurveNearValue | `float` |  |
| InFPScaleMaxLen | `float` |  |
| InFPScaleCurvePow | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetEnableFirstPersonFieldOfView

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInEnableFirstPersonFieldOfView | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetEnableFirstPersonScale

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInEnableFirstPersonScale | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetActive

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewActive | `bool` |  |
| bReset | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ApplyDrawDistanceOffset

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InFieldOfView | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetOrthoWidth

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InOrthoWidth | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetOrthoNearClipPlane

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InOrthoNearClipPlane | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetOrthoFarClipPlane

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InOrthoFarClipPlane | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetAspectRatio

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InAspectRatio | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetWidthHeight

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InWidthHeight | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### SetConstraintAspectRatio

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInConstrainAspectRatio | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetUseFieldOfViewForLOD

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInUseFieldOfViewForLOD | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetProjectionMode

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InProjectionMode | `ECameraProjectionMode :: Type` |  |

**Return**

- Type: 
- Description: _None_

### SetPostProcessBlendWeight

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPostProcessBlendWeight | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetCameraView

Returns camera's Point of View.
	  Called by Camera class. Subclass and postprocess to add any effects.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DeltaTime | `float` |  |
| DesiredView | `FMinimalViewInfo &` |  |

**Return**

- Type: 
- Description: _None_

### AddOrUpdateBlendable

Adds an Blendable (implements IBlendableInterface) to the array of Blendables (if it doesn't exist) and update the weight

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBlendableObject | `TScriptInterface < IBlendableInterface >` |  |
| InWeight | `float` |  |

**Return**

- Type: 
- Description: _None_

### RemoveBlendable

Removes a blendable.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBlendableObject | `TScriptInterface < IBlendableInterface >` |  |

**Return**

- Type: 
- Description: _None_

### SetbEnableModifyAdditiveOffset

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InEnable | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetEnableModifyAdditiveOffset

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### AddAdditiveOffset

Applies the given additive offset, preserving any existing offset

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Transform | `FTransform &` |  |
| FOV | `float` |  |

**Return**

- Type: 
- Description: _None_

### ClearAdditiveOffset

Removes any additive offset.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetAddtiveInfo

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OutIsAddtive | `bool &` |  |
| OutAddtiveOffset | `float &` |  |
| OutAddtiveTrans | `FTransform &` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
