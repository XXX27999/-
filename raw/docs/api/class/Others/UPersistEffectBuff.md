# UPersistEffectBuff

Buff系统归属与和平精英的技能系统，用于帮助开发者更方便快捷地实现Buff效果
  通过与Tag、Attribute等系统的配合能够通过配置就实现大部分所需的效果
  对于更细致的Buff效果也可以通过重写BP结尾的函数来实现定制化效果。

## Parents

- [UPersistEffectBase](./UPersistEffectBase.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| BuffInfo | [FPEBuffInfo](../../cppstruct/F/FP/FPEBuffInfo.md) | 生效范围：服务器&客户端<br>      Buff蓝图的配置信息 |

## Functions

### AddStackNum

生效范围：服务器
	  修改堆叠层数，修改后的层数大于等于0且小于等于最大堆叠层数(MaxStackNum)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Num | `int32` | 新增的层数 |

**Return**

- Type: 
- Description: _None_

### GetStackNum

生效范围：服务器&客户端
	 获取当前层数

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetCauser

生效范围：服务器&客户端
      获取Buff的施加者

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetCauser

生效范围：服务器
	 设置Buff的施加者

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Causer | `AActor *` | 施加者 |

**Return**

- Type: 
- Description: _None_

### TriggerAllLayer

生效范围：服务器
      触发当前所有层的Buff的效果

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### TriggerSingleLayer

生效范围：服务器
	  触发单层的Buff的效果

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### RefreshBuff

生效范围：服务器
	  重置Buff持续时间

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetBuffEnable

生效范围：服务器
	  设置Buff是否生效

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| IsEnable | `bool` | 是否生效 |

**Return**

- Type: 
- Description: _None_

### IsBuffEnable

生效范围：服务器&客户端
	  获取Buff当前是否生效

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Pause

生效范围：服务器
	  暂停Buff持续减少剩余时间

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Resume

生效范围：服务器
	  恢复Buff持续减少剩余时间

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OverwriteBuffUIInfo

生效范围：客户端
	  更改UI信息，但双端不同步

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BuffName | `FName &` | Buff名字 |
| BuffDetail | `FString &` | Buff描述 |
| BuffIconPath | `FString &` | Buff图标路径 |

**Return**

- Type: 
- Description: _None_

### GetBuffName

生效范围：服务器&客户端
	  获取Buff名字

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetBuffDetail

生效范围：服务器&客户端
	  获取Buff描述

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetBuffIconPath

生效范围：服务器&客户端
	  获取Buff图标路径

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

| Name | Type | Description |
| --- | --- | --- |
| OnTotalDurationChange_BP |  | 生效范围：服务器<br>	  当Buff持续时间改变时调用，如修改ApplyTime、修改StackNum |
| OnStackChange_BP |  | 生效范围：服务器&客户端<br>	  当Buff堆叠层数变化时调用，如调用AddStackNum、消耗一层Buff |
| OnRefresh_BP |  | 生效范围：服务器&客户端<br>	  Buff刷新时调用 |
| CanTrigger_BP |  | 生效范围：服务器<br>	  当Buff效果触发前调用，用于改写Buff触发条件，默认实现为直接返回True |
| OnTrigger_BP |  | 生效范围：服务器&客户端<br>	  当Buff效果触发时调用 |

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnStackNumChange |  | Event<br>	  生效范围：服务器&客户端<br>	  Buff层数改变事件 |
| OnUIInfoChange |  | Event<br>	  生效范围：客户端<br>	  Buff的UI信息改变事件 |

## Language

cpp
