# FFontImportOptionsData

Font import options

## Fields

| Name | Type | Description |
| --- | --- | --- |
| FontName | `FString` | Name of the typeface for the font to import |
| Height | `float` | Height of font (point size) |
| bEnableAntialiasing | `uint32` | Whether the font should be antialiased or not.  Usually you should leave this enabled. |
| bEnableBold | `uint32` | Whether the font should be generated in bold or not |
| bEnableItalic | `uint32` | Whether the font should be generated in italics or not |
| bEnableUnderline | `uint32` | Whether the font should be generated with an underline or not |
| bAlphaOnly | `uint32` | if true then forces PF_G8 and only maintains Alpha value and discards color |
| CharacterSet | `TEnumAsByte < enum EFontImportCharacterSet >` | Character set for this font |
| Chars | `FString` | Explicit list of characters to include in the font |
| UnicodeRange | `FString` | Range of Unicode character values to include in the font.  You can specify ranges using hyphens andor commas (e.g. '400-900') |
| CharsFilePath | `FString` | Path on disk to a folder where files that contain a list of characters to include in the font |
| CharsFileWildcard | `FString` | File mask wildcard that specifies which files within the CharsFilePath to scan for characters in include in the font |
| bCreatePrintableOnly | `uint32` | Skips generation of glyphs for any characters that are not considered 'printable' |
| bIncludeASCIIRange | `uint32` | When specifying a range of characters and this is enabled, forces ASCII characters (0 thru 255) to be included as well |
| ForegroundColor | [FLinearColor](../FL/FLinearColor.md) | Color of the foreground font pixels.  Usually you should leave this white and instead use the UI Styles editor to change the color of the font on the fly |
| bEnableDropShadow | `uint32` | Enables a very simple, 1-pixel, black colored drop shadow for the generated font |
| TexturePageWidth | `int32` | Horizontal size of each texture page for this font in pixels |
| TexturePageMaxHeight | `int32` | The maximum vertical size of a texture page for this font in pixels.  The actual height of a texture page may be less than this if the font can fit within a smaller sized texture page. |
| XPadding | `int32` | Horizontal padding between each font character on the texture page in pixels |
| YPadding | `int32` | Vertical padding between each font character on the texture page in pixels |
| ExtendBoxTop | `int32` | How much to extend the top of the UV coordinate rectangle for each character in pixels |
| ExtendBoxBottom | `int32` | How much to extend the bottom of the UV coordinate rectangle for each character in pixels |
| ExtendBoxRight | `int32` | How much to extend the right of the UV coordinate rectangle for each character in pixels |
| ExtendBoxLeft | `int32` | How much to extend the left of the UV coordinate rectangle for each character in pixels |
| bEnableLegacyMode | `uint32` | Enables legacy font import mode.  This results in lower quality antialiasing and larger glyph bounds, but may be useful when debugging problems |
| Kerning | `int32` | The initial horizontal spacing adjustment between rendered characters.  This setting will be copied directly into the generated Font object's properties. |
| bUseDistanceFieldAlpha | `uint32` | If true then the alpha channel of the font textures will store a distance field instead of a color mask |
| DistanceFieldScaleFactor | `int32` | Scale factor determines how big to scale the font bitmap during import when generating distance field values<br>	 Note that higher values give better quality but importing will take much longer. |
| DistanceFieldScanRadiusScale | `float` | Shrinks or expands the scan radius used to determine the silhouette of the font edges. |
