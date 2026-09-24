# UGCSkillManagerSystem

【废弃】技能管理系统接口库

## Parents

_None_

## Variables

_None_

## Functions

### GetSkillManagerComponent

【废弃】请使用 UGCPersistEffectSystem
获取技能组件
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | `Actor` | Actor 对象 |

**Return**

- Type: 
- Description: _None_

### UseSkill

【废弃】请使用 UGCPersistEffectSystem
使用技能（技能列表中，技能需配置 SET_KEY_DOWN 事件触发）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | `Actor` | Actor 对象 |
| SkillName | `string` | 技能短名 |

**Return**

_None_

### StopSkill

【废弃】请使用 UGCPersistEffectSystem
停止技能
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | `Actor` | Actor 对象 |
| SkillName | `string` | 技能短名 |

**Return**

_None_

### TriggerSkillEvent

【废弃】请使用 UGCPersistEffectSystem
使用技能（自定义触发事件类型）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | `Actor` | Actor 对象 |
| SkillName | `string` | 技能短名 |
| EventType | [UTSkillEventType](../../../cppenum/U/UT/UTSkillEventType.md) | 事件类型 |

**Return**

_None_

### UseSkillByPath

【废弃】请使用 UGCPersistEffectSystem
根据技能路径使用技能（技能列表中，技能需配置 SET_KEY_DOWN 事件触发）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | `Actor` | Actor 对象 |
| SkillPath | `string` | 技能完整路径 |

**Return**

_None_

### StopSkillByPath

【废弃】请使用 UGCPersistEffectSystem
根据技能路径停止技能
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | `Actor` | Actor 对象 |
| SkillPath | `string` | 技能完整路径 |

**Return**

_None_

### TriggerSkillEventByPath

【废弃】请使用 UGCPersistEffectSystem
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | `Actor` | Actor 对象 |
| SkillPath | `string` | 技能完整路径 |
| EventType | [UTSkillEventType](../../../cppenum/U/UT/UTSkillEventType.md) | 事件类型 |

**Return**

_None_

### StopAllSkill

【废弃】请使用 UGCPersistEffectSystem
停止所有技能
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | `Actor` | Actor 对象 |

**Return**

_None_

### AddSkill

【废弃】请使用 UGCPersistEffectSystem
添加技能
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | `Actor` | Actor 对象 |
| SkillClassPath | `string` | 技能完整路径 |

**Return**

_None_

### RemoveSkill

【废弃】请使用 UGCPersistEffectSystem
移除技能
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | `Actor` | Actor 对象 |
| SkillClassPath | `string` | 技能完整路径 |

**Return**

_None_

### IsSkillRunning

【废弃】请使用 UGCPersistEffectSystem
当前是否有技能在执行
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | `Actor` | Actor 对象 |

**Return**

- Type: 
- Description: _None_

### GetSkillCD

【废弃】请使用 UGCPersistEffectSystem
获取技能冷却
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | `Actor` | Actor 对象 |
| SkillPath | `string` | 技能完整路径 |

**Return**

- Type: 
- Description: _None_

### SetSkillActive

【废弃】请使用 UGCPersistEffectSystem
激活技能
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | `Actor` | Actor 对象 |
| SkillPath | `string` | 技能完整路径 |
| NewActive | `boolean` | 技能状态 |

**Return**

_None_

### TriggerStringEvent

【废弃】请使用 UGCPersistEffectSystem
向技能抛出一个字符串类型的事件
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | `Actor` | Actor 对象 |
| SkillPath | `string` | 技能完整路径 |
| EventString | `string` | 字符串事件 |

**Return**

_None_

### TriggerUAEEvent

【废弃】请使用 UGCPersistEffectSystem
向技能抛出一个预定义的事件
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | `Actor` | Actor 对象 |
| SkillPath | `string` | 技能完整路径 |
| EventType | `UAESkillEvent` | 预定义事件 |

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua
