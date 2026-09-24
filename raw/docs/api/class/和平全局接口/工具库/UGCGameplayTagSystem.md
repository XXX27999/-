# UGCGameplayTagSystem

GameplayTag接口库

## Parents

_None_

## Variables

| Name | Type | Description |
| --- | --- | --- |
| UGCGameplayTagSystem.Tags.PawnState |  |  |

## Functions

### RequestGameplayTag

根据字符串获取FGameplayTag
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TagString | `string` | Tag的字符串 |

**Return**

- Type: 
- Description: _None_

### IsValidTag

检查一个Tag是否合法
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Tag | `UGCGameplayTag\|string\|FGameplayTag` | Tag |

**Return**

- Type: 
- Description: _None_

### IsUGCGameplayTag

检查一个Tag是否是UGCGameplayTag
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Tag | [UGCGameplayTag](../../Others/UGCGameplayTag.md) | UGCGameplayTag的lua对象 |

**Return**

- Type: 
- Description: _None_

### MatchesTag

检查TagA是否与TagB匹配
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TagA | `UGCGameplayTag\|string\|FGameplayTag` | Tag |
| TagB | `UGCGameplayTag\|string\|FGameplayTag` | Tag |
| bExactMatch | `boolean` | 是否精确匹配 |

**Return**

- Type: 
- Description: _None_

### EqualsTag

检查TagA是否与TagB相等
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TagA | `UGCGameplayTag\|string\|FGameplayTag` | Tag |
| TagB | `UGCGameplayTag\|string\|FGameplayTag` | Tag |

**Return**

- Type: 
- Description: _None_

### CreateGameplayTagContainer

创建一个空的FFGameplayTagContainer
生效范围：服务器&客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CreateGameplayTagContainerFromTag

创建一个包含指定FGameplayTag的FGameplayTagContainer
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SingleTag | `UGCGameplayTag\|string\|FGameplayTag` | 传入FGameplayTagContainer中的FGameplayTag |

**Return**

- Type: 
- Description: _None_

### CreateGameplayTagContainerFromArray

创建一个包含一组FGameplayTag的FGameplayTagContainer
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GameplayTags | `FGameplayTag[]` | 传入FGameplayTagContainer中的FGameplayTags |

**Return**

- Type: 
- Description: _None_

### AddGameplayTagToContainer

将单个FGameplayTag添加到传入的FGameplayTagContainer中
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TagContainer | [FGameplayTagContainer](../../../cppstruct/F/FG/FGameplayTagContainer.md) | 要追加到的FGameplayTagContainer |
| Tag | [FGameplayTag](../../../cppstruct/F/FG/FGameplayTag.md) | 要添加到FGameplayTagContainer中的FGameplayTag |

**Return**

_None_

### RemoveGameplayTagFromContainer

从传入的FGameplayTagContainer中移除单个FGameplayTag，若找到并移除则返回 true ，否则返回 false
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TagContainer | [FGameplayTagContainer](../../../cppstruct/F/FG/FGameplayTagContainer.md) | 要从中移除的FGameplayTagContainer |
| Tag | [FGameplayTag](../../../cppstruct/F/FG/FGameplayTag.md) | 要从FGameplayTagContainer中移除的FGameplayTag |

**Return**

- Type: 
- Description: _None_

### HasTag

检查FGameplayTagContainer是否包含特定的FGameplayTag
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TagContainer | [FGameplayTagContainer](../../../cppstruct/F/FG/FGameplayTagContainer.md) | 要从中查找指定FGameplayTag的FGameplayTagContainer |
| Tag | [FGameplayTag](../../../cppstruct/F/FG/FGameplayTag.md) | 要从FGameplayTagContainer中检查的FGameplayTag |
| bExactMatch | `boolean` | 是否精确匹配 |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua
