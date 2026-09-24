# ASTExtraBaseCharacter

主角类（PlayerPawn）

## Parents

- [ASTExtraCharacter](../角色类（Pawn）/ASTExtraCharacter.md)
- ISTExtraInputInterface
- IPickupProxyFactory
- ISTExtraBaseCharacter_UGCEventInterface
- IGISPlayerInterface
- IGenericAbilityCarrierInterface
- IItemSkillV2RecevierInterface
- IInteractorInterface
- IDamageNumberInterface
- IMeleeAttackOwnerInterface

## Variables

_None_

## Functions

### DSTeleportToLocationOrRotation

生效范围：服务器
	  传送主角，只有服务器上调用生效，客户端调用无效

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| location | [FVector](../../../cppstruct/F/FV/FVector.md) | 位置 |
| rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | 旋转 |
| setLoc | `bool` | 是否修改位置 |
| setRot | `bool` | 是否修改旋转 |
| ResetVelocity | `bool` | 是否重置速度 |
| bRecordTeleportInfo | `bool` | 是否记录传送时间用于射击校验，如无特殊需求保持默认配置 |

**Return**

- Type: 
- Description: _None_


## Event

| Name | Type | Description |
| --- | --- | --- |
| UGC_WeaponShootBulletEvent |  | 发射子弹事件<br>	 生效范围C |
| UGC_WeaponBulletHitEvent |  | 子弹命中事件<br>	 生效范围SC |
| UGC_ChangeCurrentUsingWeaponEvent |  | 当前武器变化事件<br>	 生效范围SC |
| UGC_EquipWeaponEvent |  | 装备武器事件，仅装备在身上，非当前手持武器<br>	 生效范围SC |
| UGC_WeaponStartFireEvent |  | 开火调用事件，仅在按下开火时调用一次<br>	 生效范围SC |
| UGC_WeaponStopFireEvent |  | 停火调用事件<br>	 生效范围SC |
| UGC_WeaponSwitchEvent |  | 切换武器事件<br>	 生效范围C |
| UGC_ReloadStartEvent |  | 开始换弹事件<br>	 生效范围SC |
| UGC_ReloadEndEvent |  | 换弹结束事件<br>	 生效范围SC |
| UGC_OpenScopeEvent |  | 开镜事件<br>	 生效范围C |
| UGC_CloseScopeEvent |  | 开镜结束事件<br>	 生效范围C |
| UGC_EnterPawnStateEvent |  | 进入某个PawnState事件<br>	 生效范围SC |
| UGC_LeavePawnStateEvent |  | 离开某个PawnState事件<br>	 生效范围SC |
| UGC_PlayerPickUpEvent |  | 玩家拾取事件<br>	 生效范围SC |
| UGC_PlayerDeadEvent |  | 玩家死亡事件<br>	 生效范围SC |
| UGC_TakeDamageOverrideEvent |  | 重载伤害事件，返回值为修改后的伤害<br>	 生效范围S |

## Delegate

_None_

## Language

cpp
