# VirtualItemManager

UGC虚拟物品全局管理器

## Parents

_None_

## Variables

| Name | Type | Description |
| --- | --- | --- |
| VirtualItemManager.OnVirtualItemNumUpdatedDelegate |  | 生效范围：客户端<br>虚拟物品数量发生变化时触发 |
| VirtualItemManager.OnItemNumUpdatedDelegate |  | 生效范围：客户端<br>物品数量（包括背包物品）发生变化时触发 |
| VirtualItemManager.AddItemResultDelegate |  | 添加物品后触发<br>生效范围：客户端&&服务器<br>@param Result VirtualItemAddItemResult @添加结果 |
| VirtualItemManager.RemoveItemResultDelegate |  | 移除物品后触发<br>生效范围：客户端&&服务器<br>@param Result VirtualItemRemoveItemResult @移除结果 |
| VirtualItemManager.TransferToBackpackResultDelegate |  | 转移虚拟物品到背包时触发<br>生效范围：客户端&&服务器<br>@param Result VirtualItemTransferResult @转移结果 |
| VirtualItemManager.TableDataReadyDelegate |  | 表格配置数据加载好时触发<br>生效范围：客户端&&服务器 |

## Functions

### AddVirtualItems

添加多种虚拟物品
生效范围：服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `UUGCPlayerController` | 玩家控制器 |
| ItemList | `table` | 物品列表，key为物品ID，value为数量 |
| RequestMark | `string` | 发起请求标记。会传回AddItemResultDelegate的Result中，可以省略 |

**Return**

- Type: 
- Description: _None_

### AddVirtualItem

添加虚拟物品
生效范围：服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `UUGCPlayerController` | 玩家控制器 |
| ItemID | `number` | 虚拟物品ID |
| Num | `number` | 添加的物品数量 |
| RequestMark | `string` | 发起请求标记。会传回AddItemResultDelegate的Result中，可以省略 |

**Return**

- Type: 
- Description: _None_

### RemoveVirtualItem

移除虚拟物品
生效范围：服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `UUGCPlayerController` | 玩家控制器 |
| ItemID | `number` | 虚拟物品ID |
| Num | `number` | 移除的物品数量 |
| Callback | [Delegate](../基础功能/Delegate.md) | 回调，可不传参 |

**Return**

_None_

### RemoveItem

移除虚拟物品，如果物品配置了到背包的映射，则只以背包中的数量为准
生效范围：服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `UUGCPlayerController` | 玩家控制器 |
| ItemID | `number` | 虚拟物品ID |
| Num | `number` | 移除的物品数量 |
| Callback | `Delegate\|function` | 回调，可不传参 |

**Return**

_None_

### GetVirtualItemNum

获取虚拟物品数量（不包含已转移背包的数量）
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品ID |
| PlayerController | `UUGCPlayerController` | 玩家控制器，客户端调用可以不传参，即默认主控玩家控制器 |

**Return**

- Type: 
- Description: _None_

### GetItemNum

获取虚拟物品数量（包括已转移到背包的物品）
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品ID |
| PlayerController | `UUGCPlayerController` | 玩家控制器，客户端调用可以不传参，即默认主控玩家控制器 |

**Return**

- Type: 
- Description: _None_

### GetFreeItemNum

获取非绿洲币购买的物品数量
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品ID |
| PlayerController | `UUGCPlayerController` | 玩家控制器，客户端调用可以不传参，即默认主控玩家控制器 |

**Return**

- Type: 
- Description: _None_

### GetOasisItemNum

获取绿洲币购买的物品数量
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品ID |
| PlayerController | `UUGCPlayerController` | 玩家控制器，客户端调用可以不传参，即默认主控玩家控制器 |

**Return**

- Type: 
- Description: _None_

### GetMappedItemNum

获取已映射到背包的物品数量
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品ID |
| PlayerController | `UUGCPlayerController` | 玩家控制器，客户端调用可以不传参，即默认主控玩家控制器 |

**Return**

- Type: 
- Description: _None_

### TransferToBackpack

将虚拟物品转移到背包（需配置映射表UGCObjectMapping）
 生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `PlayerController` | 玩家控制器 |
| ItemID | `number` | 物品ID |
| ItemNum | `number` | 数量, 不传则默认全部转移 |
| bPartial | `boolean` | 是否在背包空间不足时部分转移, 默认false |

**Return**

_None_

### GetItemDatas

获取所有虚拟物品ID的信息
 生效范围：客户端&&服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetItemData

获取虚拟物品ID的信息
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` |  |

**Return**

- Type: 
- Description: _None_

### GetClassicItemID

【废弃】请使用 GetMappedItemID
 获取经典物品ID
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 虚拟物品ID |

**Return**

- Type: 
- Description: _None_

### GetMappedItemID

获取虚拟物品ID对应的背包物品ID
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 虚拟物品ID |

**Return**

- Type: 
- Description: _None_

### GetReverseMappingDatas

获取所有经典物品ID到虚拟物品ID映射数据
 生效范围：客户端&&服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetIsEnableMappingItem

获取是否已启用虚拟物品到背包物品的映射
 生效范围：客户端&&服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetVirtualItemID

获取虚拟物品ID
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ClassicItemID | `number` | 经典物品ID |

**Return**

- Type: 
- Description: _None_

### GetOwnedVirtualItems

获取所有已持有的虚拟物品
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `UUGCPlayerController` | 玩家控制器，客户端调用可以不传参，即默认主控玩家控制器 |

**Return**

- Type: 
- Description: _None_

### GetOwnedItems

获取所有已持有的物品（包括已映射到背包的经典物品）
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `UUGCPlayerController` | 玩家控制器，客户端调用可以不传参，即默认主控玩家控制器 |

**Return**

- Type: 
- Description: _None_

### GetUntransferredItems

获取未转移到背包的物品
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `UUGCPlayerController` | 玩家控制器，客户端调用可以不传参，即默认主控玩家控制器 |

**Return**

- Type: 
- Description: _None_

### SetAutoTransferActive

设置是否开启自动转移背包
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bActive | `boolean` | 是否开启自动转移 |

**Return**

_None_

### SetGetItemUIActive

设置是否显示获得物品弹窗
如果在已显示弹窗后设置为不显示，则在当前所有弹窗显示结束后再生效

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bShow | `bool` | 是否显示 |

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua
