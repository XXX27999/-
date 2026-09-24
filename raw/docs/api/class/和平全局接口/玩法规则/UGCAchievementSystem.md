# UGCAchievementSystem

徽章专用接口库

## Parents

_None_

## Variables

_None_

## Functions

### AddAchievementProgress

累积徽章进度
计数为覆盖累计，单场内多次调用不会累加计数，需自行计算累计总数单次调用
详细使用流程参考wiki (https://developer.gp.qq.com/wiki/#/lvzhou_huizhang.html)
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerKey | `number` | 玩家PlayerKey |
| AchievementID | `number` | 徽章ID |
| Count | `number` | 徽章计数 |

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua
