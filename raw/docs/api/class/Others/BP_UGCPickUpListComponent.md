# BP_UGCPickUpListComponent

UGC物品拾取组件

## Parents

_None_

## Variables

| Name | Type | Description |
| --- | --- | --- |
| BP_UGCPickUpListComponent.RefreshInterval |  |  |
| BP_UGCPickUpListComponent.bCanAutoPickC |  |  |
| BP_UGCPickUpListComponent.HideForAimC |  |  |
| BP_UGCPickUpListComponent.bNeedRefresh |  |  |
| BP_UGCPickUpListComponent.LastItemCount |  |  |
| BP_UGCPickUpListComponent.LastCheckSum |  |  |
| BP_UGCPickUpListComponent.LastRefreshTime |  |  |
| BP_UGCPickUpListComponent.ItemUsefulCache |  |  |
| BP_UGCPickUpListComponent.PickupItemListCache |  |  |
| BP_UGCPickUpListComponent.TomBoxItemListCache |  |  |
| BP_UGCPickUpListComponent.PickUpFailCooldownMap |  |  |
| BP_UGCPickUpListComponent.PendingPickUpUID |  |  |
| BP_UGCPickUpListComponent.PickupItemListCacheChange |  |  |
| BP_UGCPickUpListComponent.TomBoxItemListCacheChange |  |  |
| BP_UGCPickUpListComponent.bUpDateListDataChange |  |  |

## Functions

### IsWeaponItem

判断物品是否为武器（射击武器，排除近战和弩）
 仅使用V2标签系统
 @param ItemID number 物品ID
 @return boolean, boolean 是否为武器, 是否为手枪

**Parameters**

_None_

**Return**

_None_

### GetHeldWeaponSlotName

获取当前手持武器的装备槽位名
 通过 WeaponManager 获取当前武器槽位 ESurviveWeaponPropSlot，映射到背包槽位名
 @return string|nil 装备槽位名

**Parameters**

_None_

**Return**

_None_

### FindBestEquipSlot

查找最佳装备槽位（仅V2标签）
 返回值说明：
   bestSlot=nil, bMatchAnySlot=false → 不匹配装备槽（背包物品）
   bestSlot=nil, bMatchAnySlot=true  → 装备类但无可用槽位（非武器槽满）
   bestSlot=string, bMatchAnySlot=true → 有可用槽位（引擎通过AddAndEquip自动处理空槽/替换）
 @param ItemID number 物品ID
 @param bIsWeapon boolean 是否为武器
 @return string|nil 最佳槽位名, boolean 物品是否匹配到装备槽

**Parameters**

_None_

**Return**

_None_

### CheckEquipSlot

检查物品的装备槽位信息（纯检查，不执行拾取）
 供主面板调用，根据检查结果决定拾取方式
 @param ItemID number 物品ID
 @return string|nil bestSlot 最佳槽位名
 @return boolean bMatchAnySlot 物品是否匹配到装备槽
 @return boolean bIsWeapon 是否为武器

**Parameters**

_None_

**Return**

_None_

### SortItems

物品排序比较函数：按有用性、规则优先级、自动拾取标记、OrderWeight排序
 @param a table 物品数据A
 @param b table 物品数据B
 @return boolean a是否应该排在b前面

**Parameters**

_None_

**Return**

_None_

### InitPickupRules

【工具函数】初始化拾取规则链
 功能：从蓝图变量PickupRulesCollection读取规则配置，构建规则链PickupRuleChain
 依赖：self.PickupRulesCollection（蓝图变量，Struct_PickUpRules结构体）

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CreateRuleResult

【工具函数】创建规则评估结果
 功能：创建规则评估结果的统一格式，供规则函数返回

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| match | `boolean` | 是否命中该规则 |
| score | `number` | 评分（越高排序越靠前） |
| count | `number` | 需要拾取的数量 |
| autoPick | `boolean` | 是否自动拾取 |

**Return**

_None_

### GetBackpackComponent

【工具函数】获取背包组件
 功能：从PlayerController获取背包组件
 依赖：STExtraBlueprintFunctionLibrary.GetBackpackComponentFromController(PC)

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetWeaponManagerComponent

【工具函数】获取武器管理组件
 功能：从Pawn获取武器管理组件
 依赖：self:GetPawn()、BC:GetWeaponManager()

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetBackpackItemCount

【工具函数】获取背包中指定物品的数量（含已装备的）
 功能：统计背包和装备槽中指定物品的总数量
 依赖：self:GetBackpackComponent()

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemDefineID | [FItemDefineID](../../cppstruct/F/FI/FItemDefineID.md) | 物品定义ID |

**Return**

- Type: 
- Description: _None_

### GetTotalItemCountByID

【工具函数】获取指定ItemID的持有总量（背包 + 已装备武器槽）
 功能：获取物品在背包和装备槽中的总数量，用于武器类物品的RecommendPickCount判断
 依赖：UGCBackpackSystemV2.GetItemDefineIDsByIDV2(PC, ItemID)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品TypeSpecificID |

**Return**

- Type: 
- Description: _None_

### GetItemHandle

【工具函数】获取物品配置Handle
 功能：从UGCItemSystemV2获取物品配置Handle，包含OrderWeight、RecommendPickCount等配置
 依赖：UGCItemSystemV2.GetConfigItemHandle(ItemID)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品ID |

**Return**

- Type: 
- Description: _None_

### GetRecommendPickCount

【工具函数】获取物品推荐拾取数量
 功能：从物品配置Handle中获取推荐拾取数量，nil表示不拾取
 依赖：self:GetItemHandle(ItemID)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品ID |

**Return**

- Type: 
- Description: _None_

### GetItemOrderWeight

【工具函数】获取物品排序权重
 功能：从物品配置Handle中获取排序权重，用于同类物品比较
 依赖：self:GetItemHandle(ItemID)、ItemUtils.GetItemWeightForOrder(ItemID)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品ID |

**Return**

- Type: 
- Description: _None_

### GetItemQuality

【工具函数】获取物品品质等级
 功能：获取物品品质等级（0-5），用于排序和替换判断
 依赖：UGCItemSystemV2.GetItemQualityV2(ItemID)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品ID |

**Return**

- Type: 
- Description: _None_

### GetItemLevel

【工具函数】获取物品等级
 功能：获取物品等级（适用于背包、防具、头盔等装备，如一级/二级/三级）
 依赖：UGCItemSystemV2.GetItemLevelV2(ItemID)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品ID |

**Return**

- Type: 
- Description: _None_

### HasTag

【工具函数】检查物品是否具有指定标签
 功能：使用V2标签系统检查物品是否具有指定标签
 依赖：UGCItemSystemV2.ItemHasTagV2(ItemID, TagName)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `number` | 物品ID |
| TagName | `string` | 标签名 |

**Return**

- Type: 
- Description: _None_

### GetSwitcherConfig

【工具函数】获取背包开关配置
 功能：获取背包系统的开关配置（如自动拾取手枪等）
 依赖：self:GetBackpackComponent()、BackpackComp:GetSwitcherCfgList(configName)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| configName | `string` | 配置名（如"AutoPickUpPistol"） |

**Return**

- Type: 
- Description: _None_

### RuleWeapon

武器规则：排除近战/弩 → 检查槽位（空槽位优先，无空槽位可替换）
 手枪: 当前无手枪+长枪没满+开启"自动拾取手枪" → 自动拾取；可替换槽位 → 自动拾取(低优先)
 长枪: 不足两把 → 自动拾取；可替换槽位 → 自动拾取(低优先)
 @param ItemDefineID FItemDefineID 物品定义ID
 @param Count number 物品数量
 @return table RuleResult

**Parameters**

_None_

**Return**

_None_

### RuleAttachment

配件规则：遍历所有武器检查配件适配性
 有空位 → 拾取；比同槽位配件更好(OrderWeight/品质) → 替换拾取
 快扩(Tag=Item.Attachments.Magazine)最高优先级：品质优先，OrderWeight次之
 普通配件：OrderWeight优先，品质次之
 @param ItemDefineID FItemDefineID 物品定义ID
 @param Count number 物品数量
 @return table RuleResult

**Parameters**

_None_

**Return**

_None_

### RuleAmmo

弹药规则：遍历所有武器检查是否使用此弹药
 需求总量 = RecommendPickCount(配表默认弹药量) * 使用该弹药的武器数
 背包总弹量低于需求总量 → 拾取差值
 @param ItemDefineID FItemDefineID 物品定义ID
 @param Count number 物品数量
 @return table RuleResult

**Parameters**

_None_

**Return**

_None_

### RuleMedicine

药品规则：每种药品单独配置拾取数量(RecommendPickCount)
 背包数量低于推荐值 → 拾取差值
 @param ItemDefineID FItemDefineID 物品定义ID
 @param Count number 物品数量
 @return table RuleResult

**Parameters**

_None_

**Return**

_None_

### RuleThrowable

投掷物规则：背包数量低于RecommendPickCount → 拾取差值
 @param ItemDefineID FItemDefineID 物品定义ID
 @param Count number 物品数量
 @return table RuleResult

**Parameters**

_None_

**Return**

_None_

### GetItemDurabilityRatio

获取物品耐久度比例（当前耐久度/最大耐久度）
 无耐久度词条或满耐久返回1
 @param ItemID number 物品ID
 @param ItemDefineID FItemDefineID|nil 物品DefineID
 @return number 耐久度比例（0~1）

**Parameters**

_None_

**Return**

_None_

### ShouldPickupBetterEquipment

比较两件装备，返回是否应该拾取新装备
 比较优先级：等级 > 品质 > 权重 > 耐久度（仅AvatarEquipment）
 耐久度阈值逻辑：当等级/品质差距在1级以内，耐久度差距超过阈值时，优先考虑耐久度
 @param NewItemID number 新物品ID
 @param OldItemID number 旧物品ID
 @param bIsAttchement boolean 是否为配件
 @param NewItemDefineID FItemDefineID|nil 新物品DefineID
 @param OldItemDefineID FItemDefineID|nil 旧物品DefineID
 @return boolean, number bShouldPickup, score

**Parameters**

_None_

**Return**

_None_

### RuleArmorBackpack

防具背包规则：检查装备槽位，比较装备品质
 有空槽位 → 拾取（检查RecommendPickCount）
 槽位全满 → 使用ShouldPickupBetterEquipment比较装备品质，更好的装备 → 替换拾取
 同时检查 RecommendPickCount 控制拾取数量
 @param ItemDefineID FItemDefineID 物品定义ID
 @param Count number 物品数量
 @return table RuleResult

**Parameters**

_None_

**Return**

_None_

### RuleGeneralOrder

通用排序规则(所有物品)：score = Handle.OrderWeight * 100 + 品质
 用于兜底排序，不触发自动拾取
 @param ItemDefineID FItemDefineID 物品定义ID
 @param Count number 物品数量
 @return table RuleResult

**Parameters**

_None_

**Return**

_None_

### Server_SetEquipReason

服务器端 RPC：设置指定物品的装备Reason（为客户端预测拾取做准备）
 @param PlayerController UserData 玩家控制器（系统自动传入）
 @param ItemDefineID table 物品DefineID

**Parameters**

_None_

**Return**

_None_

### Server_ResetEquipReason

服务器端 RPC：重置指定物品的装备Reason
 @param PlayerController UserData 玩家控制器（系统自动传入）
 @param ItemDefineID table 物品DefineID

**Parameters**

_None_

**Return**

_None_

### GetUGCAvailableServerRPCs

获取RPC列表 (注意不要使用GetAvailableServerRPCs)

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CheckItemIsEquipped

检查指定物品实例是否已装备到任何槽位
 @param PlayerController UserData 玩家控制器
 @param ItemDefineID table 物品实例的 DefineID（通过 totable(MainItemData.ID) 获得）
 @return boolean 该特定物品实例是否已装备

**Parameters**

_None_

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua
