# UGCEMPZoneManager

电磁干扰区管理器

## Parents

_None_

## Variables

| Name | Type | Description |
| --- | --- | --- |
| UGCEMPZoneManager.SuccessfullyGeneratedElectromagnetic |  | param InstanceID number<br>@param CenterLocation FVector |
| UGCEMPZoneManager.SuccessfullyStopElectromagnetic |  | param InstanceID number |
| UGCEMPZoneManager.NormalEndElectromagnetic |  | param InstanceID number |
| UGCEMPZoneManager.SuccessfullyStartElectromagnetic |  | param InstanceID number |
| UGCEMPZoneManager.AffectedElectromagneticPlayers |  | param AffectedPlayerKeys number |
| UGCEMPZoneManager.__EMPZoneMarkTypeID |  |  |
| UGCEMPZoneManager.__EMPZoneMarkInstIDs |  |  |

## Functions

### _ValidateAndClampConfig

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Config | `UGCEMPZoneConfig` |  |

**Return**

- Type: 
- Description: _None_

### _GetInstanceDetailData

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstanceID | `number` |  |

**Return**

- Type: 
- Description: _None_

### _GetConfigByIndex

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Index | `number` |  |

**Return**

- Type: 
- Description: _None_

### _ModifyConfigByIndex

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Index | `number` |  |
| NewConfig | `table` |  |

**Return**

- Type: 
- Description: _None_

### _GetElectromagneticAreaConfigs

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstanceID | `number\|nil` |  |

**Return**

- Type: 
- Description: _None_

### _ConvertToLuaConfigs

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ElectromagneticInstances | `table` |  |

**Return**

- Type: 
- Description: _None_

### _GenerateNextInstanceID

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### _MapLuaConfigToComponent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| LuaConfig | `UGCEMPZoneConfig` |  |

**Return**

- Type: 
- Description: _None_

### _SyncCapsuleRadius

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EMPZoneActor | `AEMPZoneActor` |  |
| InstanceData | `table` |  |

**Return**

- Type: 
- Description: _None_

### _WriteConfigToComponent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Comp | `UEMPZoneControlComponent` |  |
| ComponentConfig | `FEMPZoneCfg` |  |

**Return**

- Type: 
- Description: _None_

### CreateEMPZone

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ConfigID | `string` |  |
| CenterLocation | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

_None_

### _CreateEMPZoneActor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstanceID | `number` |  |

**Return**

- Type: 
- Description: _None_

### DestroyElectromagneticArea

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstanceID | `number` |  |

**Return**

- Type: 
- Description: _None_

### _DestroyAllElectromagneticAreas

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ModifyConfigElectromagneticArea

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ConfigIndex | `number` |  |
| ParameterName | `string` |  |
| NewValue | `any` |  |

**Return**

- Type: 
- Description: _None_

### GetAllConfigElectromagneticArea

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetSpecifyElectromagneticAreaList

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstanceID | `number` |  |

**Return**

- Type: 
- Description: _None_

### _NotifyClientHideMapMark

当 EMPZone 销毁时隐藏小地图标记

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstanceID | `number` |  |

**Return**

_None_

### Client_OnEMPZoneMapMarkShow

[Client RPC] 显示 EMPZone 小地图标记

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstanceID | `number` | 实例ID |
| LocX | `number` | 位置X坐标 |
| LocY | `number` | 位置Y坐标 |
| LocZ | `number` | 位置Z坐标 |
| EffectRadius | `number` | 影响半径 |
| ZoneState | `number` | 区域状态 |

**Return**

_None_

### Client_OnEMPZoneMapMarkHide

[Client RPC] 隐藏 EMPZone 小地图标记

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstanceID | `number` | 实例ID |

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua
