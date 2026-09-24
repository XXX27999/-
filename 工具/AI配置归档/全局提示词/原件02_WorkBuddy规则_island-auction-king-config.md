---
alwaysApply: false
paths: "**/IslandAuctionKing/**"
---

# IslandAuctionKing 功能脚本配置规范

## 按功能分类创建文件夹与配置表规范（全局强制）
1. **禁止全部堆放在同一个表中**：后续所有功能脚本变量存入编辑器表中时，**必须按功能模块/领域创建独立子文件夹与专用配置表（DataTable）存放**，严禁把所有变量都塞在同一个大表（如 AuctionGlobalConfigTable）中。
2. **存放目录与命名规范**：
   - 路径规则：`Asset/Data/Table/Customized/<功能模块名>/<功能模块名>ConfigTable`
   - 常用功能目录示例：
     - UI 布局与容量：`Asset/Data/Table/Customized/UI/UIConfigTable`（或 `UILayoutConfigTable`）
     - 玩法与时长：`Asset/Data/Table/Customized/Gameplay/GameplayConfigTable`（或 `DurationConfigTable`）
     - 结算与补偿：`Asset/Data/Table/Customized/Settlement/SettlementConfigTable`
     - 角色机制：`Asset/Data/Table/Customized/Character/CharacterConfigTable`
     - 情报系统：`Asset/Data/Table/Customized/Intel/IntelConfigTable`
     - 测试与调试：`Asset/Data/Table/Customized/Test/TestConfigTable`
3. **表结构模版规范（统一 4 列结构，全部为字符串类型）**：
   每个功能配置表必须严格按照以下结构建立 4 列：
   - **列 1**：列名 `配置类型`（内部字段 `ValueType`），类型 `字符串`，列注释/提示：`配置值类型：int、float、bool 或 string。`
   - **列 2**：列名 `配置值`（内部字段 `Value`），类型 `字符串`，列注释/提示：`运行时由 AuctionConfig 读取的具体配置值。`
   - **列 3**：列名 `配置说明`（内部字段 `Description`），类型 `字符串`，列注释/提示：`说明配置用途、默认值和修改注意事项。`
   - **列 4**：列名 `修改注意事项`（内部字段 `ModificationNotes`），类型 `字符串`，列注释/提示：`保存配置修改边界、关联依赖和生效方式。`
4. **统一读取与注册**：
   - 新建功能配置表后，必须在 `AuctionConfig`（或配置加载管理器）中注册该表格的读取路径。
   - 配置项行名继续使用稳定的英文点号路径（如 `UI.CharacterSlotCount`、`Settlement.LossCompensationRate`）。
   - 脚本通过 `AuctionConfig.Get*` 读取，必须提供默认回退值并记录读取日志。
5. **扫描与展开要求**：
   - 新增或修改功能脚本时，先扫描该脚本内所有可调变量；任何玩法数值、时长、容量、概率、测试开关、UI 尺寸坐标、提示持续时间或资源路径都必须登记到对应功能的 DataTable 中，不得硬编码。
   - Lua 嵌套表和数组必须展开成标量行（例如 `Duration.Preparing`、`BidThresholds.1`；数组字符串用逗号分隔）。

## 配置命名规范

### UI 容量配置（UI.*）
用于界面槽位数量、容器容量等可调节的 UI 限制。
- UI.CharacterSlotCount - 角色选择界面按钮槽位数量
- UI.PropSlotCount - 道具选择界面列表槽位数量
- UI.InfoCardCount - 情报面板可见卡片数量
- UI.CollectibleSlotCount - 测试UI藏品显示槽数量

### UI 布局常量（UI.*）
用于固定坐标、尺寸、间距等 UI 布局参数。建议按子系统分组。
- UI.InfoCard.FirstTop - 第一张情报卡顶部坐标
- UI.InfoCard.Width - 情报卡背景宽度
- UI.Codex.ItemWidth - 图鉴卡片宽度
- UI.TestWarehouse.StartX - 网页预览仓库布局起点横坐标

### 业务逻辑配置（Character.*, History.*, Intel.*, Gameplay.*）
用于游戏机制相关的数量、触发条件等。
- Character.ExpectedCount - 预期角色总数（用于初始化容量）
- History.MaxEntriesPerKind - 每类历史记录最大条数
- Intel.PublicTriggerRounds - 触发公共情报的竞拍轮次（逗号分隔）
- Gameplay.Duration.Bidding - 竞拍阶段时长

### 测试与开发开关（Test.*, Debug.*）
用于 PIE 调试、自动化测试、日志级别等开发辅助功能。
- Test.AutoRestartEnabled - 对局结束后是否自动重启
- Test.SkipWaitingPhase - PIE启动后是否跳过等待阶段直接进入准备
- Debug.VerboseLogging - 是否输出详细调试日志

### 结算配置（Settlement.*）
- Settlement.LossCompensationRate - 竞拍成功玩家收益亏损时，每位其余参赛玩家获得的亏损补偿比例；当前默认 0.25。

## Lua 读取规范

### 统一读取接口
```lua
local AuctionConfig = UGCGameSystem.UGCRequire("Script.Function.AuctionConfig")

-- 数值配置
local slotCount = AuctionConfig.GetNumber("UI.CharacterSlotCount", 6)

-- 布尔配置
local autoRestart = AuctionConfig.GetBoolean("Test.AutoRestartEnabled", false)

-- 字符串配置
local triggerRounds = AuctionConfig.GetString("Intel.PublicTriggerRounds", "1,3")
```

### 生命周期要求

**❌ 错误示范：模块加载时读取**
```lua
-- 模块加载时表格系统未就绪，GetNumber 将返回默认值
local SLOT_COUNT = AuctionConfig.GetNumber("UI.PropSlotCount", 8)

function SomeService.Initialize()
    for i = 1, SLOT_COUNT do  -- 永远使用默认值 8，表格配置不生效
        -- ...
    end
end
```

**✅ 正确示范：函数内动态读取**
```lua
-- 方式1：模块级辅助函数（推荐用于频繁调用的配置）
local function GetSlotCount()
    return AuctionConfig.GetNumber("UI.PropSlotCount", 8)
end

function SomeService.Initialize()
    local slotCount = GetSlotCount()  -- 运行时读取，表格已加载
    ugcprint("【SomeService+Initialize】关键数据 slotCount=" .. tostring(slotCount))
    for i = 1, slotCount do
        -- ...
    end
end

-- 方式2：直接在函数内读取（推荐用于一次性配置）
function SomeService.Refresh()
    local cardCount = AuctionConfig.GetNumber("UI.InfoCardCount", 5)
    -- ...
end
```

## 生命周期与端侧

1. 配置表在 UGCGameState:ReceiveBeginPlay 表格系统准备完成后由 AuctionConfig.LoadFromTable（或对应模块加载器）显式加载；模块加载阶段不得提前读取运行时表格。
2. 服务端和客户端各自从本地表格加载配置，不需要 RPC 同步。
3. 服务端逻辑必须保留 HasAuthority 校验；客户端只读取配置，不得通过配置表修改服务端权威数据（金币、仓库、出价）。
4. 配置读取失败时必须打印以 【脚本名+函数名】 开头的错误日志，并使用默认值或明确失败，不得静默吞错。

## 新增配置流程

### 1. 确定功能归属与配置名称
- 按功能模块确定存放文件夹和表：如 UI 相关放入 `Asset/Data/Table/Customized/UI/UIConfigTable`
- 行名使用稳定点号分层：`UI.InfoCard.Width`、`Settlement.LossCompensationRate`

### 2. 添加到对应功能配置表
使用 UGCAskQ MCP Python 接口：
```python
import unreal_engine as ue
from unreal_engine.classes import DataTable

# 加载对应功能模块目录下的配置表
table_obj = ue.load_object(DataTable, "/IslandAuctionKing/Asset/Data/Table/Customized/UI/UIConfigTable")
new_row = table_obj.data_table_empty_row()
new_row.ValueType = "int"  # 或 "float", "bool", "string"
new_row.Value = "10"
new_row.Description = "新功能的数量上限"
new_row.ModificationNotes = "修改注意事项：确认关联脚本和默认回退值。边界：整数 >= 1。生效：重新 PIE。"
table_obj.data_table_add_row("UI.NewFeature.MaxCount", new_row)
table_obj.save_package()
```

### 3. 功能脚本中读取
```lua
local AuctionConfig = UGCGameSystem.UGCRequire("Script.Function.AuctionConfig")

local function GetMaxCount()
    return AuctionConfig.GetNumber("UI.NewFeature.MaxCount", 10)
end

function NewFeatureService.DoSomething()
    local maxCount = GetMaxCount()
    ugcprint("【NewFeatureService+DoSomething】关键数据 maxCount=" .. tostring(maxCount))
    -- ...
end
```

### 4. 验证生效
- 重新调试 PIE（配置表修改、初始化逻辑变更时必须）
- 观察配置表加载日志
- 观察功能脚本日志确认读取到正确的配置值

## 修改流程

1. 修改表格资产必须先备份，使用 UGCAskQ MCP 的 Resolve → Plan → Execute 流程；写入后立即回读表结构、行名、类型和值。
2. 修改蓝图或 UI 属性同样必须使用 UGCAskQ MCP，_JsonOutput 仅用于只读核查。
3. 新增功能优先创建独立 Script/Function/*.lua 服务脚本，由其他脚本调用，避免把业务逻辑直接堆入蓝图脚本。
4. 每个新增或修改函数都要有入口、关键数据、分支/错误和出口日志；关键 API 调用使用 pcall 保护。

## 验证

1. 修改普通 Lua 函数体后可热更新；涉及配置表、初始化、组件、事件或蓝图结构时必须重新调试 PIE。
2. 配置表修改后必须重新调试 PIE，PIE 运行中的修改不会生效。
3. 提交前执行 Lua 语法检查，核对配置行名与 AuctionConfig.Get* 路径一致，并记录实际验证结果。

## 常见错误

### ❌ 什么时候不应该用配置表
- 纯算法常量（如 PI、UTF-8 掩码）
- 不影响玩法平衡、UI 布局、测试行为的固定值
- 后续不可能需要调整的值

### ❌ 将所有功能配置堆在同一个大表中
- 错误：所有新增变量全部丢在 `AuctionGlobalConfigTable`
- 正确：按功能域在 `Asset/Data/Table/Customized/<Domain>/` 创建专用表并注册

### ❌ 模块加载时读取配置
```lua
local SLOT_COUNT = AuctionConfig.GetNumber("UI.PropSlotCount", 8)  -- 错误：表格未加载
```

### ❌ 硬编码 UI 布局常量
```lua
local INFO_CARD_WIDTH = 677  -- 错误：应从配置表读取
```

### ✅ 正确做法
```lua
local function GetInfoCardWidth()
    return AuctionConfig.GetNumber("UI.InfoCard.Width", 677)
end
```

## 快速检查清单

新增功能时：
- [ ] 已按功能在 `Asset/Data/Table/Customized/<功能模块>/` 下创建/归类配置表
- [ ] 表结构包含 4 列（配置类型、配置值、配置说明、修改注意事项），列提示符合规范
- [ ] 所有可调参数已添加到对应功能配置表
- [ ] 在 `AuctionConfig` 中注册了该配置表
- [ ] 功能脚本通过 AuctionConfig.Get* 读取
- [ ] 读取逻辑在函数内，非模块加载时
- [ ] 提供了合理的默认回退值
- [ ] 重新 PIE 验证生效

修改现有功能时：
- [ ] 识别并迁移硬编码常量
- [ ] 更新所有引用该常量的代码
- [ ] 删除原硬编码声明
- [ ] 添加关键数据日志
- [ ] 重新 PIE 验证生效

## 参考文档
详细规范参见 Script/Function/CONFIG_STANDARDS.md。
