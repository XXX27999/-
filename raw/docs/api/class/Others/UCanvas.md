# UCanvas

A drawing canvas.

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| OrgX | `float` |  |
| OrgY | `float` |  |
| ClipX | `float` |  |
| ClipY | `float` |  |
| DrawColor | [FColor](../../cppstruct/F/FC/FColor.md) |  |
| bCenterX | `uint32` |  |
| bCenterY | `uint32` |  |
| bNoSmooth | `uint32` |  |
| SizeX | `int32` |  |
| SizeY | `int32` |  |
| ColorModulate | [FPlane](../../cppstruct/F/FP/FPlane.md) |  |
| DefaultTexture | `UTexture2D *` |  |
| GradientTexture0 | `UTexture2D *` |  |
| ReporterGraph | `UReporterGraph *` | Helper class to render 2d graphs on canvas |

## Functions

### K2_DrawLine

Draws a line on the Canvas.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ScreenPositionA | `FVector2D` | Starting position of the line in screen space. |
| ScreenPositionB | `FVector2D` | Ending position of the line in screen space. |
| Thickness | `float` | How many pixels thick this line should be. |
| RenderColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | Color to render the line. |

**Return**

- Type: 
- Description: _None_

### K2_DrawTexture

Draws a texture on the Canvas.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| RenderTexture | `UTexture *` | Texture to use when rendering. If no texture is set then this will use the default white texture. |
| ScreenPosition | `FVector2D` | Screen space position to render the texture. |
| ScreenSize | `FVector2D` | Screen space size to render the texture. |
| CoordinatePosition | `FVector2D` | Normalized UV starting coordinate to use when rendering the texture. |
| CoordinateSize | `FVector2D` | Normalized UV size coordinate to use when rendering the texture. |
| RenderColor | `FLinearColor` | Color to use when rendering the texture. |
| BlendMode | `EBlendMode` | Blending mode to use when rendering the texture. |
| Rotation | `float` | Rotation, in degrees, to render the texture. |
| PivotPoint | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | Normalized pivot point to use when rotating the texture. |

**Return**

- Type: 
- Description: _None_

### K2_DrawMaterial

Draws a material on the Canvas.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| RenderMaterial | `UMaterialInterface *` | Material to use when rendering. Remember that only the emissive channel is able to be rendered as no lighting is performed when rendering to the Canvas. |
| ScreenPosition | `FVector2D` | Screen space position to render the texture. |
| ScreenSize | `FVector2D` | Screen space size to render the texture. |
| CoordinatePosition | `FVector2D` | Normalized UV starting coordinate to use when rendering the texture. |
| CoordinateSize | `FVector2D` | Normalized UV size coordinate to use when rendering the texture. |
| Rotation | `float` | Rotation, in degrees, to render the texture. |
| PivotPoint | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | Normalized pivot point to use when rotating the texture. |

**Return**

- Type: 
- Description: _None_

### K2_DrawText

Draws text on the Canvas.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| RenderFont | `UFont *` | Font to use when rendering the text. If this is null, then a default engine font is used. |
| RenderText | `FString &` | Text to render on the Canvas. |
| ScreenPosition | `FVector2D` | Screen space position to render the text. |
| RenderColor | `FLinearColor` | Color to render the text. |
| Kerning | `float` | Horizontal spacing adjustment to modify the spacing between each letter. |
| ShadowColor | `FLinearColor` | Color to render the shadow of the text. |
| ShadowOffset | `FVector2D` | Pixel offset relative to the screen space position to render the shadow of the text. |
| bCentreX | `bool` | If true, then interpret the screen space position X coordinate as the center of the rendered text. |
| bCentreY | `bool` | If true, then interpret the screen space position Y coordinate as the center of the rendered text. |
| bOutlined | `bool` | If true, then the text should be rendered with an outline. |
| OutlineColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | Color to render the outline for the text. |

**Return**

- Type: 
- Description: _None_

### K2_DrawBorder

Draws a 3x3 grid border with tiled frame and tiled interior on the Canvas.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BorderTexture | `UTexture *` | Texture to use for border. |
| BackgroundTexture | `UTexture *` | Texture to use for border background. |
| LeftBorderTexture | `UTexture *` | Texture to use for the tiling left border. |
| RightBorderTexture | `UTexture *` | Texture to use for the tiling right border. |
| TopBorderTexture | `UTexture *` | Texture to use for the tiling top border. |
| BottomBorderTexture | `UTexture *` | Texture to use for the tiling bottom border. |
| ScreenPosition | `FVector2D` | Screen space position to render the texture. |
| ScreenSize | `FVector2D` | Screen space size to render the texture. |
| CoordinatePosition | `FVector2D` | Normalized UV starting coordinate to use when rendering the border texture. |
| CoordinateSize | `FVector2D` | Normalized UV size coordinate to use when rendering the border texture. |
| RenderColor | `FLinearColor` | Color to tint the border. |
| BorderScale | `FVector2D` | Scale of the border. |
| BackgroundScale | `FVector2D` | Scale of the background. |
| Rotation | `float` | Rotation, in degrees, to render the texture. |
| PivotPoint | `FVector2D` | Normalized pivot point to use when rotating the texture. |
| CornerSize | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | Frame corner size in percent of frame texture (should be < 0.5f). |

**Return**

- Type: 
- Description: _None_

### K2_DrawBox

Draws an unfilled box on the Canvas.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ScreenPosition | `FVector2D` | Screen space position to render the text. |
| ScreenSize | `FVector2D` | Screen space size to render the texture. |
| Thickness | `float` | How many pixels thick the box lines should be. |

**Return**

- Type: 
- Description: _None_

### K2_DrawTriangle

Draws a set of triangles on the Canvas.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| RenderTexture | `UTexture *` | Texture to use when rendering the triangles. If no texture is set, then the default white texture is used. |
| Triangles | `TArray < FCanvasUVTri >` | Triangles to render. |

**Return**

- Type: 
- Description: _None_

### K2_DrawMaterialTriangle

Draws a set of triangles on the Canvas.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| RenderMaterial | `UMaterialInterface *` | Material to use when rendering. Remember that only the emissive channel is able to be rendered as no lighting is performed when rendering to the Canvas. |
| Triangles | `TArray < FCanvasUVTri >` | Triangles to render. |

**Return**

- Type: 
- Description: _None_

### K2_DrawPolygon

Draws a polygon on the Canvas.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| RenderTexture | `UTexture *` | Texture to use when rendering the triangles. If no texture is set, then the default white texture is used. |
| ScreenPosition | `FVector2D` | Screen space position to render the text. |
| Radius | `FVector2D` | How large in pixels this polygon should be. |
| NumberOfSides | `int32` | How many sides this polygon should have. This should be above or equal to three. |
| RenderColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | Color to tint the polygon. |

**Return**

- Type: 
- Description: _None_

### K2_Project

Performs a projection of a world space coordinates using the projection matrix set up for the Canvas.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldLocation | [FVector](../../cppstruct/F/FV/FVector.md) | World space location to project onto the Canvas rendering plane. |

**Return**

- Type: 
- Description: _None_

### K2_Deproject

Performs a deprojection of a screen space coordinate using the projection matrix set up for the Canvas.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ScreenPosition | `FVector2D` | Screen space position to deproject to the World. |
| WorldOrigin | `FVector &` | Vector which is the world position of the screen space position. |
| WorldDirection | `FVector &` | Vector which can be used in a trace to determine what is "behind" the screen space position. Useful for object picking. |

**Return**

- Type: 
- Description: _None_

### K2_StrLen

Returns the wrapped text size in screen space coordinates.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| RenderFont | `UFont *` | Font to use when determining the size of the text. If this is null, then a default engine font is used. |
| RenderText | `FString &` | Text to determine the size of. |

**Return**

- Type: 
- Description: _None_

### K2_TextSize

Returns the clipped text size in screen space coordinates.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| RenderFont | `UFont *` | Font to use when determining the size of the text. If this is null, then a default engine font is used. |
| RenderText | `FString &` | Text to determine the size of. |
| Scale | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | Scale of the font to use when determining the size of the text. |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
