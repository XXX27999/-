# UGCPrivilegeSystem

特权系统接口库

## Parents

_None_

## Variables

_None_

## Functions

### GetPlayerPrivilegesInformation

获取玩家特权 ID 信息列表，如果玩家没有特权 ID 信息或者在 PIE 环境下返回 nil
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UID | `number` | 玩家UID |

**Return**

- Type: 
- Description: _None_

### DoesPlayerHavePrivileges

判断玩家是否拥有特权，没有特权或者在 PIE 环境下返回 false
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UID | `number` | 玩家UID |

**Return**

- Type: 
- Description: _None_

### AddPrivilegeEmblemFlagUI

给指定队友（不包含主控玩家自己）添加绿洲特权徽章UI标记
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerState | `PlayerState` | 队友PlayerState |
| NameColorHexStr | `string` | 玩家名字颜色 |
| bHideTeammatePositionItemName | `boolean` | 是否隐藏队友标记名 |

**Return**

_None_

### RemovePrivilegeEmblemFlagUI

给指定队友（不包含主控玩家自己）移除绿洲特权徽章UI标记
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerState | `PlayerState` | 队友PlayerState |

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua
