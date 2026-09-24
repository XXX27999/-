# UPaperTileMapComponent

A component that handles rendering and collision for a single instance of a UPaperTileMap asset.

  This component is created when you drag a tile map asset from the content browser into a Blueprint, or
  contained inside of the actor created when you drag one into the level.

  NOTE: This is an early access preview class.  While not considered production-ready, it is a step beyond
  'experimental' and is being provided as a preview of things to come:
   - We will try to provide forward-compatibility for content you create.
   - The classes may change significantly in the future.
   - The code is in an early state and may not meet the desired polish  quality bar.
   - There is probably no documentation or example content yet.
   - They will be promoted out of 'Early Access' when they are production ready.

  @see UPrimitiveComponent, UPaperTileMap

## Parents

- [UMeshComponent](./UMeshComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| MapWidth_DEPRECATED | `int32` |  |
| MapHeight_DEPRECATED | `int32` |  |
| TileWidth_DEPRECATED | `int32` |  |
| TileHeight_DEPRECATED | `int32` |  |
| DefaultLayerTileSet_DEPRECATED | `UPaperTileSet *` |  |
| Material_DEPRECATED | `UMaterialInterface *` |  |
| TileLayers_DEPRECATED | `TArray < UPaperTileLayer * >` |  |
| TileMapColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |
| UseSingleLayerIndex | `int32` |  |
| bUseSingleLayer | `bool` |  |
| TileMap | `UPaperTileMap *` |  |
| bShowPerTileGridWhenSelected | `bool` |  |
| bShowPerLayerGridWhenSelected | `bool` |  |
| bShowOutlineWhenUnselected | `bool` |  |

## Functions

### CreateNewTileMap

Creates a new tile map of the specified size, replacing the TileMap reference (or dropping the previous owned one)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MapWidth | `int32` | Width of the map (in tiles) |
| MapHeight | `int32` | Height of the map (in tiles) |
| TileWidth | `int32` | Width of one tile (in pixels) |
| TileHeight | `int32` | Height of one tile (in pixels) |
| PixelsPerUnrealUnit | `float` |  |
| bCreateLayer | `bool` | Should an empty layer be created? |

**Return**

- Type: 
- Description: _None_

### OwnsTileMap

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetTileMap

Change the PaperTileMap used by this instance.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewTileMap | `UPaperTileMap *` |  |

**Return**

- Type: 
- Description: _None_

### GetMapSize

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MapWidth | `int32 &` |  |
| MapHeight | `int32 &` |  |
| NumLayers | `int32 &` |  |

**Return**

- Type: 
- Description: _None_

### GetTile

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| X | `int32` |  |
| Y | `int32` |  |
| Layer | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetTile

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| X | `int32` |  |
| Y | `int32` |  |
| Layer | `int32` |  |
| NewValue | [FPaperTileInfo](../../cppstruct/F/FP/FPaperTileInfo.md) |  |

**Return**

- Type: 
- Description: _None_

### ResizeMap

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewWidthInTiles | `int32` |  |
| NewHeightInTiles | `int32` |  |

**Return**

- Type: 
- Description: _None_

### AddNewLayer

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetTileMapColor

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetTileMapColor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_

### GetLayerColor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Layer | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetLayerColor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewColor | `FLinearColor` |  |
| Layer | `int32` |  |

**Return**

- Type: 
- Description: _None_

### MakeTileMapEditable

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetTileCornerPosition

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TileX | `int32` |  |
| TileY | `int32` |  |
| LayerIndex | `int32` |  |
| bWorldSpace | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetTileCenterPosition

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TileX | `int32` |  |
| TileY | `int32` |  |
| LayerIndex | `int32` |  |
| bWorldSpace | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetTilePolygon

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TileX | `int32` |  |
| TileY | `int32` |  |
| Points | `TArray < FVector > &` |  |
| LayerIndex | `int32` |  |
| bWorldSpace | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetDefaultCollisionThickness

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Thickness | `float` |  |
| bRebuildCollision | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetLayerCollision

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Layer | `int32` |  |
| bHasCollision | `bool` |  |
| bOverrideThickness | `bool` |  |
| CustomThickness | `float` |  |
| bOverrideOffset | `bool` |  |
| CustomOffset | `float` |  |
| bRebuildCollision | `bool` |  |

**Return**

- Type: 
- Description: _None_

### RebuildCollision

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
