# ASTExtraCharacter

角色类

## Parents

- AUAECharacter
- IUAESkillInterface
- ISTBaseBuffCarrierInterface
- IDamageableInterface
- IWeaponOwnerInterface
- IWeaponOwnerProxyFactory
- IAttrModifyInterface
- IItemGenerateInterface
- IObjectPoolInterface
- IActorHiddenInterface
- ILaserSeekAndLockOwnerInterface
- IBulletHitInterface
- IGameAttributeCarrierInterface
- IPickerEffectInterface
- ICustomMovementInterface
- IGenericCharacterInterface
- ITargetFilterInfoProviderInterface
- IStateAbilityInterface
- IOwnershipChainInterface
- IFieldApplyInterface
- ICharacterTypeInterface
- ISkillAbilityInterface

## Variables

_None_

## Functions

_None_

## Event

| Name | Type | Description |
| --- | --- | --- |
| UGC_GetDamageNumberConfigIndex |  | 获取伤害数字配置索引<br>	  生效范围C |
| UGC_PreTakeDamageEvent |  | 受到伤害前，返回值可以修改伤害值<br>	 生效范围S |

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| UGC_OnHPChangedDelegate |  | Delegate<br>	 生效范围SC<br>	 怪物血量变化 |
| UGC_OnTakeDamageDelegate |  | Delegate<br>	 生效范围S<br>	 受到伤害后 |

## Language

cpp
