# UGCMiscFunctionSystem

游戏杂项函数接口库

## Parents

_None_

## Variables

_None_

## Functions

### StartAirRoute

开始航线飞行
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldObjectContext | [UObject](../../Others/UObject.md) | 世界上下文对象 |

**Return**

_None_

### StartAirDrop

【废弃】请使用 UGCAirDropManagerSystem
开始空投
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldObjectContext | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| Index | `number` | 定时普通空投设置中的配置序号（AirDropConfigsUGC） |
| AirDropType | [EAirDropType](../../../cppenum/E/EA/EAirDropType.md) | 空投箱空投类型一般为 EAirDropType.AirDrop_NormalAirDrop |

**Return**

_None_

### StartNormalAirDrop

【废弃】请使用 UGCAirDropManagerSystem
自定义空投
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldObjectContext | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| StartPos | `Vector2D` | 飞机起始点,结构：{X=x,Y=y} |
| DropPos | `Vector2D` | 飞机结束点，结构：{X=x,Y=y} |
| Distance | `number` | 空投点距离起始点的比例 （0-1）的一个范围，0=StartPos，1=DropPos |
| AirDropType | [EAirDropType](../../../cppenum/E/EA/EAirDropType.md) | 空投箱空投类型一般为EAirDropType.AirDrop_NormalAirDrop |

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua
