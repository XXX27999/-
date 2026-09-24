# BuffListUI

## 功能概述

支持玩家屏幕的 [Buff](./20087_Buff编辑器.md) 和 [被动技能](../技能编辑器2.0/20110_被动技能.md) 列表 UI，支持展开/收起、动态增删、多行自动排版。

|功能|说明|
|-|-|
|Buff 显示|显示玩家身上的 ``PersistEffectBuff`` 类型效果（需 ``bShowUI = true`` ）|
|被动技能显示|显示已激活且类型为 ``AlwaysShow`` 的被动技能 ( ``UPESkillPassiveSkill`` )|
|展开/收起|点击按钮切换两种模式，收起时显示 11 个 【+】 箭头按钮，展开时最多显示 23 个|
|动态增删|监听 Buff 增删和被动技能状态变化，实时更新 UI|
|多行自动排版|4 个 ``WrapGroupBox`` 容器，按需显隐和分配子项，支持自动换行|
|显示顺序保证|通过 ``SelectSkill()`` 统一排序，确保显示顺序与效果添加顺序一致|

## 快速配置

### 创建BuffListUI

在UI编辑器中，选择 【元件】 → 【系统】 → 【BuffList】 进行创建

![image.png](../../../../_assets/images/6bf32ecf_9MF82image.png)

### 加入到战斗主UI界面显示

BuffList基本没有可手动配置的参数，创建出来后直接使用即可实现对应功能

![image.png](../../../../_assets/images/2224836e_8Mq6uimage.png)

## UI 结构说明

![image.png](../../../../_assets/images/bde7668c_IlGw5image.png)

## 核心数据结构

```lua
-- 内部状态表（定义在文件顶部）
{
    bInitDoOnce = false,          -- 防重复初始化标记
    BuffList = {},                -- Buff 原始列表
    ActivePassives = {},          -- 已激活的被动技能（AlwaysShow 类型）
    DisplayEffects = {},          -- 合并后的待显示效果列表（Buff + 被动技能）
    WrapGroupBoxes = {},          -- 4个容器的引用数组
    IsExpanded = false,           -- 当前是否展开
    ListenComp = nil,             -- 消息监听组件引用
    ShowEffectList = {},          -- 最终实际渲染的效果列表（截取后）
}
```

### 关键数组关系

```lua
角色身上的 Effect 数据
        │
        ▼
  GetAllEffects() ──────────► 原始全量数据
        │
        ▼
  SelectSkill() ─────────────► 过滤+排序
        │                      - Buff: 仅保留 bShowUI=true
        │                      - 被动: 仅保留 ActivePassives 中存在的
        ▼
  DisplayEffects[] ──────────► 合并后待显示列表
        │
        ▼
  UpdateEffectList() ────────► 按模式截取
        │                      - 收起: 最多11个（或12个特殊处理）
        │                      - 展开: 最多23个
        ▼
  ShowEffectList[] ──────────► 最终渲染列表
        │
        ▼
  ArrangeEffects() ──────────► 分配到4个 WrapGroupBox 并刷新UI
```

### 生命周期

![image.png](../../../../_assets/images/19120bfe_02jVXimage.png)

## 显示规则与容量

**模式对比**

|状态|显示数量|特殊条件|
|-|-|-|
|收起 (``IsExpanded=false``)|≤ 11 个|当 ``DisplayEffects == 12`` 时临时改为显示 23 个|
|展开 (``IsExpanded=true``)|≤ 23 个|正常满容量展示|
|≤ 12 个总效果|全部显示|不显示展开按钮|

**展开按钮显隐逻辑**

- DisplayEffects 数量 > 12  →  Button_Expand 可见
- DisplayEffects 数量 ≤ 12  →  Button_Expand 隐藏

**UI 自动分配策略（ArrangeEffects）**

当需要 增加 UI 时：
- 如果 WrapGroupBox_01 未满（<5）→ 直接添加
- 如果 WrapGroupBox_01 已满且有隐藏的 WrapBox → 将01的内容迁移到新WrapBox，再添加新项
- 收起模式下从 WrapGroupBox_04 向前查找空位；特殊情况 DisplayEffects==12 时从01开始

当需要 减少 UI 时：
- 如果 WrapGroupBox_01 有内容 → 从末尾移除
- 如果 WrapGroupBox_01 为空 → 从 WrapGroupBox_02~04 中找到有内容的，将其前5个迁移回01并隐藏该WrapBox

## 使用示例

### 基础使用（自动运行）

BuffList_0 是一个自包含组件，一旦被创建并 AddToViewport 即可自动运行：

```lua
-- 在 UGCGameState 或 HUD 的 Lua 脚本中
function MyHUD:ReceiveBeginPlay()
    local BuffListClass = UE.LoadClass("/Game/.../BuffList_0.BuffList_0_C")
    local PC = UGCGameSystem.GetLocalPlayerController()

    self.BuffListWidget = UserWidget.NewWidgetObjectBP(PC, BuffListClass)
    if self.BuffListWidget then
        -- 添加到视口即可，内部会自动完成初始化
        self.BuffListWidget:AddToViewport(100)
    end
end
```

组件会自动获取：
1. 获取本地 PlayerController 和 Pawn
2. 绑定 Buff/被动技能的事件监听
3. 首次扫描已有的效果并显示

### 手动触发刷新

```lua
-- 强制刷新所有效果显示
if self.BuffListWidget then
    self.BuffListWidget.DisplayEffects = self.BuffListWidget:SelectSkill()
    self.BuffListWidget:UpdateEffectList()
end
```

### 程序化展开/收起

```lua
-- 代码中控制展开收起（等同于点击按钮）
if self.BuffListWidget then
    self.BuffListWidget.IsExpanded = true  -- 或 false
    self.BuffListWidget.WidgetSwitcher_Expand:SetActiveWidgetIndex(
        self.BuffListWidget.IsExpanded and 0 or 1
    )
    self.BuffListWidget:UpdateEffectList()
end
```

### 查询当前显示状态

```lua
-- 获取当前正在显示的效果数量
local count = self.BuffListWidget:GetCurrentUICount()

-- 获取所有Buff子Widget
local allWidgets = self.BuffListWidget:GetAllWidgetInWrapBox()
for i, widget in ipairs(allWidgets) do
    print(string.format("Slot %d: %s", i, tostring(widget)))
end
```

### 自定义 Buff 过滤

如果需要在 ``SelectSkill()`` 基础上追加额外过滤逻辑：

```lua
-- 可以覆写 SelectSkill 或在其之后做二次过滤
local originalSelect = self.BuffListWidget.SelectSkill
self.BuffListWidget.SelectSkill = function(self)
    local effects = originalSelect(self)
    -- 自定义过滤：例如排除特定ID的Buff
    local filtered = {}
    for _, eff in ipairs(effects) do
        if not self:IsHiddenBuff(eff) then
            table.insert(filtered, eff)
        end
    end
    return filtered
end
```

## 核心 API 参考

### 效果获取函数

|函数名|说明|
|-|-|
|GetAllBuffList|获取玩家身上所有 ``PersistEffectBuff`` 类型的效果|
|GetAllPassiveSkillList|获取玩家所有被动技能|
|GetAllEffects|获取合并的全部效果数据（供 ``SelectSkill()`` 使用）|

### 显示筛选

|函数名|说明|
|-|-|
|SelectSkill|从全部 Effect 中按顺序筛选出需要显示的|

规则：
- 遍历 GetAllEffects() 返回的所有效果
- 如果是 Buff 类型：仅保留 bShowUI == true 的
- 如果是 被动技能类型：仅在 ActivePassives 列表中存在的才保留
- 保持原始顺序（即添加顺序）

### UI 刷新链路

**UpdateEffectList**

截取 DisplayEffects 生成 ShowEffectList，触发重新排版：
1. 根据 ``IsExpanded`` 确定显示上限（11 或 23）
2. 特殊处理：``DisplayEffects`` == 12 时强制上限为 23
3. 控制 ``Button_Expand`` 的显隐
4. 若总数 ≤ 上限：取全部
5. 若总数 > 上限：取最后 N 个（最新添加的优先显示）
6. 调用 ``ArrangeEffects``() 排版

**ArrangeEffects**

根据 ``ShowEffectList`` 长度与当前 UI 数量对比，执行增删操作，然后调用 ``RefreshByShowEffectList()``

**RefreshByShowEffectList**

遍历所有 WrapGroupBox 中的已有子项，逐个设置数据：
- Buff 类型 → 调用 ``SetBuffinfo(buffData)``
- 被动技能类型 → 调用 ``SetPassiveSkillInfo(skillData)``

### 事件回调

|事件函数名|说明|
|-|-|
|OnEffectApplied|新效果添加时的回调|
|OnEffectUnapplied|获取玩家所有被动技能|
|OnExpandButtonClicked|获取合并的全部效果数据（供 ``SelectSkill()`` 使用）|
|OnUpdateItemEffect|WrapGroupBox 创建/更新子项时的回调（通过 ``groupBox.OnUpdateItem`` 绑定）|

### 辅助函数

|函数名|说明|
|-|-|
|CreateOneWrapGroupBoxChildUI|创建单个 ``030_Buff_Item_UIBP`` 子项 Widget 实例|
|GetCurrentUICount|统计4个 ``WrapGroupBox`` 中所有子项的总数|
|GetAllWidgetInWrapBox|获取所有 ``WrapGroupBox`` 中的全部子 ``Widget`` 引用|
|RemoveActivePassive|从 ``ActivePassives`` 数组中移除指定被动技能|
