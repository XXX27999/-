# UImage

The image widget allows you to display a Slate Brush, or texture or material in the UI.

   No Children

## Parents

- [UWidget](./UWidget.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| BrushImage | `TSoftObjectPtr < UObject >` |  |
| bIsEnhancedImage | `bool` |  |
| ForceAsyncLoadReference | `bool` |  |
| BrushAssetReference | `FStringAssetReference` |  |
| Brush | [FSlateBrush](../../cppstruct/F/FS/FSlateBrush.md) | Image to draw |
| BrushMaterialParamNames | `FString` |  |
| BrushDelegate | `FGetSlateBrush` | A bindable delegate for the Image. |
| ColorAndOpacity | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | Color and opacity |
| ColorAndOpacityDelegate | `FGetLinearColor` | A bindable delegate for the ColorAndOpacity. |
| bIsUseEnhancedHitTest | `bool` | 是否使用自定义触摸响应区域，在运行时修改无效 |
| HitTestAreaRadius | `float` | 圆形响应区域的半径，最大为控件边长一半，-1为控件大小一半 |
| OnMouseButtonDownEvent | `FOnPointerEvent` |  |

## Functions

### GetBrush

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetColorAndOpacity

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InColorAndOpacity | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_

### SetColorRGBStr

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| HexString | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### SetBrushImageReference

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AssetReference | `FStringAssetReference` |  |

**Return**

- Type: 
- Description: _None_

### SetBrushImageReferenceWithMatchSize

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AssetReference | `FStringAssetReference` |  |
| bMatchSize | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetBrushImageReferenceWithColor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AssetReference | `FStringAssetReference` |  |
| Color | `FLinearColor` |  |
| bMatchSize | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetOpacity

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InOpacity | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetBrush

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBrush | `FSlateBrush &` |  |

**Return**

- Type: 
- Description: _None_

### SetBrushFromAsset

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Asset | `USlateBrushAsset *` |  |

**Return**

- Type: 
- Description: _None_

### SetBrushFromTexture

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Texture | `UTexture2D *` |  |
| bMatchSize | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetBrushFromTextureDynamic

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Texture | `UTexture2DDynamic *` |  |
| bMatchSize | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetBrushFromMaterial

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Material | `UMaterialInterface *` |  |

**Return**

- Type: 
- Description: _None_

### GetDynamicMaterial

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetDisablePaint

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InDisablePaint | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ReleaseAsyncSetBrushHandle

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnAsyncLoadImageAssetComplete

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnAsyncLoadAssetComplete

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnImageChangeDelegate |  |  |

## Language

cpp
