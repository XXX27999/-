# 绿洲 UMG 设计态缩放、裁剪与白块排错

> 类型：通用知识
> 主题：UI / ScaleBox Stretch / Clipping / 设计态白块 / 切图原尺寸 / 设计器页签刷新
> 适用范围：全局通用（绿洲 UMG 编辑器）。项目像素、资产名、plan_id 只作证据，不得当默认值。
> 证据状态：官方确认 + 项目实测归纳
> 来源：官方 Wiki 20269；UScaleBox / UWidget / EStretch / EWidgetClipping / FSlateFontInfo；UGCAskQ 引擎反射元数据 `enum:EStretch` / `enum:EStretchDirection`（2026-09-15 实测）；IslandAuctionKing 2026-09-07 至 2026-09-15 的 MCP 回读、PIE 实测与 .uasset 二进制浮点偏移比对
> 更新时间：2026-09-15
> 关联主题：绿洲编辑器控件位置与尺寸准确性、绿洲通用UI编辑规范与排错、绿洲编辑器UI截图与验证、绿洲UMG文字透明点击层与贴边锚点摆放
> 排除范围：不覆盖玩法数据刷新、RPC、事件绑定；不把 ZhuJieMian / AuctionSettlementUI 的具体坐标写成所有项目默认值
> 官方依据：`D:\oasis-skill-plus\docs\wiki\进阶内容\UI系统\20269_UI自适应屏幕.md`；`D:\oasis-skill-plus\docs\api\class\Others\UScaleBox.md`；`D:\oasis-skill-plus\docs\api\class\Others\UWidget.md`；`D:\oasis-skill-plus\docs\api\cppenum\E\ES\EStretch.md`；`D:\oasis-skill-plus\docs\api\cppenum\E\EW\EWidgetClipping.md`；`D:\oasis-skill-plus\docs\api\cppstruct\F\FS\FSlateFontInfo.md`。知识库未覆盖 ScaleToFill 裁切公式的官方说明。

## 来源与官方依据

- **官方确认**：自适应层次是「画布 → 尺寸框 1920×1080 → 缩放框 → 外层画布」。缩放框四向拉伸、四边偏移 0。居中弹窗改尺寸框对齐为居中；贴边件改对应边对齐。见 [20269_UI自适应屏幕](../../../docs/wiki/进阶内容/UI系统/20269_UI自适应屏幕.md)。
- **官方确认**：`UScaleBox.SetStretch` 写入 `EStretch`；并行字段 `StretchPc` 控制 PC 端，只改无后缀一套不够。`None=0`、`Fill=1`、`ScaleToFit=2`、`ScaleToFitX=3`、`ScaleToFitY=4`、`ScaleToFill=5`、`ScaleBySafeZone=6`、`UserSpecified=7`。见 [UScaleBox](../../../docs/api/class/Others/UScaleBox.md)、[EStretch](../../../docs/api/cppenum/E/ES/EStretch.md)。
  - **枚举元数据补全（2026-09-15）**：官方枚举 tooltip 给出语义 —— `ScaleToFit(2)` = 等比放大/缩小「直到再放就会裁切」（= 完整装入，`scale = min(sx, sy)`）；`ScaleToFill(5)` = 等比放大「直到四边都达到或超过区域」并**裁掉较长边**（= 覆盖，`scale = max(sx, sy)`）。可见 `ScaleToFill` 是**等比**的，不是 X/Y 各自拉伸；宽高比不一致时它永远会裁一边。
  - **`StretchDirection`（`EStretchDirection`）**：`Both=0`（可放大可缩小）、`DownOnly=1`（只缩不放）、`UpOnly=2`（只放不缩）。根 ScaleBox 通常用 `Both(0)`。
- **官方确认（EditCondition 约束）**：`USizeBox.WidthOverride` / `HeightOverride` 受 `bOverride_WidthOverride` / `bOverride_HeightOverride` 约束。**只写数值、不开约束开关时，值会落进 CDO 但运行时不生效**，SizeBox 的期望尺寸退化为内容的自然尺寸。见 [py:guide property](../../../docs/api/class/Others/UWidget.md)（`has_metadata('EditCondition')` → `get_metadata('EditCondition')` → 先置 True 再写目标属性）。
- **官方确认**：`UWidget.SetClipping` 阻止越界绘制；跨裁剪区无法合批，不要给每层都开裁剪。`ClipToBoundsAlways=3` 是硬边界。见 [UWidget.Clipping](../../../docs/api/class/Others/UWidget.md)、[EWidgetClipping](../../../docs/api/cppenum/E/EW/EWidgetClipping.md)。
- **官方确认**：`FSlateFontInfo.FontObject` 是 UMG 字体对象；字号过大应用小字体加 Scale。见 [FSlateFontInfo](../../../docs/api/cppstruct/F/FS/FSlateFontInfo.md)。
- **项目实测归纳**：设计器预览区不是 16:9 时，设计态 `ScaleToFill` 会裁切贴边 HUD；空画刷和复制残留会在设计态画白块/色块；MCP 写入后已打开页签不刷新。证据见文末项目页，像素不可复用。

## 核心结论

固定布局 UI 要同时管四件事：舞台、缩放时机、设计态占位、页签缓存。缺一就会在编辑器里“看起来错了”，但运行时未必同一原因。

1. **舞台锁 1920×1080。** 业务坐标只写设计舞台像素。切图或参考图不是该尺寸时，按原像素居中，不要硬拉满。
2. **设计态不要用 ScaleToFill 看完整舞台。** 预览区宽高比不等于 16:9 时，`ScaleToFill(5)` 按较长边放大、较短边被裁。项目实测做法：设计态 `Stretch=None(0)` 看完整 1920；PIE 再对根 ScaleBox `SetStretch(ScaleToFit=2)`，并同步 `StretchPc`。
3. **Stretch=None 时负 Offsets 会撑大包围盒。** 贴边 HUD 的负 Top/Left 会把设计器白边画到 1920 虚线框外。硬边界用 SizeBox/Canvas `SetClipping(ClipToBoundsAlways=3)`，SizeBox 对齐改为 Fill；不要给每个叶子开裁剪。
4. **空画刷和复制残留在设计态会画实心块。** `UImage.Brush.ResourceObject=None`、`UBorder.Background.ResourceObject=None` 即使 `Collapsed` / `HitTestInvisible`，设计器仍可能画白矩形或色块。复制来的无用控件要 `widget_remove`，不要只折叠。
5. **中文「字」方块优先查 FontObject。** 整段回写 `widget.Font` 会把 `FontObject` 清成 `None`。只对 `FSlateFontInfo` 做 `set_field("FontObject"/"TypefaceFontName"/"Size")`。
6. **MCP 写完必须关掉已打开的「编辑 Xxx」页签再开。** 写入 API 成功也返回 `None`。FlaUI 枚举不到提权编辑器、`PrintWindow` 白图，都不能当设计态验收。
7. **尺寸框的重载开关必须和数值一起写。** `WidthOverride` / `HeightOverride` 只在 `bOverride_WidthOverride` / `bOverride_HeightOverride` 为 True 时生效。漏开开关时资产回读「数值全对」，设计器也看不出异常，但**运行时**尺寸框的期望尺寸退化成内容的自然尺寸，根 ScaleBox 会按更小的基准算缩放 —— 于是画面被放大到超出画布。
8. **内容被「放大」而不是「缩小」，指向根缩放基准比视口小。** 视口比设计舞台小时 `ScaleToFit` 应得到 `scale < 1`；若实测 `scale > 1`，说明 ScaleBox 拿到的内容期望尺寸小于分配区域，优先查尺寸框重载开关是否生效，再查是否有多余包裹层。

## 可执行步骤

### 1. 自适应根结构

按官方 20269 建立：

`CanvasPanel（铺满视口） -> ScaleBox（四向拉伸，偏移 0） -> SizeBox（WidthOverride=1920，HeightOverride=1080） -> CanvasPanel（业务控件）`

- 居中弹窗：SizeBox 水平/垂直居中。
- 贴边 HUD：里层点锚点跟随底图，不要把贴边件改成左上角绝对坐标去追 1920。详见 [绿洲 UMG 文字、透明点击层与贴边锚点摆放](./绿洲UMG文字透明点击层与贴边锚点摆放.md)。

**尺寸框必须两阶段写（否则重载静默失效）**：

1. 先开约束开关：`sz.bOverride_WidthOverride = True`、`sz.bOverride_HeightOverride = True`。
2. 再写数值：`sz.WidthOverride = 1920.0`、`sz.HeightOverride = 1080.0`。
3. 保存后回读**四个字段**：两个 `bOverride_*` 必须为 True，两个数值必须为 1920 / 1080。只回读数值会漏掉本类缺陷。

同类资产横向对照最快：若同项目其他同级蓝图的 `bOverride_*` 都是 True，只有目标资产是 False，即写入遗漏。

### 1.1 运行时缩放的取证量测

判断根缩放是否按设计舞台正确适配，不要靠目视缩放：

1. 抓 PIE 客户端**绘制区**（`GetClientRect` + `ClientToScreen`，不是整窗，避免标题栏/边框混进量测）。
2. 取一个已知设计距离（如重复行的行间距 `D`），在截图上量出运行时像素距离 `P`。
3. `运行时缩放 = P / D`；与 `min(视口宽/设计宽, 视口高/设计高)`（ScaleToFit）或 `max(...)`（ScaleToFill）对账。
4. 面板应有矩形也可用 `设计偏移 - 居中余量` 反算：ScaleToFit 下 `屏幕X = (视口宽 - 设计宽×scale)/2 + 设计X×scale`。

### 1.2 量测判据：用「边缘位置」，不要用「结构相关系数」

同一个界面在不同机器、不同时间抓图，**像素级差异与结构相关系数会被 3D 背景淹没**，不能作为 UI 是否一致的判据：

| 判据 | 是否可用 | 原因（同项目实测） |
| --- | --- | --- |
| 原始像素差 / 归一化边缘相关系数 `edge_corr` | ❌ | 由场景背景主导。同一场景两次 PIE 抓图 `edge_corr = 0.989`；跨机器、同 UI 仅 `0.199` —— 数值高低反映的是场景相似度，不是 UI |
| 右侧纯色带宽度 | ⚠️ 辅助 | 能提示「未铺满留黑边」，但 UI 面板自身纯色区也会误报 |
| **UI 边缘位置比例（`V_EDGE`）** | ✅ | 「右侧 0.60~0.98 区间内竖直边缘能量的峰值列 ÷ 视口宽」。对光照、色调不敏感，只反映几何位置 |

用 `V_EDGE` 时必须先对**同一套 UI**做基准标定（例：某项目 1280×720 视口下 `0.824~0.826` = `Stretch=0` 原始态，`0.96+` = 铺满态），且**只在同取景下比较**（窗口尺寸相同 ≠ 取景相同）。

**两个抓图陷阱**：

1. **渲染未完成就量测**：PIE `start` 返回不代表主界面已渲染。首帧常落在完全不同的数值上（实测 `0.7031`，右侧还有近 200px 纯色带），约十几秒后才收敛到真实值。**必须轮询到连续多帧稳定再判定**。
2. **整窗 vs 绘制区**：一律抓客户端绘制区（`GetClientRect` + `ClientToScreen`），整窗会把标题栏/边框算进比例。

### 1.3 改根 ScaleBox 的 `Stretch`：必须回读子控件槽位

> **写入副作用（项目实测，机制待官方确认）**：通过 MCP 写根 `UScaleBox` 的 `Stretch` 并 `save_package()` 后，**该 ScaleBox 子树内子控件的 `CanvasPanelSlot.LayoutData.Offsets` 可能被重新布局计算并落盘**。

实测后果：某项目复原 `Stretch = 2 → 0` 后，`Stretch` 回读正确，但右下角两个按钮的槽位被写成偏小值（宽高 `140×130` → `99.96×98.20` 与 `118.80×108.80`，并伴随位置偏移），**视觉上按钮明显变小变偏**，而回读 `Stretch` 完全正常。

因此改完 `Stretch` 之后的核验清单必须包含：

- [ ] 回读 `Stretch` / `StretchDirection` / `StretchPc` / `StretchDirectionPc`（勿只写无后缀一套）
- [ ] **回读该子树内所有可见控件的 `CanvasPanelSlot.Offsets`**（至少是锚点非默认、尺寸非整数的那些）
- [ ] 非拉伸锚点下 `Offsets.Right` / `Offsets.Bottom` 即**控件宽高**，`Left` / `Top` 是相对锚点的偏移
- [ ] 重新 PIE 后按 1.2 的判据复验

### 1.4 版本比对取证：浮点命中偏移

判断两个 `.uasset` 版本某控件几何是否「同位同值」，比截图更硬的做法是**在二进制里搜浮点**：

```python
import struct
pat = struct.pack('<f', -418.0)   # 目标几何值
offs = [i for i in range(len(blob)) if blob.startswith(pat, i)]
```

- **命中偏移集合相同** ⇒ 该浮点处在序列化流中位置与值都一致（几何未变）。
- **偏移整体平移**（例：全体 +47 字节）⇒ 前面有字段长度变化（如枚举文本 `EStretch::ScaleToFit` 的增删），但几何本身正常。
- **命中值消失、出现新值** ⇒ 几何真的被改了，可直接读取新旧值算出尺寸变化。

配合「控件名字符串段（如 `OpenRewardButton`）的 ASCII 偏移是否与基准逐一对齐」，可快速确认序列化结构有无错位。

> **注意**：`save_package()` 每次整包重写都会重新生成一批**元数据序号**（形如 `01, 92, 93 … a3` vs 基准全 `00`），这类差异与控件几何无关，不要当成几何变更。

### 2. 设计态与运行时 Stretch 分开

| 时机 | Stretch | 目的 |
| --- | --- | --- |
| 设计器 | `None(0)`，同步 `StretchPc=0` | 看到完整 1920 舞台，不被当前预览区裁切 |
| PIE / 运行时 | `ScaleToFit(2)`，同步 `StretchPc=2` | 等比适配；非 16:9 留边，不裁顶栏和会场 |

禁止项：

- 不要用 `ScaleToFill(5)` 当“铺满大分辨率”的默认方案。项目实测它会裁贴边 HUD。
- 不要用 `Fill(1)` 当根缩放。旧舞台会被拉变形或溢出画布。
- 不要 silent 把 ScaleToFit 改回 ScaleToFill 去消灭超宽屏黑边；那是产品选择，需单独授权。

运行时取根 ScaleBox：先 `widget.WidgetTree.RootWidget`，失败再按名取。取不到就不要假装已经 SetStretch。

### 3. 切图按原像素居中

参考图、导入 PNG、控件 Size 三者必须同一基准：

1. 确认 SizeBox 仍是 1920×1080。
2. 回读贴图像素宽高 `artW × artH`。
3. 底板 `SetPosition((1920-artW)/2, (1080-artH)/2)`，`SetSize(artW, artH)`。
4. 子面板相对底板重排，不要沿用硬拉满后的绝对坐标。
5. 切图已烘焙标题时，折叠重复的 Title TextBlock / Title Image，避免叠字和白条。

### 4. 设计态白块与残留控件

写入前先回读 `Visibility`、`Brush.ResourceObject` / `Background.ResourceObject`、`DrawAs`：

| 现象 | 处理 |
| --- | --- |
| 空头像/空立绘白矩形 | 设计态 `Collapsed`；运行时有 Texture 才 `SetBrushFromTexture` 并改为 `HitTestInvisible` |
| 空容器白条 | 折叠空 VBox/HBox；把盖住整栏的标题 Slot 收到真实标题带 |
| 复制残留色块 | `ue.widget_remove(bp, name)`，同步删 Lua `---@field`；不要只 `Collapsed` |
| 运行时才绑定的动态图 | 设计态不要留空 Image 在可见层；占位必须透明且折叠，或移出验收视线 |

`Collapsed` 不是设计器保证不绘制。项目实测：无贴图 UBorder/Button 在设计器里仍画实心色。

### 5. 字体与页签

1. 回读每个可见 TextBlock 的 `FontObject`、`TypefaceFontName`、`Size`、默认 `Text`。
2. `FontObject` 为 `None` 时，用 `font.set_field(...)` 补字体；禁止 `w.Font = f`。
3. `compile_blueprint` + `save_package` 后重新 `load_object` 回读。
4. 关掉已打开的设计器页签再打开，再截图或目视。
5. 蓝图/组件/初始化变更必须重新 PIE；不要用热更新判断设计态修改。

## 常见错误

- 设计器预览是 1855×1410 一类非 16:9，却把根 ScaleBox 设成 ScaleToFill，顶栏和会场被裁出白框，误判为锚点漂了。
- Stretch=None 后贴边 HUD 画到 1920 虚线框外的大白边，继续改点锚点，而不是给 SizeBox/Canvas 开硬裁剪。
- 把 1639×960 切图硬拉成 1920×1080，头像框变形、按钮压进底板。
- 运行时 Lua 会 `SetBrushFromTexture`，设计态就留下空 Image，编辑器截图出现白头像/白条。
- 从角色选择复制道具选择后，只折叠 `CharacterPanel`，设计器仍画大方块。
- 列表卡绝对铺在 AdaptiveCanvas 上，第五张压底栏；应 `ScrollBox.AddChild`。
- MCP 写入后对着旧页签截图，或把提权编辑器的白 `PrintWindow` 当验收。
- 用户已在设计器摆正并保存，下一轮又用旧 `ApplyLayout` 覆盖。
- **只写 `WidthOverride=1920` / `HeightOverride=1080` 而不开 `bOverride_*`**：资产回读数值全对、设计器看着正常，但运行时尺寸框无重载 → 内容期望尺寸退化为自然尺寸（例如 `401+1117=1518` 宽）→ 根 ScaleBox 按 1518 而非 1920 计算 → `ScaleToFill(5)` 得 `scale = max(1920/1518, 视口高/1080) ≈ 1.26`，画面被放大 1.26 倍、右侧贴边、底部被裁，容易被误判成「坐标写错了」。
- **把「运行时被放大」当成锚点问题**：放大是缩放基准问题（尺寸框重载 / 包裹层），锚点只决定位置。先量 `运行时缩放 = 实测间距 / 设计间距`，`>1` 就不要再去改锚点。

## 相关页面

- [绿洲编辑器控件位置与尺寸准确性](./绿洲编辑器控件位置与尺寸准确性.md)
- [绿洲通用 UI 编辑规范与排错](./绿洲通用UI编辑规范与排错.md)
- [绿洲 UMG 文字、透明点击层与贴边锚点摆放](./绿洲UMG文字透明点击层与贴边锚点摆放.md)
- [绿洲编辑器 UI 截图与验证](./绿洲编辑器UI截图与验证.md)
- [MCP UI 编辑与高保真还原知识库](./MCP-UI编辑与高保真还原知识库.md)
- [绿洲 UI 枚举与结构体速查](./绿洲UI枚举与结构体速查.md)
- Wiki 短索引：[绿洲 UMG 设计态缩放裁剪与白块排错](../../../../wiki/概念/绿洲UMG设计态缩放裁剪与白块排错.md)

项目证据（数值不可当全局默认）：

- [2026-09-15 AuctionGuaranteeGoldUI 画刷 ResourceObject 与 Slot 对齐修复](../../../IslandAuctionKing/蓝图与UI/2026-09-15_AuctionGuaranteeGoldUI_画刷ResourceObject与Slot对齐修复.md)（含第二轮：尺寸框重载开关未开导致运行时放大 1.264 倍并裁切）
- [2026-09-10 ZhuJieMian 设计态 None 运行时 ScaleToFit](../../../IslandAuctionKing/蓝图与UI/2026-09-10_ZhuJieMian设计态None运行时ScaleToFit.md)
- [2026-09-11 ZhuJieMian HUD 收回 1920 画布](../../../IslandAuctionKing/蓝图与UI/2026-09-11_ZhuJieMian_HUD收回1920画布.md)
- [2026-09-11 AuctionSettlementUI 切图原尺寸居中](../../../IslandAuctionKing/蓝图与UI/2026-09-11_AuctionSettlementUI_切图原尺寸居中.md)
- [2026-09-11 AuctionSettlementUI 设计态白块修复](../../../IslandAuctionKing/蓝图与UI/2026-09-11_AuctionSettlementUI_设计态白块修复.md)
- [2026-09-07 AuctionPropSelectUI 删除角色残留控件](../../../IslandAuctionKing/蓝图与UI/2026-09-07_AuctionPropSelectUI_删除角色残留控件.md)
- [2026-09-08 AuctionHouseSelectUI PIE 乱码与点卡选场](../../../IslandAuctionKing/蓝图与UI/2026-09-08_AuctionHouseSelectUI_PIE乱码与点卡选场.md)
- [2026-09-09 AuctionPropSelectUI 滑动框与文字归位](../../../IslandAuctionKing/蓝图与UI/2026-09-09_AuctionPropSelectUI_滑动框与文字归位.md)

## 待查证

- 官方 Wiki 的 EStretch 枚举页没有 ScaleToFit / ScaleToFill 的语义说明；**2026-09-15 已由引擎反射元数据 tooltip 补全语义**（`scale = min/max(sx, sy)`，`ScaleToFill` 等比并裁较长边），但「Wiki 未写」这一条仍成立，引用时请标「引擎枚举元数据」而非「Wiki 官方说明」。
- PD3D_SM5 下根 ScaleBox 取的是 `StretchPc` / `StretchDirectionPc`，移动端语义未在本次实测，未做移动端视口复现。
- `widget.WidgetTree.RootWidget` 在绿洲 Lua 是否始终可写，未做最小复现。
- 设计器在 ClipToBoundsAlways 之后是否仍按未裁剪包围盒画外框，关页签后若白边仍在，应改把贴边底图收到 1920 内，而不是继续加裁剪。
- `GetOffsets()` 在部分点锚点下返回不完整，见贴边锚点页待查证。
