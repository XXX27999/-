# UGCBackPackSystem

背包系统接口库

## Parents

_None_

## Variables

_None_

## Functions

### GetBackpackComponent

获取背包组件(客户端仅能获取到自己的）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### AddItem

添加道具
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| ItemID | `number` | 物品ID |
| Count | `number` | 数量 |

**Return**

- Type: 
- Description: _None_

### DropItem

掉落道具（入参为ItemID，不关心具体哪个道具）
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| ItemID | `number` | 物品ID |
| Count | `number` | 数量 |
| IsDestroy | `boolean` | 是否直接销毁，不掉落地面 |

**Return**

- Type: 
- Description: _None_

### UseItem

使用道具（入参为ItemID，不关心具体哪个道具）
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| ItemID | `number` | 物品ID |

**Return**

- Type: 
- Description: _None_

### DisuseItem

停止使用物品（入参为ItemID，默认选择同ID第一个，仅对物资编辑器生成的绷带，饮料类物资生效）
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| ItemID | `number` | 物品ID |

**Return**

- Type: 
- Description: _None_

### DropItemByInstanceID

根据InstanceID（物品实例ID）掉落道具
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| InstanceID | `number` | 物品实例ID（唯一） |
| Count | `number` | 数量 |
| IsDestroy | `boolean` | 是否直接销毁，不掉落地面 |

**Return**

- Type: 
- Description: _None_

### UseItemByInstanceID

根据InstanceID（物品实例ID）使用道具
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| InstanceID | `number` | 物品实例ID（唯一） |

**Return**

- Type: 
- Description: _None_

### DisuseItemByInstanceID

根据InstanceID（物品实例ID）停止使用道具（仅对物资编辑器生成的绷带，饮料类物资生效）
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| InstanceID | `number` | 物品实例ID（唯一） |

**Return**

- Type: 
- Description: _None_

### GetItemCount

获取道具数量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| ItemID | `number` | 物品ID |

**Return**

- Type: 
- Description: _None_

### GetAllItemData

获取背包里所有道具数据
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### GetAllItemDataByItemID

获取ItemData列表
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| ItemID | `number` | 物品ID |

**Return**

- Type: 
- Description: _None_

### GetItemDataByInstanceID

根据InstanceID（物品实例ID）获取ItemData
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| InstanceID | `number` | 物品实例ID（唯一） |

**Return**

- Type: 
- Description: _None_

### GetCapacity

获取背包剩余容量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### GetMaxCapacity

获取背包最大剩余容量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### HasItemBySubType

是否拥有某类物品
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| ItemSubType | `number` | 道具字类型 |

**Return**

- Type: 
- Description: _None_

### GetWeaponsInBackpack

获取背包中的武器
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### GetWeaponAttachmentsInBackpack

获取背包中的武器配件
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### GetArmorInBackpack

获取当前防弹衣
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### GetHelmetInBackpack

获取当前头盔
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### GetConsumablesInBackpack

获取背包中的所有消耗品
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### IsAttachItemType

通过传入物品ID判断是否拥有某类物品，例：可传入AKM的物品ID，判断是否拥有枪械
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品ID |

**Return**

- Type: 
- Description: _None_

### IsGunItemType

传入物品ID判断是否为枪械
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品ID |

**Return**

- Type: 
- Description: _None_

### GetPickupWrapperClassPath

获取PickupWrapperClass路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品ID |

**Return**

- Type: 
- Description: _None_

### GetAllAttachmentDefineIDInBackpack

获取背包内所有枪械配件DefineID
生效范围：服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### GetAllUnEquipedAttachmentDefineIDInBackpack

获取背包内所有未装备的枪械配件DefineID
生效范围：服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua
