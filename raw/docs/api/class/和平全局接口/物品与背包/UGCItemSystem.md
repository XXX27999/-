# UGCItemSystem

道具系统接口库

## Parents

_None_

## Variables

_None_

## Functions

### GetItemType

获取物品ItemType
对应表格数据：和平精英\表格\物品表中ItemType列
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品ID |

**Return**

- Type: 
- Description: _None_

### GetItemSubType

获取ItemSubType
对应表格数据：和平精英\表格\物品表中ItemSubType列
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品ID |

**Return**

- Type: 
- Description: _None_

### GetItemData

获取道具数据
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品ID |

**Return**

- Type: 
- Description: _None_

### IsUGCItem

是否为绿洲物品（物资编辑器中自定义物品）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品ID |

**Return**

- Type: 
- Description: _None_

### IsCanUseInBackpack

返回道具在背包中是否可以使用
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品ID |

**Return**

- Type: 
- Description: _None_

### GetPickupWrapperClassPath

通过ItemID获取Wrapper路径
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品ID |

**Return**

- Type: 
- Description: _None_

### SetWrapperToGround

将Wrapper设置贴在地面
Wrapper.bDropedByPlayer为True时，贴地功能生效
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WrapperActor | [APickUpWrapperActor](../../和平类事件/地面可拾取物类/APickUpWrapperActor.md) | 可拾取物 |

**Return**

- Type: 
- Description: _None_

### GetWrapperItemID

获取Wrapper关联的ItemID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WrapperActor | [APickUpWrapperActor](../../和平类事件/地面可拾取物类/APickUpWrapperActor.md) | 可拾取物 |

**Return**

- Type: 
- Description: _None_

### ModifyWrapperItemCount

修改Wrpaaer中物品的数量
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WrapperActor | [APickUpWrapperActor](../../和平类事件/地面可拾取物类/APickUpWrapperActor.md) | 可拾取物 |
| Count | `number` | 修改后的数量 |

**Return**

- Type: 
- Description: _None_

### DoPickWrapper

拾取Wrapper
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` |  |
| WrapperActor | [APickUpWrapperActor](../../和平类事件/地面可拾取物类/APickUpWrapperActor.md) | 可拾取物 |

**Return**

- Type: 
- Description: _None_

### IsWrapperDropedByPlayer

Wrapper是否是由玩家丢弃生成
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WrapperActor | [APickUpWrapperActor](../../和平类事件/地面可拾取物类/APickUpWrapperActor.md) | 可拾取物 |

**Return**

- Type: 
- Description: _None_

### SetWrapperPickUpRadius

设置Wrapper的可拾取范围
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WrapperActor | [APickUpWrapperActor](../../和平类事件/地面可拾取物类/APickUpWrapperActor.md) | 可拾取物 |
| Radius | `number` | 可拾取范围，单位厘米 |

**Return**

- Type: 
- Description: _None_

### GetQualityTexturePath

获取品质色的128*128纹理路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| QualityRank | `number` | 品质等级 |

**Return**

- Type: 
- Description: _None_

### GetBigQualityTexturePath

获取品质色的128*256纹理路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| QualityRank | `number` | 品质等级 |

**Return**

- Type: 
- Description: _None_

### GetQualityBarTexturePath

获取品质色条纹理路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| QualityRank | `number` | 品质等级 |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua
