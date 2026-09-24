# UGCMathUtility

数学工具接口库

## Parents

_None_

## Variables

_None_

## Functions

### Sin

返回A的正弦值(sin)，结果为弧度制

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `number` | A |

**Return**

- Type: 
- Description: _None_

### Asin

返回A的反正弦值(arcsin)，结果为弧度制

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `number` | A |

**Return**

- Type: 
- Description: _None_

### Cos

返回A的余弦值(cos)，结果为弧度制

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `number` | A |

**Return**

- Type: 
- Description: _None_

### Acos

返回A的反余弦值(arccos)，结果为弧度制

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `number` | A |

**Return**

- Type: 
- Description: _None_

### Tan

返回A的正切值(tan)，结果为弧度制

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `number` | A |

**Return**

- Type: 
- Description: _None_

### Atan

返回A的反正切值(arctan)，结果为弧度制

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `number` | A |

**Return**

- Type: 
- Description: _None_

### DegSin

返回A的正弦值(sin)，结果为角度制

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `number` | A |

**Return**

- Type: 
- Description: _None_

### DegAsin

返回A的反正弦值(arcsin)，结果为角度制

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `number` | A |

**Return**

- Type: 
- Description: _None_

### DegCos

返回A的余弦值(cos)，结果为角度制

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `number` | A |

**Return**

- Type: 
- Description: _None_

### DegAcos

返回A的反余弦值(arccos)，结果为角度制

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `number` | A |

**Return**

- Type: 
- Description: _None_

### DegTan

返回A的正切值(tan)，结果为角度制

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `number` | A |

**Return**

- Type: 
- Description: _None_

### DegAtan

返回A的反正切值(arctan)，结果为角度制

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `number` | A |

**Return**

- Type: 
- Description: _None_

### DegAtan2

返回A/B的反正切值(atan2)，结果为角度制

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `number` | A |
| B | `number` | B |

**Return**

- Type: 
- Description: _None_

### RandomFloat

返回一个介于0和1之间的随机浮点数

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### RandomFloatInRange

生成一个介于Min和Max之间的随机数

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InMin | `number` | 最小值 |
| InMax | `number` | 最大值 |

**Return**

- Type: 
- Description: _None_

### Lerp

根据Alpha在A和B之间线性插值（Alpha=0时返回A，Alpha=1时返回B））

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `number` | A |
| B | `number` | B |
| Alpha | `number` | Alpha |

**Return**

- Type: 
- Description: _None_

### FClamp

【废弃】请使用 UGCMathUtility.Clamp
返回限制在A和B之间的值（包含A和B）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InValue | `number` | 值 |
| InMin | `number` | 最小值 |
| InMax | `number` | 最大值 |

**Return**

- Type: 
- Description: _None_

### MapRangeClamped

将数值从一个输入范围映射到另一个输出范围（数值会被限制在输入范围内）。（例如：将0.5从0→1范围映射到0→50范围会得到25）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InValue | `number` | 值 |
| InMinIn | `number` | 输入范围最小值 |
| InMaxIn | `number` | 输入范围最大值 |
| InMinOut | `number` | 输出范围最小值 |
| InMaxOut | `number` | 输出范围最大值 |

**Return**

- Type: 
- Description: _None_

### NearlyEqualFloat

返回A是否近似等于B（|A - B| < 误差容限）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `number` | A |
| B | `number` | B |
| Tolerance | `number` | 误差容限 |

**Return**

- Type: 
- Description: _None_

### NotEqualFloat

如果A不等于B则返回true

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `number` | A |
| B | `number` | B |

**Return**

- Type: 
- Description: _None_

### Now

返回当前计算机的本地日期和时间

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Today

返回当前计算机的本地日期

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### UtcNow

返回当前计算机的UTC日期和时间

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetYear

返回A的年分量值

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FDateTime` | A |

**Return**

- Type: 
- Description: _None_

### GetMonth

返回A的月分量值

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FDateTime` | A |

**Return**

- Type: 
- Description: _None_

### DaysInMonth

返回给定年份和月份的天数

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Year | `number` | 年份 |
| Month | `number` | 月份 |

**Return**

- Type: 
- Description: _None_

### AddVector

向量加法

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FVector](../../cppstruct/F/FV/FVector.md) | A |
| B | [FVector](../../cppstruct/F/FV/FVector.md) | B |

**Return**

- Type: 
- Description: _None_

### AddVector2D

返回二维向量A和二维向量B的和（A + B）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | A |
| B | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | B |

**Return**

- Type: 
- Description: _None_

### SubtractVector

向量减法

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FVector](../../cppstruct/F/FV/FVector.md) | A |
| B | [FVector](../../cppstruct/F/FV/FVector.md) | B |

**Return**

- Type: 
- Description: _None_

### SubtractVector2D

返回二维向量A和二维向量B的差（A - B）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | A |
| B | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | B |

**Return**

- Type: 
- Description: _None_

### MultiplyVector

将向量A按B缩放

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FVector](../../cppstruct/F/FV/FVector.md) | A |
| B | `number` | B |

**Return**

- Type: 
- Description: _None_

### MultiplyVector2D

将二维向量A按B缩放

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | A |
| B | `number` | B |

**Return**

- Type: 
- Description: _None_

### VSize

返回向量的长度

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FVector](../../cppstruct/F/FV/FVector.md) | A |

**Return**

- Type: 
- Description: _None_

### VSize2D

返回二维向量的长度

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | A |

**Return**

- Type: 
- Description: _None_

### VSizeSquared

返回向量的长度的平方

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FVector](../../cppstruct/F/FV/FVector.md) | A |

**Return**

- Type: 
- Description: _None_

### VSizeSquared2D

返回二维向量的长度的平方

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | A |

**Return**

- Type: 
- Description: _None_

### EqualVector

判断向量A是否在允许误差范围内等于向量B

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FVector](../../cppstruct/F/FV/FVector.md) | A |
| B | [FVector](../../cppstruct/F/FV/FVector.md) | B |
| Tolerance | `number` | 允许误差，默认为1.e-4f |

**Return**

- Type: 
- Description: _None_

### NotEqualVector

判断向量A是否在允许误差范围内不等于向量B

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FVector](../../cppstruct/F/FV/FVector.md) | A |
| B | [FVector](../../cppstruct/F/FV/FVector.md) | B |
| Tolerance | `number` | 允许误差，默认为1.e-4f |

**Return**

- Type: 
- Description: _None_

### DotVector

返回两个向量的点积

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FVector](../../cppstruct/F/FV/FVector.md) | A |
| B | [FVector](../../cppstruct/F/FV/FVector.md) | B |

**Return**

- Type: 
- Description: _None_

### CrossVector

返回两个向量的叉积

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FVector](../../cppstruct/F/FV/FVector.md) | A |
| B | [FVector](../../cppstruct/F/FV/FVector.md) | B |

**Return**

- Type: 
- Description: _None_

### DotVector2D

返回两个二维向量的点积

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | A |
| B | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | B |

**Return**

- Type: 
- Description: _None_

### CrossVector2D

返回两个二维向量的叉积

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | A |
| B | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | B |

**Return**

- Type: 
- Description: _None_

### RotateVector

返回向量A经过 Rotator B 旋转后的结果

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FVector](../../cppstruct/F/FV/FVector.md) | A |
| B | [FRotator](../../cppstruct/F/FR/FRotator.md) | B |

**Return**

- Type: 
- Description: _None_

### RotateAngleAxis

返回向量A绕Axis轴旋转AngleDeg角度后的结果

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FVector](../../cppstruct/F/FV/FVector.md) | A |
| AngleDeg | `number` | AngleDeg |
| Axis | [FVector](../../cppstruct/F/FV/FVector.md) | Axis |

**Return**

- Type: 
- Description: _None_

### Normal

返回向量A的单位法向量

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FVector](../../cppstruct/F/FV/FVector.md) | A |

**Return**

- Type: 
- Description: _None_

### Normal2D

返回二维向量A的单位法向量

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | A |

**Return**

- Type: 
- Description: _None_

### VLerp

根据Alpha值在向量A和向量B之间线性插值（Alpha=0时返回100%A，Alpha=1时返回100%B）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FVector](../../cppstruct/F/FV/FVector.md) | A |
| B | [FVector](../../cppstruct/F/FV/FVector.md) | B |
| Alpha | `number` | Alpha |

**Return**

- Type: 
- Description: _None_

### RandomUnitVector

返回一个长度为1的随机向量

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### RandomPointInBoundingBox

返回指定边界框内的随机点

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Origin | [FVector](../../cppstruct/F/FV/FVector.md) | Origin |
| BoxExtent | [FVector](../../cppstruct/F/FV/FVector.md) | BoxExtent |

**Return**

- Type: 
- Description: _None_

### ProjectVectorOnToVector

将向量V投影到目标向量Target上并返回投影向量，如果Target长度接近零，则返回零向量

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| V | [FVector](../../cppstruct/F/FV/FVector.md) | V |
| Target | [FVector](../../cppstruct/F/FV/FVector.md) | Target |

**Return**

- Type: 
- Description: _None_

### FInterpTo

根据当前值到目标值的插值进行平滑过渡，实现流畅的过度效果

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Current | `number` | 当前值 |
| Target | `number` | 目标值 |
| DeltaTime | `number` | 平滑时间 |
| InterpSpeed | `number` | 插值速度 |

**Return**

- Type: 
- Description: _None_

### FInterpConstantTo

以恒定速率向目标值变换

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Current | `number` | 当前值 |
| Target | `number` | 目标值 |
| DeltaTime | `number` | 平滑时间 |
| InterpSpeed | `number` | 插值速度 |

**Return**

- Type: 
- Description: _None_

### VInterpTo

根据向量表示的当前位置与目标位置的距离平滑地接近目标位置，实现流畅的追踪效果

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Current | [FVector](../../cppstruct/F/FV/FVector.md) | 当前位置 |
| Target | [FVector](../../cppstruct/F/FV/FVector.md) | 目标位置 |
| DeltaTime | `number` | 平滑时间 |
| InterpSpeed | `number` | 插值速度 |

**Return**

- Type: 
- Description: _None_

### VInterpConstantTo

以恒定速率向向量表示的目标位置移动

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Current | [FVector](../../cppstruct/F/FV/FVector.md) | 当前位置 |
| Target | [FVector](../../cppstruct/F/FV/FVector.md) | 目标位置 |
| DeltaTime | `number` | 平滑时间 |
| InterpSpeed | `number` | 插值速度 |

**Return**

- Type: 
- Description: _None_

### Vector2DInterpTo

根据二维向量表示的当前位置与目标位置的距离平滑地接近目标位置，实现流畅的追踪效果

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Current | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | 当前位置 |
| Target | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | 目标位置 |
| DeltaTime | `number` | 平滑时间 |
| InterpSpeed | `number` | 插值速度 |

**Return**

- Type: 
- Description: _None_

### Vector2DInterpConstantTo

以恒定速率向二维向量表示的目标位置移动

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Current | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | 当前位置 |
| Target | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | 目标位置 |
| DeltaTime | `number` | 平滑时间 |
| InterpSpeed | `number` | 插值速度 |

**Return**

- Type: 
- Description: _None_

### RInterpTo

根据当前旋转角度平滑过渡到目标旋转角度，实现流畅的旋转效果

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Current | [FRotator](../../cppstruct/F/FR/FRotator.md) | 当前旋转角度 |
| Target | [FRotator](../../cppstruct/F/FR/FRotator.md) | 目标旋转角度 |
| DeltaTime | `number` | 平滑时间 |
| InterpSpeed | `number` | 插值速度 |

**Return**

- Type: 
- Description: _None_

### RInterpConstantTo

以恒定速率向目标旋转角度旋转

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Current | [FRotator](../../cppstruct/F/FR/FRotator.md) | 当前旋转角度 |
| Target | [FRotator](../../cppstruct/F/FR/FRotator.md) | 目标旋转角度 |
| DeltaTime | `number` | 平滑时间 |
| InterpSpeed | `number` | 插值速度 |

**Return**

- Type: 
- Description: _None_

### FindClosestPointOnSegment

查找线段上距离给定点最近的点

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Point | [FVector](../../cppstruct/F/FV/FVector.md) | 需要计算最近点的目标点 |
| SegmentStart | [FVector](../../cppstruct/F/FV/FVector.md) | 线段起点 |
| SegmentEnd | [FVector](../../cppstruct/F/FV/FVector.md) | 线段终点 |

**Return**

- Type: 
- Description: _None_

### FindClosestPointOnLine

找到无限长直线上距离给定点最近的点

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Point | [FVector](../../cppstruct/F/FV/FVector.md) | 需要计算最近点的目标点 |
| LineOrigin | [FVector](../../cppstruct/F/FV/FVector.md) | 直线上的参考点 |
| LineDirection | [FVector](../../cppstruct/F/FV/FVector.md) | 直线上的方向向量(无需归一化) |

**Return**

- Type: 
- Description: _None_

### GetPointDistanceToSegment

计算点到线段的最短距离

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Point | [FVector](../../cppstruct/F/FV/FVector.md) | 需要计算最近点的目标点 |
| SegmentStart | [FVector](../../cppstruct/F/FV/FVector.md) | 线段起点 |
| SegmentEnd | [FVector](../../cppstruct/F/FV/FVector.md) | 线段终点 |

**Return**

- Type: 
- Description: _None_

### GetPointDistanceToLine

计算点到无限长直线的最短距离

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Point | [FVector](../../cppstruct/F/FV/FVector.md) | 需要计算距离的目标 |
| LineOrigin | [FVector](../../cppstruct/F/FV/FVector.md) | 直线上的参考点 |
| LineDirection | [FVector](../../cppstruct/F/FV/FVector.md) | 直线上的方向向量(无需归一化) |

**Return**

- Type: 
- Description: _None_

### ProjectVectorOnToPlane

将向量投影到由法向量定义的平面上

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| V | [FVector](../../cppstruct/F/FV/FVector.md) | 需要投影的向量 |
| PlaneNormal | [FVector](../../cppstruct/F/FV/FVector.md) | 法向量 |

**Return**

- Type: 
- Description: _None_

### NegateVector

向量取反

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| V | [FVector](../../cppstruct/F/FV/FVector.md) | 需要取反的向量 |

**Return**

- Type: 
- Description: _None_

### ClampVectorSize

将向量长度限制在最小值和最大值之间

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| V | [FVector](../../cppstruct/F/FV/FVector.md) | 需要限制长度的向量 |
| Min | `number` | 最小长度 |
| Max | `number` | 最大长度 |

**Return**

- Type: 
- Description: _None_

### GetMinElement

找出向量中(X, Y或Z)的最小分量

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| V | [FVector](../../cppstruct/F/FV/FVector.md) | 需要计算最小分量的向量 |

**Return**

- Type: 
- Description: _None_

### GetMaxElement

找出向量中(X, Y或Z)的最大分量

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| V | [FVector](../../cppstruct/F/FV/FVector.md) | 需要计算最大分量的向量 |

**Return**

- Type: 
- Description: _None_

### GetDirectionUnitVector

计算从一个位置指向另一个位置的单位方向向量

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| From | [FVector](../../cppstruct/F/FV/FVector.md) | 起点 |
| To | [FVector](../../cppstruct/F/FV/FVector.md) | 终点 |

**Return**

- Type: 
- Description: _None_

### EqualName

如果A和B相等则返回true (A == B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `string` | A |
| B | `string` | B |

**Return**

- Type: 
- Description: _None_

### NotEqualName

如果A和B不相等则返回true (A ~= B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `string` | A |
| B | `string` | B |

**Return**

- Type: 
- Description: _None_

### MakeBox

通过最小点和最大点创建一个FBox，并将IsValid设为true

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Min | [FVector](../../cppstruct/F/FV/FVector.md) | 最小点 |
| Max | [FVector](../../cppstruct/F/FV/FVector.md) | 最大点 |

**Return**

- Type: 
- Description: _None_

### MakeBox2D

通过最小点和最大点创建一个FBox2D，并将IsValid设为true

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Min | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | 最小点 |
| Max | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | 最大点 |

**Return**

- Type: 
- Description: _None_

### MakeVector

创建一个向量 {X, Y, Z}

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| X | `number` | X |
| Y | `number` | Y |
| Z | `number` | Z |

**Return**

- Type: 
- Description: _None_

### BreakVector

将向量分解为X、Y和Z分量

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| V | [FVector](../../cppstruct/F/FV/FVector.md) | 向量 |

**Return**

- Type: 
- Description: _None_

### MakeVector2D

创建一个二维向量 {X, Y}

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| X | `number` | X |
| Y | `number` | Y |

**Return**

- Type: 
- Description: _None_

### BreakVector2D

将二维向量分解为X和Y分量

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| V | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | 向量 |

**Return**

- Type: 
- Description: _None_

### GetForwardVector

按给定旋转角度旋转世界前向向量

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InRot | [FRotator](../../cppstruct/F/FR/FRotator.md) | 旋转角度 |

**Return**

- Type: 
- Description: _None_

### GetRightVector

按给定旋转角度旋转世界右向量

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InRot | [FRotator](../../cppstruct/F/FR/FRotator.md) | 旋转角度 |

**Return**

- Type: 
- Description: _None_

### GetUpVector

按给定旋转角度旋转世界上向量

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InRot | [FRotator](../../cppstruct/F/FR/FRotator.md) | 旋转角度 |

**Return**

- Type: 
- Description: _None_

### GetYawPitchFromVector

将向量分解为Yaw(偏航角)和Pitch(俯仰角)旋转值(角度制，不限制范围)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| V | [FVector](../../cppstruct/F/FV/FVector.md) | 向量 |

**Return**

- Type: 
- Description: _None_

### MakeRotator

使用以度数为单位提供的旋转值创建旋转器{Roll, Pitch, Yaw}

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Roll | `number` | Roll |
| Pitch | `number` | Pitch |
| Yaw | `number` | Yaw |

**Return**

- Type: 
- Description: _None_

### FindLookAtRotation

查找一个物体在起始位置指向目标位置所需的旋转角度

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Start | [FVector](../../cppstruct/F/FV/FVector.md) | 起始位置 |
| Target | [FVector](../../cppstruct/F/FV/FVector.md) | 目标位置 |

**Return**

- Type: 
- Description: _None_

### MakeRotFromX

仅使用X轴构建Rotator。Y和Z轴未指定但将保持正交归一。X轴无需归一化

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| XAxis | [FVector](../../cppstruct/F/FV/FVector.md) | X轴 |

**Return**

- Type: 
- Description: _None_

### MakeRotFromY

仅使用Y轴构建Rotator。X和Z轴未指定但将保持正交归一。Y轴无需归一化

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| YAxis | [FVector](../../cppstruct/F/FV/FVector.md) | Y轴 |

**Return**

- Type: 
- Description: _None_

### MakeRotFromZ

仅使用Z轴构建Rotator。X和Y轴未指定但将保持正交归一。Z轴无需归一化

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ZAxis | [FVector](../../cppstruct/F/FV/FVector.md) | Z轴 |

**Return**

- Type: 
- Description: _None_

### MakeRotFromXY

使用给定的X和Y轴构建矩阵。X轴保持不变，Y轴会微调以确保正交性。Z轴将被计算得出。输入向量无需归一化

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| XAxis | [FVector](../../cppstruct/F/FV/FVector.md) | X轴 |
| YAxis | [FVector](../../cppstruct/F/FV/FVector.md) | Y轴 |

**Return**

- Type: 
- Description: _None_

### MakeRotFromXZ

使用给定的X和Z轴构建矩阵。X轴保持不变，Z轴会微调以确保正交性。Y轴将被计算得出。输入向量无需归一化

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| XAxis | [FVector](../../cppstruct/F/FV/FVector.md) | X轴 |
| ZAxis | [FVector](../../cppstruct/F/FV/FVector.md) | Z轴 |

**Return**

- Type: 
- Description: _None_

### MakeRotFromYX

使用给定的Y和X轴构建矩阵。Y轴保持不变，X轴会微调以确保正交性。Z轴将被计算得出。输入向量无需归一化

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| YAxis | [FVector](../../cppstruct/F/FV/FVector.md) | Y轴 |
| XAxis | [FVector](../../cppstruct/F/FV/FVector.md) | X轴 |

**Return**

- Type: 
- Description: _None_

### MakeRotFromYZ

使用给定的Y和Z轴构建矩阵。Y轴保持不变，Z轴会微调以确保正交性。X轴将被计算得出。输入向量无需归一化

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| YAxis | [FVector](../../cppstruct/F/FV/FVector.md) | Y轴 |
| ZAxis | [FVector](../../cppstruct/F/FV/FVector.md) | Z轴 |

**Return**

- Type: 
- Description: _None_

### MakeRotFromZX

使用给定的Z和X轴构建矩阵。Z轴保持不变，X轴会微调以确保正交性。Y轴将被计算得出。输入向量无需归一化

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ZAxis | [FVector](../../cppstruct/F/FV/FVector.md) | Z轴 |
| XAxis | [FVector](../../cppstruct/F/FV/FVector.md) | X轴 |

**Return**

- Type: 
- Description: _None_

### MakeRotFromZY

使用给定的Z和Y轴构建矩阵。Z轴保持不变，Y轴会微调以确保正交性。X轴将被计算得出。输入向量无需归一化

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ZAxis | [FVector](../../cppstruct/F/FV/FVector.md) | Z轴 |
| YAxis | [FVector](../../cppstruct/F/FV/FVector.md) | Y轴 |

**Return**

- Type: 
- Description: _None_

### BreakRotator

将Rotator分解为{Roll, Pitch, Yaw}角度值(单位:度)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Rotator | [FRotator](../../cppstruct/F/FR/FRotator.md) | Rotator |

**Return**

- Type: 
- Description: _None_

### MakeTransform

根据位置、旋转和缩放创建Transform

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Location | [FVector](../../cppstruct/F/FV/FVector.md) | 位置 |
| Rotation | [FRotator](../../cppstruct/F/FR/FRotator.md) | 旋转 |
| Scale | [FVector](../../cppstruct/F/FV/FVector.md) | 缩放 |

**Return**

- Type: 
- Description: _None_

### BreakTransform

将transform分解为{Location, Rotation, Scale}值

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Transform | [FTransform](../../cppstruct/F/FT/FTransform.md) | Transform |

**Return**

- Type: 
- Description: _None_

### Conv_VectorToLinearColor

将向量转换为LinearColor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vector | [FVector](../../cppstruct/F/FV/FVector.md) | 向量 |

**Return**

- Type: 
- Description: _None_

### Conv_ColorToLinearColor

将Color转换为LinearColor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Color | [FColor](../../cppstruct/F/FC/FColor.md) | Color |

**Return**

- Type: 
- Description: _None_

### Conv_LinearColorToColor

将LinearColor转换为Color

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| LinearColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | LinearColor |

**Return**

- Type: 
- Description: _None_

### Conv_VectorToVector2D

将向量转换为二维向量

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vector | [FVector](../../cppstruct/F/FV/FVector.md) | 向量 |

**Return**

- Type: 
- Description: _None_

### Conv_Vector2DToVector

将二维向量转换为向量

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vector2D | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | 二维向量 |

**Return**

- Type: 
- Description: _None_

### HSVToRGB

根据HSV分量创建颜色

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| H | `number` | 色相 |
| S | `number` | 饱和度 |
| V | `number` | 明度 |
| A | `number` | 透明度 |

**Return**

- Type: 
- Description: _None_

### RGBToHSV

将颜色分解为单独的HSV分量（以及透明度）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Color | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | Color |

**Return**

- Type: 
- Description: _None_

### Conv_HSVToRGB

将HSV线性颜色转换为RGB颜色（其中H在R分量，S在G分量，V在B分量）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| HSV | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | HSV |

**Return**

- Type: 
- Description: _None_

### Conv_RGBToHSV

将RGB线性颜色转换为HSV（其中H存储在R分量，S存储在G分量，V存储在B分量）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| RGB | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | RGB |

**Return**

- Type: 
- Description: _None_

### HexToRGB

将十六进制颜色字符串转换为RGB

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| HexString | `string` | 十六进制颜色字符串 |
| bSRGB | `boolean` | 是否使用sRGB颜色空间 |

**Return**

- Type: 
- Description: _None_

### RGBToHex

将RGB颜色转换为十六进制字符串

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| RGB | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | RGB |
| bSRGB | `boolean` | 是否使用sRGB颜色空间 |

**Return**

- Type: 
- Description: _None_

### Conv_VectorToRotator

创建一个使X轴朝向指定方向向量的Rotator

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| XAxis | [FVector](../../cppstruct/F/FV/FVector.md) | X轴 |

**Return**

- Type: 
- Description: _None_

### Conv_RotatorToVector

获取旋转后的X轴方向向量

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Rotator | [FRotator](../../cppstruct/F/FR/FRotator.md) | Rotator |

**Return**

- Type: 
- Description: _None_

### TransformLocation

使用指定的变换矩阵转换位置坐标
例如：若T是某物体的变换矩阵，此操作会将局部坐标系的位置转换到世界坐标系

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| T | [FTransform](../../cppstruct/F/FT/FTransform.md) | 变换矩阵 |
| Location | [FVector](../../cppstruct/F/FV/FVector.md) | 局部坐标系下的位置 |

**Return**

- Type: 
- Description: _None_

### TransformDirection

使用指定的变换矩阵转换方向向量 - 不会改变向量长度
例如：若T是某物体的变换矩阵，此操作会将局部坐标系的方向向量转换到世界坐标系

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| T | [FTransform](../../cppstruct/F/FT/FTransform.md) | 变换矩阵 |
| Direction | [FVector](../../cppstruct/F/FV/FVector.md) | 局部坐标系下的方向向量 |

**Return**

- Type: 
- Description: _None_

### TransformRotation

使用指定的变换矩阵转换Rotator
例如：若T是某物体的变换矩阵，此操作会将局部坐标系的旋转转换到世界坐标系

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| T | [FTransform](../../cppstruct/F/FT/FTransform.md) | 变换矩阵 |
| Rotation | [FRotator](../../cppstruct/F/FR/FRotator.md) | 局部坐标系下的旋转 |

**Return**

- Type: 
- Description: _None_

### RandomBool

随机返回 true 或 false，概率各占 50%

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### RandomBoolWithWeight

根据指定权重获取随机概率结果。权重范围为 0.0 - 1.0
例如：权重 = 0.6，返回值将有 60% 的概率为 True

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Weight | `number` | 权重 |

**Return**

- Type: 
- Description: _None_

### RandomInteger

返回一个随机数，范围在0到Max - 1之间，每个数出现的概率相同

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Max | `number` | 最大值 |

**Return**

- Type: 
- Description: _None_

### Clamp

返回限制在A和B之间的值(包含A和B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `number` | 值 |
| Min | `number` | 最小值 |
| Max | `number` | 最大值 |

**Return**

- Type: 
- Description: _None_

### RandomIntegerInRange

返回Min和Max之间的随机整数(包含Min和Max)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Min | `number` | 最小值 |
| Max | `number` | 最大值 |

**Return**

- Type: 
- Description: _None_

### IsPointInBox

判断给定点是否在盒子内（包括在盒子边界上的点）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Point | [FVector](../../cppstruct/F/FV/FVector.md) | 要测试的点 |
| BoxOrigin | [FVector](../../cppstruct/F/FV/FVector.md) | 盒子的原点 |
| BoxExtent | [FVector](../../cppstruct/F/FV/FVector.md) | 盒子在各个轴上的范围（从原点出发的距离） |

**Return**

- Type: 
- Description: _None_

### IsPointInBoxWithTransform

判断给定点是否在具有特定变换的盒子内（包含边界点)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Point | [FVector](../../cppstruct/F/FV/FVector.md) | 要测试的点 |
| BoxWorldTransform | [FTransform](../../cppstruct/F/FT/FTransform.md) | 盒子从组件空间到世界空间的变换 |
| BoxExtent | [FVector](../../cppstruct/F/FV/FVector.md) | 盒子在组件空间中的范围（各轴距原点的距离） |

**Return**

- Type: 
- Description: _None_

### EqualRotator

检查Rotator A 和 B 是否在指定误差范围内相等 (A == B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FRotator](../../cppstruct/F/FR/FRotator.md) | 旋转量A |
| B | [FRotator](../../cppstruct/F/FR/FRotator.md) | 旋转量B |
| ErrorTolerance | `number` | 误差范围 |

**Return**

- Type: 
- Description: _None_

### NotEqualRotator

检查Rotator A 和 B 是否在指定误差范围内不相等 (A != B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FRotator](../../cppstruct/F/FR/FRotator.md) | 旋转量A |
| B | [FRotator](../../cppstruct/F/FR/FRotator.md) | 旋转量B |
| ErrorTolerance | `number` | 误差范围 |

**Return**

- Type: 
- Description: _None_

### ComposeRotators

组合两个旋转，返回先应用A再应用B的结果旋转

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FRotator](../../cppstruct/F/FR/FRotator.md) | 旋转量A |
| B | [FRotator](../../cppstruct/F/FR/FRotator.md) | 旋转量B |

**Return**

- Type: 
- Description: _None_

### GetAxes

获取该旋转对应的前向、右向和上向三个基准方向向量

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Rotator | [FRotator](../../cppstruct/F/FR/FRotator.md) | 旋转量 |

**Return**

- Type: 
- Description: _None_

### NormalRotator

标准化Rotator

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FRotator](../../cppstruct/F/FR/FRotator.md) | 旋转量 |

**Return**

- Type: 
- Description: _None_

### RandomRotator

生成一个随机旋转角度，可选择是否包含绕Z轴的随机旋转

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bRoll | `boolean` | 是否包含绕Z轴的随机旋转 |

**Return**

- Type: 
- Description: _None_

### RLerp

基于Alpha值在A和B之间线性插值（Alpha=0时返回100%A，Alpha=1时返回100%B）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FRotator](../../cppstruct/F/FR/FRotator.md) | 起始旋转量 |
| B | [FRotator](../../cppstruct/F/FR/FRotator.md) | 目标旋转量 |
| Alpha | `number` | 插值比例（0-1） |
| bShortestPath | `boolean` | 是否采用最短路径插值 |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua
