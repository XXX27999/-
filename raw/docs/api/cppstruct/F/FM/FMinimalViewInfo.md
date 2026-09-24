# FMinimalViewInfo

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Location | [FVector](../FV/FVector.md) | Location |
| LocationLocalSpace | [FVector](../FV/FVector.md) | Location In Local Space |
| Rotation | [FRotator](../FR/FRotator.md) | Rotation |
| ViewTag | `FName` |  |
| FOV | `float` | The field of view (in degrees) in perspective mode (ignored in Orthographic mode) |
| bUseFirstPersonParameters | `uint32` |  |
| FirstPersonFOV | `float` | The horizontal field of view (in degrees) used for primitives tagged as "IsFirstPerson". |
| FirstPersonScale | `float` | The scale to apply to primitives tagged as "IsFirstPerson". This is used to scale down primitives towards the camera such that they are small enough not to intersect with the scene. |
| FirstPersonScaleParameters | [FVector](../FV/FVector.md) |  |
| OrthoWidth | `float` | The desired width (in world units) of the orthographic view (ignored in Perspective mode) |
| OrthoNearClipPlane | `float` | The near plane distance of the orthographic view (in world units) |
| OrthoFarClipPlane | `float` | The far plane distance of the orthographic view (in world units) |
| AspectRatio | `float` |  |
| bConstrainAspectRatio | `uint32` |  |
| bUseFieldOfViewForLOD | `uint32` |  |
| ProjectionMode | `TEnumAsByte < ECameraProjectionMode :: Type >` |  |
| PostProcessBlendWeight | `float` | Indicates if PostProcessSettings should be applied. |
| PostProcessSettings | [FPostProcessSettings](../FP/FPostProcessSettings.md) | Post-process settings to use if PostProcessBlendWeight is non-zero. |
| OffCenterProjectionOffset | [FVector2D](../FV/FVector2D.md) | Off-axis  off-center projection offset as proportion of screen dimensions |
