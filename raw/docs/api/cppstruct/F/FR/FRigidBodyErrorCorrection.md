# FRigidBodyErrorCorrection

Rigid body error correction data

## Fields

| Name | Type | Description |
| --- | --- | --- |
| LinearDeltaThresholdSq | `float` | max squared position difference to perform velocity adjustment |
| LinearInterpAlpha | `float` | strength of snapping to desired linear velocity |
| LinearRecipFixTime | `float` | inverted duration after which linear velocity adjustment will fix error |
| AngularDeltaThreshold | `float` | max squared angle difference (in radians) to perform velocity adjustment |
| AngularInterpAlpha | `float` | strength of snapping to desired angular velocity |
| AngularRecipFixTime | `float` | inverted duration after which angular velocity adjustment will fix error |
| BodySpeedThresholdSq | `float` | min squared body speed to perform velocity adjustment |
