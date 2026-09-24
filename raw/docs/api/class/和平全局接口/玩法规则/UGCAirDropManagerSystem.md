# UGCAirDropManagerSystem

空投系统接口库

## Parents

_None_

## Variables

_None_

## Functions

### GenerateAirDrop

生成指定ID空投
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ID | `number` | 空投配置ID |
| DroppingLocation | [FVector](../../../cppstruct/F/FV/FVector.md) | 掉落位置 结构Vector={X=0,Y=0,Z=0} |
| DroppingSpeed | `number` | 掉落速度 |

**Return**

- Type: 
- Description: _None_

### GetAllAirDropConfigs

获得所有空投配置
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ID | `number` | 空投配置ID |

**Return**

- Type: 
- Description: _None_

### DestroyAirDrop

销毁指定实例ID空投
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InsID | `number` | 指定实例ID的空投 0.1s 后销毁 |

**Return**

- Type: 
- Description: _None_

### GetAirDropItemList

获取指定实例ID空投的物品列表
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InsID | `number` | 空投实例InsID |

**Return**

- Type: 
- Description: _None_

### GetAllAirDropInstanceIDs

获取当前场景内所有的实例ID
生效范围：服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua
