# UGCDebugSystem

调试系统接口库

## Parents

_None_

## Variables

_None_

## Functions

### PrintToScreen

屏幕左上角逐行打印字符串
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InString | `string` | 要打印的字符串 |
| Color | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| Duration | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

**Return**

_None_

### FlushOnScreenDebugMessages

清除屏幕上持续时间未过的字符串
生效范围：客户端

**Parameters**

_None_

**Return**

_None_

### DrawDebugLine

绘制直线
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| LineStart | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| LineEnd | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| Color | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| Duration | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

**Return**

_None_

### DrawDebugPoint

绘制点
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Position | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| Size | `number` | 点的大小 |
| Color | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| Duration | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

**Return**

_None_

### DrawDebugArrow

绘制箭头
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| LineStart | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| LineEnd | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| Color | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| Duration | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

**Return**

_None_

### DrawDebugCircle

绘制圆
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Center | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| Radius | `number` | 圆的半径 |
| Color | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| Duration | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |
| YAxis | [FVector](../../../cppstruct/F/FV/FVector.md) | 椭圆半长轴方向向量，模长影响缩放; 缺省为{X=0,Y=1,Z=0}; 结构Vector={X=0,Y=0,Z=0} |
| ZAxis | [FVector](../../../cppstruct/F/FV/FVector.md) | 椭圆半短轴方向向量，模长影响缩放; 缺省为{X=0,Y=0,Z=1}; 结构Vector={X=0,Y=0,Z=0} |
| bDrawAxis | `boolean` | 缺省为0 |

**Return**

_None_

### DrawDebugCoordinateSystem

绘制坐标系
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AxisLoc | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| AxisRot | [FRotator](../../../cppstruct/F/FR/FRotator.md) | 结构Rot={Pitch=0,Yaw=0,Roll=0} |
| Scale | `number` | 坐标轴长度; 缺省为100 |
| Duration | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

**Return**

_None_

### DrawDebugBox

绘制盒子
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Center | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| Extent | [FVector](../../../cppstruct/F/FV/FVector.md) | 表示盒子中心到各面的距离; 结构Vector={X=0,Y=0,Z=0} |
| Rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | 结构Rot={Pitch=0,Yaw=0,Roll=0} |
| Color | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| Duration | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

**Return**

_None_

### DrawDebugSphere

绘制球体
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Center | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| Radius | `number` | 球的半径 |
| Color | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| Duration | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

**Return**

_None_

### DrawDebugCylinder

绘制圆柱体
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| Radius | `number` | 底面半径 |
| Color | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| Duration | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

**Return**

_None_

### DrawDebugCapsule

绘制胶囊
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Center | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| HalfHeight | `number` | 胶囊半高 |
| Radius | `number` | 截面圆半径 |
| Rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | 结构Rot={Pitch=0,Yaw=0,Roll=0}; |
| Color | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| Duration | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

**Return**

_None_

### DrawDebugString

绘制文本
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TextLocation | [FVector](../../../cppstruct/F/FV/FVector.md) | 未绑定Actor时为世界坐标，绑定Actor时为相对Actor的坐标; 结构Vector={X=0,Y=0,Z=0} |
| Text | `string` | 显示的文本 |
| TestBaseActor | [AActor](../../Others/AActor.md) | 绑定在哪个Actor上 |
| Color | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| Duration | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

**Return**

_None_

### FlushDebugStrings

清空场景中持续时间未过的调试文本（不包括UI）
生效范围：客户端

**Parameters**

_None_

**Return**

_None_

### FlushDebugLines

清空场景中持续时间未过的调试图形
生效范围：客户端

**Parameters**

_None_

**Return**

_None_

### DrawDebugActorName

绘制Actor名称
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | [AActor](../../Others/AActor.md) | 目标Actor |
| Offset | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| Color | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| Duration | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

**Return**

_None_

### DrawDebugActorMoveTrack

绘制Actor运动轨迹
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | [AActor](../../Others/AActor.md) | 目标Actor |
| Color | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| Duration | `number` | 缺省为0，此时运动轨迹将持续保留 |

**Return**

_None_

### DrawDebugDistance

绘制Self到Target的连线和距离数值
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Self | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| Target | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| Color | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| Duration | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

**Return**

_None_

### DrawDebugTargetAimedAt

绘制准心瞄准物体名称
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Length | `number` | 生效距离，缺省为10000 |
| Duration | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

**Return**

_None_

### DrawDebugLineTraceSingle

绘制射线与第一处命中标记
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| Color | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| Duration | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

**Return**

_None_

### DrawDebugLineTraceMulti

绘制射线与全部命中标记
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| Color | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| Duration | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

**Return**

_None_

### DrawDebugSphereTraceSingle

绘制沿射线运动的球体轨迹与第一处命中标记
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| Radius | `number` | 球体半径 |
| Color | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| Duration | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

**Return**

_None_

### DrawDebugSphereTraceMulti

绘制沿射线运动的球体轨迹与全部命中标记
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| Radius | `number` | 球体半径 |
| Color | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| Duration | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

**Return**

_None_

### DrawDebugBoxTraceSingle

绘制沿射线运动的方盒轨迹与第一处命中标记
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| HalfSize | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| Orientation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | 结构Rot={Pitch=0,Yaw=0,Roll=0} |
| Duration | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

**Return**

_None_

### DrawDebugBoxTraceMulti

绘制沿射线运动的方盒轨迹与全部命中标记
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| HalfSize | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| Orientation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | 结构Rot={Pitch=0,Yaw=0,Roll=0} |
| Duration | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

**Return**

_None_

### DrawDebugCapsuleTraceSingle

绘制沿射线运动的胶囊轨迹与第一处命中标记
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| Radius | `number` | 胶囊截面圆半径 |
| HalfSize | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| Duration | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

**Return**

_None_

### DrawDebugCapsuleTraceMulti

绘制沿射线运动的胶囊轨迹与全部命中标记
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| Radius | `number` | 胶囊截面圆半径 |
| HalfSize | [FVector](../../../cppstruct/F/FV/FVector.md) | 结构Vector={X=0,Y=0,Z=0} |
| Duration | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

**Return**

_None_

### DrawDebugActorCollision

绘制碰撞盒
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | [AActor](../../Others/AActor.md) | 目标Actor |
| Color | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| Duration | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

**Return**

_None_

### DrawDebugActorBounds

绘制包围盒
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | [AActor](../../Others/AActor.md) | 目标Actor |
| Color | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| Duration | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua
