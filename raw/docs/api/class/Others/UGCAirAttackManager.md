# UGCAirAttackManager

UGC轰炸区全局管理器

## Parents

_None_

## Variables

| Name | Type | Description |
| --- | --- | --- |
| UGCAirAttackManager.SuccessfullyGeneratedBombing |  | 轰炸区生成成功事件<br>当轰炸区域成功创建并准备开始预警时触发<br>生效范围：服务器&客户端<br>@param InstanceID number @轰炸实例唯一标识符<br>@param CenterLocation FVector @轰炸中心位置坐标 |
| UGCAirAttackManager.SuccessfullyStopBombing |  | 轰炸区停止成功事件<br>当轰炸区域被成功停止（主动停止或异常结束）时触发<br>生效范围：服务器&客户端<br>@param InstanceID number @被停止的轰炸实例唯一标识符 |
| UGCAirAttackManager.NormalEndBombing |  | 轰炸正常结束事件<br>当轰炸区域按计划完成所有炸弹投放后正常结束时触发<br>生效范围：服务器&客户端<br>@param InstanceID number @结束的轰炸实例唯一标识符<br>@param TotalBombsDropped number @实际投放的炸弹总数 |
| UGCAirAttackManager.SuccessfullyStartBombing |  | 轰炸正式开始事件<br>当轰炸预警结束后，开始正式投放炸弹时触发<br>生效范围：服务器&客户端<br>@param InstanceID number @开始轰炸的实例唯一标识符 |
| UGCAirAttackManager.AffectedBombingPlayers |  | 玩家受影响事件<br>当炸弹爆炸并对范围内玩家造成伤害时触发<br>生效范围：服务器&客户端<br>@param BombLocation FVector @炸弹爆炸位置坐标<br>@param AffectedPlayerKeys number[] @受到影响的玩家PlayerKey数组 |
| UGCAirAttackManager.__BombingPromiseFutures |  |  |
| UGCAirAttackManager.__WarningTimers |  |  |
| UGCAirAttackManager.__AirAttackMarks |  |  |
| UGCAirAttackManager.__MarkGraphIDs |  |  |

## Functions

### ExecuteAirAttack

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ConfigInput | `number\|UGCAirAttackConfig` | 空袭配置索引或配置对象 |
| CenterLocation | `FVector\|nil` | 轰炸中心位置，nil时使用原点（系统会自动通过射线检测将炸弹位置修正到地面高度） |

**Return**

- Type: 
- Description: _None_

### AbortAirAttack

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstanceID | `number` | 要终止的空袭实例ID，nil时终止所有空袭 |

**Return**

_None_

### Multicast_ExecuteAirAttack

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BroadcastData | `table` | 广播数据 {InstanceID, Seed, CenterLocation, GeneratedBy} |

**Return**

_None_

### Multicast_AbortAirAttack

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstanceID | `number` | 要终止的空袭实例ID，nil时终止所有空袭 |

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua
