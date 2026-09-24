# UGC_Backpack_Item_UIBP

背包格子控件

@class UGC_Backpack_Item_UIBP_C:UUserWidget
@field CanvasPanel_Lock UCanvasPanel
@field CanvasPanel_CommonItem UCanvasPanel
@field CanvasPanel_New UCanvasPanel
@field UGCCommonDragDropItem UUGCCommonDragDropItem_C
@field HorizontalBox_Unlock UHorizontalBox
@field Text_UnlockCurrencyNum UTextBlock
@field TextBlock_Num UTextBlock
@field Image_Currency UImage

## Parents

_None_

## Variables

_None_

## Functions

### LoadCommonItemWidget

异步加载CommonItem控件（通过UGCBackpackSystemV2外部接口）

**Parameters**

_None_

**Return**

_None_

### ShowSelected

格子显示选中状态

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bSelect | `boolean` | 是否选中 |

**Return**

_None_

### UpdateItemData

更新格子数据(!!!)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemDefineID | `ItemDefineID` | 物品DefineID |
| Count | `number` | 数量 |
| AdditionData | `table` | 控件额外数据, 选中数据/拖拽数据都会包含 |

**Return**

_None_

### UpdateDragData

更新格子拖拽数据(!!!)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DragType | `string` | 拖拽类型，用于区分不同的拖拽处理 |
| DragDirectionMode | `EDragDropDirectionMode` | 默认自由拖拽，若处于滚动列表中，需与滚动方向相反设置 |
| DragClickCallback | `function` | 拖拽点击回调 |
| DragStartCallback | `function` | 拖拽开始回调 |
| DragCancelCallback | `function` | 拖拽取消回调 |

**Return**

_None_

### UpdateItemState

更新格子解锁状态

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| State | [EBackpackItemState](../../cppenum/E/EB/EBackpackItemState.md) | 格子状态, 默认为Unlock |

**Return**

_None_

### SetCustomUIList

设置格子叠加UI

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SoftWidgetPaths | `FSoftClassPath[]` | 叠加UI路径列表 |
| PostCallback | `function` | 叠加UI加载完成回调 {UISlot:挂点Slot, CustomUI:叠加控件} |

**Return**

_None_

### SetUnlockInfo

显示解锁信息

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bShow | `boolean` | 是否显示解锁信息 |
| CoinID | `number` | 代币物品ID |
| CostNum | `number` | 解锁所需代币数量 |

**Return**

_None_

### GetUIData

控件的UI数据

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetIsNewItem

显示 新 标记

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNew | `boolean` | 是否显示 新 标记 |

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua
