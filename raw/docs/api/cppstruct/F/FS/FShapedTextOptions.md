# FShapedTextOptions

Common data for all widgets that use shaped text.
  Contains the common options that should be exposed for the underlying Slate widget.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| bOverride_TextShapingMethod | `uint32` |  |
| bOverride_TextFlowDirection | `uint32` |  |
| TextShapingMethod | [ETextShapingMethod](../../../cppenum/E/ET/ETextShapingMethod.md) | Which text shaping method should the text within this widget use? (unset to use the default returned by GetDefaultTextShapingMethod) |
| TextFlowDirection | [ETextFlowDirection](../../../cppenum/E/ET/ETextFlowDirection.md) | Which text flow direction should the text within this widget use? (unset to use the default returned by GetDefaultTextFlowDirection) |
