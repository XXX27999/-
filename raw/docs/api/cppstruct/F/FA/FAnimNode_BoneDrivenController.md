# FAnimNode_BoneDrivenController

This is the runtime version of a bone driven controller, which maps part of the state from one bone to another (e.g., 2  source.x -> target.z)

## Fields

| Name | Type | Description |
| --- | --- | --- |
| SourceBone | `FBoneReference` |  |
| SourceComponent | `TEnumAsByte < EComponentType :: Type >` |  |
| DrivingCurve | `UCurveFloat *` | Curve used to map from the source attribute to the driven attributes if present (otherwise the Multiplier will be used) |
| Multiplier | `float` |  |
| bUseRange | `bool` |  |
| RangeMin | `float` |  |
| RangeMax | `float` |  |
| RemappedMin | `float` |  |
| RemappedMax | `float` |  |
| DestinationMode | [EDrivenDestinationMode](../../../cppenum/E/ED/EDrivenDestinationMode.md) |  |
| ParameterName | `FName` | Name of Morph Target to drive using the source attribute |
| TargetBone | `FBoneReference` |  |
| TargetComponent_DEPRECATED | `TEnumAsByte < EComponentType :: Type >` |  |
| bAffectTargetTranslationX | `uint32` |  |
| bAffectTargetTranslationY | `uint32` |  |
| bAffectTargetTranslationZ | `uint32` |  |
| bAffectTargetRotationX | `uint32` |  |
| bAffectTargetRotationY | `uint32` |  |
| bAffectTargetRotationZ | `uint32` |  |
| bAffectTargetScaleX | `uint32` |  |
| bAffectTargetScaleY | `uint32` |  |
| bAffectTargetScaleZ | `uint32` |  |
| ModificationMode | [EDrivenBoneModificationMode](../../../cppenum/E/ED/EDrivenBoneModificationMode.md) |  |
