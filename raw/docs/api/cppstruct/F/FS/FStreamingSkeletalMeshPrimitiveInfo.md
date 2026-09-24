# FStreamingSkeletalMeshPrimitiveInfo

Information about a streaming StaticMesh that a primitive uses for rendering.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| SkeletalMesh | `USkeletalMesh *` |  |
| Bounds | [FBoxSphereBounds](../FB/FBoxSphereBounds.md) | The streaming bounds of the StaticMesh, usually the component material bounds.<br>	  Usually only valid for registered component, as component bounds are only updated when the components are registered.<br>	  otherwise only PackedRelativeBox can be used.Irrelevant when the component is not registered, as the component could be moved by ULevel::ApplyWorldOffset()<br>	  In that case, only PackedRelativeBox is meaningful. |
