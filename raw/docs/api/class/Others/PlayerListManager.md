# PlayerListManager

玩家列表全局管理器

## Parents

_None_

## Variables

| Name | Type | Description |
| --- | --- | --- |
| PlayerListManager.PlayerListUpdateDelegate |  | 玩家列表数据更新委托<br>生效范围：客户端<br>@param PlayerListData FPlayerListEntry[] @排序后的玩家列表 |

## Functions

### UpdatePlayerSortValue

更新排序属性值
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `BP_UGCPlayerController_C` | 玩家控制器 |
| UID | `number` | 玩家UID |
| SortValue | `number` | 排序数值 |

**Return**

- Type: 
- Description: _None_

### UpdatePlayerDisplayValue

更新展示属性值
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `BP_UGCPlayerController_C` | 玩家控制器 |
| UID | `number` | 玩家UID |
| DisplayValue | `number` | 展示数值 |

**Return**

- Type: 
- Description: _None_

### GetPlayerListData

获取排序后的玩家列表
生效范围：服务器&客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetPlayerListConfig

获取玩家列表配置
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
