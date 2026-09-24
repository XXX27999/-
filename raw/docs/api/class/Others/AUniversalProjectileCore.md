# AUniversalProjectileCore

通用抛体基类

## Parents

- [AActor](./AActor.md)
- IObjectPoolInterface
- IOwnershipChainInterface

## Variables

_None_

## Functions

_None_

## Event

| Name | Type | Description |
| --- | --- | --- |
| ReceiveOnBounce |  | 弹跳时的额外接口<br>	 生效范围：SC |
| ReceiveLaunchBullet |  | 发射时的额外接口<br>	 生效范围：S |
| SetTarget |  | 修改Target的接口，能触发对应目标修改接口<br>	 生效范围：SC |
| ReceiveOnProjectileDestroyed |  | 销毁时的额外接口<br>	 生效范围：SC |

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnBulletHitDelegate |  | Delegate<br>	  生效范围S<br>	  通用抛体命中事件 |
| OnLaunchBulletDelegate |  | Delegate<br>	  生效范围S<br>	  抛体发射事件 |

## Language

cpp
