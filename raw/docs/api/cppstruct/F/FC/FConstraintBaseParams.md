# FConstraintBaseParams

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Stiffness | `float` | Stiffness of the soft constraint. Only used when Soft Constraint is on. |
| Damping | `float` | Damping of the soft constraint. Only used when Soft Constraint is on. |
| Restitution | `float` | Controls the amount of bounce when the constraint is violated. A restitution value of 1 will bounce back with the same velocity the limit was hit. A value of 0 will stop dead. |
| ContactDistance | `float` | Determines how close to the limit we have to get before turning the joint on. Larger value will be more expensive, but will do a better job not violating constraints. A smaller value will be more efficient, but easier to violate. |
| bSoftConstraint | `uint8` | Whether we want to use a soft constraint (spring). |
