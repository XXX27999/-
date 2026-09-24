# UGCActorComponentUtility

Actor接口库

## Parents

_None_

## Variables

_None_

## Functions

### SpawnActor

在游戏世界中生成指定类型的 Actor
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| ActorClass | `UClass` | 要生成的 Actor 类型，需通过 UGCObjectUtility.LoadClass 加载类引用 |
| Location | `Vector` | 生成位置坐标，推荐使用 {X=1,Y=1,Z=1} 构造 |
| Rotation | `Rotator` | 生成旋转角度，推荐使用 {X=0,Y=0,Z=0} 构造 |
| Scale3D | `Vector` | 可生成缩放比例，推荐使用 {X=1,Y=1,Z=1} 构造，默认值: Vector(0,0,0)，建议使用Vector(1,1,1)保持原始比例 |
| Owner | `Actor` | 新生成 Actor 的所属对象 |

**Return**

- Type: 
- Description: _None_

### DestroyActor

销毁Actor
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InActor | [AActor](../../Others/AActor.md) | Actor |

**Return**

_None_

### ToString

获取Actor的ToString
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InActor | [AActor](../../Others/AActor.md) | Actor |

**Return**

- Type: 
- Description: _None_

### GetOwner

获取Actor的Owner
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InActor | [AActor](../../Others/AActor.md) | Actor |

**Return**

- Type: 
- Description: _None_

### SetOwner

设置Actor的Owner
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InActor | [AActor](../../Others/AActor.md) | Actor |
| InOwner | [AActor](../../Others/AActor.md) | Owner |

**Return**

_None_

### GetUltimateOwnerActor

获取技能，武器，Buff等持有者acotr
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InActor | [AActor](../../Others/AActor.md) | Actor |

**Return**

- Type: 
- Description: _None_

### GetUltimateController

获取技能，武器，Buff等持有者的Controller
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InActor | [AActor](../../Others/AActor.md) | Actor |

**Return**

- Type: 
- Description: _None_

### AttachToActor

附着到Actor上
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InActor | [AActor](../../Others/AActor.md) | Actor |
| InAttachTo | [AActor](../../Others/AActor.md) | 需要附着到的Actor |
| LocationRule | [EAttachmentRule](../../../cppenum/E/EA/EAttachmentRule.md) | 附着位置规则 |
| RotationRule | [EAttachmentRule](../../../cppenum/E/EA/EAttachmentRule.md) | 附着旋转规则 |
| ScaleRule | [EAttachmentRule](../../../cppenum/E/EA/EAttachmentRule.md) | 附着缩放规则 |
| InSocketName | `string` | 需要附着到的SocketName |

**Return**

_None_

### AttachToComponent

附着到Component上
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InActor | [AActor](../../Others/AActor.md) | Actor |
| InAttachTo | [USceneComponent](../../Others/USceneComponent.md) | 需要附着到的Actor |
| LocationRule | [EAttachmentRule](../../../cppenum/E/EA/EAttachmentRule.md) | 附着位置规则 |
| RotationRule | [EAttachmentRule](../../../cppenum/E/EA/EAttachmentRule.md) | 附着旋转规则 |
| ScaleRule | [EAttachmentRule](../../../cppenum/E/EA/EAttachmentRule.md) | 附着缩放规则 |
| InSocketName | `string` | 需要附着到的SocketName |
| bWeldSimulatedBodies | `boolean` | 是否保持相对位置不变/是否焊接为模拟刚体 |

**Return**

_None_

### DetachFromParent

将Component从父Actor上拆离
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InComponent | [USceneComponent](../../Others/USceneComponent.md) | Actor |
| bMaintainWorldPosition | `boolean` | 是否保持位置不变 |
| bCallModify | `boolean` | 是否调用Modify |

**Return**

_None_

### GetRootComponent

获取根组件
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InActor | [AActor](../../Others/AActor.md) | Actor |

**Return**

- Type: 
- Description: _None_

### GetComponentsByOwner

获取Actor上的所有Component
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InActor | [AActor](../../Others/AActor.md) | Actor |

**Return**

- Type: 
- Description: _None_

### GetComponentsByClass

获取Actor上指定类的Component
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InActor | [AActor](../../Others/AActor.md) | Actor |
| InComonentClass | `UClass` | 指定Component的Class |

**Return**

- Type: 
- Description: _None_

### GetComponentsByTag

获取Actor上指定Tag的Component
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InActor | [AActor](../../Others/AActor.md) | Actor |
| InComonentClass | `UClass` | ComponentClass |
| Tag | `string` | Tag |

**Return**

- Type: 
- Description: _None_

### GetAllActorsOfClass

获取指定Class在场景里的所有Actor
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | WorldContextObject |
| ActorClass | `UClass` | ActorClass |

**Return**

- Type: 
- Description: _None_

### GetAllActorsWithTag

获取指定Tag在场景里的所有Actor
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | WorldContextObject |
| Tag | `string` | Tag |

**Return**

- Type: 
- Description: _None_

### GetActorTransform

获取Actor的Transform
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InActor | [AActor](../../Others/AActor.md) | Actor |

**Return**

- Type: 
- Description: _None_

### GetSceneComponentWorldTransform

获取场景组件的世界Transform
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSceneComponent | [USceneComponent](../../Others/USceneComponent.md) | 场景组件 |

**Return**

- Type: 
- Description: _None_

### SetActorTransform

设置Actor的Transform
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InActor | [AActor](../../Others/AActor.md) | Actor |
| InTransform | [FTransform](../../../cppstruct/F/FT/FTransform.md) | Transform |

**Return**

_None_

### HasAuthority

判断是否为权威端
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InActor | [AActor](../../Others/AActor.md) | Actor |

**Return**

- Type: 
- Description: _None_

### CreateAndRegisterComponent

创建并注册组件
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InComponentClass | `UClass` | 要创建组件对应的Class |
| InOuter | [UObject](../../Others/UObject.md) | Outer |
| InComponentName | `string` | 要创建组件对应的Class对应的ObjectName |

**Return**

_None_

### DestroyComponent

销毁组件
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InActor | [AActor](../../Others/AActor.md) | Actor |
| InComponent | [UActorComponent](../../Others/UActorComponent.md) | 要销毁的组件 |

**Return**

_None_

### GetOverlappingActorsWithPrimitiveComponent

获取与PrimitiveComponent重叠的Actor
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPrimitiveComponent | [UPrimitiveComponent](../../Others/UPrimitiveComponent.md) | 组件 |
| Transform | [FTransform](../../../cppstruct/F/FT/FTransform.md) | 组件的Transform |
| ObjectTypes | `ESceneQueryType[]` | 对象类型列表 |
| ActorClassFilter | `UClass` | 要检测的Actor类型（默认值：nil为全部类型的Actor） |
| ActorsToIgnore | `AActor[]` | 需要忽略的Actor列表 |

**Return**

- Type: 
- Description: _None_

### GetActorByActorInstancePath

在运行时通过Actor实例路径获取Actor，对关卡编辑器实例列表里任意Actor右键，选择GetActorInstancePath即可获取路径
生效范围：客户端&服务器
路径格式：PackageName.ObjectPath，例如：UGCmap.test_8

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstancePath | `string` | 实例路径 |

**Return**

- Type: 
- Description: _None_

### SetActorTickEnabled

启用或禁用 Actor 的 Tick
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | [AActor](../../Others/AActor.md) | 目标 Actor |
| bEnabled | `boolean` | 是否启用 Tick |

**Return**

_None_

### IsActorTickEnabled

查询 Actor 的 Tick 是否启用
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | [AActor](../../Others/AActor.md) | 目标 Actor |

**Return**

- Type: 
- Description: _None_

### SetActorLocation

设置 Actor 的世界坐标位置
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | [AActor](../../Others/AActor.md) | 目标 Actor |
| Location | `Vector` | 新坐标位置 |

**Return**

_None_

### GetActorLocation

获取 Actor 的世界坐标位置
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | [AActor](../../Others/AActor.md) | 目标 Actor |

**Return**

- Type: 
- Description: _None_

### SetActorRotation

设置 Actor 的世界旋转
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Rotation | `Rotator` | 新旋转角度 |

**Return**

_None_

### GetActorRotation

获取 Actor 的世界旋转
生效范围：服务器&客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetActorScale

设置 Actor 的缩放
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | [AActor](../../Others/AActor.md) | 目标 Actor |
| Scale | `Vector` | 新的缩放值 |

**Return**

_None_

### GetActorScale

获取 Actor 的缩放
生效范围：服务器&客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetActorVisible

设置 Actor 的可见性
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | [AActor](../../Others/AActor.md) | 目标 Actor |
| bVisible | `boolean` | 是否可见 |

**Return**

_None_

### IsActorVisible

查询 Actor 当前是否可见
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | [AActor](../../Others/AActor.md) | 目标 Actor |

**Return**

- Type: 
- Description: _None_

### GetComponentOwner

获取组件所属的 Actor
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Component | `UComponent` | 任意组件 |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua
