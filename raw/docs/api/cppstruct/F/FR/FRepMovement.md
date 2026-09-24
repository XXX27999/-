# FRepMovement

Replicated movement data of our RootComponent.
   Struct used for efficient replication as velocity and location are generally replicated together (this saves a repindex)
   and velocity.Z is commonly zero (most position replications are for walking pawns).

## Fields

| Name | Type | Description |
| --- | --- | --- |
| LinearVelocity | [FVector](../FV/FVector.md) |  |
| AngularVelocity | [FVector](../FV/FVector.md) |  |
| Location | [FVector](../FV/FVector.md) |  |
| Rotation | [FRotator](./FRotator.md) |  |
| bSimulatedPhysicSleep | `uint8` | If set, RootComponent should be sleeping. |
| bRepPhysics | `uint8` | If set, additional physic data (angular velocity) will be replicated. |
| bPredictionLocation | `uint8` | If set, Location should be autonomous proxy prediction location |
| LocationQuantizationLevel | [EVectorQuantization](../../../cppenum/E/EV/EVectorQuantization.md) | Allows tuning the compression level for the replicated location vector. You should only need to change this from the default if you see visual artifacts. |
| VelocityQuantizationLevel | [EVectorQuantization](../../../cppenum/E/EV/EVectorQuantization.md) | Allows tuning the compression level for the replicated velocity vectors. You should only need to change this from the default if you see visual artifacts. |
| RotationQuantizationLevel | [ERotatorQuantization](../../../cppenum/E/ER/ERotatorQuantization.md) | Allows tuning the compression level for replicated rotation. You should only need to change this from the default if you see visual artifacts. |
