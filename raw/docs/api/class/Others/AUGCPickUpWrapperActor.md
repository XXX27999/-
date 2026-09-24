# AUGCPickUpWrapperActor

地面拾取物Actor

## Parents

- [APickUpWrapperActor](../和平类事件/地面可拾取物类/APickUpWrapperActor.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| bPickUpWidgetEnable | `bool` | 是否启用拾取物控件 |
| PickUpWidgetClass | `TSoftClassPtr < UUGCWrapperPositionWidget >` | 拾取物控件蓝图路径 |
| PickUpWidgetLocOffset | [FVector](../../cppstruct/F/FV/FVector.md) | 拾取物控件位置偏移 |
| PickUpWidgetMaxShowNum | `int32` | 拾取物控件最大显示个数 |

## Functions

### OnRep_DefineID_BP

拾取物DefineID更改时触发
	  生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetDefineID

获取拾取物物品的实例ID
	  DS & 客户端 可调用

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetItemCount

获取拾取物物品的物品数量
	  DS & 客户端 可调用

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### TryGetBatchedMeshes

尝试用合批缓存创建并附加组件到拾取物
	  只在客户端有效（IS_CLIENT）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InItemID | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SubmitForCaching

提交源 Actor 给合批缓存；请求被受理后注册替换回调。

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InItemID | `int32` |  |
| SourceActors | `TArray < AActor * > &` | 当前已附加到拾取物的显示用子Actor |

**Return**

- Type: 
- Description: _None_

### CanShowPickUpWidget

拾取物控件是否可见
	  可重载并自定义
	  客户端 被调用

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

| Name | Type | Description |
| --- | --- | --- |
| OnInitPickupWrapper |  | 当地面拾取物初始化后回调<br>	  可重载并自定义<br>	  DS & 客户端 被调用<br><br>	  能通过此事件，实现自定义的初始化逻辑 |
| OnItemPickup |  | 当地面拾取物被拾取后回调<br>	  可重载并自定义<br>	  DS 被调用<br><br>	  能通过此事件，实现自定义的被拾取后处理逻辑 |
| OnItemCountChange |  | 当地面拾取物物品数量改变时回调(拾取物销毁时也会有回调)<br>	  如果是拾取导致的改变，时机略晚于 OnItemPickup<br>	  可重载并自定义<br>	  DS & 客户端 被调用<br><br>	  能通过此事件，实现自定义的物品数量改变处理逻辑 |
| OnUnInitPickupWrapper |  | 当地面拾取物销毁前回调<br>	  可重载并自定义<br>	  DS & 客户端 被调用<br><br>	  能通过此事件，实现自定义的反初始化逻辑 |
| OnBatchedMeshesReplaced |  | 合批结果已替换原始子Actor后回调（用于清空 Lua MeshActorList 等）<br>	  客户端 被调用 |

## Delegate

_None_

## Language

cpp
