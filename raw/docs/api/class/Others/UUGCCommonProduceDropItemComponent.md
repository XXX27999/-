# UUGCCommonProduceDropItemComponent

掉落组件

## Parents

- UCommonProduceDropItemBaseComponent
- IObjectPoolInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| StepTime | `int32` | 每波掉落次数 |
| StepGap | `float` | 每波掉落间隔 |
| DelayDropTime | `float` | 起始掉落延迟 |
| StrategySelector | `FUGCDropItemStrategySelector` | 掉落方案配置 |

## Functions

### StartDrop

按照配置进行一次掉落行为
	  生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DropItemActor | `AActor *` | 需要掉落物资的Actor，一般为配置掉落物组件的Actor本身 |
| Killer | `AController *` | 击杀者或交互者，当掉落物类型为直接进入背包时或者掉落方向为面相玩家时必须，其他时候可以为Null |
| TraceIgnoreActors | `TArray < AActor * >` | 掉落检测射线忽略的Actor数组 |
| AttachComponent | `USceneComponent *` |  |

**Return**

- Type: 
- Description: _None_

### StartDropByProduceID

指定掉落方案进行一次 Wrapper 掉落
	  生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ProduceID | `int32` | 掉落方案ID |
| ProduceGroupID | `int32` | 掉落组方案ID(掉落组ID不为-1，掉落组ID生效。掉落组ID为-1,则掉落ID生效) |
| EntityType | `EUGCGenerateItemEntityType` | 掉落物类型 |
| RelatedPlayer | `ACharacter *` | 当掉落物方向为面相玩家时必须，当掉落物类型为进入背包时必须，其他时候可以为Null |

**Return**

- Type: 
- Description: _None_

### SetBluePrintDropItemConfig

动态设置掉落物组，会强制将掉落物列表生成方式改为蓝图配置
	  生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ConfigItem | `TArray < FUGCGenerateDropItemInfo >` | 需要动态修改的掉落物蓝图配置 |
| EntityType | `EUGCGenerateItemEntityType` | 掉落物类型 |
| ConfigID | `int32` | 需要修改的配置项索引，索引无效时修改失败 |

**Return**

- Type: 
- Description: _None_

### SetProduceIDConfig

动态设置掉落串，会强制将掉落物列表生成方式改为读表
	  生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InProduceID | `int32` | 需要动态修改的掉落方案ID |
| ProduceGroupID | `int32` | 需要动态修改的掉落方案组ID |
| EntityType | `EUGCGenerateItemEntityType` | 掉落物类型 |
| ConfigID | `int32` | 需要修改的配置项索引，索引无效时修改失败 |

**Return**

- Type: 
- Description: _None_

### AddDropConfig

动态添加掉落，按照选择类型添加
	  生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InProduceID | `int32` | 需要添加的掉落方案ID，如果不需要添加读表配置方案请传参-1 |
| ProduceGroupID | `int32` | 需要添加的掉落方案组ID，如果不需要添加读表配置方案请传参-1 |
| ConfigItem | `TArray < FUGCGenerateDropItemInfo >` | 需要添加的掉落物蓝图配置 |
| EntityType | [EUGCGenerateItemEntityType](../../cppenum/E/EU/EUGCGenerateItemEntityType.md) | 掉落物类型 |

**Return**

- Type: 
- Description: _None_

### ClearDropConfig

动态清空配置，蓝图或读表
	  生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SelectType | [EUGCDropItemListGeneratorType](../../cppenum/E/EU/EUGCDropItemListGeneratorType.md) | 需要清空的配置 |

**Return**

- Type: 
- Description: _None_

### SetGeneratorType

动态修改掉落物列表生成方式
	  生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SelectType | [EUGCDropItemListGeneratorType](../../cppenum/E/EU/EUGCDropItemListGeneratorType.md) | 生成方式 |

**Return**

- Type: 
- Description: _None_

### SetDynamicCenterOffset

动态设置掉落圆环偏移
      生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InDynamicCenterOffset | [FVector](../../cppstruct/F/FV/FVector.md) | 偏移量 |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnDropOver |  | 当前掉落结束后触发<br>	  最后一个拾取物被创建时就触发，不会等抛物线动效走完<br>	  广播范围：DS |

## Language

cpp
