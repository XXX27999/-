# FBuildPromotionImportWorkflowSettings

Holds settings for the import workflow stage of the build promotion test

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Diffuse | [FEditorImportWorkflowDefinition](../FE/FEditorImportWorkflowDefinition.md) | Import settings for the Diffuse texture |
| Normal | [FEditorImportWorkflowDefinition](../FE/FEditorImportWorkflowDefinition.md) | Import settings for the Normalmap texture |
| StaticMesh | [FEditorImportWorkflowDefinition](../FE/FEditorImportWorkflowDefinition.md) | Import settings for the static mesh |
| ReimportStaticMesh | [FEditorImportWorkflowDefinition](../FE/FEditorImportWorkflowDefinition.md) | Import settings for the static mesh to re-import |
| BlendShapeMesh | [FEditorImportWorkflowDefinition](../FE/FEditorImportWorkflowDefinition.md) | Import settings for the blend shape |
| MorphMesh | [FEditorImportWorkflowDefinition](../FE/FEditorImportWorkflowDefinition.md) | Import settings for the morph mesh |
| SkeletalMesh | [FEditorImportWorkflowDefinition](../FE/FEditorImportWorkflowDefinition.md) | Import settings for the skeletal mesh |
| Animation | [FEditorImportWorkflowDefinition](../FE/FEditorImportWorkflowDefinition.md) | Import settings for the animation asset.  (Will automatically use the skeleton of the skeletal mesh above) |
| Sound | [FEditorImportWorkflowDefinition](../FE/FEditorImportWorkflowDefinition.md) | Import settings for the sound |
| SurroundSound | [FEditorImportWorkflowDefinition](../FE/FEditorImportWorkflowDefinition.md) | Import settings for the surround sound (Select any of the channels.  It will auto import the rest) |
| OtherAssetsToImport | `TArray < FEditorImportWorkflowDefinition >` | Import settings for any other assets you may want to import |
