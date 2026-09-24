# FAnimNode_QuadrupedTerrainAdapting

## Fields

| Name | Type | Description |
| --- | --- | --- |
| bEnable | `bool` |  |
| bDrawDebug | `bool` |  |
| RayTrace_SphereRadius | `float` |  |
| RayTrace_MaxGroundAngle | `float` |  |
| RayTrace_LHandBottom | [FBoneSocketTarget](../FB/FBoneSocketTarget.md) |  |
| RayTrace_RHandBottom | [FBoneSocketTarget](../FB/FBoneSocketTarget.md) |  |
| RayTrace_LFootBottom | [FBoneSocketTarget](../FB/FBoneSocketTarget.md) |  |
| RayTrace_RFootBottom | [FBoneSocketTarget](../FB/FBoneSocketTarget.md) |  |
| bActorAdjustRotationFloor | `bool` |  |
| bEnableSlopeAdapting | `bool` |  |
| bResetSlopeAdaptingOnSkipCal | `bool` |  |
| bEaseSlopeAdaptingOnDisable | `bool` |  |
| bEnableLionDanceSlopeAdapting | `bool` |  |
| bEnableUpdateChildrenComps | `bool` |  |
| UpdateChildrenCompsFrequency | `int32` |  |
| SlopeAdapting_Pelvis | `FBoneReference` |  |
| SlopeAdapting_Pelvis1 | `FBoneReference` |  |
| SlopeAdapting_Pelvis2 | `FBoneReference` |  |
| SlopeAdapting_LClavicle | `FBoneReference` |  |
| SlopeAdapting_RClavicle | `FBoneReference` |  |
| SlopeAdapting_LThigh | `FBoneReference` |  |
| SlopeAdapting_RThigh | `FBoneReference` |  |
| SlopeAdapting_Root | `FBoneReference` |  |
| TraceDownLength | `float` |  |
| SlopeAdapting_PelvisLimitHeight | `float` |  |
| SlopeAdapting_LimitSlopeAngle | `float` |  |
| SlopeAdapting_PositionLerpSpeed | `float` |  |
| SlopeAdapting_RotationLerpSpeed | `float` |  |
| SlopeAdapting_BehindLegModifyFactor | `float` |  |
| BoneToFlooroffset | `float` |  |
| bEnableLegAdapting | `bool` |  |
| LegAdapting_IKLerpSpeed | `float` |  |
| LegAdapting_IKMaxHeight | `float` |  |
| LegAdapting_LHand | [FAnimNode_TwoBoneIK](./FAnimNode_TwoBoneIK.md) |  |
| LegAdapting_RHand | [FAnimNode_TwoBoneIK](./FAnimNode_TwoBoneIK.md) |  |
| LegAdapting_LFoot | [FAnimNode_TwoBoneIK](./FAnimNode_TwoBoneIK.md) |  |
| LegAdapting_RFoot | [FAnimNode_TwoBoneIK](./FAnimNode_TwoBoneIK.md) |  |
| fSlopeAdaptOffset | `float` |  |
| bApplySlopeAdaptingPelvisPositiontNoMove | `bool` | ApplySlopeAdapting的时候，是否不调整盆骨的高度（调试用：只走旋转、不做几何补偿，<br>	 用于对比验证旋转方案在不做位置补偿时的效果） |
| SlopeAdaptingMode | [ESlopeAdaptingMode](../../../cppenum/E/ES/ESlopeAdaptingMode.md) | 斜坡适配方案选择。默认 Legacy 走原逻辑，与现有四足资产完全兼容。<br>	 选 CapsuleCenterRotation_LongLegShortLeg 时走新方案AB（绕胶囊中心整体旋转的等价实现）。<br>	 选 CapsuleCenterRotation_LongLeg的话，推荐开启EnableLegAdapting |
| bAutoCalculateLegLength | `bool` | 仅方案A使用：是否自动从骨架默认姿态计算腿长（取 max(前腿平均, 后腿平均)）。<br>	 自动模式下首次计算后会缓存。关闭后使用下面 SlopeAdapting_LegLengthForCompensation 手填值。 |
| SlopeAdapting_LegLengthForCompensation | `float` | 仅方案A使用：手填腿长（仅当 bAutoCalculateLegLength=false 时生效）。<br>	 用于补偿 4 腿反向 Roll 后产生的脚浮空：ΔZ = -L  (1 - cos(α))。 |
| bEnableRollAdapting | `bool` | 仅方案AB使用：是否启用绕 ActorForward 轴的 Roll 适配（左右侧坡度）。<br>	 默认关闭：仅做 Pitch（前后坡度）。启用后会额外计算并叠加左右侧坡的 Roll 旋转。 |
| bClampHorizontalDelta | `bool` | 是否钳制水平方向位移（方案AB）。默认关闭：水平位移是几何正确的，不应被截断。<br>	 仅在调试或特殊场景下打开，限制水平位移幅度。 |
| SlopeAdapting_HorizontalDeltaLimit | `float` | 仅当 bClampHorizontalDelta=true 时生效：水平位移钳制上限（cm）。 |
| bEnableLionDanceLegAdapting | `bool` |  |
| bEnableFootAdapting | `bool` |  |
| FootAdapting_LHand | `FBoneReference` |  |
| FootAdapting_RHand | `FBoneReference` |  |
| FootAdapting_LFoot | `FBoneReference` |  |
| FootAdapting_RFoot | `FBoneReference` |  |
| FootAdapting_LimitRotation | [FRotator](../FR/FRotator.md) |  |
| FootAdapting_RotationLerpSpeed | `float` |  |
