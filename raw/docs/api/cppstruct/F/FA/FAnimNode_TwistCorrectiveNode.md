# FAnimNode_TwistCorrectiveNode

This is the node that apply corrective morphtarget for twist
  Good example is that if you twist your neck too far right or left, you're going to see odd stretch shape of neck,
  This node can detect the angle and apply morphtarget curve
  This isn't the twist control node for bone twist

## Fields

| Name | Type | Description |
| --- | --- | --- |
| BaseFrame | [FReferenceBoneFrame](../FR/FReferenceBoneFrame.md) | Base Frame of the reference for the twist node |
| TwistFrame | [FReferenceBoneFrame](../FR/FReferenceBoneFrame.md) |  |
| TwistPlaneNormalAxis | `FAxis` | Normal of the Plane that we'd like to calculate angle calculation from in BaseFrame. Please note we're looking for Normal Axis |
| RangeMax | `float` |  |
| RemappedMin | `float` |  |
| RemappedMax | `float` |  |
| Curve | `FAnimCurveParam` |  |
