# FSimSpaceSettings

Settings for the system which passes motion of the simulation's space into the simulation. This allows the simulation to pass a
  fraction of the world space motion onto the bodies which allows Bone-Space and Component-Space simulations to react to world-space
  movement in a controllable way.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| MasterAlpha | `float` |  |
| VelocityScaleZ | `float` |  |
| MaxLinearVelocity | `float` |  |
| MaxAngularVelocity | `float` |  |
| MaxLinearAcceleration | `float` |  |
| MaxAngularAcceleration | `float` |  |
| ExternalLinearDrag_DEPRECATED | `float` |  |
| ExternalLinearDragV | [FVector](../FV/FVector.md) |  |
| ExternalLinearVelocity | [FVector](../FV/FVector.md) |  |
| ExternalAngularVelocity | [FVector](../FV/FVector.md) |  |
