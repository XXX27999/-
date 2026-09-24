# UGCAirAttachSystem

轰炸区接口库

## Parents

_None_

## Variables

_None_

## Functions

### GenerateBombingArea

生成轰炸区
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ConfigID | `number` | 轰炸配置 ID |
| Location | [FVector](../../cppstruct/F/FV/FVector.md) | 轰炸中心坐标（系统会自动通过射线检测将炸弹位置修正到地面高度） |

**Return**

- Type: 
- Description: _None_

### StopBombingArea

停止轰炸区
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstanceID | `number` | 轰炸实例 ID |

**Return**

- Type: 
- Description: _None_

### ModifyBombingAreaConfig

修改轰炸区参数
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ConfigID | `number` | 轰炸配置 ID |
| ParameterType | `string` | 参数类型（如："AttackAreaRadius", "EscapeTime", "AttackLastingTime"等） |
| NewValue | `number` | 新的参数值 |

**Return**

- Type: 
- Description: _None_

### GetAllConfigBombingArea

查看当前全部轰炸区
生效范围：服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetSpecifyBombingAreaList

查看指定轰炸区参数
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstanceID | `number` | 轰炸实例 ID |

**Return**

- Type: 
- Description: _None_

### GetAirAttackManager

获取轰炸区管理器
生效范围：服务器&客户端

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
