# CommodityOperationManager

UGC商业化购买流程全局管理器

## Parents

_None_

## Variables

| Name | Type | Description |
| --- | --- | --- |
| CommodityOperationManager.BuyProductResultDelegate |  | 生效范围：客户端&&服务端<br>发起购买商品后触发<br>@param Result BuyProductResult @购买结果 |
| CommodityOperationManager.LimitProductUpdateDelegate |  | 生效范围：客户端&&服务端<br>限购商品购买次数发生变化时触发 |
| CommodityOperationManager.PurchasedProductListUpdateDelegate |  | 生效范围：客户端&&服务端<br>商品购买次数发生变化时触发 |

## Functions

### BuyProduct

发起商品购买
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ProductID | `number` | 商品的ID |
| Num | `number` | 购买商品数量 |
| CurrentPrice | `number` | 发起购买时的价格，用于校验 |
| bCheckPrivilege | `boolean` | 是否检查玩家特权（即当前商品为仅特权可购买），默认false |

**Return**

- Type: 
- Description: _None_

### ServerBuyProduct

发起自定义货币商品购买
生效范围：服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerKey | `number` | 发起购买者的 PlayerKey |
| ProductID | `number` | 商品的ID |
| Num | `number` | 购买商品数量 |
| CurrentPrice | `number` | 发起购买时的价格，用于校验 |
| bCheckPrivilege | `boolean` | 是否检查玩家特权（即当前商品为仅特权可购买），默认false |

**Return**

_None_

### CanAfford

检查是否买得起指定数量的商品
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ProductID | `number` | 商品的ID |
| Num | `number` | 购买的商品数量 |
| PlayerController | `UUGCPlayerController` | 玩家控制器，客户端可以不传 |

**Return**

- Type: 
- Description: _None_

### GetLimitPurchasedTimes

获得限购商品的购买次数
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ProductID | `number` | 商品的ID |
| PlayerController | `UUGCPlayerController` | 玩家控制器，客户端可以不传 |

**Return**

- Type: 
- Description: _None_

### GetAllLimitPurchasedProducts

获取所有已购买的限购商品
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `UUGCPlayerController` | 玩家控制器，客户端可以不传 |

**Return**

- Type: 
- Description: _None_

### GetPurchasedTimes

获得商品的累计购买次数
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ProductID | `number` | 商品的ID |
| PlayerController | `UUGCPlayerController` | 玩家控制器，客户端可以不传 |

**Return**

- Type: 
- Description: _None_

### GetAllPurchasedProducts

获取所有已购买的商品
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `UUGCPlayerController` | 玩家控制器，客户端可以不传 |

**Return**

- Type: 
- Description: _None_

### GetAllProductData

获取所有商品信息
生效范围：客户端&&服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetProductData

获取指定商品信息
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ProductID | `number` | 商品的ID |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua
