# FEmitterDynamicParameter

Helper structure for displaying the parameter.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| ParamName | `FName` | The parameter name - from the material DynamicParameter expression. READ-ONLY |
| bUseEmitterTime | `uint32` | If true, use the EmitterTime to retrieve the value, otherwise use Particle RelativeTime. |
| bSpawnTimeOnly | `uint32` | If true, only set the value at spawn time of the particle, otherwise update each frame. |
| ValueMethod | `TEnumAsByte < enum EEmitterDynamicParameterValue >` | Where to get the parameter value from. |
| bScaleVelocityByParamValue | `uint32` | If true, scale the velocity value selected in ValueMethod by the evaluated ParamValue. |
| ParamValue | [FRawDistributionFloat](../FR/FRawDistributionFloat.md) | The distriubtion for the parameter value. |
