# UFont

A font object, for use by Slate, UMG, and Canvas.

  A font can either be:
     Runtime cached - The font contains a series of TTF files that combine to form a composite font. The glyphs are cached on demand when required at runtime.
     Offline cached - The font contains a series of textures containing pre-baked cached glyphs and their associated texture coordinates.

## Parents

- [UObject](./UObject.md)
- IFontProviderInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| FontCacheType | [EFontCacheType](../../cppenum/E/EF/EFontCacheType.md) | What kind of font caching should we use? This controls which options we see |
| Characters | `TArray < FFontCharacter >` | List of characters in the font.  For a MultiFont, this will include all characters in all sub-fonts!  Thus,<br>		the number of characters in this array isn't necessary the number of characters available in the font |
| Textures | `TArray < UTexture2D * >` | Textures that store this font's glyph image data |
| IsRemapped | `int32` | True if font is 'remapped'.  That is, the character array is not a direct mapping to unicode values.  Instead,<br>		all characters are indexed indirectly through the CharRemap array |
| EmScale | `float` | Font metrics. |
| Ascent | `float` | @todo document |
| Descent | `float` | @todo document |
| Leading | `float` | @todo document |
| Kerning | `int32` | Default horizontal spacing between characters when rendering text with this font |
| ImportOptions | [FFontImportOptionsData](../../cppstruct/F/FF/FFontImportOptionsData.md) | Options used when importing this font |
| NumCharacters | `int32` | Number of characters in the font, not including multiple instances of the same character (for multi-fonts).<br>		This is cached at load-time or creation time, and is never serialized. |
| MaxCharHeight | `TArray < int32 >` | The maximum height of a character in this font.  For multi-fonts, this array will contain a maximum<br>		cached at load-time or creation time, and is never serialized. |
| ScalingFactor | `float` | Scale to apply to the font. |
| LegacyFontSize | `int32` | The default size of the font used for legacy Canvas APIs that don't specify a font size |
| LegacyFontName | `FName` | The default font name to use for legacy Canvas APIs that don't specify a font name |
| CompositeFont | [FCompositeFont](../../cppstruct/F/FC/FCompositeFont.md) | Embedded composite font data |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
