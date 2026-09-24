# UBillboardComponent

A 2d texture that will be rendered always facing the camera.

## Parents

- [UPrimitiveComponent](./UPrimitiveComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Sprite | `UTexture2D *` |  |
| bIsScreenSizeScaled | `uint32` |  |
| ScreenSize | `float` |  |
| U | `float` |  |
| UL | `float` |  |
| V | `float` |  |
| VL | `float` |  |
| SpriteCategoryName_DEPRECATED | `FName` | Sprite category that the component belongs to. Value serves as a key into the localization file. |
| SpriteInfo | [FSpriteCategoryInfo](../../cppstruct/F/FS/FSpriteCategoryInfo.md) | Sprite category information regarding the component |
| bUseInEditorScaling | `bool` | Whether to use in-editor arrow scaling (i.e. to be affected by the global arrow scale) |

## Functions

### SetSprite

Change the sprite texture used by this component

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewSprite | `UTexture2D *` |  |

**Return**

- Type: 
- Description: _None_

### SetUV

Change the sprite's UVs

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewU | `int32` |  |
| NewUL | `int32` |  |
| NewV | `int32` |  |
| NewVL | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetSpriteAndUV

Change the sprite texture and the UV's used by this component

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewSprite | `UTexture2D *` |  |
| NewU | `int32` |  |
| NewUL | `int32` |  |
| NewV | `int32` |  |
| NewVL | `int32` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
