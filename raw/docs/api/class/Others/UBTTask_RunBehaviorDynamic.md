# UBTTask_RunBehaviorDynamic

RunBehaviorDynamic task allows pushing subtrees on execution stack.
  Subtree asset can be assigned at runtime with SetDynamicSubtree function of BehaviorTreeComponent.

  Does NOT support subtree's root level decorators!

## Parents

- [UBTTaskNode](./UBTTaskNode.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| InjectionTag | [FGameplayTag](../../cppstruct/F/FG/FGameplayTag.md) | Gameplay tag that will identify this task for subtree injection |
| DefaultBehaviorAsset | `UBehaviorTree *` | default behavior to run |
| BehaviorAsset | `UBehaviorTree *` | current subtree |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
