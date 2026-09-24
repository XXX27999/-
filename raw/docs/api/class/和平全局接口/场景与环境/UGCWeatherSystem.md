# UGCWeatherSystem

天气系统接口库

## Parents

_None_

## Variables

_None_

## Functions

### LoadWeatherSequence

加载天气序列
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `PlayerController` | 玩家控制器 |
| WeatherSequence | `WeatherSequence` | 天气序列资源 |
| BlendTime | `number` | 过渡时间 |

**Return**

_None_

### UnloadWeatherSequence

卸载天气序列
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `PlayerController` | 玩家控制器 |
| WeatherSequence | `WeatherSequence` | 天气序列资源 |

**Return**

_None_

### SeekWeatherSequence

设置天气序列播放进度
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `PlayerController` | 玩家控制器 |
| WeatherSequence | `WeatherSequence` | 天气序列资源 |
| Time | `number` | 目标时间 |

**Return**

_None_

### PauseWeatherSequence

暂停天气序列
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `PlayerController` | 玩家控制器 |
| WeatherSequence | `WeatherSequence` | 天气序列资源 |

**Return**

_None_

### ResumeWeatherSequence

继续天气序列
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `PlayerController` | 玩家控制器 |
| WeatherSequence | `WeatherSequence` | 天气序列资源 |

**Return**

_None_

### GetCurrentWeatherSequence

获取当前天气序列
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `PlayerController` | 玩家控制器 |

**Return**

- Type: 
- Description: _None_

### GetCurrentWeatherPlayPercentage

获取当前天气播放进度
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `PlayerController` | 玩家控制器 |

**Return**

- Type: 
- Description: _None_

### GetCurrentWeatherTime

获取当前天气时间
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `PlayerController` | 玩家控制器 |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua
