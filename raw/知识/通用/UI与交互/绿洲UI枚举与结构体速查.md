# 绿洲 UI 枚举与结构体速查

> 来源：[2026-08-26 UI 画刷与控件样式官方查证](../来源记录/2026-08-26_UI画刷与样式官方查证.md)、项目证据：[IslandAuctionKing UI 贴图批量修正 MCP 回读](../../../IslandAuctionKing/日志证据/2026-08-26_UI贴图批量修正MCP回读.md)（会话日期 2026-08-26）
> 官方依据（枚举）：`raw/docs/api/cppenum/E/ES/ESlateBrushDrawType.md`、`ESlateBrushTileType.md`、`ESlateBrushMirrorType.md`、`ESlateBrushImageType.md`、`ESlateColorStylingMode.md`、`EStretch.md`、`EStretchDirection.md`、`raw/docs/api/cppenum/E/EW/EWidgetClipping.md`、`raw/docs/api/cppenum/E/ET/ETextWrappingPolicy.md`、`raw/docs/api/cppenum/T/TE/TextureGroup.md`、`TextureCompressionSettings.md`、`TextureMipGenSettings.md`
> 官方依据（结构体）：`raw/docs/api/cppstruct/F/FS/FSlateBrush.md`、`raw/docs/api/cppstruct/F/FB/FButtonStyle.md`、`raw/docs/api/cppstruct/F/FS/FSlateFontInfo.md`、`raw/docs/api/cppstruct/F/FS/FSlateColor.md`、`raw/docs/api/cppstruct/F/FS/FSlateSound.md`、`raw/docs/api/cppstruct/F/FF/FFontOutlineSettings.md`、`raw/docs/api/cppstruct/F/FM/FMargin.md`
> 官方依据（贴图设置）：`raw/docs/wiki/新手入门/资源管理与编辑/资源编辑/300_贴图与材质编辑.md` 第 2 节「UI贴图设置」
> 交叉核对：2026-08-26 通过 UGCAskQ MCP `ue_read queries=["enum:*"]` / `schema:*?level=full` 在 `IslandAuctionKing`（UE 4.18.1）编辑器内逐项复核，整数值与官方 md 一致。
> 用途：本页是 [MCP UI 编辑与高保真还原知识库](MCP-UI编辑与高保真还原知识库.md) 的附录。MCP 写枚举属性时按整数赋值（`obj.EnumProp = <int>`），必须查表，不得凭名称顺序猜。

---

## 核心结论

1. **UMG 枚举属性在 Python 侧一律用整数赋值**，MCP 不接受枚举名字符串；数值以本页为准。
2. **`DrawAs` 决定 `Margin` 是否生效**：官方 ToolTip 明确 `Box(1)` = 3x3 盒，边与中心按 Margin 拉伸；`Border(2)` = 3x3 边框，边平铺、中心留空；`Image(3)` = **margin is ignored**；`RoundedBox(4)` = 实心矩形带描边与圆角。
3. **`Clipping` 有真实性能代价**：官方枚举 ToolTip 写明 Slate 无法跨裁剪区合批，两个设了裁剪的控件树内部绘制永不合批，会增加 GPU 开销。文本类溢出优先用 `OnDemand(4)` 而不是给每层容器都开 `ClipToBounds(1)`。
4. **UI 贴图四项设置有官方出处**，其中 `Mip Gen Settings = TMGS_NoMipmaps` 的整数值是 **13**，不是 2（2 是 `TMGS_Sharpen0`）。
5. **字体不要靠放大字号**：`FSlateFontInfo.Size` 的官方 ToolTip 直接给出中文警告——手机端无法渲染过大的字体图集，大字体需求要用「小字体 + 调整 Scale」。

---

## 一、画刷相关枚举

### ESlateBrushDrawType（`FSlateBrush.DrawAs`）

| 值 | 名称 | 面板中文 | 官方说明 |
| --- | --- | --- | --- |
| 0 | `NoDrawType` | 无 | 不绘制 |
| 1 | `Box` | 框 | 绘制 3x3 盒，四边与中心按 `Margin` 拉伸 |
| 2 | `Border` | 边框 | 绘制 3x3 边框，四边平铺，中心为空 |
| 3 | `Image` | 图像 | 直接绘制图像，**忽略 `Margin`** |
| 4 | `RoundedBox` | 圆角框 | 实心矩形，带描边与圆角半径 |

### ESlateBrushTileType（`FSlateBrush.Tiling`）

| 值 | 名称 |
| --- | --- |
| 0 | `NoTile` |
| 1 | `Horizontal` |
| 2 | `Vertical` |
| 3 | `Both` |

> 官方 ToolTip：`Tiling` 仅在 **Image 模式**下生效。

### ESlateBrushMirrorType（`FSlateBrush.Mirroring`）

| 值 | 名称 |
| --- | --- |
| 0 | `NoMirror` |
| 1 | `Horizontal` |
| 2 | `Vertical` |
| 3 | `Both` |

> 官方 ToolTip：仅在 Image 模式生效，且**通常只用于源纹理来自摄像头等硬件设备的动态画刷**，普通 UI 不要动它。

### ESlateBrushImageType（`FSlateBrush.ImageType`）

| 值 | 名称 |
| --- | --- |
| 0 | `NoImage` |
| 1 | `FullColor` |
| 2 | `Linear` |
| 3 | `Vector` |

### ESlateColorStylingMode（`FSlateColor.ColorUseRule`）

| 值 | 名称 | 含义 |
| --- | --- | --- |
| 0 | `UseColor_Specified` | 使用 `SpecifiedColor` 指定的颜色（改着色时必须是这个） |
| 1 | `UseColor_ColorTable` | 取色表 |
| 2 | `UseColor_Foreground` | 继承前景色 |
| 3 | `UseColor_Foreground_Subdued` | 继承弱化前景色 |
| 4 | `UseColor_UseStyle` | 由样式决定 |

> 写 `Brush.TintColor.SpecifiedColor` 后若界面颜色不变，先检查 `ColorUseRule` 是否为 `0`。

---

## 二、布局与文本相关枚举

### EWidgetClipping（`UWidget.Clipping` / `SetClipping`）

| 值 | 名称 | 官方说明摘要 |
| --- | --- | --- |
| 0 | `Inherit` | 不裁剪子控件，继承上一个开启裁剪的祖先的裁剪区 |
| 1 | `ClipToBounds` | 裁剪到自身边界，并与已有裁剪区求交 |
| 2 | `ClipToBoundsWithoutIntersecting` | 裁剪到自身边界但**不**求交，压入新裁剪状态，可渲染到会裁剪的父级之外；仍无法忽略 `Always` |
| 3 | `ClipToBoundsAlways` | 裁剪到自身边界并求交，**不可被忽略**，适合 UI 硬边界（不希望动画/特效越界的区域） |
| 4 | `OnDemand` | 仅当期望尺寸大于实际分配尺寸时才裁剪；官方注明此模式**主要为文本添加**，避免为每个可能装文本的容器都强开裁剪而毁掉合批 |

### EStretch（`UScaleBox.Stretch` / `StretchPc`）

| 值 | 名称 |
| --- | --- |
| 0 | `None` |
| 1 | `Fill` |
| 2 | `ScaleToFit` |
| 3 | `ScaleToFitX` |
| 4 | `ScaleToFitY` |
| 5 | `ScaleToFill` |
| 6 | `ScaleBySafeZone` |
| 7 | `UserSpecified` |

### EStretchDirection（`UScaleBox.StretchDirection` / `StretchDirectionPc`）

| 值 | 名称 | 含义 |
| --- | --- | --- |
| 0 | `Both` | 可放大也可缩小 |
| 1 | `DownOnly` | 只允许缩小 |
| 2 | `UpOnly` | 只允许放大 |

> `UScaleBox` 有**两套并行字段**：`Stretch/StretchDirection/UserSpecifiedScale/UserSpecifiedScaleBias/IgnoreInheritedScale`（Category `Stretching`）与后缀 `Pc` 的同名字段（Category `StretchingPC`）。改缩放行为时若只改无后缀的一套，PC 端可能仍走 `*Pc`，需一并核对。
> `UserSpecifiedScale` 官方 ToolTip：**仅在 `UserSpecified(7)` 时生效**。

### ETextWrappingPolicy（`UTextLayoutWidget.WrappingPolicy`）

| 值 | 名称 |
| --- | --- |
| 0 | `DefaultWrapping` |
| 1 | `AllowPerCharacterWrapping` |

> 长串连续英文/数字撑破容器时，把它设为 `1`（允许按字符换行），等价于 Web 侧的 `overflow-wrap:anywhere`。

---

## 三、贴图导入相关枚举与官方 UI 贴图设置

### 官方 UI 贴图设置（`300_贴图与材质编辑.md` 第 2 节，原文照抄）

```
Compression Settings：默认使用TCQ_Default
Compression Quality：TCQ_Highest
Mip Gen Settings:TMGS_NoMipmaps
Texture Group:TEXTUREGROUP_UI
```

对应到 MCP 侧的属性名与整数值：

| 面板项 | 属性 | 官方取值 | 整数值 |
| --- | --- | --- | --- |
| Texture Group | `LODGroup`（DisplayName `Texture Group`） | `TEXTUREGROUP_UI` | **16** |
| Mip Gen Settings | `MipGenSettings` | `TMGS_NoMipmaps` | **13** |
| Compression Quality | `CompressionQuality` | `TCQ_Highest` | **5** |
| Compression Settings | `CompressionSettings` | `TC_Default` | **0** |
| sRGB | `SRGB` | 勾选 | `True` |

> 官方原文「Compression Settings：默认使用 TCQ_Default」中的 `TCQ_` 前缀属笔误：`CompressionSettings` 的枚举是 `TextureCompressionSettings`（`TC_Default(0)`），`TCQ_` 才是 `CompressionQuality` 的 `ETextureCompressionQuality`。两个面板项都叫 Compression，容易串行，按上表的属性名对应即可。

### TextureGroup（`Texture2D.LODGroup`）常用值

| 值 | 名称 | 用途 |
| --- | --- | --- |
| 0 | `TEXTUREGROUP_World` | 场景贴图（默认，UI 贴图**不**应留在这一组） |
| 1 | `TEXTUREGROUP_WorldNormalMap` | 场景法线 |
| 13 | `TEXTUREGROUP_Effects` | 特效贴图（官方第 3 节要求） |
| 16 | `TEXTUREGROUP_UI` | UI 贴图 |
| 43 | `TEXTUREGROUP_LobbyUI` | 大厅 UI |

### TextureMipGenSettings（`Texture2D.MipGenSettings`）关键值

| 值 | 名称 | 说明 |
| --- | --- | --- |
| 0 | `TMGS_FromTextureGroup` | 跟随贴图组 |
| 1 | `TMGS_SimpleAverage` | 2x2 平均 |
| 2 | `TMGS_Sharpen0` | 8x8 带锐化（0 = 不锐化但更柔） |
| 12 | `TMGS_Sharpen10` | 极端锐化 |
| **13** | **`TMGS_NoMipmaps`** | **UI 贴图应取此值** |
| 14 | `TMGS_LeaveExistingMips` | 保留已有 Mip 链 |
| 20 | `TMGS_Sharpen5_New` | 新版 Mip 滤波 |

### TextureCompressionSettings（`Texture2D.CompressionSettings`）常用值

| 值 | 名称 |
| --- | --- |
| 0 | `TC_Default` |
| 1 | `TC_Normalmap` |
| 2 | `TC_Masks` |
| 6 | `TC_HDR` |
| 8 | `TC_Alpha` |
| 11 | `TC_BC7` |

---

## 四、UI 结构体字段速查

### FSlateBrush（官方描述：包含如何绘制一个 Slate 元素的信息）

| 字段 | 类型 | 官方说明 | 备注 |
| --- | --- | --- | --- |
| `ImageSize` | `FVector2D` | 资源在 Slate 单位下的尺寸 | 面板「图像大小」 |
| `Margin` | `FMargin` | **Box 与 Border 模式下使用的边距** | `DrawAs=Image` 时无效 |
| `TintColor` | `FSlateColor` | 应用于图像的着色 | 面板「着色」 |
| `ResourceObject` | `UObject*` | 本画刷要渲染的图像，**可为 UTexture 或 UMaterialInterface，或实现 AtlasedTextureInterface 的对象** | 面板「图片」 |
| `ResourceName` | `FName` | 渲染资源名 | 会残留引擎默认路径，可显式写 `'None'` |
| `UVRegion` | `FBox2D` | 可选 UV 区域，有效时**覆盖资源代理里指定的 UV 区域** | 图集裁切用 |
| `DrawAs` | `ESlateBrushDrawType` | 如何绘制图像 | 见上表 |
| `Tiling` | `ESlateBrushTileType` | **Image 模式**下如何平铺 | — |
| `Mirroring` | `ESlateBrushMirrorType` | Image 模式下如何镜像；通常只用于源纹理来自摄像头等硬件设备的动态画刷 | 普通 UI 不要动 |
| `ImageType` | `ESlateBrushImageType` | 图像类型 | — |
| `bUseImageSizeAsTextureSize` | `uint8` | 官方无描述 | 见「待查证」 |
| `bIsDynamicallyLoaded` | `uint8` | 画刷路径是否为指向 UObject 的路径 | — |
| `bHasUObject_DEPRECATED` | `uint8` | 画刷是否有 UTexture 资源 | **已废弃**，实例 `fields()` 里显示为 `bHasUObject`，不要写 |
| `Tint_DEPRECATED` | `FLinearColor` | 应用于图像的着色 | **已废弃**，用 `TintColor` |

### FButtonStyle（官方描述：表示一个 SButton 的外观）

| 字段 | 类型 | 面板中文 | 官方说明 |
| --- | --- | --- | --- |
| `Normal` | `FSlateBrush` | 法线 | 未悬停且未按下时的外观 |
| `Hovered` | `FSlateBrush` | 已悬停 | 悬停时的外观 |
| `Pressed` | `FSlateBrush` | 已按下 | 按下时的外观 |
| `Disabled` | `FSlateBrush` | 已禁用 | 禁用时的外观；**默认被设为无效资源，此时使用引擎默认禁用绘制** |
| `NormalPadding` | `FMargin` | — | 用于抵消按钮背景图边框的内边距；应用后按钮内容与边框齐平，**未按下时使用** |
| `PressedPadding` | `FMargin` | — | 同 `NormalPadding`，**按下时使用**，用于让内容跟随按钮边框图的「位移」 |
| `PressedSlateSound` | `FSlateSound` | — | 按下时播放的音效 |
| `HoveredSlateSound` | `FSlateSound` | — | 首次悬停时播放的音效 |
| `PressedSound_DEPRECATED` / `HoveredSound_DEPRECATED` | `FName` | — | **已废弃** |

> `Disabled` 官方默认是无效资源这条很关键：**不设 `Disabled` 并不等于「按钮禁用时保持常态图」**，而是回落到引擎默认禁用绘制，视觉会突变。要统一风格必须显式设四态。
> `FSlateSound` 只有一个字段 `ResourceObject`（`UObject*`，指向 `USoundBase`），官方注明由 `FSlateSoundStructCustomization` 编辑。

### FSlateFontInfo（官方描述：Slate 中字体的表示）

| 字段 | 类型 | 官方说明 |
| --- | --- | --- |
| `FontObject` | `UObject*` | 字体对象（从 UMG 或 Slate 样式资产使用时有效） |
| `FontMaterial` | `UObject*` | 渲染该字体时使用的材质 |
| `OutlineSettings` | `FFontOutlineSettings` | 字体描边设置 |
| `TypefaceFontName` | `FName` | 从默认字型中取用的字体名（`None` 取第一条） |
| `Size` | `int32` | 字号以磅（point）计量，磅到 Slate 单位的换算在 96 dpi 下完成；用 Photoshop 出稿要把 72 dpi 改成 96 dpi。**官方中文警告：手机端无法渲染过大的字体图集，且出于内存考虑也不宜将字体设置过大。若有大字体需求，请用小字体+调整 Scale 的方案。See MAXFONTSIZE** |
| `FontName_DEPRECATED` / `Hinting_DEPRECATED` | — | **已废弃** |

### FFontOutlineSettings

| 字段 | 类型 | 官方说明 |
| --- | --- | --- |
| `OutlineSize` | `int32` | 描边尺寸；在 1.0 字体缩放下该单位即为像素 |
| `OutlineMaterial` | `UObject*` | 描边材质 |
| `OutlineColor` | `FLinearColor` | 描边颜色 |
| `bSeparateFillAlpha` | `uint8` | 填充与描边 alpha 分离 |

### FSlateColor / FMargin

| 结构体 | 字段 |
| --- | --- |
| `FSlateColor` | `SpecifiedColor`（`FLinearColor`）、`ColorUseRule`（`ESlateColorStylingMode`） |
| `FMargin` | `Left` / `Top` / `Right` / `Bottom`（均为 `float`） |

---

## 五、可执行步骤：按整数值写枚举并回读

```python
import unreal_engine as ue
from unreal_engine.classes import Blueprint, Texture2D

wbp = ue.load_object(Blueprint, '/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/ZhuJieMian')

def find_widget(w, name):
    if w.get_name() == name:
        return w
    try:
        n = w.GetChildrenCount()
    except Exception:
        return None
    for i in range(n):
        r = find_widget(w.GetChildAt(i), name)
        if r:
            return r
    return None

img = find_widget(wbp.WidgetTree.RootWidget, '地图UI')
img.Brush.ResourceObject = ue.load_object(Texture2D, '/IslandAuctionKing/Asset/TuPian/TuJian/Codex_CardFrame')
img.Brush.DrawAs = 1                                  # ESlateBrushDrawType.Box
img.Brush.Tiling = 0                                  # ESlateBrushTileType.NoTile
img.Brush.TintColor.ColorUseRule = 0                  # UseColor_Specified，否则 SpecifiedColor 不生效
img.Brush.TintColor.SpecifiedColor = ue.FLinearColor(1, 0.62, 0.16, 1)

txt = find_widget(wbp.WidgetTree.RootWidget, 'DescText')
txt.WrappingPolicy = 1                                # AllowPerCharacterWrapping
txt.SetClipping(4)                                    # EWidgetClipping.OnDemand：文本专用，保留合批

ue.compile_blueprint(wbp)
wbp.save_package()

# 回读（写入 API 成功也返回 None，必须回读判定）
ue.log('DrawAs=%s Tiling=%s Rule=%s' % (img.Brush.DrawAs, img.Brush.Tiling, img.Brush.TintColor.ColorUseRule))
```

UI 贴图属性批量修正（把仍在 `TEXTUREGROUP_World` 的 UI 贴图纠正到官方设置）：

```python
import unreal_engine as ue
from unreal_engine.classes import Texture2D

for path in ['/IslandAuctionKing/Asset/TuPian/ZhuJieMian/ZJM4']:
    t = ue.load_object(Texture2D, path)
    t.LODGroup = 16              # TEXTUREGROUP_UI
    t.MipGenSettings = 13        # TMGS_NoMipmaps
    t.CompressionQuality = 5     # TCQ_Highest
    t.CompressionSettings = 0    # TC_Default
    t.SRGB = True
    t.save_package()
    ue.log('%s LODGroup=%s MipGen=%s Quality=%s' % (t.get_name(), t.LODGroup, t.MipGenSettings, t.CompressionQuality))
```

> 上面这段是**写入**代码，按项目流程必须先备份、走 UGCAskQ MCP 的 Resolve → Plan → Execute，并在写后回读。
> **2026-08-26 已在生产贴图上执行**：同样五项设置已批量应用到 `Asset/TuPian/ZhuJieMian/ZJM1–ZJM11` 与 `Asset/TuPian/TuJian/Codex_*` 共 23 张，跨对象回读 `ALL_23_COMPLIANT=True`。批量时注意：一个目录一个 plan_id、循环内逐张 `save_package()`、先读 before 做幂等。执行记录见 项目原始证据路径 `raw/IslandAuctionKing/开发记录/2026-08-26_UI贴图全量合规批量修正.md`（尚未入库，待补）。

---

## 六、常见错误

| 现象 | 原因 | 正确做法 |
| --- | --- | --- |
| UI 贴图仍然发虚/有多余 Mip | `MipGenSettings` 写成 `2`（实为 `TMGS_Sharpen0`） | 写 **13**（`TMGS_NoMipmaps`） |
| UI 贴图内存/清晰度异常 | `LODGroup` 仍是 `0`（`TEXTUREGROUP_World`）——**导入默认值就是 0**，不会自动归 UI 组 | 写 **16**（`TEXTUREGROUP_UI`），并配 `CompressionQuality=5`、`CompressionSettings=0`、`SRGB=True` |
| 九宫格底图被整体拉伸变形 | `DrawAs=Image(3)` 时 `Margin` 被官方明确忽略 | 底图用 `Box(1)`，边框用 `Border(2)`，图标才用 `Image(3)` |
| 写了 `SpecifiedColor` 但颜色没变 | `ColorUseRule` 不是 `UseColor_Specified(0)` | 先写 `ColorUseRule = 0` |
| 开了裁剪后 UI 掉帧 | 每层容器都设 `ClipToBounds(1)`，跨裁剪区无法合批 | 只在硬边界用 `ClipToBoundsAlways(3)`，文本溢出用 `OnDemand(4)` |
| 按钮禁用态变成陌生的默认样式 | `Disabled` 官方默认是无效资源，回落到引擎默认禁用绘制 | 四态全部显式设置 |
| 手机端大字号不显示或内存暴涨 | 直接把 `FSlateFontInfo.Size` 调很大 | 按官方警告用小字号 + 调 Scale（`ScaleBox` / `RenderTransform`） |
| 长串英文/数字顶破容器 | `WrappingPolicy` 为 `DefaultWrapping(0)` | 设 `1`（`AllowPerCharacterWrapping`） |
| PC 端缩放行为与移动端不一致 | 只改了 `Stretch`，没改 `StretchPc` | 两套字段一并核对 |

---

## 七、相关页面

- [MCP UI 编辑与高保真还原知识库](MCP-UI编辑与高保真还原知识库.md)
- [UGCAskQ MCP 实测陷阱清单](../工具与流程/UGCAskQ-MCP实测陷阱清单.md)
- [ZhuJieMian 画刷现状基线表](ZhuJieMian画刷现状基线表.md)
- [UGCAskQ MCP 能力矩阵](../工具与流程/UGCAskQ-MCP能力矩阵.md)
- [资源导入与路径规范](../配置与数据/资源导入与路径规范.md)
- [UI 页面切换与 Widget 生命周期](UI页面切换与Widget生命周期.md)
- 来源：[2026-08-26 UI 画刷与控件样式官方查证](../来源记录/2026-08-26_UI画刷与样式官方查证.md)

---

## 八、待查证

1. `FSlateBrush.bUseImageSizeAsTextureSize` 官方 md 与编辑器反射均无描述文字，语义未确认，不要依赖。
2. `FSlateBrush.UVRegion` 用于图集裁切的实际效果未在 PIE 中验证，仅有官方字段描述。
3. `UScaleBox.UserSpecifiedScaleBias` 的官方 ToolTip 只有 `#if UMG_SCALE_BIAS`（宏残留），实际含义未确认。
4. `ESlateBrushImageType` 各值（`FullColor` / `Linear` / `Vector`）的具体渲染差异官方无描述。
5. `TEXTUREGROUP_LobbyUI(43)` 与 `TEXTUREGROUP_UI(16)` 在绿洲工程内的适用边界未见官方说明。
6. 官方 Wiki「Compression Settings：默认使用 TCQ_Default」的前缀笔误未见官方勘误，此处按枚举定义推断，若官方后续更新需复核。
