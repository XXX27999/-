# FMeshInstancingSettings

Mesh instance-replacement settings

## Fields

| Name | Type | Description |
| --- | --- | --- |
| ActorClassToUse | `TSubclassOf < AActor >` | The actor class to attach new instance static mesh components to |
| InstanceReplacementThreshold | `int32` | The number of static mesh instances needed before a mesh is replaced with an instanced version |
| MeshReplacementMethod | [EMeshInstancingReplacementMethod](../../../cppenum/E/EM/EMeshInstancingReplacementMethod.md) | How to replace the original actors when instancing |
| bSkipMeshesWithVertexColors | `bool` | Whether to skip the conversion to an instanced static mesh for meshes with vertex colors.<br>	  Instanced static meshes do not support vertex colors per-instance, so conversion will lose<br>	  this data. |
| bUseHLODVolumes | `bool` | Whether split up instanced static mesh components based on their intersection with HLOD volumes |
