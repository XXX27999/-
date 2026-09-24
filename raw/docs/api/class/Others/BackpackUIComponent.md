# BackpackUIComponent

UGC V2背包UI组件

需启用及配合新背包系统使用，具体参见https://developer.gp.qq.com/wikieditor/#/catalog/20104

## Parents

_None_

## Variables

_None_

## Functions

### PreloadWidgetClasses

预加载所有控件 Class 并缓存：遍历 EBackpackUIComponentConfigKey
Widget_ 前缀对应单个 ClassPath，WidgetList_ 前缀对应 SoftClassPath 数组

**Parameters**

_None_

**Return**

_None_

### GetBackpackDragDropWidget

获取背包拖拽控件类
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### RefreshBackpackBtn

刷新背包入口按钮状态（等级+容量）
 由 OnBackPackCapacityRefresh 委托触发，也可手动调用

**Parameters**

_None_

**Return**

_None_

### CloseLobbyPanel

关闭大厅背包界面(已废弃)
生效范围：客户端

**Parameters**

_None_

**Return**

_None_

### OpenLobbyBackpackMainUI

打开大厅背包界面(已废弃)
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Mode | `number` | 1:背包+装备栏 2:背包+仓库 3:背包+装备栏+仓库 |

**Return**

_None_

### OnOpenBattleMainPanel

背包UI打开后执行

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Panel | [UUserWidget](./UUserWidget.md) | 背包主界面控件 |

**Return**

_None_

### OnCloseBattleMainPanel

背包UI关闭后执行

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Panel | [UUserWidget](./UUserWidget.md) | 背包主界面控件 |

**Return**

_None_

### OnOpenDeletePanel

当打开删除弹窗时调用（仅作为通知钩子，内核已用AddToSlot挂载，此处不处理AddToViewport）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Panel | [UUserWidget](./UUserWidget.md) | 面板控件 |

**Return**

_None_

### OnOpenSavePanel

当打开存入仓库确认弹窗时调用（仅作为通知钩子，内核已用AddToSlot挂载，此处不处理AddToViewport）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Panel | [UUserWidget](./UUserWidget.md) | 面板控件 |

**Return**

_None_

### OnOpenTakeOutPanel

当打开存入背包确认弹窗时调用（仅作为通知钩子，内核已用AddToSlot挂载，此处不处理AddToViewport）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Panel | [UUserWidget](./UUserWidget.md) | 面板控件 |

**Return**

_None_

### ClickLockBackpackItem

点击上锁格子的响应函数
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| type | `number` | 类型 [0:背包数据, 1:仓库数据] |

**Return**

- Type: 
- Description: _None_

### OnClickLockBackpackItem

点击上锁格子后回调(重写ClickLockBackpackItem后不会执行)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Panel | [UUserWidget](./UUserWidget.md) | 弹窗面板，取自ClickLockBackpackItem返回值，可能为nil |

**Return**

_None_

### IsDiscardAreaVisible

是否显示丢弃区域
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnOpenSaveOrWithDrawPanel

当打开存入取出代币时调用（仅作为通知钩子，内核已用AddToSlot挂载，此处不处理AddToViewport）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Panel | [UUserWidget](./UUserWidget.md) | 面板控件 |

**Return**

_None_

### OnOpenDropItemPanel

当打开丢弃物品弹窗时调用（仅作为通知钩子，内核已用AddToSlot挂载，此处不处理AddToViewport）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Panel | [UUserWidget](./UUserWidget.md) | 面板控件 |

**Return**

_None_

### GetUGCAvailableServerRPCs

获取RPC列表 (注意不要使用GetAvailableServerRPCs)

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CompareQuality

默认排序函数
生效范围: 客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Data1 | `table` | 物品数据1 {DefineID:物品DefineID, Idx:格子索引} |
| Data2 | `table` | 物品数据2 {DefineID:物品DefineID, Idx:格子索引} |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua
