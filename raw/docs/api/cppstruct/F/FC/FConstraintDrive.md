# FConstraintDrive

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Stiffness | `float` | The spring strength of the drive. Force proportional to the position error. |
| Damping | `float` | The damping strength of the drive. Force proportional to the velocity error. |
| MaxForce | `float` | The force limit of the drive. |
| bEnablePositionDrive | `uint8` | EnablesDisables position drive (orientation if using angular drive) |
| bEnableVelocityDrive | `uint8` | EnablesDisables velocity drive (angular velocity if using angular drive) |
