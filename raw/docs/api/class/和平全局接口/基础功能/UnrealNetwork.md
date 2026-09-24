# UnrealNetwork

虚幻网络库

## Parents

_None_

## Variables

_None_

## Functions

### RepLazyProperty

对声明为复制的Lazy属性执行复制

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetObject | `AActor \| UActorComponent @属性所在的Actor或Component` | 属性所在的Actor或Component |
| PropertyName | `string` | 属性名或路径 |

**Return**

_None_

### CallUnrealRPC

发送可靠单播RPC

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetPlayerController | [APlayerController](../../Others/APlayerController.md) | 目标玩家 |
| TargetObject | `AActor \| UActorComponent @目标Actor或Component` | 目标Actor或Component |
| FunctionName | `string` | RPC函数名 |

**Return**

_None_

### CallUnrealRPC_Unreliable

发送不可靠单播RPC

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetPlayerController | [APlayerController](../../Others/APlayerController.md) | 目标玩家 |
| TargetObject | `AActor \| UActorComponent @目标Actor或Component` | 目标Actor或Component |
| FunctionName | `string` | RPC函数名 |

**Return**

_None_

### CallUnrealRPC_Multicast

发送可靠广播RPC

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetObject | `AActor \| UActorComponent @目标Actor或Component` | 目标Actor或Component |
| FunctionName | `string` | RPC函数名 |

**Return**

_None_

### CallUnrealRPC_Multicast_Unreliable

发送不可靠广播RPC

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetObject | `AActor \| UActorComponent @目标Actor或Component` | 目标Actor或Component |
| FunctionName | `string` | RPC函数名 |

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua
