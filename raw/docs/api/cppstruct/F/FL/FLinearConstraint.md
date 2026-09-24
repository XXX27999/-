# FLinearConstraint

Distance constraint

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Limit | `float` | The distance allowed between between the two joint reference frames. Distance applies on all axes enabled (one axis means line, two axes implies circle, three axes implies sphere) |
| XMotion | `TEnumAsByte < enum ELinearConstraintMotion >` | Indicates the linear constraint applied along the X-axis. Free implies no constraint at all. Locked implies no movement along X is allowed. Limited implies the distance in the joint along all active axes must be less than the Distance provided. |
| YMotion | `TEnumAsByte < enum ELinearConstraintMotion >` | Indicates the linear constraint applied along the Y-axis. Free implies no constraint at all. Locked implies no movement along Y is allowed. Limited implies the distance in the joint along all active axes must be less than the Distance provided. |
| ZMotion | `TEnumAsByte < enum ELinearConstraintMotion >` | Indicates the linear constraint applied along theZX-axis. Free implies no constraint at all. Locked implies no movement along Z is allowed. Limited implies the distance in the joint along all active axes must be less than the Distance provided. |
