# UGCAttributeSystem

属性系统接口库

## Parents

_None_

## Variables

_None_

## Functions

### GetGameAttributeValue

获取指定属性数值
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AttributeOwner | [AActor](../../Others/AActor.md) | 操作属性的对象 （如玩家，枪械等，暂不支持带属性组件的普通Actor） |
| AttributeType | `UGCNativeGameAttributeType \| UGCCustomGameAttributeType @操作属性的枚举` | 操作属性的枚举 |

**Return**

- Type: 
- Description: _None_

### SetGameAttributeValue

设置指定属性数值（自动同步到客户端）
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AttributeOwner | [AActor](../../Others/AActor.md) | 操作属性的对象 （如玩家，枪械等，暂不支持带属性组件的普通Actor） |
| AttributeType | `UGCNativeGameAttributeType \| UGCCustomGameAttributeType @操作属性的枚举` | 操作属性的枚举 |
| Value | `number` | 操作数值 |

**Return**

_None_

### GetGameAttributeValueMax

获取指定属性数值的最大值
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AttributeOwner | [AActor](../../Others/AActor.md) | 操作属性的对象 （如玩家，枪械等，暂不支持带属性组件的普通Actor） |
| AttributeType | `UGCNativeGameAttributeType \| UGCCustomGameAttributeType @操作属性的枚举` | 操作属性的枚举 |

**Return**

- Type: 
- Description: _None_

### GetGameAttributeValueMin

获取指定属性数值的最小值
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AttributeOwner | [AActor](../../Others/AActor.md) | 操作属性的对象 （如玩家，枪械等，暂不支持带属性组件的普通Actor） |
| AttributeType | `UGCNativeGameAttributeType \| UGCCustomGameAttributeType @操作属性的枚举` | 操作属性的枚举 |

**Return**

- Type: 
- Description: _None_

### AddGameAttributeValue

服务端添加指定属性数值（自动同步到客户端）
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AttributeOwner | [AActor](../../Others/AActor.md) | 操作属性的对象 （如玩家，枪械等，暂不支持带属性组件的普通Actor） |
| AttributeType | `UGCNativeGameAttributeType \| UGCCustomGameAttributeType @操作属性的枚举` | 操作属性的枚举 |
| Value | `number` | 操作数值 |

**Return**

_None_

### AddGameAttributeOperation

对指定属性添加数值修改操作
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AttributeOwner | [AActor](../../Others/AActor.md) | 操作属性的对象 （如玩家，枪械等，暂不支持带属性组件的普通Actor） |
| AttributeType | `UGCNativeGameAttributeType \| UGCCustomGameAttributeType @操作属性的枚举` | 操作属性的枚举 |
| OperateType | [EAttrOperator](../../../cppenum/E/EA/EAttrOperator.md) | 操作类型 |
| Value | `number` | 操作数值 |

**Return**

- Type: 
- Description: _None_

### RemoveGameAttributeOperation

对指定属性移除特定的数值修改操作
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AttributeOwner | [AActor](../../Others/AActor.md) | 操作属性的对象 （如玩家，枪械等，暂不支持带属性组件的普通Actor） |
| OperateUniqueID | `string` | 操作属性时返回的唯一ID |

**Return**

_None_

### AddGameAttributeChangedDelegate

注册指定属性变化时的回调函数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AttributeOwner | [AActor](../../Others/AActor.md) | 操作属性的对象 （如玩家，枪械等，暂不支持带属性组件的普通Actor） |
| AttributeType | `UGCNativeGameAttributeType \| UGCCustomGameAttributeType @操作属性的枚举` | 操作属性的枚举 |
| CallbackFunction | `function` | 此属性变化时的回调函数 函数形式: function(AttributeOwner, AttrName, CurValue) end |

**Return**

- Type: 
- Description: _None_

### RemoveGameAttributeChangedDelegate

清除指定属性变化时的回调函数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AttributeOwner | [AActor](../../Others/AActor.md) | 操作属性的对象 （如玩家，枪械等，暂不支持带属性组件的普通Actor） |
| AttributeType | `UGCNativeGameAttributeType \| UGCCustomGameAttributeType @操作属性的枚举` | 操作属性的枚举 |
| ChangedDelegate | [Delegate](../基础功能/Delegate.md) | 注册回调函数时返回的代理 |

**Return**

_None_

### GetSourceObjectFromContext

获取伤害事件上下文中的原对象
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Context | `FGameMagnitudeContext` | 伤害事件上下文 |

**Return**

- Type: 
- Description: _None_

### GetVictimFromContext

获取伤害事件上下文中的受害者
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Context | `FGameMagnitudeContext` | 伤害事件上下文 |

**Return**

- Type: 
- Description: _None_

### GetCauserFromContext

获取伤害事件上下文中的攻击者
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Context | `FGameMagnitudeContext` | 伤害事件上下文 |

**Return**

- Type: 
- Description: _None_

### GetInstigatorFromContext

获取伤害事件上下文中的攻击者Controller
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Context | `FGameMagnitudeContext` | 伤害事件上下文 |

**Return**

- Type: 
- Description: _None_

### GetSourceMagnitudeFromContext

获取伤害事件上下文中的原伤害数值
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Context | `FGameMagnitudeContext` | 伤害事件上下文 |

**Return**

- Type: 
- Description: _None_

### GetDamageTypeFromContext

获取伤害事件上下文中的伤害类型
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Context | `FGameMagnitudeContext` | 伤害事件上下文 |

**Return**

- Type: 
- Description: _None_

### GetDamageTagsFromContext

获取伤害事件上下文中的伤害Tags
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Context | `FGameMagnitudeContext` | 伤害事件上下文 |

**Return**

- Type: 
- Description: _None_

### GetRecoverTagsFromContext

获取治疗事件上下文中的治疗Tags
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Context | `FGameMagnitudeContext` | 治疗事件上下文 |

**Return**

- Type: 
- Description: _None_

### GetRecoveredActorFromContext

获取治疗上下文中的被治疗者
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Context | `FGameMagnitudeContext` | 治疗事件上下文 |

**Return**

- Type: 
- Description: _None_

### GetDamagePositionTypeFromContext

获取伤害事件上下文中的伤害部位类型
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Context | `FGameMagnitudeContext` | 伤害事件上下文 |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua
