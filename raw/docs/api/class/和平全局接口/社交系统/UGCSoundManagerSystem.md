# UGCSoundManagerSystem

语音系统接口库

## Parents

_None_

## Variables

_None_

## Functions

### PlaySound2D

播放 2D 音效
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AKEvent | `UAkAudioEvent` | 音效资源（通过 UE.LoadObject(SoundPath) 获取） |

**Return**

- Type: 
- Description: _None_

### PlaySoundAtLocation

在指定位置播放音效
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AKEvent | `UAkAudioEvent` | 音效资源（通过 UE.LoadObject(SoundPath) 获取），需要导入音效时选 3D |
| Location | `Vector` | 位置 |
| Orientation | `Rotator` | 旋转 可使用 Rotator.New(Roll,Pitch,Yaw) 创建,结构 {Roll=Roll, Pitch=Pitch, Yaw=Yaw} |

**Return**

- Type: 
- Description: _None_

### PlaySoundAttachActor

依附于 Actor 播放音效
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AKEvent | `UAkAudioEvent` | 音效资源（通过 UE.LoadObject(SoundPath) 获取） |
| AttachedActor | `Actor` | 依附的 Actor |
| StopWhenAttachedToDestroyed | `boolean` | 依附的 Actor 销毁时是否停止音效播放 |

**Return**

- Type: 
- Description: _None_

### StopAllSound

停止全部音效
生效范围：客户端

**Parameters**

_None_

**Return**

_None_

### StopSoundByActor

停止指定 Actor 上的所有音效
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | `Actor` | 指定的Actor |

**Return**

_None_

### StopSoundByID

停止指定 ID 的音效
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ID | `number` | 音效 ID |

**Return**

_None_

### PlaySoundWithVolumePitch

在以指定音量音高的方式播放音效，如果播放的是同一个音效，必须在上次播放完成再开始下一个播放，音效资源必须在最新的UGC编辑器上制作生成的
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AKEvent | `UAkAudioEvent` | 音效资源（通过 UE.LoadObject(SoundPath) 获取） |
| AttachedActor | `Actor` | 依附的 Actor |
| Volume | `number` | 范围为-12到12的值 如果不想调整该参数就传一个范围以外的值 |
| Pitch | `number` | 范围为-2400到2400的值 如果不想调整该参数就传一个范围以外的值 |
| StopWhenAttachedToDestroyed | `boolean` | 依附的 Actor 销毁时是否停止音效播放 |

**Return**

- Type: 
- Description: _None_

### PlaySoundWithRange

播放指定时间范围的音频
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AKEvent | `UAkAudioEvent` | 音效资源（通过 UE.LoadObject(SoundPath) 获取） |
| AttachedActor | `Actor` | 依附的 Actor |
| StartTime | `number` | 开始时间 |
| EndTime | `number` | 结束时间 |
| ID | `number` | 音效 ID |

**Return**

_None_

### PlaySoundWithLoop

播放循环音频
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AKEvent | `UAkAudioEvent` | 音效资源（通过 UE.LoadObject(SoundPath) 获取） |
| AttachedActor | `Actor` | 依附的 Actor |

**Return**

_None_

### PlaySoundWith2D

播放2D音频
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AKEvent | `UAkAudioEvent` | 音效资源（通过 UE.LoadObject(SoundPath) 获取） |
| AttachedActor | `Actor` | 依附的 Actor |

**Return**

_None_

### SetSoundListener

切换收音的 Actor(收音监听器)
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ListenerType | `EUGCSoundListenerEnum` | 收音监听器类型 |

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua
