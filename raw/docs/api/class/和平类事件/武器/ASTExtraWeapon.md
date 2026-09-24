# ASTExtraWeapon

武器基类

## Parents

- [AActor](../../Others/AActor.md)
- IOwnerRelevancyDependencyInterface
- IRegionObjectInterface
- IActorHiddenInterface
- IAttrModifyInterface
- IActorFeedbackInterface
- IGenericAbilityCarrierInterface
- IGameAttributeCarrierInterface
- ILogicEffectInterface
- IUAESharedModuleInterface
- IOwnershipChainInterface

## Variables

_None_

## Functions

_None_

## Event

| Name | Type | Description |
| --- | --- | --- |
| OnWeaponMeshLoadFinished |  | 武器加载模型完毕的接口，之后可以获取武器的MeshComponent<br>	 生效范围：C |

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnWeaponDrawHUDDelegate |  | Delegate<br>	  生效范围C<br>	  武器绘制HUD事件，传入武器的HUDWidiget， Canvas |
| OnPressingWeaponFuncBtnDelegate |  | Delegate<br>	  生效范围C<br>	  持续按键事件，有DeltaTime传入 |
| UGC_AttachmentChangeDelegate |  | 武器配件装卸委托<br><br>	  生效范围SC |
| OnWeaponTriggerEventDelegate |  | Delegate<br>	  生效范围C<br>	  武器按键事件 |
| OnWeaponAttachToBackpackDelegate |  | Delegate<br>	  生效范围SC<br>	  武器挂背事件 |

## Language

cpp
