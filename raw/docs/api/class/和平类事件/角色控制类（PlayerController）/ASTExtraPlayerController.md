# ASTExtraPlayerController

主角控制器

## Parents

- AUAEPlayerController
- IInGameReconnectingInterface
- IGameplayTaskOwnerInterface
- ISTExtraPlayerController_UGCEventInterface
- IGISPlayerInterface
- IClickActorPCInterface
- IGetCommonBackpackInterface
- IUniversalTaskOwnerInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| BackpackComponent | `UBackpackComponent *` | 背包组件 |

## Functions

### GetPlayerCharacterSafety

获得主角Pawn,如果正在观战,取出来是nullptr

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

| Name | Type | Description |
| --- | --- | --- |
| UGCMoveEvent |  | 角色移动控制事件，需要通过接口GameSystem.SetMoveInputEventEnable开启，每次触发会执行两次该事件，分别返回X和Y值 |
| UGCLookEvent |  | 玩家转向控制事件，需要通过接口GameSystem.SetLookInputEventEnable开启，每次触发会执行两次该事件，分别返回X和Y值 |
| UGC_PlayerLostConnectionEvent |  | 玩家断线事件。 |
| UGC_PlayerReconnectedEvent |  | 玩家重连事件。 |
| UGC_InitializationCompleteEvent |  | 初始化完毕<br>	 生效范围S |
| UGC_PickupItemEvent |  | 获取道具事件，可控制当前道具是否允许获取<br>	 生效范围S |
| UGC_SwitchWeaponControlEvent |  | 切换武器控制事件，可控制当前武器是否允许切换，返回false则无法切换<br>	 生效范围C |
| UGC_StartFireControlEvent |  | 开火控制事件，可控制是否允许开火，返回false则无法开火<br>	 生效范围C |
| UGC_ReloadControlEvent |  | 换弹控制事件，可控制是否允许换弹，返回false则无法换弹<br>	 生效范围C |
| UGC_OpenScopeControlEvent |  | 开镜控制事件，可控制是否允许开镜，返回false则无法开镜<br>	 生效范围C |
| UGC_ThrowGrenadeEvent |  | 投掷控制事件，可控制是否允许投掷，返回false则无法投掷<br>	 生效范围C |
| UGC_IsSpectatingEvent |  | 是否在观战事件<br>	 生效范围SC |
| UGC_FingerMoveEvent |  | 手指移动事件<br>	 生效范围SC |
| UGC_ReleaseScreenEvent |  | 松开屏幕事件<br>	 生效范围SC |
| UGC_TouchScreenEvent |  | 触摸屏幕事件<br>	 生效范围SC |

## Delegate

_None_

## Language

cpp
