# FSplineMeshParams

Structure that holds info about spline, passed to renderer to deform UStaticMesh.
  Also used by Lightmass, so be sure to update Lightmass::FSplineMeshParams and the static lighting code if this changes!

## Fields

| Name | Type | Description |
| --- | --- | --- |
| StartPos | [FVector](../FV/FVector.md) | Start location of spline, in component space. |
| StartTangent | [FVector](../FV/FVector.md) | Start tangent of spline, in component space. |
| StartScale | [FVector2D](../FV/FVector2D.md) | X and Y scale applied to mesh at start of spline. |
| StartRoll | `float` | Roll around spline applied at start |
| StartOffset | [FVector2D](../FV/FVector2D.md) | Starting offset of the mesh from the spline, in component space. |
| EndPos | [FVector](../FV/FVector.md) | End location of spline, in component space. |
| EndTangent | [FVector](../FV/FVector.md) | End tangent of spline, in component space. |
| EndScale | [FVector2D](../FV/FVector2D.md) | X and Y scale applied to mesh at end of spline. |
| EndRoll | `float` | Roll around spline applied at end. |
| EndOffset | [FVector2D](../FV/FVector2D.md) | Ending offset of the mesh from the spline, in component space. |
