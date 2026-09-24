# UMediaTexture

Implements a texture asset for rendering video tracks from UMediaPlayer assets.

## Parents

- [UTexture](./UTexture.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| AddressX | `TEnumAsByte < TextureAddress >` | The addressing mode to use for the X axis. |
| AddressY | `TEnumAsByte < TextureAddress >` | The addressing mode to use for the Y axis. |
| AutoClear | `bool` | Whether to clear the texture when no media is being played (default = enabled). |
| ClearColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | The color used to clear the texture if AutoClear is enabled (default = black). |
| MediaPlayer | `UMediaPlayer *` | The media player asset associated with this texture. |

## Functions

### GetAspectRatio

Gets the current aspect ratio of the texture.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetHeight

Gets the current height of the texture.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetWidth

Gets the current width of the texture.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ResetFirstFrame

Reset The IsFirstFrameRender&IsFirstFrameNotify to false for iOS

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
