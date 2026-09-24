# UGCEntityTypeSystem

实体类型查询系统接口库

## Parents

_None_

## Variables

_None_

## Functions

### IsActorOfEntityType

判断Actor是否属于指定的实体类型
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | [AActor](./AActor.md) | 要检查的Actor |
| EntityTypeName | `string` | 实体类型名称 |

**Return**

- Type: 
- Description: _None_

### GetActorEntityType

获取Actor的实体类型（返回第一个匹配的）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | [AActor](./AActor.md) | 要检查的Actor |

**Return**

- Type: 
- Description: _None_

### GetActorEntityTypes

获取Actor的所有匹配的实体类型
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | [AActor](./AActor.md) | 要检查的Actor |

**Return**

- Type: 
- Description: _None_

### GetAllEntityTypeNames

获取所有已配置的实体类型名称
生效范围：服务器&客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OverlapBoxByEntityType

使用Box形状检测指定EntityType的Actor
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContext | [UObject](./UObject.md) | 世界上下文对象 |
| EntityTypeName | `string` | 实体类型名称 |
| Location | [FVector](../../cppstruct/F/FV/FVector.md) | 检测位置 |
| HalfExtent | [FVector](../../cppstruct/F/FV/FVector.md) | Box的半尺寸（默认值：{X=50, Y=50, Z=50}） |
| Rotation | [FRotator](../../cppstruct/F/FR/FRotator.md) | 旋转角度（默认值：{Pitch=0, Yaw=0, Roll=0}） |

**Return**

- Type: 
- Description: _None_

### OverlapSphereByEntityType

使用Sphere形状检测指定EntityType的Actor
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContext | [UObject](./UObject.md) | 世界上下文对象 |
| EntityTypeName | `string` | 实体类型名称 |
| Location | [FVector](../../cppstruct/F/FV/FVector.md) | 检测位置 |
| Radius | `number` | 球体半径（默认值：100） |

**Return**

- Type: 
- Description: _None_

### OverlapCapsuleByEntityType

使用Capsule形状检测指定EntityType的Actor
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContext | [UObject](./UObject.md) | 世界上下文对象 |
| EntityTypeName | `string` | 实体类型名称 |
| Location | [FVector](../../cppstruct/F/FV/FVector.md) | 检测位置 |
| Radius | `number` | 胶囊体半径（默认值：100） |
| HalfHeight | `number` | 胶囊体半高（默认值：100） |
| Rotation | [FRotator](../../cppstruct/F/FR/FRotator.md) | 旋转角度（默认值：{Pitch=0, Yaw=0, Roll=0}） |

**Return**

- Type: 
- Description: _None_

### IsActorOfClassType

检查Actor是否为指定的类类型
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | [AActor](./AActor.md) | 要检查的Actor |
| ActorClassPath | `string` | Actor类的路径 |

**Return**

- Type: 
- Description: _None_

### IsActorOfAnyClassTypes

检查Actor是否为指定类类型数组中的任意一种
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | [AActor](./AActor.md) | 要检查的Actor |
| ActorClassPaths | `string[]` | Actor类路径数组 |

**Return**

- Type: 
- Description: _None_

### IsActorOfEntityTypeByTag

判断Actor是否属于指定的实体类型（使用GameplayTag）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | [AActor](./AActor.md) | 要检查的Actor |
| EntityTypeTag | [FGameplayTag](../../cppstruct/F/FG/FGameplayTag.md) | 实体类型GameplayTag |

**Return**

- Type: 
- Description: _None_

### IsActorOfEntityTypeByTags

判断Actor是否属于指定的实体类型（使用GameplayTagContainer）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | [AActor](./AActor.md) | 要检查的Actor |
| EntityTypeTags | [FGameplayTagContainer](../../cppstruct/F/FG/FGameplayTagContainer.md) | 实体类型GameplayTag容器 |

**Return**

- Type: 
- Description: _None_

### GetActorEntityTypeAsGameplayTag

获取Actor的实体类型（返回GameplayTag）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | [AActor](./AActor.md) | 要检查的Actor |

**Return**

- Type: 
- Description: _None_

### GetActorEntityTypesAsGameplayTagContainer

获取Actor的所有匹配的实体类型（返回GameplayTagContainer）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | [AActor](./AActor.md) | 要检查的Actor |

**Return**

- Type: 
- Description: _None_

### OverlapBoxByEntityTypeTag

使用Box形状检测指定EntityType的Actor（使用GameplayTag）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContext | [UObject](./UObject.md) | 世界上下文对象 |
| EntityTypeTag | [FGameplayTag](../../cppstruct/F/FG/FGameplayTag.md) | 实体类型GameplayTag |
| Location | [FVector](../../cppstruct/F/FV/FVector.md) | 检测位置 |
| HalfExtent | [FVector](../../cppstruct/F/FV/FVector.md) | Box的半尺寸（默认值：{X=50, Y=50, Z=50}） |
| Rotation | [FRotator](../../cppstruct/F/FR/FRotator.md) | 旋转角度（默认值：{Pitch=0, Yaw=0, Roll=0}） |

**Return**

- Type: 
- Description: _None_

### OverlapBoxByEntityTypeTags

使用Box形状检测指定EntityType的Actor（使用GameplayTagContainer）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContext | [UObject](./UObject.md) | 世界上下文对象 |
| EntityTypeTags | [FGameplayTagContainer](../../cppstruct/F/FG/FGameplayTagContainer.md) | 实体类型GameplayTag容器 |
| Location | [FVector](../../cppstruct/F/FV/FVector.md) | 检测位置 |
| HalfExtent | [FVector](../../cppstruct/F/FV/FVector.md) | Box的半尺寸（默认值：{X=50, Y=50, Z=50}） |
| Rotation | [FRotator](../../cppstruct/F/FR/FRotator.md) | 旋转角度（默认值：{Pitch=0, Yaw=0, Roll=0}） |

**Return**

- Type: 
- Description: _None_

### OverlapSphereByEntityTypeTag

使用Sphere形状检测指定EntityType的Actor（使用GameplayTag）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContext | [UObject](./UObject.md) | 世界上下文对象 |
| EntityTypeTag | [FGameplayTag](../../cppstruct/F/FG/FGameplayTag.md) | 实体类型GameplayTag |
| Location | [FVector](../../cppstruct/F/FV/FVector.md) | 检测位置 |
| Radius | `number` | 球体半径（默认值：100） |

**Return**

- Type: 
- Description: _None_

### OverlapSphereByEntityTypeTags

使用Sphere形状检测指定EntityType的Actor（使用GameplayTagContainer）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContext | [UObject](./UObject.md) | 世界上下文对象 |
| EntityTypeTags | [FGameplayTagContainer](../../cppstruct/F/FG/FGameplayTagContainer.md) | 实体类型GameplayTag容器 |
| Location | [FVector](../../cppstruct/F/FV/FVector.md) | 检测位置 |
| Radius | `number` | 球体半径（默认值：100） |

**Return**

- Type: 
- Description: _None_

### OverlapCapsuleByEntityTypeTag

使用Capsule形状检测指定EntityType的Actor（使用GameplayTag）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContext | [UObject](./UObject.md) | 世界上下文对象 |
| EntityTypeTag | [FGameplayTag](../../cppstruct/F/FG/FGameplayTag.md) | 实体类型GameplayTag |
| Location | [FVector](../../cppstruct/F/FV/FVector.md) | 检测位置 |
| Radius | `number` | 胶囊体半径（默认值：100） |
| HalfHeight | `number` | 胶囊体半高（默认值：100） |
| Rotation | [FRotator](../../cppstruct/F/FR/FRotator.md) | 旋转角度（默认值：{Pitch=0, Yaw=0, Roll=0}） |

**Return**

- Type: 
- Description: _None_

### OverlapCapsuleByEntityTypeTags

使用Capsule形状检测指定EntityType的Actor（使用GameplayTagContainer）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContext | [UObject](./UObject.md) | 世界上下文对象 |
| EntityTypeTags | [FGameplayTagContainer](../../cppstruct/F/FG/FGameplayTagContainer.md) | 实体类型GameplayTag容器 |
| Location | [FVector](../../cppstruct/F/FV/FVector.md) | 检测位置 |
| Radius | `number` | 胶囊体半径（默认值：100） |
| HalfHeight | `number` | 胶囊体半高（默认值：100） |
| Rotation | [FRotator](../../cppstruct/F/FR/FRotator.md) | 旋转角度（默认值：{Pitch=0, Yaw=0, Roll=0}） |

**Return**

- Type: 
- Description: _None_

### GetAllEntityTypesAsGameplayTagContainer

获取所有已配置的实体类型（返回GameplayTagContainer）
生效范围：服务器&客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ConvertEntityTypeNameToGameplayTag

将实体类型名称转换为GameplayTag
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EntityTypeName | `string` | 实体类型名称 |

**Return**

- Type: 
- Description: _None_

### ConvertGameplayTagToEntityTypeName

将GameplayTag转换为实体类型名称
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EntityTypeTag | [FGameplayTag](../../cppstruct/F/FG/FGameplayTag.md) | 实体类型GameplayTag |

**Return**

- Type: 
- Description: _None_

### SetConfigDataAssetPath

设置自定义配置DataAsset路径
如果不调用此函数，将使用默认路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ConfigDataAssetPath | `string` | 配置DataAsset的路径 |

**Return**

_None_

### ForceReloadConfig

强制重新加载配置
配合SetConfigDataAssetPath使用，建议设置完路径后调用一次
生效范围：服务器&客户端

**Parameters**

_None_

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua
