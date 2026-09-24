# ASTExtraShootWeapon

射击武器类

## Parents

- [ASTExtraWeapon](../和平类事件/武器/ASTExtraWeapon.md)

## Variables

_None_

## Functions

_None_

## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnShootWeaponAutoReloadDel |  | Delegate<br>	  生效范围C<br>	  自动换弹事件 |
| OnCurBulletChange |  | Delegate<br>	  生效范围SC<br>	  弹药数量变化事件。注：手动修改会触发开火消耗子弹不触发 |
| OnCurBarrelBulletChangeDelegate |  | Delegate<br>	  生效范围C<br>	  膛内弹药数量变化代理 |
| OnStartFireDelegate |  | Delegate<br>	  生效范围SC<br>	  开火事件 |
| OnStopFireDelegate |  | Delegate<br>	  生效范围SC<br>	  停火事件 |
| OnWeaponShootDelegate |  | Delegate<br>	  生效范围C<br>	  射击事件 |
| OnWeaponReloadStartDelegate |  | Delegate<br>	  生效范围SC<br>	  开始换弹事件 |
| OnWeaponReloadEndDelegage |  | Delegate<br>	  生效范围SC<br>	  结束换弹事件 |
| OnWeaponEquipDelegate |  | Delegate<br>	  生效范围SC<br>	  武器装备事件 |
| OnWeaponUnEquipDelegate |  | Delegate<br>	  生效范围SC<br>	  武器卸载事件 |
| OnLeftLastBulletWhenReloadOneByOneDelegate |  | Delegate<br>	  生效范围SC<br>	  最后一发换弹通知事件 |
| OnBulletHitDelegate |  | Delegate<br>	  生效范围S<br>	  射击武器命中事件 |
| OnShootIntervalModeChangeDelegate |  | Delegate<br>	  生效范围SC<br>	  改变射速模式事件（指的是改变了武器拥有的射速模式） |
| OnChangeAmmoDelegate |  | Delegate<br>	  生效范围SC<br>	  切换武器弹药种类事件 |
| OnClipAmmoDataChangeDelegate |  | Delegate<br>	  生效范围SC<br>	  武器弹夹内弹药数据发生变化事件 |
| OnExplosionProjectileBulletExplodeDelegate |  | Delegate<br>	  生效范围SC<br>	  炮弹爆炸事件 |
| OnScopeIn |  | Delegate<br>	  生效范围C<br>	  开镜事件 |
| OnScopeOut |  | Delegate<br>	  生效范围C<br>	  关镜事件 |
| OnMaxBulletChange |  | Delegate<br>	  生效范围SC<br>	  最大弹药数量变化事件 |
| OnBulletPreShootDelegate |  | Delegate<br>	  生效范围C<br>	  子弹射出预处理事件，带有子弹参数 |
| OnBulletBeforeShootDelegate |  | Delegate<br>	  生效范围C<br>	  子弹射出事件，带有子弹参数 |
| OnBulletPostShootDelegate |  | Delegate<br>	  生效范围C<br>	  子弹射出后理事件，带有子弹参数 |

## Language

cpp
