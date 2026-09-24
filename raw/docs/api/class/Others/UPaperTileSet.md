# UPaperTileSet

A tile set is a collection of tiles pulled from a texture that can be used to fill out a tile map.

  @see UPaperTileMap, UPaperTileMapComponent

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| TileSize | [FIntPoint](../../cppstruct/F/FI/FIntPoint.md) |  |
| TileSheet | `UTexture2D *` |  |
| AdditionalSourceTextures | `TArray < UTexture * >` |  |
| BorderMargin | [FIntMargin](../../cppstruct/F/FI/FIntMargin.md) |  |
| PerTileSpacing | [FIntPoint](../../cppstruct/F/FI/FIntPoint.md) |  |
| DrawingOffset | [FIntPoint](../../cppstruct/F/FI/FIntPoint.md) |  |
| WidthInTiles | `int32` |  |
| HeightInTiles | `int32` |  |
| AllocatedWidth | `int32` |  |
| AllocatedHeight | `int32` |  |
| PerTileData | `TArray < FPaperTileMetadata >` |  |
| Terrains | `TArray < FPaperTileSetTerrain >` |  |
| TileWidth_DEPRECATED | `int32` |  |
| TileHeight_DEPRECATED | `int32` |  |
| Margin_DEPRECATED | `int32` |  |
| Spacing_DEPRECATED | `int32` |  |
| BackgroundColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | The background color displayed in the tile set viewer |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
