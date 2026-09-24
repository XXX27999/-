# 3D角色渲染为2D预览图（RenderTarget + MID）

## 概述

将3D角色模型通过 SceneCaptureComponent2D 渲染到 TextureRenderTarget2D，再作为 UImage 的显示源，实现角色选择界面中的3D预览头像功能。

**核心问题**：`RTF_RGBA32f` 格式的RenderTarget会写入非1.0的Alpha值，直接绑定到 UImage 时人物显示为半透明/仅轮廓可见。

**解决方案**：使用 MaterialInstanceDynamic（MID）+ SetBrushFromMaterial，在材质层面强制 Alpha=1.0 解决透明问题。

---

## 完整实现链路

```
SceneCaptureComponent2D（捕获3D场景）
  → TextureRenderTarget2D（RTF_RGBA32f格式）
    → MaterialInstanceDynamic（MID，父材质已处理Alpha=1）
      → UImage:SetBrushFromMaterial(MID)
```

---

## 前置条件

| 资源 | 说明 |
|------|------|
| `SceneCaptureComponent2D` | 场景捕获组件，渲染3D场景到RenderTarget |
| `SkeletalMeshComponent` | 骨骼网格体组件，显示3D角色模型 |
| `TextureRenderTarget2D` | 渲染目标纹理，格式 `RTF_RGBA32f` 或 `RTF_RGBA16f` |
| 父材质（Parent Material） | 已处理好Alpha的材质，采样 `MainTexture` 参数 |

---

## 关键脚本

### 1. 工具函数：加载资源（兼容多种方式）

```lua
local function LoadAsset(path)
    if not path or path == "" then
        return nil
    end
    if LoadObject then
        local asset = LoadObject(path)
        if asset then
            return asset
        end
    end
    if UE and UE.LoadObject then
        return UE.LoadObject(path)
    end
    return nil
end
```

### 2. 工具函数：获取UGC资源完整路径

```lua
local function GetFullUGCPath(path)
    local rootPath = ""
    if UGCMapInfoLib and UGCMapInfoLib.GetRootLongPackagePath then
        rootPath = UGCMapInfoLib.GetRootLongPackagePath()
    end
    return rootPath .. path
end
```

### 3. 创建MID并设置RenderTarget（核心修复代码）

```lua
-- 步骤1：加载父材质（内部已处理Alpha=1）
local ParentMaterialPath = "/Game/UGC/Materials/UGC_Material_ItemCapture.UGC_Material_ItemCapture"
local parentMaterial = LoadAsset(ParentMaterialPath)

if parentMaterial then
    -- 步骤2：创建动态材质实例（MID）
    -- 注意：KismetMaterialLibrary.CreateDynamicMaterialInstance
    -- 第一个参数是WorldContextObject，用self（UUserWidget/Actor）而不是nil
    local MID = KismetMaterialLibrary.CreateDynamicMaterialInstance(self, parentMaterial)

    if MID then
        -- 步骤3：加载RenderTarget并设给材质的贴图参数
        local RTPath = GetFullUGCPath("Asset/Blueprint/Prefabs/Monsters/textui.textui")
        local RT = LoadAsset(RTPath)

        if RT then
            -- FName参数直接用字符串，不要用FName("")构造
            MID:SetTextureParameterValue("MainTexture", RT)

            -- 步骤4：将材质设给UImage
            self.Image_56:SetBrushFromMaterial(MID)
        end
    end
end

-- 步骤5：额外强制不透明（安全兜底）
-- FLinearColor在Lua中用表构造，不要用 FLinearColor.New()
self.Image_56:SetColorAndOpacity({ R = 1.0, G = 1.0, B = 1.0, A = 1.0 })
```

---

## 完整范例（HeroPreviewCapture + HeroSelect）

### HeroPreviewCapture.lua（Actor蓝图脚本）

完整的 SceneCapture 控制和 MID 创建逻辑：

```lua
---@class HeroPreviewCapture_C:AActor
---@field SceneCaptureComponent2D USceneCaptureComponent2D
---@field SkeletalMesh USkeletalMeshComponent
local HeroPreviewCapture = {
    ItemCaptureMaterialPath = "/Game/UGC/Materials/UGC_Material_ItemCapture.UGC_Material_ItemCapture",
    DisplayMeshPath = "",
    RenderTarget = nil,
    DisplayMaterial = nil,
    FallbackRenderTargetSize = 1024,
}

-- 设置SceneCapture只渲染自己
local function SetupSceneCapture(self)
    if not self.SceneCaptureComponent2D then
        return false
    end
    if ESceneCapturePrimitiveRenderMode and
       ESceneCapturePrimitiveRenderMode.PRM_UseShowOnlyList then
        self.SceneCaptureComponent2D.PrimitiveRenderMode =
            ESceneCapturePrimitiveRenderMode.PRM_UseShowOnlyList
    end
    self.SceneCaptureComponent2D.ShowOnlyActors = { self }
    self.SceneCaptureComponent2D:ShowOnlyComponent(self.SkeletalMesh)
    return true
end

-- 确保MID已创建
function HeroPreviewCapture:EnsureDisplayMaterial()
    if self.DisplayMaterial then
        return self.DisplayMaterial
    end
    local material = LoadAsset(self.ItemCaptureMaterialPath)
    self.DisplayMaterial = KismetMaterialLibrary.CreateDynamicMaterialInstance(self, material)
    return self.DisplayMaterial
end

-- 确保RenderTarget已创建
function HeroPreviewCapture:EnsureRenderTarget()
    if self.RenderTarget then
        return self.RenderTarget
    end
    if self.SceneCaptureComponent2D and self.SceneCaptureComponent2D.TextureTarget then
        self.RenderTarget = self.SceneCaptureComponent2D.TextureTarget
    else
        self.RenderTarget = KismetRenderingLibrary.CreateRenderTarget2D(
            self, self.FallbackRenderTargetSize, self.FallbackRenderTargetSize,
            ETextureRenderTargetFormat.RTF_RGBA16f
        )
    end
    self.SceneCaptureComponent2D.TextureTarget = self.RenderTarget
    return self.RenderTarget
end

-- 构建材质：将RT设给MID的参数，返回修复Alpha后的材质
function HeroPreviewCapture:BuildMaterial()
    local renderTarget = self:EnsureRenderTarget()
    local displayMaterial = self:EnsureDisplayMaterial()
    displayMaterial:SetTextureParameterValue("MainTexture", renderTarget)
    return displayMaterial
end
```

### HeroSelect.lua（UI脚本片段）

将MID设给UImage：

```lua
local function SetHeroPreviewBrush(image, previewActor, displayMaterial)
    if not image then
        return false
    end
    -- 优先用材质（已修复Alpha）
    if displayMaterial then
        image:SetBrushFromMaterial(displayMaterial)
        return true
    end
    -- 回退：直接绑纹理（可能有Alpha问题）
    if previewActor and UE.IsValid(previewActor) and previewActor.GetRenderTarget then
        local renderTarget = previewActor:GetRenderTarget()
        if renderTarget then
            image:SetBrushFromTexture(renderTarget, true)
            return true
        end
    end
    return false
end
```

---

## 注意事项

| 易错点 | 正确做法 | 错误做法 |
|--------|---------|---------|
| `CreateDynamicMaterialInstance` 参数 | 传有效的 WorldContextObject（self） | 传 nil |
| `SetTextureParameterValue` 参数名 | 直接用字符串 `"MainTexture"` | `FName("MainTexture")` |
| `SetColorAndOpacity` 颜色构造 | `{ R = 1.0, G = 1.0, B = 1.0, A = 1.0 }` | `FLinearColor.New(1,1,1,1)` |
| RenderTarget路径 | 用 `GetFullUGCPath()` 加项目前缀 | 直接用相对路径 |
| 蓝图Image的Brush绑定 | **清空**蓝图中的直接绑定（设为None） | 蓝图直接绑RenderTarget |

## 关联API

- [UKismetMaterialLibrary](file:///d:/oasis-skill-plus/docs/api/class/Others/UKismetMaterialLibrary.md) — `CreateDynamicMaterialInstance`
- [UImage](file:///d:/oasis-skill-plus/docs/api/class/Others/UImage.md) — `SetBrushFromMaterial`, `SetColorAndOpacity`
- [UUserWidget](file:///d:/oasis-skill-plus/docs/api/class/Others/UUserWidget.md) — `AddToViewport`, `RemoveFromParent`
- `SetTextureParameterValue` — MID实例方法，设置材质贴图参数
