# ADecalPickupVolume

Decal Pickup Volume
  用于标定贴花合并颗粒度的 Volume Actor。
  同一个 Volume 内的所有 DecalActor 会被统一拾取为一批，合出来的图集（Atlas）是一套。
  支持 Grid 划分以控制合成 Mesh 的粒度（用于视锥剔除和遮挡剔除）。

  运行时轻量模式（非 EditorOnly）：
  - Volume 进入包体作为生成 Mesh 的 ParentActor（层级组织）
  - 编辑器专用组件（BoxComponent、GridLineComponent）通过 WITH_EDITORONLY_DATA 在 Cook 时剥离
  - 运行时仅剩空壳 AActor（无渲染、无 Tick、无碰撞，~200 bytes）

## Parents

- [AActor](./AActor.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| DummyRoot | `USceneComponent *` | 运行时根组件（空 SceneComponent，无渲染开销） |
| VolumeBox | `UBoxComponent *` | Box 组件：定义 Volume 的范围，美术可在编辑器中拖拽调整大小<br>	 仅编辑器下存在，Cook 时由 WITH_EDITORONLY_DATA 保证剥离，无需 Transient |
| bEnableGridSubdivision | `bool` | 是否启用 Grid 划分（仅 XY 维度，不划分 Z） |
| GridCellSize | `float` | 单个 Grid Cell 的世界空间大小（cm），仅 XY 维度 |
| SpriteComponent | `UBillboardComponent *` | 编辑器 3D 图标（Billboard Sprite），在 Actor Pivot 位置显示，始终面向摄像机 |
| GridLineComponent | `ULineBatchComponent *` | Grid 线可视化组件 |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
