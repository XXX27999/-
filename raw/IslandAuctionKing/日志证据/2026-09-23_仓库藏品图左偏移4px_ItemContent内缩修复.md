# 2026-09-23 仓库藏品图片相对格子左偏移 4px_ItemContent ButtonSlot 内缩

- 类型：项目实测 + 根因修复记录
- 主题：`CollectibleCodexItemUI_C` 单格内 `ItemContent` 的父级 `UButtonSlot` 内容槽配置造成仓库藏品图片相对格子向左偏移 4px；早期实测 `Padding=(4,2,4,2)`、`HAlign/VAlign=Center`，修复动作同时清零内边距并改为 Fill
- 适用范围：和平精英绿洲起源 UGC（UE4.18.1 / PCD3D_ES31 手机端），`IslandAuctionKing` 竞拍仓库 `AuctionTestUI` 单格控件 `CollectibleCodexItemUI_C`；结算界面复用同一单格控件，同类偏移风险同理
- 证据状态：项目实测（早期蓝图/CDO 只读与运行时探针 + 修复后 PIE 槽位回读 + 双客户端像素级截图对比 + Lua 语法检查）；归因边界见第二节
- 来源：
  - 用户截图 `C:\Users\ADMINI~1\AppData\Local\Temp\codex-clipboard-6420501e-3e70-4ffa-aa91-21f87d17c0dd.png`（原图 395x384）
  - 修复后双客户端截图 `备份\IslandAuctionKing\20260922_仓库藏品图左偏移\after_fix_t1.png`、`after_fix_t2.png`
  - 客户端日志 `Saved\Logs\IslandAuctionKing\Clientlog\FullLog\2026.09.23-10.23.21_client__dkck7prtmha7vq_1.log` / `_1_2.log`
  - 官方 API：`raw\docs\api\class\Others\UButtonSlot.md`、`raw\docs\api\cppenum\E\EH\EHorizontalAlignment.md`、`raw\docs\api\cppenum\E\EV\EVerticalAlignment.md`
- 更新时间：2026-09-23
- 关联主题：[2026-09-22_第十五轮_手机端仓库偏移与图鉴点击修复](./2026-09-22_第十五轮_手机端仓库偏移与图鉴点击修复.md)、[2026-09-22_单格控件内部隐藏层结构分析](./2026-09-22_单格控件内部隐藏层结构分析.md)、[2026-09-22_结算正确而竞拍仓库错误_层级机制对照](./2026-09-22_结算正确而竞拍仓库错误_层级机制对照.md)、[PIE调试启动要求_双客户端](../工具与流程/PIE调试启动要求_双客户端.md)
- 排除范围：未修改蓝图资产（`CollectibleCodexItemUI.uasset` 保持原样），修复仅落在运行时 Lua 归一化；未验证 PC 端（`pchd`）表现
- 官方依据：`UButtonSlot.Padding`（槽与内容之间的内边距）、`UButtonSlot.HorizontalAlignment` / `VerticalAlignment`（内容对齐）、`SetPadding` / `SetHorizontalAlignment` / `SetVerticalAlignment` 方法；`HAlign_Fill=0`、`VAlign_Fill=0`

## 一、现象与量化

用户截图（原图 395x384）中，紫色藏品主体水平范围 `x=13..68`，同列格子暗色实体 `x=17..72`：

- 两者宽度相同（56px），但藏品主体整体**左移 4px**。
- 偏移是**水平、恒定 4px**，不是缩放或贴图裁切问题。

已逐项排除：

- 单格根 `Slot`、`ItemButton.Slot`、`ItemImage.Slot` 均为 `0,0,85.2x85.2`。
- `RenderTranslation=(0,0)`、`RenderScale=(1,1)`、`Pivot=(0.5,0.5)`。
- 两侧画刷 `DrawAs=3`、`Tiling=0`、`ImageSize=32x32`。
- 贴图 `a7`/`a8` 均为 `101x101` RGBA，内容覆盖整幅，不存在单边留白。

## 二、根因（运行时实测）

单格层级为 `ItemButton -> ButtonSlot -> ItemContent -> CanvasPanel -> ItemImage`。

### 已直接证实

- 修复前运行时探针实测内容槽对齐为 `HAlign=2(Center)`、`VAlign=2(Center)`；修复后回读为 `0,0(Fill)`。
- 双客户端像素复测显示系统性 4px 左移消失（详见第四节），因此可以确定 `Center -> Fill` 归一化解决了用户可见偏移。

### 归因边界

- 早期运行时探针同时读到 `Padding=(4,2,4,2)`，其水平内边距数值与 4px 偏移量一致；但修复后验证会话的 `paddingBefore` 已因 `Cached` 路径先执行归一化而读为 `0,0,0,0`，无法用本轮 A/B 数据单独证明 Padding 贡献了全部 4px。
- 因此严格结论是：修复动作“Padding 清零 + 对齐改 Fill”消除了系统性偏移；其中 `Center -> Fill` 已被修复前后回读直接证实，Padding 是同时存在的早期实测原值，但其独立贡献尚需在首次 `EnsureCells` 前读取原始 Padding 才能拆分。

运行时探针（`doluastring` + `GetWidgetFromName`，客户端 hwnd 字符串十进制）：

```text
CAP3 contentSlot=ButtonSlot ...ItemButton.ButtonSlot_0
CAP3 padL=4.0
CAP3 padT=2.0
CAP3 padR=4.0
CAP3 padB=2.0
CAP3 alignH=2
CAP3 alignV=2
CAP3 hasSetPadding=true
CAP3 hasSetH=true
CAP3 hasSetV=true
```

该探针确认修复前内容槽处于非 Fill 居中且水平内边距为 4px 的状态；其布局配置与用户观测偏移方向一致。
上列探针确认修复前内容槽同时处于非 Fill 居中与 4px 水平内边距状态；当前证据可确定该内容槽布局是修复对象，但不能把 4px 全部单独归因给 Padding。

**关键取证方法**：`ItemContent` 未勾选 Is Variable，不能 `widget.ItemContent` 或 `img.Parent` 直取，必须 `widget:GetWidgetFromName("ItemContent")`；`client_hwnd` 在 `ue_pie` schema 中是**字符串**类型，传整数会报 `TypeMismatch=[client_hwnd]`。

## 三、修复

`Script/Function/AuctionWarehouseCellService.lua` 新增模块级辅助函数 `NormalizeItemContentSlot(cellWidget, cellIndex)`：

```lua
local itemContent = FindNamedWidget(cellWidget, "ItemContent")
local slot = itemContent.Slot
slot:SetPadding({Left = 0, Top = 0, Right = 0, Bottom = 0})
slot:SetHorizontalAlignment(EHorizontalAlignment.HAlign_Fill)
slot:SetVerticalAlignment(EVerticalAlignment.VAlign_Fill)
```

调用点两处（缺一不可）：

1. `EnsureCells` 的 `Cached` 快路径：旧实例可能仍保留蓝图默认非 Fill 对齐与内边距，缓存命中时重新归一化。
2. `EnsureCells` 新建格路径：在 `ItemButton.Slot` 尺寸归一化之后调用，失败只记录错误、不中断建格。

不使用固定 `+4px` 补偿，而是归一化内容槽的真实布局配置，避免掩盖后续蓝图改动。全部写入包 `pcall`，并输出入口/关键数据/错误/出口日志。

## 四、验证结果

1. Lua 语法：`luaparser` 通过 `Script\Function\AuctionWarehouseCellService.lua`。
2. PIE 双客户端手机端（`team_count=2, players_per_team=1, simulation_platform=mobile`，DebugID `_dkck7prtmha7vq`）。
3. 运行时回读：

```text
C6 pad=0.0,0.0,0.0,0.0 align=0,0
```

4. 84 格归一化日志（节选）：

```text
【AuctionWarehouseCellService+NormalizeItemContentSlot】关键数据 cellIndex=1 applied=true paddingBefore=0.0,0.0,0.0,0.0 alignBefore=2,2 paddingAfter=0.0,0.0,0.0,0.0 alignAfter=0,0
...
【AuctionWarehouseCellService+EnsureCells】关键数据 createdCount=84 cellSize=85.2 step={X=95.4,Y=93.5} overlayOrderFixed=true remedy=Raise(raised=64,failed=0,wrongBefore=64)
【AuctionWarehouseCellService+EnsureCells】出口 success=true source=Created
```

注：`paddingBefore` 在部分格显示 `0,0,0,0` 是 `SetPadding` 已被缓存路径先归一化后的读数，`alignBefore=2,2` 证明原始居中状态确实存在。

5. 像素级截图对比：

| 客户端 | 紫色主体 x0 | 同列格子 x0 | 差值 |
| --- | --- | --- | --- |
| 修复前（用户截图） | 13 | 17 | 4px |
| 修复后 T1 | 999 | 1000 | 1px |
| 修复后 T2 | 935 | 937 | 2px |

修复后残余 1~2px 为截图反锯齿与边缘判定误差，肉眼已重合，4px 系统性偏移消失。

## 五、待查证与后续

### 为什么结算界面看不出同一偏移

结算界面复用同一 `CollectibleCodexItemUI_C`，但它的**格子纹理与藏品图都画在各自单格控件的 `ItemImage` 上**（格子纹理见 `AuctionSettlementUIService.LayoutSettlementGridCells` 写 `cellWidget.ItemImage`；藏品图见 `ConfigureImageOnlyWidget` 写 `displayWidget.ItemImage`）。两者都位于各自 `ItemContent -> ButtonSlot` 内，承受同一套内容槽布局，相对关系保持对齐，肉眼看不到偏移。

竞拍仓库不同：格子纹理画在单格 `ItemImage` 内（受 `ButtonSlot` 内容槽布局影响），而藏品图是**独立覆盖层** `CollectibleImage01..32`，其 `CanvasPanelSlot` 直接对齐真实格矩形、不受 `ButtonSlot` 影响 → 两者产生约 4px 的可见差异，才显出「藏品图相对格子向左偏移」。

结论：结算界面当前无需补 `NormalizeItemContentSlot`；若未来把结算的格子纹理或藏品图改到不同层级，需重新评估。

## 六、未验证项

- 未验证 PC 端（`pchd`）表现。
- 未修改蓝图资产；若希望永久消除蓝图默认值，可在 UGCAskQ MCP `Resolve -> Plan -> Execute` 流程下改 `CollectibleCodexItemUI` 的 `ItemContent` 槽位并回读，但当前运行时修复已足够且更可控。

## 七、备份路径


- 写前 Lua 备份：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260922_仓库藏品图左偏移\pre_edit_AuctionWarehouseCellService.lua`
- 证据与探针：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260922_仓库藏品图左偏移\`
