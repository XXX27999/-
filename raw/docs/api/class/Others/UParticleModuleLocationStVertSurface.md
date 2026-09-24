# UParticleModuleLocationStVertSurface

## Parents

- UParticleModuleLocationBase

## Variables

| Name | Type | Description |
| --- | --- | --- |
| SourceType | `TEnumAsByte < enum ELocationStVertSurfaceSource >` | Whether the module uses Verts or Surfaces for locations.<br><br>	   ST_VERTSURFACESOURCE_Vert           - Use StoreVertexPostion<br>	 	ST_VERTSURFACESOURCE_ActorVert		- Use Actor Verts as the source locations.<br>	 	ST_VERTSURFACESOURCE_ActorSurface	- Use Actor Surfaces as the source locations. |
| BrustType | `TEnumAsByte < enum ELocationStVertBrustType >` |  |
| ParticleCoutingMethod | `TEnumAsByte < enum EParticleCoutingMethod >` |  |
| UniversalOffset | [FVector](../../cppstruct/F/FV/FVector.md) | An offset to apply to each vertsurface |
| bUpdatePositionEachFrame | `uint32` | If true, update the particle locations each frame with that of the vertsurface |
| bOrientMeshEmitters | `uint32` | If true, rotate mesh emitter meshes to orient w the vertsurface |
| StMeshActorParamName | `FName` | The parameter name of the skeletal mesh actor that supplies the SkelMeshComponent for in-game. |
| VertexPosition | `TArray < FVector >` |  |
| VertexNormals | `TArray < FVector >` |  |
| EditorStoreTriangleIndexArray | `TArray < int32 >` |  |
| EditorStoreTriangleNum | `int32` |  |
| EditorStoreSectionCount | `int32` |  |
| EditorStoreSectionMinVertexIndexMap | `TMap < int32 , int32 >` |  |
| EditorStoreSectionTrianglesMap | `TMap < int32 , int32 >` |  |
| PostionScale | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| ParticleSpeed | `float` |  |
| bEnforceNormalCheck | `uint32` | When true use the RestrictToNormal and NormalTolerance values to check surface normals |
| NormalToCompare | [FVector](../../cppstruct/F/FV/FVector.md) | Use this normal to restrict spawning locations |
| NormalCheckToleranceDegrees | `float` | Normal tolerance.  0 degrees means it must be an exact match, 180 degrees means it can be any angle. |
| NormalCheckTolerance | `float` | Normal tolerance.  Value between 1.0 and -1.0 with 1.0 being exact match, 0.0 being everything up to<br>		perpendicular and -1.0 being any direction or don't restrict at all. |
| bInheritVertexColor | `uint32` | If true, particles inherit the associated vertex color on spawn. This feature is not supported for GPU particles. |
| bInheritUV | `uint32` | If true, particles inherit the associated UV data on spawn. Accessed through dynamic parameter module X and Y, must be a "Spawn Time Only" parameter on "AutoSet" mode. This feature is not supported for GPU particles. |
| InheritUVChannel | `uint32` | UV channel to inherit from the spawn mesh, internally clamped to those available. |
| EditorStMesh | `UStaticMesh *` | The name of the skeletal mesh to use in the editor |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
