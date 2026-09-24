# FFoliageVertexColorChannelMask

## Fields

| Name | Type | Description |
| --- | --- | --- |
| UseMask | `uint32` | When checked, foliage will be masked from this mesh using this color channel |
| MaskThreshold | `float` | Specifies the threshold value above which the static mesh vertex color value must be, in order for foliage instances to be placed in a specific area |
| InvertMask | `uint32` | When unchecked, foliage instances will be placed only when the vertex color in the specified channel(s) is above the threshold amount.<br>	   When checked, the vertex color must be less than the threshold amount |
