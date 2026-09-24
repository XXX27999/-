# UPESkillWidget

技能UI基类

## Parents

- UUAEUserWidget
- ILuaInterface

## Variables

_None_

## Functions

### BindToSlot

将技能绑定到指定PE组件的指定Slot上
	  生效范围C

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Comp | `UPersistBaseComponent *` | 绑定的组件 |
| SlotName | [FGameplayTag](../../cppstruct/F/FG/FGameplayTag.md) | 绑定的槽位 |

**Return**

- Type: 
- Description: _None_

### GetCurrentSkill

获取当前绑定的技能
	  生效范围C

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### BindImageAndTextForSkillNameAndIcon

绑定用于显示技能图标、名字、描述的控件
	  生效范围C

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| IconImage | `UImage *` | 图标控件 |
| NameText | `UTextBlock *` | 名字控件 |
| DescribeText | `UTextBlock *` | 描述控件 |

**Return**

- Type: 
- Description: _None_

### RefreshSkillUI

刷新当前UI绑定的控件的内容
	  生效范围C

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetSkillName

获取技能名字
	  生效范围C

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetSkillDetail

获取技能描述
	  生效范围C

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetSkillIcon

获取技能图标
	  生效范围C

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### InitButton

绑定技能按钮控件
	  生效范围C

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| IconImage | `UImage *` | 图标控件 |
| NameText | `UTextBlock *` | 名字控件 |
| ClickButton | `UButton *` | 按钮控件 |

**Return**

- Type: 
- Description: _None_

### InitLayer

绑定技能使用层数控件
	  生效范围C

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| LayerText | `UTextBlock *` | 技能层数 |
| LayerPanel | `UPanelWidget *` | 技能层数的Panel控件，控制层数的显隐 |

**Return**

- Type: 
- Description: _None_

### InitCDProgress

绑定技能CD控件
	  生效范围C

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CDText | `UTextBlock *` | 技能CD时间 |
| CDProgressImage | `UImage *` | @技能CD进度条 |
| CDProgressPanel | `UPanelWidget *` | 整个CD的Panel控件，控制CD的显隐 |

**Return**

- Type: 
- Description: _None_

### InitEnergyProgress

绑定技能能量控件
	  生效范围C

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EnergyProgressImage | `UImage *` | 技能能量进度条 |
| EnergyCanvasPanel | `UPanelWidget *` | 技能能量Panel控件，控制能量进度条的显隐 |

**Return**

- Type: 
- Description: _None_

### InitTagDisableState

绑定技能显示TagDisable状态的控件
	  生效范围C

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TagDisableCanvasPanel | `UPanelWidget *` | 技能TagDisable状态的Panel控件，控制TagDisable状态的显隐 |

**Return**

- Type: 
- Description: _None_

### InitEnableState

绑定技能显示Enable状态的控件
	  生效范围C

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EnableCanvasPanel | `UPanelWidget *` | 技能Enable状态的Panel控件，控制Enable状态的显隐 |

**Return**

- Type: 
- Description: _None_

### InitVirtualJoystick

绑定技能摇杆输入控件
	  生效范围C

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| VirtualJoystickPanel | `UPanelWidget *` |  |
| VirtualJoystick | `UPESkillVirtualJoystick *` | 技能技能摇杆控件，控制摇杆的生效和失效 |

**Return**

- Type: 
- Description: _None_


## Event

| Name | Type | Description |
| --- | --- | --- |
| OnSkillBound_BP |  | 当控件绑定到新的技能时触发<br>	  生效范围C |
| UpdateCD_BP |  | 每帧触发，用于更新CD显示<br>	  生效范围C |
| OnCDStateChange_BP |  | 当控件绑定的技能CD状态变化时触发<br>	  生效范围C |
| OnSkillUIInfoChange_BP |  | 当控件绑定的技能的UI信息变化时触发<br>	  生效范围C |
| OnEnableChange_BP |  | 当控件绑定的技能Enable状态变化时触发<br>	  生效范围C |
| OnTagDisableChange_BP |  | 当控件绑定的技能被禁用Tag(PawnState.ActivatingSkill)导致无法激活时触发<br>	  生效范围C |
| OnSkillDirectionInputEnableChange_BP |  | 当控件绑定的技能的摇杆输入生效或失效时触发<br>	  生效范围C |

## Delegate

_None_

## Language

cpp
