# UGCGamePartSystem

GamePart系统接口库

## Parents

_None_

## Variables

_None_

## Functions

### GetGamePartConfig

获取指定GamePart的Config
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GamePartName | `string` | GamePart名称 |

**Return**

- Type: 
- Description: _None_

### GetGamePartGlobalActor

获取指定GamePart的GlobalActor
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GamePartName | `string` | GamePart名称 |

**Return**

- Type: 
- Description: _None_

### GetGamePartPlayerComponent

获取指定GamePart的指定玩家的指定PlayerComponent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GamePartName | `string` | GamePart名称 |
| PC | `PlayerController` | 玩家控制器 |
| PlayerComponentName | `string` | PlayerComponent名称 |

**Return**

- Type: 
- Description: _None_

### IsGamePartLoaded

获取指定GamePart是否已加载

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GamePartName | `string` | GamePart名称 |

**Return**

- Type: 
- Description: _None_

### GetAllLoadedGameParts

获取所有已加载的GamePart

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
