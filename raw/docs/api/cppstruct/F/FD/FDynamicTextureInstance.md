# FDynamicTextureInstance

Serialized ULevel information about dynamic texture instances

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Texture | `UTexture2D *` | Texture that is used by a dynamic UPrimitiveComponent. |
| bAttached | `bool` | Whether the primitive that uses this texture is attached to the scene or not. |
| OriginalRadius | `float` | Original bounding sphere radius, at the time the TexelFactor was calculated originally. |
