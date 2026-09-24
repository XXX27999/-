# UGCEMPZoneSystem

电磁干扰区接口库

## Parents

_None_

## Variables

_None_

## Functions

### GenerateElectromagneticArea

生成电磁干扰区
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ConfigID | `number` | 电磁干扰区配置 ID |
| Location | [FVector](../../cppstruct/F/FV/FVector.md) | 电磁干扰区中心坐标 |

**Return**

- Type: 
- Description: _None_

### DestroyElectromagneticArea

取消电磁干扰区
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstanceID | `number` | 电磁干扰区实例 ID |

**Return**

- Type: 
- Description: _None_

### ModifyConfigElectromagneticArea

修改电磁干扰区参数
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ConfigID | `number` | 电磁干扰区配置 ID |
| ParameterType | `string` | 参数类型 |
| NewValue | `number` | 新的参数值 |

**Return**

- Type: 
- Description: _None_

### GetAllConfigElectromagneticArea

查看当前全部电磁干扰区
生效范围：服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetSpecifyElectromagneticAreaList

查看指定电磁干扰区参数
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstanceID | `number` | 电磁干扰区实例 ID |

**Return**

- Type: 
- Description: _None_

### GetEMPZoneManager

获取电磁干扰区管理器
获取电磁干扰区全局管理器实例，用于绑定电磁干扰区相关事件
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
