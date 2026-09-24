# ADecalMergeSubVolume

Decal Merge SubVolume
  美术在 ADecalPickupVolume 内手摆的「子体积」，用于在父 Volume 范围内精细控制
  合并 Mesh 的颗粒度。一个 SubVolume = 一个独立合并颗粒度（其内部所有普通 Decal
  合成 1～N 个 Mesh Actor，按 SkyBucket 分桶）。

  关键约束：
  - Atlas 颗粒度不变：仍由父 Volume 统一聚合（一 Volume 一 Atlas）；
    SubVolume 不触发独立 Atlas 构建。
  - 共存兜底：未被任何 SubVolume 覆盖的 Decal 沿用父 Volume 的现有逻辑
    （Grid 或整 Volume）。
  - 完全 EditorOnly：本 Actor 仅服务于编辑器内的合并颗粒度划分，没有任何运行时意义。
    通过重写 IsEditorOnly() = true，Cook 流程会整体跳过该 Actor，不写入 cooked .umap，
    打包后的版本里完全不存在该 Actor（含 DummyRoot）。
    编辑器中正常加载、正常显示、正常保存到 .umap 的 Editor-only 段。

## Parents

- [AActor](./AActor.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| DummyRoot | `USceneComponent *` | 运行时根组件（空 SceneComponent，无渲染开销） |
| VolumeBox | `UBoxComponent *` | Box 组件：定义 SubVolume 的范围，美术可在编辑器中拖拽调整大小 |
| Priority | `int32` | 优先级：用于 Decal 同时落入多个 SubVolume 时的归属仲裁。<br>	  数值越大优先级越高；相同则按 Actor Name 字典序兜底。 |
| OverrideParentVolume | `TWeakObjectPtr < ADecalPickupVolume >` | 可选：父 Volume 显式绑定。留空时按「SubVolume Pivot 落入哪个 DecalPickupVolume」自动推导。<br>	  显式绑定可解决跨 Volume 边界场景下的归属歧义。 |
| SpriteComponent | `UBillboardComponent *` | 编辑器 3D 图标（Billboard Sprite），在 Actor Pivot 位置显示，始终面向摄像机 |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
