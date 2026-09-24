# UGCMultiMode

多模式匹配通用接口库

## Parents

_None_

## Variables

| Name | Type | Description |
| --- | --- | --- |
| UGCMultiMode.NotifyMatchResponseDelegate |  | 通知“开始匹配”的结果。通常会立即通知，然后进入“匹配中”的状态<br>生效范围：客户端<br>@param bSuccess boolean @是否匹配成功。通常来说 true 则把匹配界面切换到匹配中的状态，false 则把匹配界面切换到尚未开始匹配的状态 |
| UGCMultiMode.NotifyMatchSucceededDelegate |  | 通知在“匹配中”的玩家，匹配成功，即将进入新的对局游戏<br>生效范围：客户端 |
| UGCMultiMode.NotifyStatusOfReadyMatchChangedDelegate |  | 通知准备匹配的状态变化<br>生效范围：客户端<br>@param UID number @玩家 UID<br>@param NewStatus EStatusOfReadyMatch @新的准备匹配的状态<br>@param OldStatus EStatusOfReadyMatch @老的准备匹配的状态 |

## Functions

### SetModeChooseUIVisible

设置模式选择 UI 的显示/隐藏
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Visible | `boolean` | 设置为显示/隐藏 |

**Return**

_None_

### SetModeState

设置模式选择 UI 的子模式可选择状态
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ModeID | `number` | 模式 ID |
| ModeAvailability | `boolean` | 设置为可用/不可用 |

**Return**

- Type: 
- Description: _None_

### GetModeID

获取当前模式 ID
生效范围：服务器&客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetModeChooseButtonVisible

设置模式选择打开按钮的显示/隐藏
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Visible | `boolean` | 设置为显示/隐藏 |

**Return**

- Type: 
- Description: _None_

### SetPlayerFill

开启/关闭补人
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bPlayerFill | `boolean` | 目标状态 |

**Return**

_None_

### RequestMatch

开始匹配
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SubModeID | `number` | 子模式 ID |
| ResCallBack | `function` | 一个接受 bool 入参的回调函数，发起匹配的结果返回后会调用该函数 |
| Obj | [UObject](../../Others/UObject.md) | 回调函数所属的对象 |
| IsTeamUnfill | `boolean` | 是否允许不匹配队友开始匹配 |

**Return**

- Type: 
- Description: _None_

### RequestCancelMatch

请求取消匹配
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### RequestReadyMatch

请求进入准备匹配状态
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bReady | `boolean` | 是否准备匹配 |

**Return**

_None_

### QueryStatusOfReadyMatch

查询准备匹配的状态
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UID | `number` | 玩家 UID，可选，如果传入 nil 或者不传入，那么获取自己的准备匹配状态 |

**Return**

- Type: 
- Description: _None_

### GetModeSetting

获取指定ModeID的配置
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ModeID | `number` | ModeID |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua
