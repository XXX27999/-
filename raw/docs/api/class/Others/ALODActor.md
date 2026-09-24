# ALODActor

## Parents

- [AActor](./AActor.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| StaticMeshComponent | `UStaticMeshComponent *` |  |
| Proxy | `UHLODProxy *` | The mesh proxy used to display this LOD |
| Key | `FName` | The key used to validate this actor against the proxy |
| LODDrawDistance | `float` | what distance do you want this to show up instead of SubActors |
| SubActors | `TArray < AActor * >` |  |
| ClusterRefs | `TArray < FHLODClusterRef >` |  |
| bIsClusterBasedHLOD | `bool` |  |
| HLODGroupName | `FName` | 该 LODActor 所属的 HLOD Group 名称（来自 WorldSettings HLODSetup[L].HLODGroups[i].GroupName）。<br>	  NAME_None  = Default 重组通道产物，使用关卡默认 BaseMaterial 与默认 DrawDistanceScale。<br>	  非空       = 由 Group 通道产物，烘焙时按此名反查 ProxyBaseMaterial，运行时反查 LODDrawDistanceScale。 |
| DebugHighlightDuration | `float` | 调试包围盒持续时间（秒） |
| DebugHighlightColor | [FColor](../../cppstruct/F/FC/FColor.md) | 调试包围盒颜色 |
| DebugHighlightThickness | `float` | 调试包围盒线宽 |
| bDebugPrintNodeIndex | `bool` | 是否在 Cluster 节点中心打印 RefNode 索引文本（用于诊断哪个 Node 跑偏） |
| DebugHighlightRefIndices | `TArray < int32 >` | 仅高亮指定索引的 ClusterRef（针对 ClusterRefs 数组下标）。<br>	  留空 = 高亮全部 ClusterRefs；填了任意值 = 只高亮命中数组中的 RefIndex。<br>	  例：[0, 2] 表示仅高亮 ClusterRefs[0] 与 ClusterRefs[2]。 |
| LODLevel | `int32` | The hierarchy level of this actor; the first tier of HLOD is level 1, the second tier is level 2 and so on. |
| bCookStripProxyMesh | `bool` | If true, during Cook the proxy StaticMesh and Proxy reference will be stripped (set to nullptr).<br>	   The mesh asset path is saved to CachedProxyMeshPath for runtime async reload on demand.<br>	   This prevents the HLOD mesh and its textures from being loaded into memory at level load time. |
| CachedProxyMeshPath | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | Soft path to the original static mesh, used to reload after Cook strip or runtime unloading.<br>	   UPROPERTY so it is serialized into the cooked package for runtime async reload.<br>	   FSoftObjectPath is a soft reference (path string only) and does NOT prevent GC. |
| CachedNumHLODLevels | `uint8` |  |
| HLODActorDebugDynamicMaterialInstance | `UMaterialInstanceDynamic *` |  |
| SubActorsDebugDynamicMaterialInstance | `UMaterialInstanceDynamic *` |  |
| NumTrianglesInSubActors | `uint32` | Cached number of triangles contained in the SubActors |
| NumTrianglesInMergedMesh | `uint32` | Cached number of triangles contained in the SubActors |
| bOverrideMaterialMergeSettings | `bool` | Flag whether or not to use the override MaterialSettings when creating the proxy mesh |
| MaterialSettings | [FMaterialProxySettings](../../cppstruct/F/FM/FMaterialProxySettings.md) | Override Material Settings, used when creating the proxy mesh |
| bOverrideTransitionScreenSize | `bool` | Flag whether or not to use the override TransitionScreenSize for this proxy mesh |
| TransitionScreenSize | `float` | Override transition screen size value, determines the screen size at which the proxy is visible<br>	  The screen size is based around the projected diameter of the bounding<br>	  sphere of the model. i.e. 0.5 means half the screen's maximum dimension. |
| bOverrideScreenSize | `bool` | Flag whether or not to use the override ScreenSize when creating the proxy mesh |
| ScreenSize | `int32` | Override screen size value used in mesh reduction, when creating the proxy mesh |

## Functions

### DebugHighlightOwnedClusters

编辑器调试：高亮本 LODActor 管辖的所有 HISM Cluster 节点包围盒。
	  仅纯 Cluster LODActor 有效。绘制时长由 DebugHighlightDuration 控制，运行时永不调用。

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
