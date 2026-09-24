# UActivityFakePossessComponent

能够将这个Actor的控制权传递给玩家的组件

## Parents

- [UActorComponent](./UActorComponent.md)
- IFakePossessInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| OnPossess | `FFakePossesserChangeDelegate` | 获取控制权事件事件委托<br>	 @param PC 获取到这个Actor控制权的PC |
| OnUnPossess | `FFakePossesserChangeDelegate` | 解除控制权事件委托<br>	 @param PC 解除这个Actor控制权的PC |
| OnUnPossessWithReason | `FFakeUnPossessDelegate` | 解除控制权事件委托<br>	 @param PC 解除这个Actor控制权的PC<br>	 @param Reason 解除控制权的原因 |

## Functions

### FakePossess

生效范围：S
	  让一个PlayerController控制这个Actor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PC | `AController *` | 获得控制权的PlayerController |

**Return**

- Type: 
- Description: _None_

### FakeUnPossess

生效范围：S
	  解除这个Actor上的PC的控制权

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Reason | [EUnPossessReason](../../cppenum/E/EU/EUnPossessReason.md) | 解除控制权的原因 |

**Return**

- Type: 
- Description: _None_

### FakePossessWithAttach

生效范围：S
	  让一个PlayerController控制这个Actor，并将当前控制的角色Attach到这个Actor上

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PC | `AController *` | 获得控制权的PlayerController |
| AttachScene | `USceneComponent *` | Attach到的组件 |
| SocketName | `FName` | Attach到的Socket |
| bMulticastToClient | `bool` |  |

**Return**

- Type: 
- Description: _None_

### FakeUnPossessWithDettach

生效范围：S
	  解除这个Actor上的PC的控制权，并将角色从这个Actor上Detach

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Reason | [EUnPossessReason](../../cppenum/E/EU/EUnPossessReason.md) | 解除控制权的原因 |

**Return**

- Type: 
- Description: _None_

### CanBePossess

生效范围：S
	  获取是否可以由这个Character控制当前Actor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Character | `ASTExtraBaseCharacter *` | 要检查的Character |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
