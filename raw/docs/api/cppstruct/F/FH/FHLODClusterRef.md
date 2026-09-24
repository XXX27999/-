# FHLODClusterRef

记录一个 LODActor 拥有的 HISM ClusterTree 节点引用。

  方案：按 Grid 坐标分配"整 Node"。
    - 分组单元 = 一整个 ClusterTree Node（Node 中心落 Grid）。Node 要么完整归属某个 LODActor，
      要么完全不归属，绝不拆分到 instance 粒度。
    - OwnedClusterNodeIndices 是唯一主键：烘焙端按 Node 取 [FirstInstance,LastInstance]
      (Sorted) -> SortedInstances[] 映射 Logical -> 拷贝；运行时用同一 NodeIndex 下 Mask。
      两端针对同一批物理实例，不会穿帮。
    - ClusterBounds 仅用于 LODActor 位置包围盒。

  前提（打破任一条必须重新评估方案）：
    - 重组关卡不允许人为修改（实例与 ClusterTree 稳定）；
    - 使用普通 HISM（bIsFoliage=false，默认 bEnableDensityScaling=false，不会触发密度剔除重建）；
    - 一次重组对应一次 HLOD 构建。

## Fields

| Name | Type | Description |
| --- | --- | --- |
| HISMActor | `TSoftObjectPtr < AActor >` |  |
| OwnedClusterNodeIndices | `TArray < int32 >` |  |
| ClusterBounds | [FBox](../FB/FBox.md) |  |
| InstanceCount | `int32` |  |
| PerInstanceTriangleCount | `int32` |  |
