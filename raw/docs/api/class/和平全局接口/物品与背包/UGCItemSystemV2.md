# UGCItemSystemV2

V2道具系统接口库

## Parents

_None_

## Variables

| Name | Type | Description |
| --- | --- | --- |
| UGCItemSystemV2._GetterOverrides |  | 存储外部注册的 Get 重写委托<br> key: 函数名（如 "GetItemNameV2ByDefineID"）, value: 重写函数<br>@type table<string, function> |

## Functions

### RegisterItemPropertyGetOverride

注册物品属性读取函数
生效范围：服务器&客户端分别注册

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Key | [EItemOverrideKey](../../../cppenum/E/EI/EItemOverrideKey.md) | 属性枚举值，使用 EItemOverrideKey.XXX |
| Func | `fun(FItemDefineID): any @重写函数，参数和返回值与对应属性接口保持一致` | 重写函数，参数和返回值与对应属性接口保持一致 |

**Return**

- Type: 
- Description: _None_

### UnregisterItemPropertyGetOverride

注销物品属性读取函数
生效范围：服务器&客户端分别反注册

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Key | `EItemOverrideKey\|nil` | 属性枚举值，使用 EItemOverrideKey.XXX；不传则清除所有 |

**Return**

- Type: 
- Description: _None_

### GetConfigItemHandle

获取物品ItemHandle配置
可以通过它取得所有物品中配置的静态数据（只读）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |

**Return**

- Type: 
- Description: _None_

### GetItemInstanceDataManager

获取物品实例数据管理器
生效范围：服务器&客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsUGCItemV2

是否为绿洲物品（物资编辑器中自定义物品）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |

**Return**

- Type: 
- Description: _None_

### IsShouldPersist

是否持久化
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |

**Return**

- Type: 
- Description: _None_

### IsItemEquipTarget

判断物品是否为装备目标
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |

**Return**

- Type: 
- Description: _None_

### IsItemEquipAttach

判断物品是否为装备配件
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |

**Return**

- Type: 
- Description: _None_

### IsItemThrowWeapon

判断物品是否由投掷物模板创建
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |

**Return**

- Type: 
- Description: _None_

### IsObjEditorItemV2

是否为V2版本物编创建的物品
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |

**Return**

- Type: 
- Description: _None_

### GetItemNameV2

返回物品名称
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |

**Return**

- Type: 
- Description: _None_

### GetItemNameV2ByDefineID

返回物品名称（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemDefineID | [FItemDefineID](../../../cppstruct/F/FI/FItemDefineID.md) | 物品 DefineID |

**Return**

- Type: 
- Description: _None_

### GetItemSubTypeV2

返回物品子类型SubType，(比如武器类别为1，M146子类型为101)
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |

**Return**

- Type: 
- Description: _None_

### GetItemIconTextureV2

返回物品图标路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |

**Return**

- Type: 
- Description: _None_

### GetItemIconTextureV2ByDefineID

返回物品图标路径（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemDefineID | [FItemDefineID](../../../cppstruct/F/FI/FItemDefineID.md) | 物品 DefineID |

**Return**

- Type: 
- Description: _None_

### GetOwnBackpackComponent

读取物品所在背包
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemHandle | `UBattleItemHandleBase` | 物品 Handle |

**Return**

- Type: 
- Description: _None_

### GetItemIconWithPlayerSkinV2

返回物品图标路径(带玩家皮肤)，优先返回开发者自定义图标
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |
| PlayerController | `PlayerController` | 玩家 PlayerController |

**Return**

- Type: 
- Description: _None_

### GetItemIconWithPlayerSkinV2ByDefineID

返回物品图标路径(带玩家皮肤)（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemDefineID | [FItemDefineID](../../../cppstruct/F/FI/FItemDefineID.md) | 物品 DefineID |
| PlayerController | `PlayerController` | 玩家 PlayerController |

**Return**

- Type: 
- Description: _None_

### GetWhiteIconTextureV2

返回物品剪影图标路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |

**Return**

- Type: 
- Description: _None_

### GetWhiteIconTextureV2ByDefineID

返回物品剪影图标路径（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemDefineID | [FItemDefineID](../../../cppstruct/F/FI/FItemDefineID.md) | 物品 DefineID |

**Return**

- Type: 
- Description: _None_

### GetBigIconTextureV2

返回物品装备栏图标路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |

**Return**

- Type: 
- Description: _None_

### GetBigIconTextureV2ByDefineID

返回物品装备栏图标路径（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemDefineID | [FItemDefineID](../../../cppstruct/F/FI/FItemDefineID.md) | 物品 DefineID |

**Return**

- Type: 
- Description: _None_

### GetBigIconTextureWithPlayerSkinV2

返回物品装备栏图标路径(带玩家皮肤)，优先返回开发者自定义图标
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |
| PlayerController | `PlayerController` | 玩家 PlayerController |

**Return**

- Type: 
- Description: _None_

### GetBigIconTextureWithPlayerSkinV2ByDefineID

返回物品装备栏图标路径(带玩家皮肤)（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemDefineID | [FItemDefineID](../../../cppstruct/F/FI/FItemDefineID.md) | 物品 DefineID |
| PlayerController | `PlayerController` | 玩家 PlayerController |

**Return**

- Type: 
- Description: _None_

### GetItemDetailV2

返回物品详情
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |

**Return**

- Type: 
- Description: _None_

### GetItemDetailV2ByDefineID

返回物品详情（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemDefineID | [FItemDefineID](../../../cppstruct/F/FI/FItemDefineID.md) | 物品 DefineID |

**Return**

- Type: 
- Description: _None_

### GetItemPickupDetailV2

返回物品拾取描述
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |

**Return**

- Type: 
- Description: _None_

### GetItemPickupDetailV2ByDefineID

返回物品拾取描述（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemDefineID | [FItemDefineID](../../../cppstruct/F/FI/FItemDefineID.md) | 物品 DefineID |

**Return**

- Type: 
- Description: _None_

### ItemHasTagV2

是否含有某个 Tag
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |
| Tag | `string` | 物品 Tag |

**Return**

- Type: 
- Description: _None_

### GetItemTagsV2

返回物品所有 Tag
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |

**Return**

- Type: 
- Description: _None_

### ItemCanDropV2

返回物品是否可丢弃
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |

**Return**

- Type: 
- Description: _None_

### ItemCanRemoveV2

返回物品是否可销毁
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |

**Return**

- Type: 
- Description: _None_

### IsCanUseV2

返回物品在背包中是否可以使用
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |

**Return**

- Type: 
- Description: _None_

### GetItemMaxNumberOfStacksV2

返回物品最大堆叠数量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |

**Return**

- Type: 
- Description: _None_

### GetItemQualityV2

返回物品品质
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |

**Return**

- Type: 
- Description: _None_

### GetItemQualityV2ByDefineID

返回物品品质（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemDefineID | [FItemDefineID](../../../cppstruct/F/FI/FItemDefineID.md) | 物品 DefineID |

**Return**

- Type: 
- Description: _None_

### GetItemCustomizedTypeV2

返回物品自定义类型
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |

**Return**

- Type: 
- Description: _None_

### LoadItemCustomData

获取物品自定义实例化数据
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemDefineID | [FItemDefineID](../../../cppstruct/F/FI/FItemDefineID.md) | 物品DefineID |

**Return**

- Type: 
- Description: _None_

### SaveItemCustomData

保存物品自定义实例化数据
注意: 实例数据也包含了和平内置数据，应避免直接覆盖，采用下述方式添加数据
local CustomData = UGCItemSystemV2.LoadItemCustomData(ItemDefineID)
CustomData.NewKey = NewTableData -- 填充新的数据
UGCItemSystemV2.SaveItemCustomData(ItemDefineID, CustomData)
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemDefineID | [FItemDefineID](../../../cppstruct/F/FI/FItemDefineID.md) | 物品DefineID |
| ItemCustomData | `table` | 物品自定义实例化数据table |

**Return**

- Type: 
- Description: _None_

### GetItemCustomDataSize

获取物品自定义实例化数据大小（单位字节）
用于Debug实例化数据的性能占用，主要影响存档大小，以及数据从DS同步到客户端的消耗
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemDefineID | [FItemDefineID](../../../cppstruct/F/FI/FItemDefineID.md) | 物品 DefineID |

**Return**

- Type: 
- Description: _None_

### GetItemDefineID

通过物品ID创建一个全新的物品实例，并返回 DefineID
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |

**Return**

- Type: 
- Description: _None_

### GetItemDefineIDByPreset

指定实例化数据预设，创建一个全新的物品实例，并返回 DefineID
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |
| PresetIdx | `number` | 实例化数据预设索引 |

**Return**

- Type: 
- Description: _None_

### SetItemCommonReason

设置物品通用 Reason
用于操作物品时指定其中一些行为
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemDefineID | [FItemDefineID](../../../cppstruct/F/FI/FItemDefineID.md) | 物品 DefineID |
| Reason | `number` | Reason |

**Return**

_None_

### GetItemCommonReason

获取物品通用 Reason
用于操作物品时指定其中一些行为
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemDefineID | [FItemDefineID](../../../cppstruct/F/FI/FItemDefineID.md) | 物品 DefineID |

**Return**

- Type: 
- Description: _None_

### GetEquipTargetSlots

获取装备物品拥有的槽位列表
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品ID |

**Return**

- Type: 
- Description: _None_

### GetDisplayNameBySlotName

获取槽位对应的展示名
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品ID |
| SlotName | `string` | 槽位名 |

**Return**

- Type: 
- Description: _None_

### GetAttachTargetItem

获取物品附加在哪个物品上
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemDefineID | `ItemDefineID` | 物品 DefineID |

**Return**

- Type: 
- Description: _None_

### GetAttachChildItem

获取附加在物品上的子物品
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AttachParentID | `ItemDefineID` | 父物品的 DefineID |
| AttachSlot | `string` | 父物品的槽位名 |

**Return**

- Type: 
- Description: _None_

### GetAttachChildrenItem

获取所有附加在物品上的子物品
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AttachParentID | `ItemDefineID` | 父物品的 DefineID |

**Return**

- Type: 
- Description: _None_

### GetAttachAllowSlots

获取子物品可以 Attach 到父物品的哪些 Slot(不考虑槽位启用状态)
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AttachParentID | `number` | 父物品的 ItemID |
| AttachChildID | `number` | 子物品的 ItemID |

**Return**

- Type: 
- Description: _None_

### GetAttachAllowSlotsByDefineID

获取子物品可以 Attach 到父物品`实例` 的哪些 Slot(考虑槽位启用状态)
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Player | `PlayerPawn` | 玩家 |
| AttachParentDefineID | `ItemDefineID` | 父物品的 ItemDefineID |
| AttachChildID | `number` | 子物品的 ItemID |

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

### GetQualityTextColor

获取品质文字颜色
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| QualityRank | `number` | 品质等级 |

**Return**

- Type: 
- Description: _None_

### GetBackpackSimpleNameV2

返回物品背包简述
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |

**Return**

- Type: 
- Description: _None_

### GetBackpackSimpleNameV2ByDefineID

返回物品背包简述（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemDefineID | [FItemDefineID](../../../cppstruct/F/FI/FItemDefineID.md) | 物品 DefineID |

**Return**

- Type: 
- Description: _None_

### GetBigQualityTexturePath

获取品质色的128*256纹理路径(废弃，结果同GetQualityTexturePath)
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

### GetEquipmentQualityTexturePath

获取装备品质色条纹理路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| QualityRank | `number` | 品质等级 |

**Return**

- Type: 
- Description: _None_

### GetWeaponSlotAttachItemIDs

获取武器配件槽位可用配件的物品ID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 武器的物品ID |
| SlotName | `string` | 武器槽位名 |

**Return**

- Type: 
- Description: _None_

### GetPickupWrapperListByItemID

根据物品ID查询拾取物
生效范围：服务器&客户端, 客户端仅查询本地生成的

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品ID |

**Return**

- Type: 
- Description: _None_

### GetPickupWrapperListByCustomType

根据自定义类型查询拾取物
生效范围：服务器&客户端, 客户端仅查询本地生成的

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CustomType | `string` | 自定义类型 |

**Return**

- Type: 
- Description: _None_

### GetPickupWrapperListByItemTag

根据物品Tag查询拾取物
生效范围：服务器&客户端, 客户端仅查询本地生成的

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemTag | `string` | 物品Tag |

**Return**

- Type: 
- Description: _None_

### SetEquipSlotEnable

启用物品槽位
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DefineID | [FItemDefineID](../../../cppstruct/F/FI/FItemDefineID.md) | 物品DefineID |
| SlotName | `string` | 槽位名 |

**Return**

_None_

### GetEquipSlotEnable

获取物品槽位是否启用
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DefineID | [FItemDefineID](../../../cppstruct/F/FI/FItemDefineID.md) | 物品DefineID |
| SlotName | `string` | 槽位名 |

**Return**

- Type: 
- Description: _None_

### StartCustomizeDrop

指定掉落方案进行一次 Wrapper 掉落
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DropLocation | [FVector](../../../cppstruct/F/FV/FVector.md) | 掉落中心点 |
| ProduceID | `number` | 掉落方案ID |
| ProduceGroupID | `number` | 掉落组方案ID(掉落组ID不为-1，掉落组ID生效。掉落组ID为-1,则掉落ID生效) |
| EntityType | [EUGCGenerateItemEntityType](../../../cppenum/E/EU/EUGCGenerateItemEntityType.md) | 掉落物类型(可缺省，默认为Wrapper) |
| RelatedPlayer | `PlayerPawn` | 当掉落物方向为面相玩家时必须，当掉落物类型为进入背包时必须，其他时候可以为nil |
| DropActorClass | `UClass` | 掉落主体Actor类型，应继承自 UGCDropActor_BP, 可以为nil。通过创建自定义蓝图，配置掉落详细参数（掉落间隔、随机掉落范围等等）。 |

**Return**

_None_

### FindAllNearPickupItemData

找到所有玩家角色附近的地面拾取物
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### FindPickupWrapperActorByRange

查找指定距离范围内的地面拾取物
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Center | [FVector](../../../cppstruct/F/FV/FVector.md) | 中心点坐标 |
| DistanceRange | `number` | 查找距离 |

**Return**

- Type: 
- Description: _None_

### TryPickupWrapperItem

玩家角色尝试拾取地面物品（不播拾取动作）
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| TargetWrapper | [AActor](../../Others/AActor.md) | 目标地面拾取物 |
| ItemDefineID | [FItemDefineID](../../../cppstruct/F/FI/FItemDefineID.md) | 要拾取的物品 DefineID，可缺省，默认取 TargetWrapper 中的物品实例数据 |
| PickupCount | `number` | 拾取数量，可缺省，默认拾取1个 |
| CheckPickupCondition | `boolean` | 是否检查拾取条件(距离、是否穿墙等)，可缺省，默认为 true |

**Return**

_None_

### SpawnPickupWrapper

创建地面拾取物
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) | 创建位置 |
| ItemID | `number` | 拾取物物品ID |
| Count | `number` | 拾取物物品数量 |
| CustomData | `table` | 物品自定义实例化数据(可缺省，默认无自定义实例化数据) |

**Return**

- Type: 
- Description: _None_

### GetUGCPickUpListComponent

获取拾取组件(客户端）
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Player | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |

**Return**

- Type: 
- Description: _None_

### PauseAutoPick

暂停指定物品的自动拾取
生效范围：客户端
优先使用新拾取组件，若不存在则走经典面板逻辑

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPlayer | `PlayerPawn \| PlayerController \| nil @可选，玩家角色或控制器，不传则自动获取` | 可选，玩家角色或控制器，不传则自动获取 |

**Return**

_None_

### StopPick

停止拾取（清空拾取列表，关闭数据更新）
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPlayer | `PlayerPawn \| PlayerController \| nil @可选，玩家角色或控制器，不传则自动获取` | 可选，玩家角色或控制器，不传则自动获取 |

**Return**

_None_

### StartPick

开始拾取（开启数据更新）
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPlayer | `PlayerPawn \| PlayerController \| nil @可选，玩家角色或控制器，不传则自动获取` | 可选，玩家角色或控制器，不传则自动获取 |

**Return**

_None_

### GetHeadDamageReduceV2

返回外显装备头部减伤属性（仅支持ItemID，如需FItemDefineID请使用GetHeadDamageReduceV2ByDefineID）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |

**Return**

- Type: 
- Description: _None_

### GetHeadDamageReduceV2ByDefineID

返回外显装备头部减伤属性（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemDefineID | [FItemDefineID](../../../cppstruct/F/FI/FItemDefineID.md) | 物品 DefineID |

**Return**

- Type: 
- Description: _None_

### GetBodyDamageReduceV2

返回外显装备身体减伤属性（仅支持ItemID，如需FItemDefineID请使用GetBodyDamageReduceV2ByDefineID）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |

**Return**

- Type: 
- Description: _None_

### GetBodyDamageReduceV2ByDefineID

返回外显装备身体减伤属性（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemDefineID | [FItemDefineID](../../../cppstruct/F/FI/FItemDefineID.md) | 物品 DefineID |

**Return**

- Type: 
- Description: _None_

### GetItemLevelV2

返回物品等级（仅支持ItemID，如需FItemDefineID请使用GetItemLevelV2ByDefineID）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |

**Return**

- Type: 
- Description: _None_

### GetItemLevelV2ByDefineID

返回物品等级（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemDefineID | [FItemDefineID](../../../cppstruct/F/FI/FItemDefineID.md) | 物品 DefineID |

**Return**

- Type: 
- Description: _None_

### GetBackpackCellV2

返回物品扩容的背包格子数（仅支持ItemID，如需FItemDefineID请使用GetBackpackCellV2ByDefineID）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |

**Return**

- Type: 
- Description: _None_

### GetBackpackCellV2ByDefineID

返回物品扩容的背包格子数（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemDefineID | [FItemDefineID](../../../cppstruct/F/FI/FItemDefineID.md) | 物品 DefineID |

**Return**

- Type: 
- Description: _None_

### GetNewDurabilityV2ByDefineID

返回物品最大耐久度（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemDefineID | [FItemDefineID](../../../cppstruct/F/FI/FItemDefineID.md) | 物品 DefineID |

**Return**

- Type: 
- Description: _None_

### GetPickupWrapperMeshPathV2

返回物品拾取包装体模型路径（仅支持ItemID，如需FItemDefineID请使用GetPickupWrapperMeshPathV2ByDefineID）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品 ID |

**Return**

- Type: 
- Description: _None_

### GetPickupWrapperMeshPathV2ByDefineID

返回物品拾取包装体模型路径（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemDefineID | [FItemDefineID](../../../cppstruct/F/FI/FItemDefineID.md) | 物品 DefineID |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua
