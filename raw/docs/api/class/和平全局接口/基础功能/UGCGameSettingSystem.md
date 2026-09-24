# UGCGameSettingSystem

游戏配置通用接口库

## Parents

_None_

## Variables

_None_

## Functions

### GetDeviceLevel

获取设备水平（0=低端机，1=中端机，2=高端机）
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetRenderQualitySetting

获取渲染水平设置（画面品质）
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetRenderStyleSetting

获取渲染风格设置（画面风格）
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### AllowSoftwareOcclusion

是否开启软件遮挡剔除（默认开启）。2D 类游戏建议关闭，否则在手机上层次相近（接近重叠）的物体处，可能会出现（黑屏）闪烁
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnabled | `boolean` | 是否开启 |

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua
