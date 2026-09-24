# FStaticMeshSourceModel

-----------------------------------------------------------------------------
-----------------------------------------------------------------------------

  Source model from which a renderable static mesh is built.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| BuildSettings | [FMeshBuildSettings](../FM/FMeshBuildSettings.md) | Settings applied when building the mesh. |
| ReductionSettings | [FMeshReductionSettings](../FM/FMeshReductionSettings.md) | Reduction settings to apply when building render data. |
| RemeshingSettings_DEPRECATED | [FSimplygonRemeshingSettings](./FSimplygonRemeshingSettings.md) |  |
| bHasBeenSimplified | `bool` |  |
| OptimizationSettings | [FGroupedStaticMeshOptimizationSettings](../FG/FGroupedStaticMeshOptimizationSettings.md) |  |
| LODDistance_DEPRECATED | `float` | Allow per-LOD overriding of lightmap resolution<br>	UPROPERTY(EditAnywhere, Category=Lighting)<br>	int32 OverriddenLightMapRes; |
| ScreenSize | `float` | ScreenSize to display this LOD.<br>	  The screen size is based around the projected diameter of the bounding<br>	  sphere of the model. i.e. 0.5 means half the screen's maximum dimension. |
| SourceImportFilename | `FString` | The file path that was used to import this LOD. |
| bImportWithBaseMesh | `bool` | Weather this LOD was imported in the same file as the base mesh. |
