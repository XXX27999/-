# AUGCGameModeBase

游戏模式类

## Parents

- ASTExtraGameFramework
- IUGCGetDynamicConfigInterface
- IUGCGraphicScriptInterface

## Variables

_None_

## Functions

_None_

## Event

| Name | Type | Description |
| --- | --- | --- |
| UGC_PlayerPreLoadingEvent |  | 玩家预加载事件，此时玩家还在Loading中，尚未触发PostLogin，PlayerController尚未创建。<br>	  生效范围S |
| UGC_PlayerLoginEvent |  | 玩家Loading结束，进入游戏，PlayerController创建完毕，且数据初始化完成。<br>	  生效范围S |
| UGC_PlayerExitEvent |  | 玩家离开，PlayerController，PlayerPawn，PlayerState等玩家信息即将销毁。<br>	  生效范围S |
| UGC_PlayerKilledEvent |  | 玩家被淘汰事件。<br>	  生效范围S |
| UGC_PlayerRespawnEvent |  | 玩家复活事件。<br>	  生效范围S |
| UGC_SpawnedAIEvent |  | AI创建事件，此时AIController创建完毕，且数据初始化完成。<br>	  生效范围S |
| UGC_PlayerPickUpEvent |  | 玩家拾取事件<br>	 生效范围S |

## Delegate

_None_

## Language

cpp
