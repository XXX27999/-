# 2026-09-15 AuctionTestUI 竞拍界面概念图按控件拆分

> 类型：项目证据（蓝图与 UI）
> 主题：把「修仙网游风」竞拍界面概念图按 `AuctionTestUI` 当前控件树拆分为可复用部件
> 项目：IslandAuctionKing（海岛竞拍王）
> 适用范围：仅本项目。控件名、几何、资产路径均为本项目专属，不可升格为通用结论
> 证据状态：控件树为 **MCP 实测回读**（2026-09-15 18:2x，PIE 运行中）；切图坐标为**像素测量 + 人工核对**，标注为参考值（±10~20px）
> 来源：`ue_py` → `ue.widget_inspect` 全控件树回读；概念图 `C:\Users\Administrator\.workbuddy\clipboard-images\clipboard-2026-09-15T10-19-31-488Z-7f29147e.jpg`（1920x1156，用户上传）
> 更新时间：2026-09-15
> 关联主题：[竞拍UI布局与按钮画刷修复](./2026-08-31_竞拍UI布局与按钮画刷修复.md)、[AuctionTestUI_第二张参照图对齐](./2026-09-01_AuctionTestUI_第二张参照图对齐.md)、[UI 贴图全量合规清单](../资产清单/2026-08-26_UI贴图全量合规清单.md)
> 排除范围：不包含把切图导入编辑器并绑定画刷的写入步骤（属资源导入规范与 MCP 写入流程）；不包含玩法数值
> 官方依据：无（本页为项目实测回读与切图证据，不涉及官方 API 结论）

---

## 一、输入与依据

| 项 | 值 |
| --- | --- |
| 目标蓝图 | `/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/AuctionTestUI`（竞拍测试界面，即竞拍主界面） |
| 控件树来源 | UGCAskQ MCP `ue.widget_inspect`（只读，未做任何写入） |
| 回读时编辑器状态 | 工程 `IslandAuctionKing`，`is_debug_playing=true`（PIE 运行中） |
| 设计舞台 | 根链 `ScaleBox_0 → SizeBox_0 → CanvasPanel_0`，坐标体系 1920x1080 |
| 概念图 | 1920x1156（底部含 76px 水印条「豆包AI生成」，切图时按 1920x1080 裁掉） |
| 控件总数 | 回读树约 34012 字符，含 6 大板块 + 6 个浮动面板 |

## 二、当前 UI 控件骨架（MCP 回读）

根 `CanvasPanel_0` 下的 6 个板块级控件（`Size` 为 1920x1080 舞台坐标）：

| 控件 | 类 | Pos | Size | 语义 |
| --- | --- | --- | --- | --- |
| `HUDBackgroundPanel` | Border | 0,0 | 1920x1080 | 整屏底板 |
| `TopBarPanel` | Border | 11,9 | 1896x113 | 顶栏 |
| `LeftPlayerPanel` | Border | 11,131 | 545x801 | 左侧四席位 |
| `RightDetailPanel` | Border | 571,131 | 674x801 | 中间详情/情报 |
| `WarehousePanel` | Border | 1257,131 | 648x801 | 右侧仓库 |
| `FooterPanel` | Border | 11,948 | 1896x107 | 底部操作栏 |

浮动面板（初始多为折叠，`Construct` 后按需显示）：`PropPanel`(11,131,545x801)、`BidKeypadPanel`(708,268,503x545)、`SkillPanel`(480,110,880x820)、`RoundDetailPanel`(616,240,687x601)、`EmotePanel`(600,235,720x520)、`HelpPanel`(700,312,520x455)。

关键内部控件（拆分对位用）：

- 顶栏：`TitleText`(719,36,290x45)、`RoundText`(633,163)、`CountdownText`(1070,40)、`ParticipantText`(1364,40)、`PrivacyText`(596,250)、`LockedCountText`(1553,35)、`BrandEyebrowText`(32,32)
- 左栏：`ScoreText01..04`(100, 192/378/558/744)、`PlayerMarkText01..04`、`PlayerSubText01..04`、`RoundHistoryButton/Image/BidText P01..P04 × R01..R05`（4 席位 × 5 轮 = 20 格）、`RoundIndexTextPxxRxx`
- 中栏：`IntelScrollBox`(588,200,643x690)、`IntelCardBackground01..05`、`RoundProgressDot01..05`(994..1162,184)、`RoundDetailPanel` 及其 24 个子控件
- 右栏：`WarehouseTitleText`(1300,176)、`EstimatedValueText`(1282,198)、`WarehouseKnownHintText`(1614,135)、`CellButton01..36`(1296..1857, 238..791，6x6 网格，单元格 85x85)、`OpenCollectibleCodexButton`(1638,826,209x72)
- 底栏：`OpenPropPanelButton`(27,957,140x85)、`OpenHelpPanelButton`(179,957,140x85)、`OpenEmotePanelButton`(331,957,140x85)、`BidDisplayButton`(615,957,415x85)、`LockBidButton`(1030,957,154x85)

## 三、部件拆分表（切图产物）

坐标均为概念图像素（1920x1080 有效区）。切图目录：
`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260915_竞拍界面部件拆分\parts\`

| ID | 部件名 | 坐标 (x1,y1,x2,y2) | 尺寸 | 对应当前控件 | 用途 |
| --- | --- | --- | --- | --- | --- |
| 01 | `01_Plate_Background` | 0,0,1920,1080 | 1920x1080 | `HUDBackgroundPanel` | 整屏底板/底纹 |
| 02 | `02_Frame_TopBar` | 10,8,1910,116 | 1900x108 | `TopBarPanel` | 顶栏外框 |
| 03 | `03_Plate_TitlePlate` | 826,10,1078,62 | 252x52 | `TitleText` 所在位 | 中央标题牌 |
| 04 | `04_Slot_TopSmall01` | 1307,12,1490,60 | 183x48 | 顶栏右侧第 1 框（当前无控件） | 顶部小框 |
| 05 | `05_Slot_TopSmall02` | 1500,12,1683,60 | 183x48 | 顶栏右侧第 2 框（当前无控件） | 顶部小框 |
| 06 | `06_Slot_TopSmall03` | 1699,12,1882,60 | 183x48 | 顶栏右侧第 3 框（当前无控件） | 顶部小框 |
| 07 | `07_Frame_LeftPanel` | 20,120,555,860 | 535x740 | `LeftPlayerPanel` | 左栏整栏外框 |
| 08 | `08_Template_SeatCard` | 34,125,540,250 | 506x125 | `ScoreText01`+`RoundHistory*P01*` 簇 | 单席位卡模板（标题条+槽位行+进度条） |
| 09 | `09_Frame_CenterArt` | 555,120,1290,870 | 735x750 | `RightDetailPanel` | 中央大图画框 |
| 10 | `10_Art_CenterScene` | 585,145,1260,845 | 675x700 | 中央大图内容 | 仙境场景底图（可作底板/占位） |
| 11 | `11_Frame_RightPanel` | 1290,120,1912,870 | 622x750 | `WarehousePanel` | 右栏整栏外框 |
| 12 | `12_Plate_RuneSlab` | 1490,231,1742,800 | 252x569 | `CellButton01..36` 覆盖区 | 符文石板（仓库格底纹叠加） |
| 13 | `13_Frame_RightActionBar` | 1470,815,1845,900 | 375x85 | `OpenCollectibleCodexButton`(1638,826) | 右栏底部功能按钮条 |
| 14 | `14_Frame_Footer` | 10,960,1902,1070 | 1892x110 | `FooterPanel` | 底部栏外框 |
| 15 | `15_Slot_FooterSmall01` | 36,975,150,1055 | 114x80 | `OpenPropPanelButton`(27,957) | 底栏小框 1（打开道具） |
| 16 | `16_Slot_FooterSmall02` | 160,975,274,1055 | 114x80 | `OpenHelpPanelButton`(179,957) | 底栏小框 2（帮助） |
| 17 | `17_Slot_FooterSmall03` | 284,975,398,1055 | 114x80 | `OpenEmotePanelButton`(331,957) | 底栏小框 3（表情） |
| 18 | `18_Btn_FooterMain` | 500,970,1100,1055 | 600x85 | `BidDisplayButton`(615,957,415x85) | 底部中央主按钮 |
| 19 | `19_Slot_FooterRight` | 1110,975,1290,1055 | 180x80 | `LockBidButton`(1030,957,154x85) | 底部右侧按钮位 |
| 20 | `20_Deco_TopLeftOrnament` | 14,10,760,116 | 746x106 | 顶栏左段装饰 | 云纹/角花装饰条 |

核对总览图：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260915_竞拍界面部件拆分\_parts_overview.png`

## 四、概念图 ↔ 控件骨架映射（整体）

| 概念图区域 | 当前控件板块 | 吻合度 | 说明 |
| --- | --- | --- | --- |
| 顶部横栏（标题牌 + 右侧三小框） | `TopBarPanel` | 中 | 标题牌位置吻合；右侧三小框在当前控件树中**无对应控件** |
| 左侧四组卡片（标题条+槽位+进度条） | `LeftPlayerPanel` | 高 | 组数与席位一致；**槽位数不一致**（见第五节） |
| 中间大图 | `RightDetailPanel` | 中 | 当前该板块承载情报卡滚动区 + 轮次详情，非单纯大图 |
| 右侧板块（顶部条 + 符文石板 + 底部按钮） | `WarehousePanel` | 高 | 石板覆盖区正是 6x6 仓库格；底部按钮对应图鉴入口 |
| 底部横栏（三小框 + 中央长按钮） | `FooterPanel` | 高 | 三小框 ↔ 三个功能入口；长按钮 ↔ `BidDisplayButton` |
| 整屏底纹 | `HUDBackgroundPanel` | 高 | — |

## 五、差异与待确认（未擅自改动工程）

1. **槽位数量不一致**：概念图左栏每席位 4 个槽位（4×4=16），当前工程每席位 `RoundHistory*R01..R05` 为 5 格（4×5=20）。切图按概念图 4 格切出，实际对位需确认以哪边为准。
2. **顶栏右侧三小框无对应控件**：当前顶栏只有文本（`CountdownText`/`ParticipantText`/`LockedCountText`），概念图是三个带框的实心小格。若要还原，需新增 3 个 `UBorder`/`UImage` 并走 MCP 写入。
3. **符文石板是单块贯通装饰**：概念图右栏是一整块符文石板，当前是 6x6=36 个 85x85 格。石板只能作为**底纹叠加层**，不能替代格子。
4. **概念图高度 1156 ≠ 舞台 1080**：底部 76px 为生成水印条，已全部裁除；`01_Plate_Background` 按 1080 切。
5. **细粒度模板尚未切出**：单空槽、槽位选中态、进度条底/填充、进度宝石、云纹角花、紫色闪电 FX 等更细部件本轮未拆（需按 `08_Template_SeatCard` 内部相对坐标二次细化），如需要可继续。
6. 切图坐标由像素投影 + 人工核对得出，**存在 ±10~20px 误差**；正式导入前应用编辑器设计器截图对照微调。

## 六、产物清单

| 类型 | 绝对路径 |
| --- | --- |
| 切图目录（20 张 PNG） | `D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260915_竞拍界面部件拆分\parts\` |
| 切图核对总览 | `D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260915_竞拍界面部件拆分\_parts_overview.png` |
| 概念图原件（用户上传） | `C:\Users\Administrator\.workbuddy\clipboard-images\clipboard-2026-09-15T10-19-31-488Z-7f29147e.jpg` |

## 七、下一步建议

1. 确认第五节第 1、2 条后，再决定是否新增顶栏三框控件与槽位数量口径。
2. 需要还原时按 [资源导入与路径规范](../../知识/通用/配置与数据/资源导入与路径规范.md) 导入 `Asset`，五项合规属性（`LODGroup=16`/`MipGenSettings=13`/`CompressionSettings=0`/`CompressionQuality=5`/`SRGB=True`），再用 UGCAskQ MCP 绑定画刷并回读。
3. 写入前先备份到 `备份\IslandAuctionKing\20260915_竞拍界面部件拆分\`。

## 相关页面

- [竞拍UI布局与按钮画刷修复](./2026-08-31_竞拍UI布局与按钮画刷修复.md)
- [AuctionTestUI_第二张参照图对齐](./2026-09-01_AuctionTestUI_第二张参照图对齐.md)
- [UI 贴图全量合规清单](../资产清单/2026-08-26_UI贴图全量合规清单.md)
- [资源导入与路径规范](../../知识/通用/配置与数据/资源导入与路径规范.md)
