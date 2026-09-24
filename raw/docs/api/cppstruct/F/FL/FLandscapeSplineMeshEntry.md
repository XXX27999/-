# FLandscapeSplineMeshEntry

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Mesh | `UStaticMesh *` | Mesh to use on the spline |
| MaterialOverrides | `TArray < UMaterialInterface * >` | Overrides mesh's materials |
| bCenterH | `uint32` | Whether to automatically center the mesh horizontally on the spline |
| CenterAdjust | [FVector2D](../FV/FVector2D.md) | Tweak to center the mesh correctly on the spline |
| bScaleToWidth | `uint32` | Whether to scale the mesh to fit the width of the spline |
| Scale | [FVector](../FV/FVector.md) | Scale of the spline mesh, (Z=Forwards) |
| Orientation_DEPRECATED | `TEnumAsByte < LandscapeSplineMeshOrientation >` | Orientation of the spline mesh, X=Up or Y=Up |
| ForwardAxis | `TEnumAsByte < ESplineMeshAxis :: Type >` | Chooses the forward axis for the spline mesh orientation |
| UpAxis | `TEnumAsByte < ESplineMeshAxis :: Type >` | Chooses the up axis for the spline mesh orientation |
