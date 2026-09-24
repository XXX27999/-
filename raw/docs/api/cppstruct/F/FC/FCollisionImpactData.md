# FCollisionImpactData

Information about an overall collision, including contacts.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| ContactInfos | `TArray < FRigidBodyContactInfo >` | all the contact points in the collision |
| TotalNormalImpulse | [FVector](../FV/FVector.md) | the total impulse applied as the two objects push against each other |
| TotalFrictionImpulse | [FVector](../FV/FVector.md) | the total counterimpulse applied of the two objects sliding against each other |
