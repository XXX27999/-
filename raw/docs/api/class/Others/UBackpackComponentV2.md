# UBackpackComponentV2

V2背包内核组件

## Parents

- UCommonBackpackComponent
- IUGCItemContainerInterface
- IUGCItemEquipTargetInterface
- IUGCGamePartPlayerComponentInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Warehouse | `UUGCItemWarehouse_Backpack *` | 仓库对象<br>	  基类：UUGCItemWarehouseBase |

## Functions

### RemoveItemNewFlag

移除物品新标记
	  DS、Client 可调用

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DefineID | `FItemDefineID &` | 物品实例ID |

**Return**

- Type: 
- Description: _None_

### EnableItemNewFlag

激活物品新标记
	  DS、Client 可调用

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### DisableItemNewFlag

失效物品新标记
	  DS、Client 可调用

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bForever | `bool` | 是否永久失效 |

**Return**

- Type: 
- Description: _None_

### GetItemIsNew

获取物品是否新标记
	  Client 可调用

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DefineID | `FItemDefineID &` | 物品实例ID |

**Return**

- Type: 
- Description: _None_

### CheckInitPersistCompleted

查询背包是否初始化完成，完成后才可以进行背包操作

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### DisplayBackpackTipsV2

弹出背包Tips，不保证触发时实例数据一致，如需数据请手动传入
	  Server、Client

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TipKey | `FString &` | 用于匹配 BackpackTipsConfig 中配置的 Tips Key |
| ItemDefineID | `FItemDefineID &` | 要展示 Tips 的物品 DefineID |
| Count | `int32` | 物品数量，默认为 0 |
| Reason | [EUGCCommonItemReason](../../cppenum/E/EU/EUGCCommonItemReason.md) |  |

**Return**

- Type: 
- Description: _None_

### ShouldDisplayBackpackTipsV2

是否应弹出该 Tips
	  Server、Client

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TipKey | `FString &` | 用于匹配 BackpackTipsConfig 中配置的 Tips Key |
| ItemDefineID | `FItemDefineID &` | 要判断的物品 DefineID |
| Count | `int32` | 物品数量，默认为 0 |
| Reason | [EUGCCommonItemReason](../../cppenum/E/EU/EUGCCommonItemReason.md) |  |

**Return**

- Type: 
- Description: _None_


## Event

| Name | Type | Description |
| --- | --- | --- |
| CanAddItemV2 |  | 能否添加物品，能添加多少物品<br>	  可重载并自定义<br>	  DS 被调用<br><br>	  能通过此事件，决定调用 AddItemV2 时，允许添加多少物品。<br>	  即使此事件允许添加物品，也可能因为其它限制因素导致物品添加数量减少或添加失败。<br>	  部分强制添加物品的情形，会跳过此事件。 |
| CanAddItemByDefineIDV2 |  | 能否添加物品，能添加多少物品<br>	  可重载并自定义<br>	  DS 被调用<br><br>	  能通过此事件，决定添加某个实例物品时，允许添加多少物品。<br>	  此接口针对具体实例，调用AddItemV2、调用AddItemByDefineIDV2、物品转移等情形都可能触发此事件。<br>	  单次调用 AddItemV2 可能触发多次针对不同实例的 CanAddItemByDefineIDV2 判断。<br>	  即使此事件允许添加物品，也可能因为其它限制因素导致物品添加数量减少或添加失败。<br>	  部分强制添加物品的情形，会跳过此事件。 |
| OnAddItemV2 |  | 当添加物品实例后回调<br>	  可重载并自定义<br>	  DS 被调用<br><br>	  当物品实例被成功添加时触发此事件。<br>	  单次 AddItemV2 可能触发多次针对不同实例的 OnAddItem 调用（生成多个堆叠的情况）。<br>	  如果物品触发了自动装备，可能装备相关事件会先于 OnAddItemV2 被触发。 |
| CanMergeItemV2 |  | 能否合并物品(将新增的物品叠加到已有格子上)<br>	  可重载并自定义<br>	  DS 被调用<br><br>	  能通过此事件，决定多少物品能堆叠到已有堆叠（ItemDefineID）上。<br>	  此接口针对具体实例，调用AddItemV2、调用AddItemByDefineIDV2、物品转移等情形都可能触发此事件。<br>	  单次 AddItemV2 可能触发多次针对不同实例的 CanMergeItem 判断（向多个堆叠合并时）。<br>	  即使此事件允许堆叠物品，也可能因为其它限制因素导致物品堆叠数量减少或堆叠失败。<br>	  部分情形下会跳过此事件。 |
| OnMergeItemV2 |  | 当合并物品后回调(将新增的物品叠加到已有格子上)<br>	  可重载并自定义<br>	  DS 被调用<br><br>	  此接口针对具体实例，调用AddItemV2、调用AddItemByDefineIDV2、物品转移等情形都可能触发此事件。<br>	  单次 AddItemV2 可能触发多次针对不同实例的 OnMergeItemV2 事件（向多个堆叠合并时）。 |
| CanRemoveItemV2 |  | 能否移除物品，能移除多少物品<br>	  可重载并自定义<br>	  DS、Client 被调用<br><br>	  能通过此事件，决定多少物品能被移除。<br>	  此接口针对具体实例，调用RemoveItemV2、调用RemoveItemByDefineIDV2、物品转移等情形都可能触发此事件。<br>	  单次 RemoveItemV2 可能触发多次针对不同实例的 CanRemoveItemV2 判断（单个堆叠数量不足时）。<br>	  即使此事件允许移除物品，也可能因为其它限制因素导致移除数量减少或移除失败。<br>	  部分情形下会跳过此事件。 |
| OnRemoveItemV2 |  | 当移除物品后回调<br>	  可重载并自定义<br>	  DS 被调用<br><br>	  此接口针对具体实例，调用RemoveItemV2、调用RemoveItemByDefineIDV2、物品转移等情形都可能触发此事件。<br>	  单次 RemoveItemV2 可能触发多次针对不同实例的 OnRemoveItemV2 事件（单个堆叠数量不足时）。 |
| CanDropItemV2 |  | 能否丢弃物品，能丢弃多少物品<br>	  可重载并自定义<br>	  DS、Client 被调用<br><br>	  能通过此事件，决定多少物品能被丢弃。<br>	  此接口针对具体实例，调用DropItemV2、调用DropItemByDefineIDV2等情形都可能触发此事件。<br>	  单次 调用 DropItemV2 可能触发多次针对不同实例的 CanDropItemV2 判断（单个堆叠数量不足时）。<br>	  即使此事件允许丢弃物品，也可能因为其它限制因素导致丢弃数量减少或丢弃失败。<br>	  部分情形下会跳过此事件。 |
| OnDropItemV2 |  | 当丢弃物品后回调<br>	  可重载并自定义<br>	  DS 被调用<br><br>	  当物品被成功丢弃时，触发此事件。<br>	  此接口针对具体实例，调用DropItemV2、调用DropItemByDefineIDV2等情形都可能触发此事件。<br>	  单次 DropItemV2 可能触发多次针对不同实例的 OnDropItemV2 事件（单个堆叠数量不足时）。 |
| CanUseItemV2 |  | 能否使用物品<br>	  可重载并自定义<br>	  DS、Client 被调用<br><br>	  DS 触发使用物品时，会触发并判断能否使用。<br>	  即使此事件允许使用物品，也可能因为其它限制因素导致使用失败。<br>	  部分情形下会跳过此事件。<br><br>	  Client 背包UI选中物品时，会触发并判断是否显示使用按钮。 |
| OnUseItemV2 |  | 当物品触发使用后回调<br>	  可重载并自定义<br>	  DS 被调用 |
| OnDisuseItemV2 |  | 当物品触发 DisUseItem 完成后回调<br>	  可重载并自定义<br>	  DS 被调用 |
| CanAttachToSlot_Implementation |  | 其它物品是否能装备到此槽位<br>	  当物品尝试装备在背包槽位时触发<br><br>	  DS 被调用<br><br>	  开发者能通过此事件，决定调用 EquipItemV2 时，是否允许装备。<br>	  即使此事件允许装备物品，也可能因为其它限制因素导致物品装备失败。<br>	  部分强制装备物品的情形，会跳过此事件。 |
| OnAttachToSlot_Implementation |  | 当其它物品装备到此槽位<br>	  当物品成功装备在背包槽位时触发<br><br>	  DS 被调用 |
| OnDetachBySlot_Implementation |  | 当物品成功从背包槽位卸下时触发<br><br>	  DS 被调用 |
| CanAutoEquip |  | 物品能否自动装备<br>	  当配置了自动装备的物品尝试自动装备时触发<br><br>	  DS 被调用<br><br>	  开发者能通过此事件，阻止物品自动装备到背包或Attach到其它物品上。<br>	  手动装备或主动调用装备时，不受此函数影响。 |
| HandleExceedCellCapacity |  | 处理超过格子容量的物品<br>	  普通情况下，背包内容量已满时，无法添加物品。<br>	  但存在特殊情况，背包满容量时依然成功添加物品、原本不占格子的物品变为占用格子、背包容量发生变化。<br>	  超容量物品会被直接移除，移除后在此函数处理保底逻辑<br>	  默认保底逻辑为丢弃到地上<br>	  重写此事件时，请不要将超容量物品在此处重新添加到背包里<br><br>	  可重载并自定义<br>	  DS 被调用 |

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnCellCapacityChange |  | 当背包格子容量改变时广播<br>	  广播范围：服务端 & 客户端 |
| OnMaxCellCapacityChange |  | 当背包格子容量上限改变时广播<br>	  广播范围：服务端 & 客户端 |
| OnWarehouseCellCapacityChange |  | 当仓库格子容量改变时广播<br>	  广播范围：服务端 & 客户端 |
| ItemUsingStateDelegateV2 |  | 背包物品使用状态变化时广播<br>	  广播范围: 服务端 |
| ItemChangeDelegateV2 |  | 当物品实例数据发生改变时广播<br>	  广播范围：服务端 & 客户端 |
| ItemAddDelegateV2 |  | 当新增物品实例时广播<br>	  广播范围：服务端 & 客户端 |
| ItemUpdateDelegateV2 |  | 当物品实例数据更新时广播<br>	  广播范围：服务端 & 客户端 |
| ItemRemoveDelegateV2 |  | 当移除物品实例时广播<br>	  广播范围：服务端 & 客户端 |
| ItemInstanceDataChangeV2 |  | 当背包物品实例化数据发生改变时广播<br>	  广播范围：客户端 |
| ItemAttachParentChangeDelegateV2 |  | 当物品附加的Parent发生改变时广播<br>	  广播范围：服务端 & 客户端<br><br>	  ItemDefineID: 哪个物品的 Parent 发生了改变<br>	  OldAttachItem: 改变之前物品的 Parent<br>	  OldAttachSlotName: 改变之前物品所在的槽位<br>	  NewAttachItem: 改变之后物品的 Parent<br>	  NewAttachSlotName: 改变之后物品所在的槽位<br>	  如果物品是直接装备在背包上，AttachItem 将为空物品 ( TypeSpecificID 为 0 ) ，AttachSlotName 为背包槽位名称。 |
| ItemOperationInfoDelegateV2 |  | 当对物品操作成功后广播<br>	  广播范围：服务端 |

## Language

cpp
