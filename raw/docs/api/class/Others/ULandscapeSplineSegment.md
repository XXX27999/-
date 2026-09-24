# ULandscapeSplineSegment

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Connections | [FLandscapeSplineSegmentConnection](../../cppstruct/F/FL/FLandscapeSplineSegmentConnection.md) |  |
| SplineInfo | [FInterpCurveVector](../../cppstruct/F/FI/FInterpCurveVector.md) | Actual data for spline. |
| Points | `TArray < FLandscapeSplineInterpPoint >` | Spline points |
| Bounds | [FBox](../../cppstruct/F/FB/FBox.md) | Bounds of points |
| LocalMeshComponents | `TArray < USplineMeshComponent * >` | Spline meshes |
| LayerName | `FName` | Name of blend layer to paint when applying spline to landscape<br>	  If "none", no layer is painted |
| bRaiseTerrain | `uint32` | If the spline is above the terrain, whether to raise the terrain up to the level of the spline when applying it to the landscape. |
| bLowerTerrain | `uint32` | If the spline is below the terrain, whether to lower the terrain down to the level of the spline when applying it to the landscape. |
| SplineMeshes | `TArray < FLandscapeSplineMeshEntry >` | Spline meshes from this list are used in random order along the spline. |
| bEnableCollision | `uint32` | Whether to generate collision for the Spline Meshes. |
| bCastShadow | `uint32` | Whether the Spline Meshes should cast a shadow. |
| RandomSeed | `int32` | Random seed used for choosing which order to use spline meshes. Ignored if only one mesh is set. |
| LDMaxDrawDistance | `float` | Max draw distance for all the mesh pieces used in this spline |
| TranslucencySortPriority | `int32` | Translucent objects with a lower sort priority draw behind objects with a higher priority.<br>	  Translucent objects with the same priority are rendered from back-to-front based on their bounds origin.<br><br>	  Ignored if the object is not translucent.  The default priority is zero.<br>	  Warning: This should never be set to a non-default value unless you know what you are doing, as it will prevent the renderer from sorting correctly. |
| bPlaceSplineMeshesInStreamingLevels | `uint32` | Whether spline meshes should be placed in landscape proxy streaming levels (true) or the spline's level (false) |
| bRenderToTerrainVirtualTexture | `uint8` | This spline will be rendered to terrain VT if true |
| TerrainRVTRenderSortPriority | `int32` | Objects with a lower sort priority draw behind objects with a higher priority.<br>	  Objects with the same priority are rendered from back-to-front based on their bounds origin. |
| bHiddenInGame | `bool` |  |
| bSelected | `uint32` |  |
| bNavDirty | `uint32` |  |
| ForeignWorlds | `TArray < TSoftObjectPtr < UWorld > >` | World references for mesh components stored in other streaming levels |
| ModificationKey | [FGuid](../../cppstruct/F/FG/FGuid.md) | Key for tracking whether this segment has been modified relative to the mesh components stored in other streaming levels |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
