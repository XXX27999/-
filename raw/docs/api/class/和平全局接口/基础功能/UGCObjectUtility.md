# UGCObjectUtility

UObject基础接口库

## Parents

_None_

## Variables

_None_

## Functions

### FindClass

通过类名(短路径)寻找类
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InClassName | `string` | 类名 |

**Return**

- Type: 
- Description: _None_

### LoadClass

通过完整路径加载类，具体路径可以点击 "右键" - "copy reference" 得到路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InClassPath | `string` | 类的路径 |

**Return**

- Type: 
- Description: _None_

### AsyncLoadClass

通过完整路径异步加载蓝图 Class，路径规则与 LoadClass 相同
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InClassPath | `string` | 类的路径 |
| Callback | `function` | lua普通函数或lambda函数, 加载完成的资源会作为参数传给CallBack函数 (注意带函数定义带冒号和不带的区别) |
| Callback_self | [UObject](../../Others/UObject.md) | 这是为了兼容CallBack函数定义带冒号和不带冒号两种情况。如果带冒号(table:func()型,CallBack_self传入table);如果不带冒号,CallBack_self传入nil |

**Return**

- Type: 
- Description: _None_

### FindObject

通过对象名寻找对象，会遍历所有包进行寻找，性能较差，且如果出现冲突，会有警告且返回其中一个
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InObjectName | `string` | 对象名 |

**Return**

- Type: 
- Description: _None_

### LoadObject

通过完整路径加载对象，性能较好
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InObjectPath | `string` | 对象的路径 |

**Return**

- Type: 
- Description: _None_

### AsyncLoadObject

通过完整路径异步加载Object
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InObjectPath | `string` | 对象的路径 |
| Callback | `function` | lua普通函数或lambda函数, 加载完成的资源会作为参数传给CallBack函数 (注意带函数定义带冒号和不带的区别) |
| Callback_self | [UObject](../../Others/UObject.md) | 这是为了兼容CallBack函数定义带冒号和不带冒号两种情况。如果带冒号(table:func()型,CallBack_self传入table);如果不带冒号,CallBack_self传入nil |

**Return**

- Type: 
- Description: _None_

### NewObject

通过包名，类名和对象名创建对象
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Outer | [UObject](../../Others/UObject.md) | Outer 对象 |
| InClass | `UClass` | 类 |
| InObjectName | `string` | 对象名 |

**Return**

- Type: 
- Description: _None_

### NewStruct

创建新结构体对象，优先从已有的对象中查找是否有已创建对象。可传递结构体的构造参数，仅已导出结构体支持构造时赋值，传递非法参数时不保证结果正常。

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InStructName | `string` | 不带 F 的结构体名字（比如 "Transform"、"ItemDefineID"） |
| ... | `any` | 结构体的构造参数 |

**Return**

- Type: 
- Description: _None_

### NewStructAsTable

以 lua table 形式创建新结构体，优先从已有的对象中查找是否有已创建对象。可传递结构体的构造参数，传递非法参数时不保证结果正常。

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InStructName | `string` | 不带 F 的结构体名字（比如 "Transform"、"ItemDefineID"） |
| ... | `any` | 结构体的构造参数 |

**Return**

- Type: 
- Description: _None_

### GetObjectClass

通过一个对象获取对应的类
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InObject | [UObject](../../Others/UObject.md) | 对象实例 |

**Return**

- Type: 
- Description: _None_

### GetObjectOuter

通过一个对象获取对应的包
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InObject | [UObject](../../Others/UObject.md) | 对象实例 |

**Return**

- Type: 
- Description: _None_

### GetObjectName

获取对象的名字
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InObject | [UObject](../../Others/UObject.md) | 对象实例 |

**Return**

- Type: 
- Description: _None_

### GetObjectFullName

获取对象的类名以及完整路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InObject | [UObject](../../Others/UObject.md) | 对象实例 |

**Return**

- Type: 
- Description: _None_

### GetObjectPathName

获取对象的完整路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InObject | [UObject](../../Others/UObject.md) | 对象实例 |

**Return**

- Type: 
- Description: _None_

### IsObjectValid

判断对象是否有效
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InObject | [UObject](../../Others/UObject.md) | 对象实例 |

**Return**

- Type: 
- Description: _None_

### IsA

判断一个对象是否是特定类的实例
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InObject | [UObject](../../Others/UObject.md) | 对象实例 |
| InClass | `UClass` | 类 |

**Return**

- Type: 
- Description: _None_

### MarkAsGarbage

删除对象，将对象标记为带回收的垃圾
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InObject | [UObject](../../Others/UObject.md) | 对象实例 |

**Return**

_None_

### MakeSoftObjectPath

通过完整对象路径创建软路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InObjectPath | `string` | 对象的路径 |

**Return**

- Type: 
- Description: _None_

### GetPathBySoftObjectPath

获取软路径获取对象完整路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSoftObjectPath | [FSoftObjectPath](../../../cppstruct/F/FS/FSoftObjectPath.md) | 对象的软路径 |

**Return**

- Type: 
- Description: _None_

### LoadObjectBySoftPath

通过软路径加载对象
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSoftObjectPath | [FSoftObjectPath](../../../cppstruct/F/FS/FSoftObjectPath.md) | 对象的软路径 |

**Return**

- Type: 
- Description: _None_

### AsyncLoadObjectBySoftPath

通过软路径异步加载对象
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSoftObjectPath | [FSoftObjectPath](../../../cppstruct/F/FS/FSoftObjectPath.md) | 对象的软路径 |
| Callback | `function` | lua普通函数或lambda函数, 加载完成的资源会作为参数传给CallBack函数 (注意带函数定义带冒号和不带的区别) |
| Callback_Self | [UObject](../../Others/UObject.md) | 这是为了兼容CallBack函数定义带冒号和不带冒号两种情况。如果带冒号(table:func()型,CallBack_self传入table);如果不带冒号,CallBack_self传入nil |

**Return**

- Type: 
- Description: _None_

### GetAllActorsOfClass

【废弃】请使用UGCActorComponentUtility.GetAllActorsOfClass
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 世界中任意对象 |
| ActorClass | `UClass` | 要找的Actor对应的类。必须指定，否则结果数组将为空 |

**Return**

- Type: 
- Description: _None_

### RemoveReferencedObject

移除引用关联（如果有UObject泄露等问题，可用此函数手动释放Lua侧对UObject的引用）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | [UObject](../../Others/UObject.md) | 需要释放引用的 UObject |

**Return**

_None_

### GetObjectsOfClass

以 lua table 形式获取某个类的所有对象列表

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Class | `UClass` | 要找的 UObject 对应的类 |
| bIncludeDerivedClasses | `boolean` | 是否包括派生类 |

**Return**

- Type: 
- Description: _None_

### GetObjectsWithOuter

以 lua table 形式获取以目标对象为 Outer 的所有 UObject 列表

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Outer | [UObject](../../Others/UObject.md) | Outer 对象 |
| bIncludeNestedObjects | `boolean` | 是否包括嵌套对象 |

**Return**

- Type: 
- Description: _None_

### ClassIsChildOf

判断一个类是否是另一个类的子类

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TestClass | `UClass` | 子类 |
| ParentClass | `UClass` | 父类 |

**Return**

- Type: 
- Description: _None_

### GetDisplayName

获取对象的显示名称
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | [UObject](../../Others/UObject.md) | 对象实例 |

**Return**

- Type: 
- Description: _None_

### GetClassDefaultObject

获取类默认对象
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Class | `UClass` | 类 |

**Return**

- Type: 
- Description: _None_

### MakeWeakObjectPtr

创建弱对象指针
生效范围：服务器 & 客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InObject | [UObject](../../Others/UObject.md) | 对象 |

**Return**

- Type: 
- Description: _None_

### GetObjectFromWeakObjectPtr

从弱对象指针获取对象
生效范围：服务器 & 客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InWeakObjectPtr | `WeakObjectPtr` | 弱对象指针 |

**Return**

- Type: 
- Description: _None_

### IsWeakObjectPtrValid

判断弱对象指针是否有效
生效范围：服务器 & 客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InWeakObjectPtr | `WeakObjectPtr` | 弱对象指针 |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua
