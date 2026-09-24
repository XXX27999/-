# 商店分页UI切换模式

> 日期：2026-06-24  
> 功能：绿洲起源闪电商店系统中，多个分页UI（道具/宠物/福利）之间的切换模式，以及子UI叠加弹出模式  
> 项目：pet_paradise

---

## 一、功能概述

闪电商店系统包含三个主分页（道具列表、宠物列表、福利页）以及"确认购买"子UI。页面之间可以互相跳转，且所有页面共享统一的切换流程：

1. **加载**目标UI的蓝图类
2. **创建**UI实例
3. **显示**到视口
4. **关闭/销毁**当前UI

该模式在项目中被多次使用，形成了标准化的代码模式。

---

## 二、实现模式

### 2.1 页面间切换模式（跳转并销毁当前页）

核心步骤（5步），以 [ShanDian_DJLZB.lua](file:///d:/WeGameApps/rail_apps/OasisEraEditor(2001776)/ShadowTrackerExtra/UGCProjects/pet_paradise/Script/Blueprint/Prefabs/UI/ShanDian/ShanDian_DJLZB.lua#L113-L136) 中`ChonWuButton_69_OnClicked`（道具页跳宠物页）为例：

```lua
-- 宠物按钮 → 跳转宠物页 ShanDian_CWJB
function ShanDian_DJLZB:ChonWuButton_69_OnClicked()
    ugcprint("【ShanDian_DJLZB+ChonWuButton_69_OnClicked】=== 开始[跳转宠物页] ===")

    -- 步骤1：获取 PlayerController，失败则提前返回
    local PlayerController = STExtraGameplayStatics.GetFirstPlayerController(self)
    if not PlayerController then
        ugcprint("【ShanDian_DJLZB+ChonWuButton_69_OnClicked】错误: PlayerController为空")
        return nil
    end

    -- 步骤2：通过 UGCGameSystem.GetUGCResourcesFullPath 加载目标UI蓝图类
    local CWClass = UE.LoadClass(UGCGameSystem.GetUGCResourcesFullPath(
        'Asset/Blueprint/Prefabs/UI/ShanDian/ShanDian_CWJB.ShanDian_CWJB_C'))
    if not CWClass then
        ugcprint("【ShanDian_DJLZB+ChonWuButton_69_OnClicked】错误: 无法加载ShanDian_CWJB类")
        return nil
    end

    -- 步骤3：使用 UserWidget.NewWidgetObjectBP 创建UI实例
    local CWUI = UserWidget.NewWidgetObjectBP(PlayerController, CWClass)
    if not CWUI then
        ugcprint("【ShanDian_DJLZB+ChonWuButton_69_OnClicked】错误: 无法创建ShanDian_CWJB实例")
        return nil
    end

    -- 步骤4：AddToViewport 显示新页面（商店内页面 ZOrder=500）
    CWUI:AddToViewport(500)

    -- 步骤5：隐藏并销毁当前UI
    ugcprint("【ShanDian_DJLZB+ChonWuButton_69_OnClicked】宠物页已打开，关闭当前页")
    UGCWidgetManagerSystem.HideWidget(self)
    UGCWidgetManagerSystem.DestroyWidget(self)

    ugcprint("【ShanDian_DJLZB+ChonWuButton_69_OnClicked】=== [跳转宠物页]完毕 ===")
    return nil
end
```

### 2.2 子UI叠加弹出模式（不销毁当前页）

以 [ShanDian_DJLZB.lua](file:///d:/WeGameApps/rail_apps/OasisEraEditor(2001776)/ShadowTrackerExtra/UGCProjects/pet_paradise/Script/Blueprint/Prefabs/UI/ShanDian/ShanDian_DJLZB.lua#L210-L235) 中`OpenQueRenUI`（在道具页上弹出确认购买弹窗）为例：

```lua
--- 打开确认购买UI并加载商品数据（作为DJLZB的子UI）
---@param RowName string 商品行名
local function OpenQueRenUI(self, RowName)
    ugcprint("【ShanDian_DJLZB+OpenQueRenUI】=== 开始[打开确认购买UI] ===, RowName=" .. tostring(RowName))
    local PlayerController = STExtraGameplayStatics.GetFirstPlayerController(self)
    if not PlayerController then
        ugcprint("【ShanDian_DJLZB+OpenQueRenUI】错误: PlayerController为空")
        return
    end
    local QueRenClass = UE.LoadClass(UGCGameSystem.GetUGCResourcesFullPath(
        'Asset/Blueprint/Prefabs/UI/ShanDian/QueRen/QueRen.QueRen_C'))
    if not QueRenClass then
        ugcprint("【ShanDian_DJLZB+OpenQueRenUI】错误: 无法加载QueRen类")
        return
    end
    local QueRenUI = UserWidget.NewWidgetObjectBP(PlayerController, QueRenClass)
    if not QueRenUI then
        ugcprint("【ShanDian_DJLZB+OpenQueRenUI】错误: 无法创建QueRen实例")
        return
    end
    -- 关键差异：ZOrder=501，叠加在当前页（ZOrder=500）之上
    QueRenUI:AddToViewport(501)
    -- 传入数据到子UI
    QueRenUI:LoadProductData(RowName)
    -- 注意：此处不销毁当前页 self，仅叠加弹出
    ugcprint("【ShanDian_DJLZB+OpenQueRenUI】确认购买UI已打开, RowName=" .. tostring(RowName))
    ugcprint("【ShanDian_DJLZB+OpenQueRenUI】=== [打开确认购买UI]完毕 ===")
end
```

### 2.3 关闭当前页（恢复默认布局）

以 [ShanDian_DJLZB.lua](file:///d:/WeGameApps/rail_apps/OasisEraEditor(2001776)/ShadowTrackerExtra/UGCProjects/pet_paradise/Script/Blueprint/Prefabs/UI/ShanDian/ShanDian_DJLZB.lua#L168-L177) 中`Image_686_OnMouseButtonDownEvent`（关闭按钮）为例：

```lua
--- 关闭按钮 → 隐藏并销毁当前UI，恢复默认主界面布局
function ShanDian_DJLZB:Image_686_OnMouseButtonDownEvent(MyGeometry, MouseEvent, ReturnValue)
    ugcprint("【ShanDian_DJLZB+Image_686_OnMouseButtonDownEvent】=== 开始[关闭当前UI] ===")
    -- 恢复默认主界面布局（切回游戏默认UI布局）
    local DefaultLayoutPath = UGCGameSystem.GetUGCResourcesFullPath(
        'Asset/UI/NewUGCWidgetLayoutBlueprint.NewUGCWidgetLayoutBlueprint_C')
    UGCWidgetManagerSystem.SetWidgetLayout(DefaultLayoutPath)
    UGCWidgetManagerSystem.HideWidget(self)
    UGCWidgetManagerSystem.DestroyWidget(self)
    ugcprint("【ShanDian_DJLZB+Image_686_OnMouseButtonDownEvent】=== [关闭当前UI]完毕 ===")
    return nil
end
```

与页面切换的关键区别：关闭时需要调用 `SetWidgetLayout` 恢复默认UI布局，而页面间切换不需要（因为商店页面使用相同的商店布局）。

### 2.4 停留在当前页（忽略跳转）

当用户点击已在当前页的按钮时，不做任何操作：

```lua
-- 道具按钮（已在当前页，不跳转）
function ShanDian_DJLZB:DaoJuButton_172_OnClicked()
    ugcprint("【ShanDian_DJLZB+DaoJuButton_172_OnClicked】已在道具页，忽略跳转")
    return nil
end
```

---

## 三、涉及的API

| API | 调用端 | 说明 |
|-----|--------|------|
| `STExtraGameplayStatics.GetFirstPlayerController(self)` | 客户端 | 获取本地玩家控制器，切换UI前必须判空 |
| `UGCGameSystem.GetUGCResourcesFullPath(path)` | 客户端 | 获取资源完整路径，path 格式为 `'Asset/Blueprint/Prefabs/.../蓝图名.蓝图名_C'` |
| `UE.LoadClass(fullPath)` | 客户端 | 加载蓝图类，返回 `UClass`，使用前必须判空 |
| `UserWidget.NewWidgetObjectBP(PlayerController, UClass)` | 客户端 | 创建 UI Widget 实例，返回 `UUserWidget`，使用前必须判空 |
| `UUserWidget:AddToViewport(ZOrder)` | 客户端 | 添加UI到视口，ZOrder 控制层级 |
| `UGCWidgetManagerSystem.HideWidget(Widget)` | 客户端 | 隐藏Widget（先隐藏再销毁，避免残留） |
| `UGCWidgetManagerSystem.DestroyWidget(Widget)` | 客户端 | 销毁Widget实例，释放资源 |
| `UGCWidgetManagerSystem.SetWidgetLayout(LayoutPath)` | 客户端 | 设置主界面布局（商店页用 `ShanDianZhuUI`，关闭时恢复默认 `NewUGCWidgetLayoutBlueprint`） |

---

## 四、ZOrder 层级约定

| ZOrder | 用途 | 示例 |
|--------|------|------|
| 500 | 商店主页面（道具/宠物/福利页） | `ShanDian_DJLZB`, `ShanDian_CWLZB`, `ShanDian_FL` |
| 501 | 叠加在商店页上的子UI（弹窗类） | `QueRen`（确认购买弹窗） |

---

## 五、关键文件

| 文件 | 说明 | 切换目标 |
|------|------|----------|
| [ShanDian_DJLZB.lua](file:///d:/WeGameApps/rail_apps/OasisEraEditor(2001776)/ShadowTrackerExtra/UGCProjects/pet_paradise/Script/Blueprint/Prefabs/UI/ShanDian/ShanDian_DJLZB.lua) | 道具列表页（含分页按钮跳转到第2页） | 宠物 → `ShanDian_CWJB`, 福利 → `ShanDian_FL`, 下一页 → `ShanDian_DJLZB_2`, 确认购买 → `QueRen` |
| [ShanDian_CWLZB.lua](file:///d:/WeGameApps/rail_apps/OasisEraEditor(2001776)/ShadowTrackerExtra/UGCProjects/pet_paradise/Script/Blueprint/Prefabs/UI/ShanDian/ShanDian_CWLZB.lua) | 宠物列表页 | 道具 → `ShanDian_DJJB`, 福利 → `ShanDian_FL` |
| [ShanDian_FL.lua](file:///d:/WeGameApps/rail_apps/OasisEraEditor(2001776)/ShadowTrackerExtra/UGCProjects/pet_paradise/Script/Blueprint/Prefabs/UI/ShanDian/ShanDian_FL.lua) | 福利页（月卡/季卡购买） | 宠物 → `ShanDian_CWLZB`, 道具 → `ShanDian_DJLZB` |

页面跳转关系图：
```
道具页(DJLZB) <──> 宠物页(CWLZB) <──> 福利页(FL)
     ^                  ^                  ^
     └──────────────────┴──────────────────┘
           三者可通过顶部标签按钮互相跳转
```

---

## 六、注意事项

1. **销毁顺序**：必须先 `HideWidget` 再 `DestroyWidget`，否则可能出现视觉残留或报错。项目中所有切换点均遵循此顺序。

2. **ZOrder 层级**：
   - 同级页面切换用相同的 ZOrder（均为500），切换后旧页面被销毁，不需要层级管理
   - 子UI叠加时用更高 ZOrder（501），确保弹窗显示在页面之上，且不销毁底层页面

3. **布局恢复**：
   - 页面间切换时**不需要**调用 `SetWidgetLayout`，因为商店各页面共用同一个商店布局 `ShanDianZhuUI`
   - 关闭商店（点X按钮）时**必须**调用 `SetWidgetLayout` 恢复默认布局 `NewUGCWidgetLayoutBlueprint`

4. **三步判空**：跳转前必须依次判空 `PlayerController`、加载的 `Class`、创建的 `UI` 实例，每一步失败都应提前 `return nil` 并打印错误日志

5. **路径格式**：`GetUGCResourcesFullPath` 的参数格式固定为 `'Asset/Blueprint/Prefabs/UI/子文件夹/蓝图名.蓝图名_C'`，注意结尾的 `_C` 后缀不可省略

6. **蓝图名对照**：同一个页面的不同tab可能对应不同蓝图（如道具页Tab-1是 `ShanDian_DJJB`，Tab-2是 `ShanDian_DJLZB_2`），跳转前需确认目标蓝图名是否正确

7. **Construct 中统一设置布局**：所有商店页面在 `Construct` 中均执行 `SetWidgetLayout(ShanDianZhuUI)`，确保该页面加载时使用正确的商店主UI布局
