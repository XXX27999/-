# UGCCommoditySystem

商业化库

## Parents

_None_

## Variables

| Name | Type | Description |
| --- | --- | --- |
| UGCCommoditySystemImplementation.UseUGCCommodityResultDelegate |  |  |
| UGCCommoditySystem.BuyUGCCommodityResultDelegate |  | 玩家购买商品后广播<br>生效范围：服务器&客户端 |
| UGCCommoditySystem.CompensateUGCCommodityDelegate |  | 补偿玩家商品后广播<br>生效范围：服务器&客户端<br>@param PlayerKey number @玩家PlayerKey<br>@param UID number @玩家UID<br>@param CommodityID number @物品ID<br>@param Count number @物品数量<br>@param ProductID number @商品ID |
| UGCCommoditySystem.CompensateUGCCommodityBatchDelegate |  | 补偿玩家商品后批量广播<br>生效范围：服务器<br>@param PlayerKey number @玩家PlayerKey<br>@param UID number @玩家UID<br>@param CommodityList table @补偿列表 |
| UGCCommoditySystem.UseRedemptionCodeResultDelegate |  | 玩家使用兑换码后逐个物品广播<br>生效范围：服务器&客户端<br>@param Result EUseRedemptionCodeResult @使用兑换码结果<br>@param PlayerKey number @玩家PlayerKey<br>@param UID number @玩家UID<br>@param CommodityID number @物品ID<br>@param Count number @物品数量<br>@param ProductID number @商品ID |
| UGCCommoditySystem.UseRedemptionCodeBatchResultDelegate |  | 玩家使用兑换码后批量广播<br>生效范围：服务器<br>@param Result EUseRedemptionCodeResult @使用兑换码结果<br>@param PlayerKey number @玩家PlayerKey<br>@param UID number @玩家UID<br>@param CommodityList table @兑换列表 |
| UGCCommoditySystem.BuyUGCCommodityResultBetweenGamesDelegate |  | 如果本次游戏对局的商品数据跟上一局结算时的物品数据有差异，那么服务端会在 PlayerController:Server_OnUGCCommodityPlayerDataReady() 之前广播此 Delegate<br>可以在PlayerController:ReceiveBeginPlay() 里监听这个 Delegate<br>@param PlayerKey number @玩家PlayerKey<br>@param UID number @玩家UID<br>@param CommodityID number @物品ID<br>@param Count number @物品数量<br>生效范围：服务器 |
| UGCCommoditySystem.UseUGCCommodityResultDelegate |  | 物品使用时广播<br>生效范围：服务器&客户端 |
| UGCCommoditySystem.UGCProductsChangedDelegate |  | 在商品列表发生变化时广播<br>生效范围：服务器&客户端 |
| UGCCommoditySystem.UGCCommodityPlayerDataChangedDelegate |  | 在UGCCommoditySystem.GetAllPlayerUGCCommodityList() 和 UGCCommoditySystem.GetUGCCommodityList()返回值发生改变时广播<br>生效范围：服务器&客户端 |
| UGCCommoditySystem.BuyUGCCommodityBatchResultDelegate |  | 批量购买结果广播<br>生效范围：服务器&客户端<br>@param bSuccess boolean @是否成功<br>@param PlayerKey number @玩家PlayerKey<br>@param UID number @玩家UID<br>@param CommodityList table @购买结果列表 {{CommodityID=, Count=}, ...}<br>@param Context string @上下文 |

## Functions

### GetTicket

获取玩家货币(绿洲币/灰度币)
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerKey | `number` | 玩家PlayerKey，服务器调用必传 |

**Return**

- Type: 
- Description: _None_

### GetActiveCoin

获取启元币
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerKey | `number` | 玩家PlayerKey，服务器调用必传 |

**Return**

- Type: 
- Description: _None_

### BuyUGCCommodity

购买绿洲商品
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BuyCommodityCMD | `string` | 购买协议，参考：EUGCCommodityCommandType |
| Name | `string` | 物品的名称 |
| Icon | `string` | 物品图标 |
| Desc | `string` | 物品的描述 |
| Count | `number` | 单次购买的数量 |
| Cost | `number` | 单个物品的价格 Cost 必须传入 UGCCommoditySystem.GetSellingPriceAfterDiscount 的返回值 |

**Return**

- Type: 
- Description: _None_

### BuyUGCPrivilegeCommodity

购买绿洲特权商品
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BuyCommodityCMD | `string` | 购买协议，参考：EUGCCommodityCommandType |
| Name | `string` | 物品的名称 |
| Icon | `string` | 物品图标 |
| Desc | `string` | 物品的描述 |
| Count | `number` | 单次购买的数量 |
| Cost | `number` | 单个物品的价格 Cost 必须传入 UGCCommoditySystem.GetSellingPriceAfterDiscount 的返回值 |

**Return**

- Type: 
- Description: _None_

### BuyUGCCommodity2

购买绿洲商品
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ProductID | `number` | 商品 ID |
| Icon | `string` | 物品图标 |
| Desc | `string` | 物品的描述 |
| Count | `number` | 单次购买的数量 |

**Return**

- Type: 
- Description: _None_

### BuyUGCPrivilegeCommodity2

购买绿洲特权商品
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ProductID | `number` | 商品 ID |
| Icon | `string` | 物品图标 |
| Desc | `string` | 物品的描述 |
| Count | `number` | 单次购买的数量 |

**Return**

- Type: 
- Description: _None_

### BuyUGCCommodityBatch

批量购买绿洲商品
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BuyList | `table` | 购买列表 {{ProductID=number, Count=number, bCheckPrivilege=boolean}, ...} |

**Return**

- Type: 
- Description: _None_

### UseUGCCommodity

使用绿洲物品
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UseCommodityCMD | `string` | 使用协议，参考：EUGCCommodityCommandType |
| CommodityID | `number` | 物品ID |
| Name | `string` | 物品的名称 |
| Icon | `string` | 物品图标 |
| Desc | `string` | 物品的描述 |
| Count | `number` | 单次消耗的数量 |
| bShowDialog | `boolean` | 是否二次确认 |

**Return**

- Type: 
- Description: _None_

### UseUGCCommodity2

使用绿洲物品
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `PlayerController` | 玩家控制器 在 DS 端调用的话 PlayerController 必须传，客户端可传 nil，否则调用无效 |
| ObjectID | `number` | 物品ID |
| Icon | `string` | 物品图标，填 nil 则使用 UGCObject.ItemSmallIcon（UGCObject 表格中的 ItemSmallIcon（小icon） 字段） |
| Desc | `string` | 物品的描述，填 nil 则使用 UGCObject.ItemDesc（UGCObject 表格中的 ItemDesc（物品描述） 字段） |
| Count | `number` | 单次消耗的数量 |
| bShowDialog | `boolean` | bShowDialog 在 DS 忽略 |

**Return**

- Type: 
- Description: _None_

### RegBuyCMD

注册商品购买协议
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BuyCommodityCMD | `string` | 购买协议，参考：EUGCCommodityCommandType |
| ProductID | `number` | 商品的ID |
| Count | `number` | 单次购买的数量 |

**Return**

_None_

### RegUseCMD

注册使用物品协议
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UseCommodityCMD | `string` | 使用商品协议，参考：EUGCCommodityCommandType |
| CommodityID | `number` | 物品的ID |
| Count | `number` | 单次消耗的数量 |

**Return**

_None_

### UseRedemptionCode

使用兑换码
PIE下调用该接口默认兑换成功，触发兑换结果 {ItemID=1001, Count=1, ProductID=900001}
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UID | `number` | 玩家的UID |
| RedemptionCode | `string` | 兑换码 |

**Return**

_None_

### GetAllPlayerUGCCommodityList

获取所有玩家的物品数据
生效范围：服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetUGCCommodityList

获取主控端物品数据
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerKey | `number` | 玩家PlayerKey，服务器调用必传 |

**Return**

- Type: 
- Description: _None_

### GetAllPlayerUGCProductList

获取所有玩家的绿洲商品限购数据
生效范围：服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetUGCProductList

获取所有玩家的绿洲商品限购数据
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ClearCommodity

清空所有已购买物品
生效范围：客户端

**Parameters**

_None_

**Return**

_None_

### GetSellingPriceAfterDiscount

获取折扣后商品价格
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BuyCommodityCMDOrProductID | `string\|int` | 购买商品协议 或者 商品ID |

**Return**

- Type: 
- Description: _None_

### OpenRedeemPage

打开兑换码页面
生效范围：客户端

**Parameters**

_None_

**Return**

_None_

### ShowRechargeEntryUI

显示绿洲币充值界面
生效范围：客户端

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
