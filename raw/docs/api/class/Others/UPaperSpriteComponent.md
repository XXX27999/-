# UPaperSpriteComponent

A component that handles rendering and collision for a single instance of a UPaperSprite asset.

  This component is created when you drag a sprite asset from the content browser into a Blueprint, or
  contained inside of the actor created when you drag one into the level.

  @see UPrimitiveComponent, UPaperSprite

## Parents

- [UMeshComponent](./UMeshComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| SourceSprite | `UPaperSprite *` |  |
| MaterialOverride_DEPRECATED | `UMaterialInterface *` |  |
| SpriteColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

## Functions

### SetSprite

Change the PaperSprite used by this instance.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewSprite | `UPaperSprite *` |  |

**Return**

- Type: 
- Description: _None_

### GetSprite

Gets the PaperSprite used by this instance.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetSpriteColor

Set color of the sprite

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
