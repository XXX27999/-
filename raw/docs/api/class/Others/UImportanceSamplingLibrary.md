# UImportanceSamplingLibrary

## Parents

- UBlueprintFunctionLibrary

## Variables

_None_

## Functions

### RandomSobolFloat

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Index | `int32` | - Which sequential point |
| Dimension | `int32` | - Which Sobol dimension (0 to 15) |
| Seed | `float` | - Random seed (in the range 0-1) to randomize across multiple sequences |

**Return**

- Type: 
- Description: _None_

### NextSobolFloat

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Index | `int32` | - Which sequential point |
| Dimension | `int32` | - Which Sobol dimension (0 to 15) |
| PreviousValue | `float` | - The Sobol value for Index-1 |

**Return**

- Type: 
- Description: _None_

### RandomSobolCell2D

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Index | `int32` | - Which sequential point in the cell (starting at 0) |
| NumCells | `int32` | - Size of cell grid, 1 to 32768. Rounded up to the next power of two |
| Cell | `FVector2D` | - Give a point from this integer grid cell |
| Seed | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | - Random 2D seed (components in the range 0-1) to randomize across multiple sequences |

**Return**

- Type: 
- Description: _None_

### NextSobolCell2D

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Index | `int32` | - Which sequential point |
| NumCells | `int32` | - Size of cell grid, 1 to 32768. Rounded up to the next power of two |
| PreviousValue | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | - The Sobol value for Index-1 |

**Return**

- Type: 
- Description: _None_

### RandomSobolCell3D

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Index | `int32` | - Which sequential point in the cell (starting at 0) |
| NumCells | `int32` | - Size of cell grid, 1 to 1024. Rounded up to the next power of two |
| Cell | `FVector` | - Give a point from this integer grid cell |
| Seed | [FVector](../../cppstruct/F/FV/FVector.md) | - Random 3D seed (components in the range 0-1) to randomize across multiple sequences |

**Return**

- Type: 
- Description: _None_

### NextSobolCell3D

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Index | `int32` | - Which sequential point |
| NumCells | `int32` | - Size of cell grid, 1 to 1024. Rounded up to the next power of two |
| PreviousValue | [FVector](../../cppstruct/F/FV/FVector.md) | - The Sobol value for Index-1 |

**Return**

- Type: 
- Description: _None_

### MakeImportanceTexture

Create an FImportanceTexture object for texture-driven importance sampling from a 2D RGBA8 texture

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Texture | `UTexture2D *` | - Texture object to use. Must be RGBA8 format. |
| WeightingFunc | `TEnumAsByte < EImportanceWeight :: Type >` | - How to turn the texture data into probability weights |

**Return**

- Type: 
- Description: _None_

### BreakImportanceTexture

Get texture used to create an ImportanceTexture object

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ImportanceTexture | `FImportanceTexture &` | - The source ImportanceTexture object |
| Texture | `UTexture2D * &` |  |
| WeightingFunc | `TEnumAsByte < EImportanceWeight :: Type > &` | - How to turn the texture data into probability weights |

**Return**

- Type: 
- Description: _None_

### ImportanceSample

Distribute sample points proportional to Texture2D luminance.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Texture | `FImportanceTexture &` |  |
| Rand | `FVector2D &` | - Random 2D point with components evenly distributed between 0 and 1 |
| Samples | `int` | - Total number of samples that will be used |
| Intensity | `float` | - Total intensity for light |
| SamplePosition | `FVector2D &` |  |
| SampleColor | `FLinearColor &` |  |
| SampleIntensity | `float &` |  |
| SampleSize | `float &` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
