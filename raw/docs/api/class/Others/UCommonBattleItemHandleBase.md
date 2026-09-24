# UCommonBattleItemHandleBase

通用扩展 ItemHandle 基类

## Parents

- UBattleItemHandleBase
- ICommonBattleItemUseInterface

## Variables

_None_

## Functions

_None_

## Event

| Name | Type | Description |
| --- | --- | --- |
| CanCreateItemHandleV2 |  | 能否创建物品 Handle<br>	  可重载并自定义<br>	  DS 被调用 |
| OnCreateItemHandleV2 |  | 当创建物品 Handle 后回调<br>	  可重载并自定义<br>	  DS 被调用 |
| CanDestoryItemHandleV2 |  | 能否销毁物品 Handle<br>	  可重载并自定义<br>	  DS 被调用 |
| OnDestoryItemHandleV2 |  | 销毁物品 Handle 前回调<br>	  可重载并自定义<br>	  DS 被调用 |
| CanUpdateItemCountV2 |  | 能否更新此物品实例的数量<br>	  可重载并自定义<br>	  DS 被调用 |
| OnUpdateItemCountV2 |  | 物品数量更新后回调<br>	  可重载并自定义<br>	  DS 被调用 |

## Delegate

_None_

## Language

cpp
