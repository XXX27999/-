# UGCSimpleCharacterSystem

怪物小动物系统接口库

## Parents

_None_

## Variables

_None_

## Functions

### GetHealth

获取当前血量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SimpleCharacter | `ASTExtraSimpleCharacterBase` | 小动物/ ASTExtraSimpleCharacter @怪物 |

**Return**

- Type: 
- Description: _None_

### SetHealth

设置当前血量（不会超过血量最大值）
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SimpleCharacter | `ASTExtraSimpleCharacterBase` | 小动物/ ASTExtraSimpleCharacter @怪物 |
| Health | `number` | 血量 |

**Return**

_None_

### GetHealthMax

获取当前最大血量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SimpleCharacter | `ASTExtraSimpleCharacterBase` | 小动物/ ASTExtraSimpleCharacter @怪物 |

**Return**

- Type: 
- Description: _None_

### SetHealthMax

设置当前最大血量（当前血量不会随之变大，但如果超过最大血量，则会变小）
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SimpleCharacter | `ASTExtraSimpleCharacterBase` | 小动物/ ASTExtraSimpleCharacter @怪物 |
| HealthMax | `number` | 最大血量 |

**Return**

_None_

### GetSpeedScale

获取移动速度系数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SimpleCharacter | `ASTExtraSimpleCharacterBase` | 小动物/ ASTExtraSimpleCharacter @怪物 |

**Return**

- Type: 
- Description: _None_

### SetSpeedScale

设置移动速度系数
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SimpleCharacter | `ASTExtraSimpleCharacterBase` | 小动物/ ASTExtraSimpleCharacter @怪物 |
| SpeedScale | `number` | 移动系数 |

**Return**

_None_

### IsInvincible

获取是否无敌
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SimpleCharacter | `ASTExtraSimpleCharacterBase` | 小动物/ ASTExtraSimpleCharacter @怪物 |

**Return**

- Type: 
- Description: _None_

### SetInvincible

设置是否无敌
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SimpleCharacter | `ASTExtraSimpleCharacterBase` | 小动物/ ASTExtraSimpleCharacter @怪物 |
| IsInvincible | `boolean` | 是否无敌 |

**Return**

_None_

### IsAlive

获取是否存活
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SimpleCharacter | `ASTExtraSimpleCharacterBase` | 小动物/ ASTExtraSimpleCharacter @怪物 |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua
