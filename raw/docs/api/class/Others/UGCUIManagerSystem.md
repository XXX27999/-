# UGCUIManagerSystem

UI管理器（客户端）

## Parents

_None_

## Variables

_None_

## Functions

### RegisterViewModel

会在依赖它的View创建时实例化

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| VMKey | `string` | ViewModel的Key，与UI的Key相互独立 |
| ViewModel | `UGCViewModel` | ViewModel原型 |

**Return**

_None_

### NewViewModel

创建新的ViewModel
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### NewView

创建新的View，绑定到指定的ViewModel
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### NewItemView

创建新的ItemView（列表项View），用于Collection绑定场景
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### NewCollectionBinder

创建新的UGCMVVMCollectionBinder，用于派生自定义集合绑定器
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### RegisterWidgetUpdater

注册自定义的Widget更新函数
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BindType | `string` | 自定义的绑定类型名 |
| UpdaterFunc | `fun(Widget:userdata, Value:any) @更新函数` | 更新函数 |

**Return**

_None_

### RegisterConverter

注册自定义值转换器
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Name | `string` | 转换器名称 |
| ConverterFunc | `fun(Value:any, ...:any):any @转换函数` | 转换函数 |

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua
