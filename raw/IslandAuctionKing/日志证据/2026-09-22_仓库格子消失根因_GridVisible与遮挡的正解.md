# 竞拍仓库「格子消失」根因与「格子可见 + 藏品图在上」正解

日期：2026-09-22（第八轮）
项目：IslandAuctionKing（海岛竞拍王）
现象（用户肉眼验收，权威）：**仓库格子整块不见，连边框都没有**。

---

## 一、根因：两个独立缺陷叠加

### 缺陷 1（决定性）：`UButton.BackgroundColor.A` 是本引擎的「整格绘制开关」

第七轮把 `GRID_TEXTURE_TINT_COLOR.A` 由 `1.00` 改为 `0.00`，并在三处强制把背景格底色 alpha 归零：

| 文件 | 位置 | 第七轮写法 |
|---|---|---|
| `AuctionWarehouseImageMaterialService.lua` | 常量 | `GRID_TEXTURE_TINT_COLOR = {A = 0.00}` |
| 同上 | `GetGridBaseColor` | **无条件**把返回色 alpha 归零 |
| `AuctionTestUIService.lua` | `RefreshWarehouse` | 新增 `cellBgColor` 二次归零 |
| `AuctionWarehouseCellService.lua` | `EnsureCells` | `ItemButton:SetBackgroundColor({A=0})` |

**实测结果：格子连纹理带边框一起消失。**

原因：格子外观来自 `ApplyGridTexture` 写入 `button.WidgetStyle.Normal/Hovered/Pressed/Disabled`
四个 `FSlateBrush.ResourceObject` 的「格子」纹理；而 `UButton.BackgroundColor.A` 在这一版引擎里
**同时控制该按钮是否参与绘制**。`A=0` 时引擎直接跳过整个按钮的绘制，
`WidgetStyle` 里的纹理一并消失。

> **结论：格子外观与「是否遮挡」共用同一个通道，无法通过调 alpha 在同一层上「既显又不遮」。**

第七轮注释里写的「置 `A=0` 只让按钮不再画不透明底板，**不会影响格子边框/纹理的显示**」
是**错误推断**，已被用户实测否定。该注释本轮已删除。

### 缺陷 2（叠加）：`ApplyCellChrome` 给每格写 `SetClipping(ClipToBounds)` 把整格裁没

`AuctionWarehouseCellService.ApplyCellChrome:349`（第七轮及以前）：

```lua
pcall(cellWidget.SetClipping, cellWidget, CLIP_TO_BOUNDS)
```

`ClipToBounds` 的语义是「把该控件裁到**它自己当前的尺寸矩形**内」。
但本函数复用的是**仓库格**的正常显示路径，而仓库格挂进画布时的尺寸是
`layout.cellSize`（默认 **85.2**），单格蓝图内的控件却是按图鉴卡片尺寸设计的：

- `ItemArt` 实测 `Pos(18,12) Size(224,141)`

→ **224×141 的内容被裁进 85.2×85.2 的矩形里，整格内容被裁掉。**

**反证（同引擎现成对照组）**：`AuctionSettlementUIService.ApplyWarehouseCellChrome:563`
同样写 `ClipToBounds`，却不产生副作用。差异在：

| 维度 | 结算（正确） | 竞拍仓库（出错） |
|---|---|---|
| 背景格父容器 | `WarehouseGrid`（**WrapBox**） | `WarehouseContentCanvas`（**CanvasPanel**） |
| 格子尺寸来源 | WrapBox 的 desired-size（`SetDesiredSizeOverride` 写全） | 画布槽位 `SetSize(cellSize=85.2)` |
| 裁切矩形 vs 内容 | 一致 | **差 2.6 倍，内容被裁没** |

---

## 二、正解：格子保持不透明可见，遮挡靠「绘制顺序」

本引擎已定论（第七轮四次受控实验）：

> **CanvasPanel 绘制顺序 = 父容器子控件插入顺序（后者在上）。**
> `Slot:SetZOrder` 数值写入生效但**不驱动**绘制顺序。

因此唯一可行的解法是：**让藏品覆盖层排在全部背景格之后（画布末尾）**，
而不是压低背景格的透明度。

对照 `AuctionSettlementUIService` 的完整做法（两条同时成立才正确）：

1. `InitializeWarehouseGrid:647` 写 `ItemButton:SetBackgroundColor({A=0})`；
2. `CreateOverlayWidgetForItem:1093` 用 `NewWidgetObjectBP` **新建图片实例**并
   `AddChildToCanvasSafe(layout.ParentCanvas, overlayWidget)` **追加到末尾**。

竞拍仓库缺的正是第 2 条：它用**蓝图预置**的 `CollectibleImage01..32` +
`AddChildToCanvas` **搬迁**，对已在同一父容器内的控件**不改变相对顺序**，
覆盖层永远落在背景格之前 → 被遮挡。

---

## 三、本轮落地改动（4 处，3 文件）

| 文件 | 位置 | 改动 |
|---|---|---|
| `AuctionWarehouseImageMaterialService.lua` | 常量 `GRID_TEXTURE_TINT_COLOR` | `A` 由 `0.00` **改回 `1.00`** |
| 同上 | `GetGridBaseColor` | **删除无条件 alpha 归零**，改为原样透传（无表时回退格子乘色） |
| 同上 | `ApplyGridTexture` / `ApplyCellTexture` | 注释纠正（原文案断言「与底色无关」已被实测否定） |
| `AuctionTestUIService.lua` | `RefreshWarehouse` 背景格循环 | **删除 `cellBgColor` 二次归零**，改回 `button:SetBackgroundColor(gridBaseColor)` |
| `AuctionWarehouseCellService.lua` | `EnsureCells` | **删除** `ItemButton:SetBackgroundColor({A=0})`（避免与上游时序互相覆盖） |
| 同上 | `ApplyCellChrome` | **删除 `SetClipping(ClipToBounds)`**（缺陷 2 根因）；删除常量 `CLIP_TO_BOUNDS` |

保留不动的关键部分：

- `EnsureOverlays` / `RaiseOverlays`：**真正的重挂**（`RemoveFromParent` → `AddChildToCanvas`），
  这是解决遮挡的唯一有效手段，第八轮继续保留。
- `EnsureOverlayOrder`：按「父容器子控件序号」断言覆盖层是否在末格之后（不依赖 z）。
- 覆盖层点击层 `TRANSPARENT_CLICK_LAYER_COLOR`（`A=0`）**保持不变且安全**：
  它是**覆盖层**的命中区按钮，不承载需要显示的纹理，A=0 只让它自身不可见（期望行为）。

---

## 四、验收判据

重跑双客户端 PIE（`team_count=2`，`AuctionConfig.RequiredPlayers=2`）后，逐项核对：

1. **仓库格子恢复可见**（84 格边框/纹理齐全，不再整块消失）；
2. **藏品图浮在格子上方**（滑动到任意位置、上下滚动均不被格盖住）；
3. 覆盖层层级日志 `EnsureOverlayOrder ... wrongCount=0`；
4. `ApplyCellChrome ... clipToBoundsApplied=false`。

三项均满足才算修复完成；缺任意一项即为未修复。
