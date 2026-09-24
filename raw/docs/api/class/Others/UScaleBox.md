# UScaleBox

Allows you to place content with a desired size and have it scale to meet the constraints placed on this box's alloted area.  If
  you needed to have a background image scale to fill an area but not become distorted with different aspect ratios, or if you need
  to auto fit some text to an area, this is the control for you.

   Single Child
   Aspect Ratio

## Parents

- [UContentWidget](./UContentWidget.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Stretch | `TEnumAsByte < EStretch :: Type >` | The stretching rule to apply when content is stretched |
| StretchDirection | `TEnumAsByte < EStretchDirection :: Type >` | Controls in what direction content can be scaled |
| UserSpecifiedScale | `float` | Optional scale that can be specified by the User. Used only for UserSpecified stretching. |
| UserSpecifiedScaleBias | `float` | Scale bias that can fit to the content, especially for the text exceeded the bounds.<br>	 #if UMG_SCALE_BIAS |
| IgnoreInheritedScale | `bool` | Optional bool to ignore the inherited scale. Applies inverse scaling to counteract parents before applying the local scale operation. |
| UsePcParams | `bool` |  |
| StretchPc | `TEnumAsByte < EStretch :: Type >` |  |
| StretchDirectionPc | `TEnumAsByte < EStretchDirection :: Type >` |  |
| UserSpecifiedScalePc | `float` |  |
| UserSpecifiedScaleBiasPc | `float` |  |
| IgnoreInheritedScalePc | `bool` |  |
| bSingleLayoutPass | `bool` | Only perform a single layout pass, if you do this, it can save a considerable<br>	  amount of time, however, some things like text may not look correct.  You may also<br>	  see the UI judder between frames.  This generally is caused by not explicitly<br>	  sizing the widget, and instead allowing it to layout based on desired size along<br>	  which won't work in Single Layout Pass mode. |
| bFroceSlateLayoutCachingCalcSize | `bool` |  |
| bForceUseLastUnPrepassChildSize | `bool` |  |

## Functions

### SetStretch

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InStretch | `EStretch :: Type` |  |

**Return**

- Type: 
- Description: _None_

### SetStretchDirection

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InStretchDirection | `EStretchDirection :: Type` |  |

**Return**

- Type: 
- Description: _None_

### SetUserSpecifiedScale

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InUserSpecifiedScale | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetIgnoreInheritedScale

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInIgnoreInheritedScale | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetUserSpecifiedScaleBias

#if UMG_SCALEBOX_BIAS

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InUserSpecifiedScaleBias | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetPcParamController

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InValue | `int32` |  |

**Return**

- Type: 
- Description: _None_

### OnUIRectOffsetChange

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
