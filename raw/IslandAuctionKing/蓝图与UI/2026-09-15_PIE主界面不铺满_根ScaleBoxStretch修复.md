# 2026-09-15 PIE 主界面不铺满：根 ScaleBox Stretch 归零 + Lua 手写 RenderScale 双重缩放

> 类型：项目证据（蓝图与 UI / 运行时）
> 主题：`ZhuJieMian` 主界面在 PIE 下只占视口左上约 83%（右侧与下方露出 3D 场景）的根因与修复
> 适用范围：仅 `IslandAuctionKing` 项目；通用自适应做法见 [绿洲 UMG 设计态缩放裁剪与白块排错](../../知识/通用/UI与交互/绿洲UMG设计态缩放裁剪与白块排错.md)
> 证据状态：项目实测（MCP 回读 + PIE 日志 + 截图模板匹配量化）；自适应层次结构为官方确认
> 更新时间：2026-09-15
> 官方依据：`raw/docs/wiki/进阶内容/UI系统/20269_UI自适应屏幕.md`
> 关联主题：[2026-09-14_ZhuJieMian主界面底图导入与设置](./2026-09-14_ZhuJieMian主界面底图导入与设置.md)、[ZhuJieMian 画刷现状基线表](../../知识/通用/UI与交互/ZhuJieMian画刷现状基线表.md)
> 排除范围：`AuctionTestUI`（Stretch=2）、`AuctionSettlementUI`（Stretch=5）本轮实测均正常，不在修复范围

---

## 一、结论

1. **根因是两个叠加错误，不是单一配置问题**：
   - 资产侧：`ZhuJieMian` 根缩放框 `CanvasPanel_0_Wrapper_Wrapper`（`UScaleBox`）的 `Stretch` 为 **0（None，不缩放）**，且 PC 端双字段 `StretchPc` 同为 0，与官方自适应要求的 **2（ScaleToFit）** 不符。
   - 脚本侧：`AuctionHubUIService.ApplyViewportFit` 旧逻辑在 PIE 运行时**手写** `SetRenderScale(0.667)` + `SetPositionInViewport` + `SetDesiredSizeInViewport` + `SetAnchorsInViewport`，并把根 ScaleBox 的 `Stretch` 强制设为 0（旧 `mode=DynamicScaleToFit` 分支）。
2. **UMG 渲染空间与物理视口像素存在视口缩放差**：手写 `SetRenderScale` 会与根 ScaleBox 的缩放**叠加**，把整屏界面再缩一次。实测 1280×720 PIE 客户端区下，主界面底图只铺满 **1060×596（0.828 × 0.828）**，右侧/下方露出 3D 场景。
3. **「编辑器正常、PIE 不正常」是错觉**：编辑器设计态不走 Lua 的 `ApplyViewportFit`，直接按设计尺寸渲染；只有 PIE/运行时才执行手写缩放，所以差异只在 PIE 暴露。
4. 修复后同一视口下铺满 **1276×720（0.997 × 1.000）**，残留 4px 为黑边取整误差，非布局缺陷。

---

## 二、根因定位过程

### 2.1 三套 UI 自适应层横向对比（`ue_py` 只读）

| 蓝图 | 根 ScaleBox | Stretch | StretchDirection | StretchPc | 判定 |
| --- | --- | --- | --- | --- | --- |
| `ZhuJieMian` | `CanvasPanel_0_Wrapper_Wrapper` | **0** | 0 | **0** | ❌ 异常（不缩放） |
| `AuctionTestUI` | 同构 | 2 | 0 | 2 | ✅ 正常 |
| `AuctionSettlementUI` | 同构 | 5 | 0 | 5 | ✅ 正常（ScaleToFill 类） |

`ZhuJieMian` 的自适应层次与官方一致：
`CanvasPanel_0_Wrapper_Wrapper`(ScaleBox，四向拉伸/Offsets 全 0) → `CanvasPanel_0_Wrapper`(SizeBox，WidthOverride/HeightOverride = 1920/1080，重载已开) → `CanvasPanel_0`(CanvasPanel) → `参考图`(Image，四向拉伸/ZOrder=-5) + 其余 45 个控件。

### 2.2 截图量化（模板匹配 `ZJMBackground`）

脚本：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260915_PIE主界面不铺满\compare_fit.py`
（1/4 降采样 + 邻域位置搜索 + 缩放搜索，避免全分辨率双重循环超时）

```
bg natural = (1671, 941)
[before] frame=1280x720 rect=(0,0)-(1060,596) coverage=0.828 x 0.828 scale(rel bg)=0.635
[after ] frame=1280x720 rect=(0,0)-(1276,720) coverage=0.997 x 1.000 scale(rel bg)=0.765
SUMMARY coverage(bg/frame): before=0.828 x 0.828 -> after=0.997 x 1.000
```

边缘能量佐证：修复前右侧强竖边出现在 `col 1056/1057`（0.82 处，即 UI 边界），修复后移到 `col 1234/1243`（0.96~0.97 处，即视口内 UI 元素本身）。

---

## 三、修复内容

### 3.1 资产侧（UGCAskQ MCP，Resolve → Plan → Execute）

- 资产：`/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/ZhuJieMian`
- plan_id：`plan_16784780_1b93aa0e`
- 控件：`CanvasPanel_0_Wrapper_Wrapper`（`UScaleBox`）

| 属性 | 修复前 | 修复后 |
| --- | --- | --- |
| `Stretch` | 0 | **2**（ScaleToFit） |
| `StretchDirection` | 0 | 0 |
| `StretchPc` | 0 | **2** |
| `StretchDirectionPc` | 0 | 0 |
| `UsePcParams` | False | False（保持；PC 端靠 `StretchPc` 覆盖） |

回读：重载后 `AFTER_RELOAD Stretch=2`，控件总数 `TREE_COUNT=46`（与 2026-09-14 基线一致，无控件丢失）。

> 写入教训：ScaleBox 有 **移动端 / PC 双字段**。只写 `Stretch` 不改 `StretchPc`，在 PC（PCD3D_SM5）下仍按 PC 字段取值，会误判为「写了没生效」。本项目 `UsePcParams=False` 但 PC 字段同样需要同步写，否则编辑器与 PIE 表现不一致。

### 3.2 脚本侧（`Script/Function/AuctionHubUIService.lua`）

重写 `ApplyViewportFit`：

- **删除**：`SetRenderScale` / `SetPositionInViewport` / `SetDesiredSizeInViewport` / `SetAnchorsInViewport` 全部手写缩放与视口定位；删除把根 ScaleBox 设为 `Stretch=0` 的 `DynamicScaleToFit` 分支。
- **新增**：对每个控件实例**一次性**（`widget.AuctionHubViewportFitApplied` 幂等标记）把根缩放框参数校正为配置表值，并同步 PC 双字段：
  ```lua
  local stretchValue = math.floor(AuctionConfig.GetNumber("UI.Hub.ScaleBoxStretch", 2) + 0.5)
  local directionValue = math.floor(AuctionConfig.GetNumber("UI.Hub.ScaleBoxStretchDirection", 0) + 0.5)
  if widget.AuctionHubViewportFitApplied ~= true then
      local fixOK, fixError = pcall(function()
          scaleBox:SetStretch(stretchValue)
          scaleBox:SetStretchDirection(directionValue)
          scaleBox.UsePcParams = false
          scaleBox.StretchPc = stretchValue
          scaleBox.StretchDirectionPc = directionValue
      end)
      widget.AuctionHubViewportFitApplied = true
  end
  ```
- 函数头写入硬约束注释：**严禁运行时改写控件 RenderScale / 视口锚点 / 视口期望尺寸**。
- 调用点注释同步：`Refresh`（窗口变化后自检缩放框自适应）、`CreateAndShow`（自适应结构自检结果）。

> 经验归纳：整屏 UI 的铺满**只应由根 ScaleBox 负责**。任何在 Lua 里按视口像素比例再算一次 `SetRenderScale` 的做法，都会与 UMG 自身的视口缩放叠加，症状统一为「UI 缩在屏幕一角、四周露出 3D 场景」，且**只在 PIE 出现、编辑器看不见**。

---

## 四、验证

1. **MCP 回读**：`Stretch=2` 持久化（重载后仍为 2），控件总数 46 不变。
2. **PIE 日志**（客户端）：
   ```
   【AuctionHubUIService+ApplyViewportFit】关键数据 mode=ScaleBoxFit view=1280.0x720.0 design=1920x1080
   【AuctionHubUIService+ApplyViewportFit】分支 缩放框参数已校正 stretch=2 direction=0 pcSame=true
   ```
3. **截图量化**：修复后客户端区截图 `capture/pie_hub_fixed_client.png`（1280×720），覆盖率 0.997 × 1.000。
4. **生效方式**：已重新调试 PIE 验证生效（资产 + 初始化相关逻辑变更，需重新 PIE，不可只热更新）。

---

## 五、备份与产物

备份根目录：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260915_PIE主界面不铺满\`

| 路径 | 说明 |
| --- | --- |
| `before\ZhuJieMian.uasset.bak` | 写前资产备份（102,260 字节） |
| `before\AuctionHubUIService.lua.bak` | 写前脚本备份 |
| `staging\pie_ui_shot.jpg` | 用户报障 PIE 截图（1282×752） |
| `analyze\analyze_pie_shot.py` / `report.txt` | 报障截图底图定位与边缘能量分析 |
| `compare_fit.py` / `analyze\compare_report.txt` | 修复前后铺满比例量化对比 |
| `capture\capture_pie_window.py` / `pie_hub_fixed_client.png` | ctypes 抓 PIE 客户端窗口截图 |

> 工具坑：本机 PowerShell 工具的 stdout 不回传（需 `Out-File` 落盘再读），且 `Add-Type` 编译 C# 被安全策略拦截；窗口截图改用 Python `ctypes` + `PIL.ImageGrab` 实现。系统 Python 无 PIL，需 venv 安装 `pillow numpy`（venv：`C:/Users/Administrator/.workbuddy/binaries/python/envs/default`）。

---

## 六、追加排查（同日）：编辑器设计器「UI 控件变小」

### 6.1 结论

1. **设计坐标基准确认为 1920×1080**（不是 1280×720）：
   - `MatchButton` 的 `CanvasPanelSlot` 锚点为 **右-上**（`Anchors.Minimum = (1.0, 0.0)`），`Offsets = L -413.9 / T 431.0 / R 333.2(宽) / B 63.6(高)`；
     按 1920×1080 推算 → `x = 1920 - 413.9 = 1506`（画布 78.4% 处）、`y = 431`（39.9% 处），
     与设计器截图中「开始匹配」的位置吻合；按 1280×720 推算（67.7% / 59.9%）不吻合。
   - `玩家名称` 同样以底部锚定推算 y = 1080 − 235 = 845（78.2% 处）与截图吻合。
   - `CanvasPanel_0_Wrapper`（`USizeBox`）`WidthOverride = 1920.0`、`HeightOverride = 1080.0`（重载均开启），与坐标基准一致。
2. **1280×720 视口下控件按设计的 66.7% 呈现是正确行为**，不是缺陷：
   `ScaleToFit` 缩放系数 = 视口宽 / 设计宽 = 1280 / 1920 = 0.667；把上述任意控件坐标整体等比换算后观感完全一致
   （即「改设计基准为 1280×720」不会让控件变大），因此**不存在既铺满屏幕、又让 1920×1080 设计在 1280×720 视口按 100% 显示的资产改法**。
   真正决定观感尺寸的是「设计基准宽 : 视口宽」这个比值。
3. **设计器「控件变小」的直接原因是资产被 MCP 写入后设计器视图停留在失效渲染**（画布上只剩极小一块内容，其余为空白网格，缩放标尺方向异常）。
   用 `close_editor_for_asset(wbp)` → `open_editor_for_asset(wbp)` 刷新视图后，画布恢复为内容满铺的 1:1 呈现。
   —— 这是**编辑器视图状态**问题，不是资产数据问题；本轮未再改动任何资产。

### 6.2 证据与产物（追加）

| 路径 | 说明 |
| --- | --- |
| `capture2\uieditor_full.png` | 刷新前：设计器画布大面积为空，内容缩到极小一块（用户看到的「变小」） |
| `capture2\desktop_full.png` / `uieditor_hi.png` | 整桌面抓取 + 按窗口裁剪（本次确认 `ImageGrab` 直传 bbox 与整桌面裁剪结果一致，差异来自 `ShowWindow(SW_RESTORE)` 改变了窗口尺寸） |
| `capture2\uieditor_max_full.png` / `uieditor_max_canvas.png` | 刷新后：ZhuJieMian 画布内容满铺，控件恢复 1:1 呈现 |
| `measure_control_scale.py` / `build_scale_compare.py` / `analyze\control_scale_compare.png` | 归一化对比修复前/后 PIE 截图的控件与底图比例，确认控件与底图**同比**放大 1.204 倍（即 PIE 中控件并未变小） |

### 6.3 补充工具经验

- 本机 `ShowWindow(hwnd, SW_RESTORE=9)` 会把最大化窗口还原成小窗口，抓图前先记录 rect；要最大化用 `SW_MAXIMIZE=3`。
- `ImageGrab.grab(bbox=..., all_screens=True)` 在本机多屏（虚拟桌面 3840×1080）下工作正常，但抓到的尺寸会因窗口被还原而变化，别误判为缩放失真。
- MCP 反射读取结构体：`FAnchors` 需 `slot.get_property("LayoutData").get_field("Anchors")` 后再 `get_field("Minimum"/"Maximum")`；
  `FVector2D` 的成员是**小写** `.x` / `.y`（`.X` 会报 AttributeError）。
- 窗口枚举需按标题找「UI编辑器」（绿洲 UMG 设计器是独立顶层窗口），编辑器主进程标题形如 `ShadowTrackerExtra (64 位，PCD3D_SM5) <pid>, Compiled: ...`。

---

## 七、最终处置（同日 12:48）：按需求方要求整体复原

> **本节覆盖前三节的操作结论。** 需求方评估后认为「设计器与 PIE 中控件观感尺寸变小」不可接受，明确下达「直接复原到对话最开始的版本」。

### 7.1 复原内容

| 目标 | 复原动作 | 回读结果 |
| --- | --- | --- |
| `Script/Function/AuctionHubUIService.lua` | 用写前备份 `before\AuctionHubUIService.lua.bak` 整文件覆盖 | 66,784 字节；第 938 行 `SetRenderScale`、第 939 行 `SetPositionInViewport`、第 966 行 `mode=DynamicScaleToFit` 旧逻辑回归 |
| `Asset/Blueprint/Prefabs/UI/ZhuJieMian`（根 `CanvasPanel_0_Wrapper_Wrapper`） | MCP plan `plan_16786615_eec827d2`：`SetStretch(0)`；`StretchDirection=0`、`StretchPc=0`、`StretchDirectionPc=0`；`save_package()` | `Stretch=0 StretchDirection=0 StretchPc=0 StretchDirectionPc=0 UsePcParams=False` |

- 「已修复版」另存于 `备份\IslandAuctionKing\20260915_PIE主界面不铺满\revert_before\`：
  `ZhuJieMian.uasset.fixed`（102,622 B）、`AuctionHubUIService.lua.fixed`（64,658 B）。
- 配置表侧无变化：复原后的脚本与 `_JsonOutput` 中 `ScaleBoxStretch` **0 处命中** → 本项目未新增 `UI.Hub.ScaleBoxStretch*` 行，无需回滚 DataTable。
- 生效方式：**重新调试 PIE**（蓝图资产 + 初始化逻辑变更）。

### 7.2 复原后事实（用于后续决策，构成对第二节的限定）

1. 1280×720 PIE 下主界面回到**只铺满约 0.828 × 0.828（1060×596）**，右侧与下方露出 3D 场景 —— 这是需求方**明确要求保留**的版本。
2. 设计器在 `Stretch=0` 下渲染为**设计坐标 1:1**：控件明显变大，且内容会**越出画布右/下边界被裁切**；`Stretch=2` 下才显示为 1280×720 视口的真实结果（0.667）。二者不可兼得：
   - `Stretch=0` → 观感尺寸＝设计尺寸，但整屏不铺满（PIE 缺陷回归）；
   - `Stretch=2` → 整屏铺满，但尺寸按「视口宽/设计宽」等比缩小。
3. 因此 2026-09-15 的铺满修复与设计器观感尺寸属**互斥取舍**，不是实现 bug；后续若要同时满足，只能改运行分辨率或重新按目标分辨率设计布局。

---

## 八、复原后的「不一致」复核（同日 12:59）

> ⚠️ **本章结论已被[第九章](#九真因锁定与修复同日-13351405二进制级取证)修正。** 本章只核对了根 ScaleBox 的 `Stretch` 等属性，**未回读子控件槽位**，因此把「与原来 UI 不一致」误判为纯设计器内存态问题。实际资产里右下角两个按钮的槽位几何确实残留了偏差（见第九章）。

需求方反馈「与原来 UI 不一致」。**本章原始复核结论（不完整，保留以备对照）**：资产数据与运行时均已回到原始状态，差异来自设计器标签页持有的旧内存态渲染。

### 8.1 复核证据

| 维度 | 结果 |
| --- | --- |
| 资产属性回读 | `Stretch=0 StretchDirection=0 StretchPc=0 StretchDirectionPc=0 UsePcParams=False UserSpecifiedScale=1.0` —— 与复原目标一致 |
| PIE 运行时 | 客户端 1280×720，UI 面板 1056×594，覆盖率 **0.8250 × 0.8250**（原始报障测量为 0.828 × 0.828） |
| Lua | 66,784 字节，与写前备份逐字节一致 |
| 设计器画布 | 强制 `close_editor_for_asset` → `open_editor_for_asset` 后，内容按 1920×1080 设计坐标 **1:1** 呈现、右/下越出 1280×720 画布被裁切 —— 即 `Stretch=0` 的原始设计态外观 |

### 8.2 关键机制

> **改动 root ScaleBox 的 `Stretch` 后，已打开的 UMG 设计器标签页不会跟随磁盘上的 `.uasset` 变化**，仍渲染打开时的内存副本。因此：
> - 只调 `open_editor_for_asset` 不够，必须 `close_editor_for_asset` → `open_editor_for_asset`；
> - 否则会把「旧内存态」误判为「本次改动后的外观」，产生「改了没生效 / 与原来不一致」的错误结论。

### 8.3 遗留项（非资产数据）

设计器画布左下角「屏幕尺寸」标签在我方 close/reopen 后显示 `1280 x 720 (16:9)`，而更早截取为 `1920 x 1080`。已核实该设置：

- **不在**资产数据：`schema:UGCWidgetBlueprint` 全部 Edit/BlueprintVisible 属性无任何 Design/Size 字段；生成类 `...ZhuJieMian_C`（继承 `UAEUserWidget`）同样 0 命中；
- **不在**工程 ini：`ShadowTrackerExtra\Saved\Config\WindowsUGCEditor\*.ini` 仅命中 `[AssetEditorManager] OpenAssetsAtExit` 等资产列表，无预览分辨率键；

⇒ 只能由设计器界面的「屏幕尺寸」下拉选择，无法通过 MCP / 配置写入。

另记：`.uasset` 字节数 102,260 B（写前）→ 102,622 B（现在）。修复与复原各触发一次 `save_package()` 整包重写，所有可读属性已回原值；**未做磁盘文件级覆盖**，因编辑器仍持有该资产内存态，覆盖会造成内存/磁盘不一致且必须重启编辑器（本项目记忆：内存脏时禁止 save）。


---

## 九、真因锁定与修复（同日 13:35–14:05，二进制级取证）

> **本章修正第八章结论。** 「与原来 UI 不一致」的**真实资产根因**是：12:48 那次复原操作在把根 ScaleBox `Stretch` 改回 0 的同时，**副作用把右下角两个按钮 `OpenRewardButton` / `OpenHelpButton` 的 `CanvasPanelSlot.LayoutData.Offsets` 重算成了偏小值**。

### 9.1 取证方法：浮点命中偏移比对

对 `.uasset` 全文件做 `struct.pack('<f', v)` 搜索，比较各候选版本的**命中偏移**。命中偏移相同 ⇒ 该浮点处在序列化流中的位置与值都一致；偏移不同 ⇒ 结构发生了变化。这比截图量测更硬，且不受光照、分辨率、视口缩放影响。

### 9.2 四个版本的槽位对照

| 文件（写前备份） | `OpenRewardButton` / `OpenHelpButton` 几何 | 槽位浮点命中偏移 |
| --- | --- | --- |
| `before\ZhuJieMian.uasset.bak`（10:18，**对话最开始**） | L=-418 / -300，T=-155，**R=140，B=130** | 50974 / 51474 / 51032 / 51532 / 51061 / 51561 |
| `revert_before\ZhuJieMian.uasset.fixed`（12:18，我方的 Stretch=2 修复版） | L=-418 / -300，T=-155，R=140，B=130 | 整体 **+47**（51021 / 51521 / 51079 / 51108）——几何正常，仅因 `Stretch` 文本变化导致序列化变长而后移 |
| `before_restore2\ZhuJieMian.uasset.1315`（13:15） | **L=-396.80 / -278.80，T=-132.63 / -133.80，R=99.96 / 118.80，B=98.20 / 108.80** | **偏差在此版本出现** |
| 修复后当前态 | L=-418 / -300，T=-155，R=140，B=130 | 与 10:18 版**逐字节同位** ✓ |

推得的尺寸变化（非拉伸锚点下 `Offsets.Right/Bottom` 即控件宽高）：

| 按钮 | 原始 | 偏差态 | 变化 |
| --- | --- | --- | --- |
| `OpenRewardButton` | 140 × 130 | 99.96 × 98.20 | 宽 −28.6%，高 −24.5% |
| `OpenHelpButton` | 140 × 130 | 118.80 × 108.80 | 宽 −15.1%，高 −16.3% |

且 `Left` 绝对值同步变小（−418→−396.80、−300→−278.80）⇒ 右移；`Top` 绝对值变小（−155→−132.63）⇒ 上移。视觉结果就是右下角两个按钮**又小又偏**，与「原来 UI」肉眼可辨地不一致。

> **机制推断（待官方/更多样本验证）**：`SetStretch` + `save_package()` 触发了 ScaleBox 所在子树的重建，编辑器对子 `CanvasPanelSlot` 做了重新布局计算并把结果落盘。属**写入副作用**，不是 `SetStretch` 本身的值错误 —— 第十二章旁证：`Stretch` 的回读值始终正确。

### 9.3 修复动作

- 写前备份：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260915_PIE主界面不铺满\before_restore2\`
  （`ZhuJieMian.uasset.1315` 102,575 B / md5 `909D53E7C1166F9715EDD505D31185CF`；`AuctionHubUIService.lua.1315` 66,784 B；`MANIFEST.txt`）
- 另在 `before_pie_restart\` 留存修复后即重启 PIE 前的状态（md5 `F83CA0D12A494684D1C3CD3D6588B9BF`）。
- MCP PRV 计划 `plan_16789055_52b774be`：从 `WidgetTree.RootWidget` 递归遍历（Panel 走 `Slots[i].Content`，Border/Button 走 `Content`/`Child`），命中 `OpenRewardButton` / `OpenHelpButton` 后对其 `CanvasPanelSlot` 写
  `LayoutData.Offsets = (-418, -155, 140, 130)` / `(-300, -155, 140, 130)`，`save_package()`。
- **必须补 `ue.compile_blueprint(wbp)` 再 `save_package()`**：UMG 控件树在 `.uasset` 内与 `WidgetBlueprintGeneratedClass` 内各存一份，只写一份时另一份不变、回读仍显示旧值（本轮首次写入后仍能读到旧几何，加编译后才一致）。

### 9.4 修复后核验

| 项 | 结果 |
| --- | --- |
| 相对 `1315`（偏差态） | 差 1,756 B（1.712%） |
| 相对 `orig`（对话最开始） | 差 1,940 B（1.891%），长度均为 102,575 B |
| 差异分布 | 全部落在 `[24..60]`（文件头 GUID/时间类）与 `[80490..85305]` 两段，内容是 UE 保存时生成的**元数据序号**（当前 `01, 92, 93 … a3` vs 原始全 `00`），**与控件几何无关** |
| 控件名字符串段 `[80400..81500]` | `true` / `CharacterTitleText` / `ZhuJieMian` / `OpenRewardButton` … 全部候选的 ASCII 偏移与原始**逐一对齐** |
| `EStretch::ScaleToFit` 出现次数 | `orig` = 0、当前 = 0、我方 Stretch=2 修复版 = 1 ⇒ 确认 `Stretch` 已回到原始值 |
| `AuctionHubUIService.lua` | 66,784 B，md5 `55010EBA901BC01C31730C052AC23D75`，与写前备份逐字节一致 |
| MCP 编辑器上下文 | `is_compiled=true`、`has_unsaved_changes=false` ⇒ 内存态与磁盘态一致 |

### 9.5 运行时复验（PIE）

蓝图资产**不可热更**，且旧 PIE 会话（客户端日志 13:25:47）持有的是修复前内存态，故必须 `ue_pie stop` → `start`。

判据用 `V_EDGE`（右侧 0.60~0.98 区间竖直边缘能量峰值列 ÷ 视口宽），历史标定：`0.824~0.826` = `Stretch=0` 原始态。

| 画面 | `V_EDGE` | 说明 |
| --- | --- | --- |
| 报障原图 `clipboard-2026-09-15T04-08-39-554Z-8c8ddff1.jpg`（12:08） | **0.8242** | 对话最开始 |
| 复原后基准 `capture3\pie_hub_reverted_client.png` | **0.8250** | 12:48 复原后 |
| **修复后当前 PIE**（`capture8\pie_main_ui_stretch0.png`） | **0.8250**，连续 3 帧不变 | ✓ 三者一致 |

> ⚠️ **量测陷阱（本轮踩到，已纠正）**：PIE `start` 返回后立刻抓图会拿到**主界面尚未渲染的首帧**，`V_EDGE` 落在 `0.7031`、右侧出现 193px 纯色带，若据此判断会得出「画面既不是 0.825 也不是铺满」的错误结论。必须轮询到连续多帧稳定（本轮约 15 s）再量测。

### 9.6 新增工具经验

1. **`edge_corr`（归一化边缘相关系数）不能当 UI 判据**：它由 3D 场景背景主导 —— 同一场景两次 PIE 抓图 `N vs D = 0.989`，而跨机器同 UI `N vs A = 0.199`。**UI 判据只能用 `V_EDGE`**，且必须同取景才可比（工作记忆既有告诫：窗口尺寸相同 ≠ 取景相同）。
2. **改根 `ScaleBox` 的 `Stretch` 后，必须回读其子树内所有关键控件的槽位几何**，不能只验证 `Stretch` 本身 —— 本轮漏判正是由此产生，且直到下一次量测才暴露。
3. **PIE 重启后必须等主界面稳定再量测**（见 9.5 陷阱）。
4. **禁止用 bash 内联 Python 写含反引号的 Markdown**：shell 会把 `` ` `` 当命令替换，整段内容被吞空。写文档一律 Write 落盘脚本再执行（本轮已踩并回滚重写）。
5. 编辑器内存态与磁盘态不一致时，**文件级覆盖不会改变运行中的 PIE**（PIE 从编辑器内存加载资产）；此时应走「MCP 写入 + `compile_blueprint` + `save_package`」，或「覆盖文件 + 重启编辑器」。

### 9.7 产物

- 脚本（知识库备份目录，ASCII 文件名）：`wait_and_measure_pie.py`、`stable_capture_pie.py`、`edge_structure_cmp.py`、`vedge_all.py`、`append_memory_section.py`
- 截图：`capture8\pie_main_ui_stretch0.png`（主界面全图）、`rightbottom_buttons_3x.png`（按钮区 3× 放大）、`pie_main_ui_annotated.png`（含红框标注）、`compare_A_D_N.png`（报障原图 / 复原基准 / 修复后 三图归一化对比）
- 报告：`analyze\capture6_report.txt`、`analyze\capture7_report.txt`、`analyze\capture8_report.txt`、`analyze\edge_structure_cmp.txt`、`analyze\vedge_all.txt`
