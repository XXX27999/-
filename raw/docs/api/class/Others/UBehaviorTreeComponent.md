# UBehaviorTreeComponent

## Parents

- [UBrainComponent](./UBrainComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| NodeInstances | `TArray < UBTNode * >` | instanced nodes |

## Functions

### GetTagCooldownEndTime

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CooldownTag | [FGameplayTag](../../cppstruct/F/FG/FGameplayTag.md) |  |

**Return**

- Type: 
- Description: _None_

### AddCooldownTagDuration

add to the cooldown tag's duration

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CooldownTag | `FGameplayTag` |  |
| CooldownDuration | `float` |  |
| bAddToExistingDuration | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetDynamicSubtree

assign subtree to RunBehaviorDynamic task specified by tag

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InjectTag | `FGameplayTag` |  |
| BehaviorAsset | `UBehaviorTree *` |  |

**Return**

- Type: 
- Description: _None_

### GetUGCMobBTDebugInfo

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OutTreeInfo | `FUGCMobBTDebugInfo &` |  |
| OutBlackBoardInfo | `TArray < FUGCMobBTBlackBoardInfo > &` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
