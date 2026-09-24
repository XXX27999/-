# UGCVoiceManagerSystem

语音系统接口库

## Parents

_None_

## Variables

_None_

## Functions

### GetGVoiceInterface

获取 Voice 组件
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetPlayerMemberID

获取玩家的语音房间 MemberID
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerKey | `number` | 角色的 PlayerKey |

**Return**

- Type: 
- Description: _None_

### JoinVoiceRoom

加入语音房间
RoomKey 为语音房间唯一标识，可由自己进行拼接
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| RoomKey | `string` | 语音房间 Key |

**Return**

_None_

### QuitVoiceRoom

退出 UGC 语音房间
生效范围：客户端

**Parameters**

_None_

**Return**

_None_

### GetVoiceRoomKey

获取当前房间 RoomKey
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetGlobalVoiceRadius

设置全局语音生效范围
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Radius | `number` | 全局语音半径（单位：cm） |

**Return**

_None_

### SetVoiceRoomSoundEnable

开启/关闭语音房间喇叭
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| IsEnable | `boolean` | 开启或者关闭喇叭 |

**Return**

_None_

### SetVoiceRoomMicrophoneEnable

开启/关闭语音房间麦克风
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| IsEnable | `boolean` | 开启或者关闭麦克风 |

**Return**

_None_

### SetGlobalVoiceSoundEnable

开启/关闭全局语音喇叭
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| IsEnable | `boolean` | 开启或者关闭喇叭 |

**Return**

_None_

### SeGlobalVoiceMicrophoneEnable

开启/关闭 全局语音麦克风
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| IsEnable | `boolean` | 开启或者关闭麦克风 |

**Return**

_None_

### SetVoiceRoomPlayerMuteState

设置语音房间指定玩家语音屏蔽（静音）状态
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MemberID | `number` | 当前房间要被屏蔽的玩家的 UID |
| IsMute | `boolean` | 是否屏蔽 |

**Return**

_None_

### SetGlobalVoicePlayerMuteState

设置全局房间指定玩家语音屏蔽（静音）状态
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MemberID | `number` | 当前房间要被屏蔽的玩家的 MemberID |
| IsMute | `boolean` | 是否屏蔽 |

**Return**

_None_

### IsVoiceRoomSoundEnable

获得语音房间声音（喇叭）开关状态
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsVoiceRoomMicrophoneEnable

获得语音房间麦克风开关状态
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsGlobalVoiceSoundEnable

获得全局语音声音（喇叭）开关状态
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsGlobalVoiceMicrophoneEnable

获得全局语音麦克风开关状态
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### JoinGlobalVoiceRoom

加入全局语音房间（依赖于全局语音房间的某个范围可听可说,区域语音，包厢等等）
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GlobalVoiceRoomId | `number` | 区域小房间的 index |

**Return**

_None_

### QuitGlobalVoiceRoom

退出全局语音房间（区域语音，包厢等等）
生效范围：客户端

**Parameters**

_None_

**Return**

_None_

### CloseCivilVoiceDetect

关闭文明语音检测和 lbs 小号限制
生效范围：客户端

**Parameters**

_None_

**Return**

_None_

### GetNormalizedMicVolume

获取归一化麦克风音量（0-100）
通过 GetMicLevelDB 获取 dB 值，映射到 0-100 的归一化范围
映射公式: normalized = clamp(round((db + 96) / 96 * 100), 0, 100)
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua
