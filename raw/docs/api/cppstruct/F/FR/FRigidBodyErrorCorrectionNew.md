# FRigidBodyErrorCorrectionNew

Rigid body error correction data

## Fields

| Name | Type | Description |
| --- | --- | --- |
| PingExtrapolation | `float` | Value between 0 and 1 which indicates how much velocity<br>		and ping based correction to use |
| PingLimit | `float` | For the purpose of extrapolation, ping will be clamped to this value |
| ErrorPerLinearDifference | `float` | Error per centimeter |
| ErrorPerAngularDifference | `float` | Error per degree |
| MaxRestoredStateError | `float` | Maximum allowable error for a state to be considered "resolved" |
| MaxLinearHardSnapDistance | `float` |  |
| PositionLerp | `float` | How much to directly lerp to the correct position. Generally<br>		increase precision along with jerkiness. |
| AngleLerp | `float` | How much to directly lerp to the correct angle. |
| LinearVelocityCoefficient | `float` | This is the coefficient `k` in the differential equation:<br>		the velocity in a replication step. |
| AngularVelocityCoefficient | `float` | This is the angular analog to LinearVelocityCoefficient. |
| ErrorAccumulationSeconds | `float` | Number of seconds to remain in a heuristically<br>		unresolveable state before hard snapping. |
| ErrorAccumulationDistanceSq | `float` | If the body has moved less than the square root of<br>		frame, then error may accumulate towards a hard snap. |
| ErrorAccumulationSimilarity | `float` | If the previous error projected onto the current error<br>		hard snap. |
