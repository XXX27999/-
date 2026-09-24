# UTileMapBlueprintLibrary

A collection of utility methods for working with tile map components

  @see UPaperTileMap, UPaperTileMapComponent

## Parents

- UBlueprintFunctionLibrary

## Variables

_None_

## Functions

### GetTileUserData

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Tile | [FPaperTileInfo](../../cppstruct/F/FP/FPaperTileInfo.md) |  |

**Return**

- Type: 
- Description: _None_

### GetTileTransform

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Tile | [FPaperTileInfo](../../cppstruct/F/FP/FPaperTileInfo.md) |  |

**Return**

- Type: 
- Description: _None_

### BreakTile

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Tile | `FPaperTileInfo` |  |
| TileIndex | `int32 &` |  |
| TileSet | `UPaperTileSet * &` |  |
| bFlipH | `bool &` |  |
| bFlipV | `bool &` |  |
| bFlipD | `bool &` |  |

**Return**

- Type: 
- Description: _None_

### MakeTile

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TileIndex | `int32` |  |
| TileSet | `UPaperTileSet *` |  |
| bFlipH | `bool` |  |
| bFlipV | `bool` |  |
| bFlipD | `bool` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
