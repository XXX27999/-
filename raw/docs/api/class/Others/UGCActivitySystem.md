# UGCActivitySystem

活动系统库（需要启用活动GamePart）

## Parents

_None_

## Variables

| Name | Type | Description |
| --- | --- | --- |
| UGCActivitySystem.OnActivityInfoReadyDelegate |  | 活动信息准备好时触发的委托<br>生效范围：客户端&&服务器 |
| UGCActivitySystem.OnUpdateValidActivityIDsDelegate |  | 更新有效活动时触发的委托<br>活动系统会按照每个活动配置的生效周期来定期更新有效活动<br>生效范围：客户端&&服务器 |

## Functions

### IsActivityInfoReady

活动信息是否已准备好
生效范围：客户端&&服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetAllActivityInfos

获取所有活动的信息
生效范围：客户端&&服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetActivityInfo

获取指定活动ID的活动信息
生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ActivityID | `int` | 活动ID |

**Return**

- Type: 
- Description: _None_

### GetValidActivityIDs

获取所有有效的活动ID
生效范围：客户端&&服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetNearestPeriodIndex

获取指定活动距当前时间最近的生效周期序号，
如果已经没有符合条件的开启周期，则返回最后一个生效周期的序号
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ActivityID | `int` | 活动ID |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua
