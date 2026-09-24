# UFontFace

A font face asset contains the raw payload data for a source TTFOTF file as used by FreeType.
  During cook this asset type generates a ".ufont" file containing the raw payload data (unless loaded "Inline").

## Parents

- [UObject](./UObject.md)
- IFontFaceInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| SourceFilename | `FString` | The filename of the font face we were created from. This may not always exist on disk, as we may have previously loaded and cached the font data inside this asset. |
| Hinting | [EFontHinting](../../cppenum/E/EF/EFontHinting.md) | The hinting algorithm to use with the font face. |
| LoadingPolicy | [EFontLoadingPolicy](../../cppenum/E/EF/EFontLoadingPolicy.md) | Enum controlling how this font face should be loaded at runtime. See the enum for more explanations of the options. |
| LayoutMethod | [EFontLayoutMethod](../../cppenum/E/EF/EFontLayoutMethod.md) | Which method should we use when laying out the font? Try changing this if you notice clipping or height issues with your font. |
| FontFaceData_DEPRECATED | `TArray < uint8 >` | The data associated with the font face. This should always be filled in providing the source filename is valid. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
