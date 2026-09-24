# UPaperSprite

Sprite Asset

  Stores the data necessary to render a single 2D sprite (from a region of a texture)
  Can also contain collision shapes for the sprite.

  @see UPaperSpriteComponent

## Parents

- [UObject](./UObject.md)
- IInterface_CollisionDataProvider
- ISlateTextureAtlasInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| SourceUV | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |
| SourceDimension | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |
| SourceTexture | `UTexture2D *` |  |
| AdditionalSourceTextures | `TArray < UTexture * >` |  |
| BakedSourceUV | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |
| BakedSourceDimension | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |
| BakedSourceTexture | `UTexture2D *` |  |
| DefaultMaterial | `UMaterialInterface *` |  |
| AlternateMaterial | `UMaterialInterface *` |  |
| Sockets | `TArray < FPaperSpriteSocket >` |  |
| SpriteCollisionDomain | `TEnumAsByte < ESpriteCollisionMode :: Type >` |  |
| PixelsPerUnrealUnit | `float` |  |
| BodySetup | `UBodySetup *` |  |
| AlternateMaterialSplitIndex | `int32` |  |
| BakedRenderData | `TArray < FVector4 >` |  |
| OriginInSourceImageBeforeTrimming | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |
| SourceImageDimensionBeforeTrimming | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |
| bTrimmedInSourceImage | `bool` |  |
| bRotatedInSourceImage | `bool` |  |
| SourceTextureDimension | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |
| PivotMode | `TEnumAsByte < ESpritePivotMode :: Type >` |  |
| CustomPivotPoint | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |
| bSnapPivotToPixelGrid | `bool` |  |
| CollisionGeometry | [FSpriteGeometryCollection](../../cppstruct/F/FS/FSpriteGeometryCollection.md) |  |
| CollisionThickness | `float` |  |
| RenderGeometry | [FSpriteGeometryCollection](../../cppstruct/F/FS/FSpriteGeometryCollection.md) |  |
| AtlasGroup | `UPaperSpriteAtlas *` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
