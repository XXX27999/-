# FUGCDamageNumberParams

自定义伤害数字参数

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Items | `TArray < FUGCCustomDamageNumberItemParams >` | 显示单元列表 |
| TimeLife | `float` | 显示时间 |
| MoveTimeLife | `float` | 飞行时间 |
| DrawColor | [FLinearColor](../FL/FLinearColor.md) | 数字的颜色 |
| DrawOutlineColor | [FLinearColor](../FL/FLinearColor.md) | 数字的描边颜色 |
| DrawOutlineSize | `float` | 数字的描边大小 |
| FadeInTime | `float` | 淡入时间 |
| FadeOutTime | `float` | 淡出时间 |
| SizeScaleRange | [FVector2D](../FV/FVector2D.md) | 初始尺寸缩放范围 |
| MoveScaleRange | [FVector2D](../FV/FVector2D.md) | 移动距离缩放范围 |
| OriginPositionRangeX | [FVector2D](../FV/FVector2D.md) | 初始位置水平偏移范围 |
| OriginPositionRangeY | [FVector2D](../FV/FVector2D.md) | 初始位置垂直偏移范围 |
| MoveDirection | [FVector2D](../FV/FVector2D.md) | 飞行角度范围，范围-180到180 |
| bFollowTarget | `bool` | 是否跟随目标 |
