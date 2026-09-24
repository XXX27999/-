# UAnimCompress

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Description | `FString` | Name of Compression Scheme used for this asset |
| bNeedsSkeleton | `uint32` | Compression algorithms requiring a skeleton should set this value to true. |
| TranslationCompressionFormat | `TEnumAsByte < AnimationCompressionFormat >` | Format for bitwise compression of translation data. |
| RotationCompressionFormat | `TEnumAsByte < AnimationCompressionFormat >` | Format for bitwise compression of rotation data. |
| ScaleCompressionFormat | `TEnumAsByte < AnimationCompressionFormat >` | Format for bitwise compression of scale data. |
| MaxCurveError | `float` | Max error for compression of curves using remove redundant keys |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
