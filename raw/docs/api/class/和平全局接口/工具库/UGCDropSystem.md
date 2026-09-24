# UGCDropSystem

掉落系统接口库

## Parents

_None_

## Variables

_None_

## Functions

### DropItems

根据掉落信息进行物品掉落
根据权重掉落：每次掉落一个物品
根据概率掉落：每次根据物品表的物品数量掉落物品
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DropID | `number` | 掉落ID |

**Return**

- Type: 
- Description: _None_

### DropItemsByGroup

根据掉落组信息进行物品掉落
掉落组配置参考掉落表格配置（DropGroup Table）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DropGroupID | `number` | 掉落组ID |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua
