# 2026-09-14 ZhuJieMian 主界面底图导入与设置

> 类型：项目证据（蓝图与 UI）
> 主题：`ZhuJieMian` 整屏底图控件 `参考图` 的贴图导入与设计态绑定
> 适用范围：仅 `IslandAuctionKing` 项目；通用做法见 [资源导入与路径规范](../../知识/通用/配置与数据/资源导入与路径规范.md)
> 证据状态：项目实测（MCP 写入 + 跨会话回读 + 磁盘核对）；贴图属性为官方确认口径
> 更新时间：2026-09-14
> 官方依据：`raw/docs/wiki/新手入门/资源管理与编辑/277_资源导入.md`、`raw/docs/wiki/新手入门/资源管理与编辑/资源编辑/300_贴图与材质编辑.md`
> 来源：[2026-09-14 主界面底图导入与拖拽导入受阻查证](../../知识/通用/来源记录/2026-09-14_主界面底图导入与拖拽导入受阻查证.md)
> 关联主题：[ZhuJieMian 画刷现状基线表](../../知识/通用/UI与交互/ZhuJieMian画刷现状基线表.md)、[竞拍 UI 贴图导入与运行时替换](../资产清单/2026-08-31_竞拍UI贴图导入与运行时替换.md)
> 排除范围：竞拍界面（`AuctionTestUI`）与结算界面（`AuctionSettlementUI`）底图不在本页范围

---

## 一、结论

1. 主界面整屏底图控件已确认为 `ZhuJieMian` 根 `CanvasPanel_0` 下第 1 个子控件 **`参考图`（`UImage`）**：锚点四向拉伸 `(0,0)-(1,1)`、Offsets 全 0、`ZOrder=-5`（全树最低）。
2. **该控件在本轮写入前的 `Brush.ResourceObject` 为 `None`（设计态无贴图）**，与 [ZhuJieMian 画刷现状基线表](../../知识/通用/UI与交互/ZhuJieMian画刷现状基线表.md) 2026-08-26 记录的 `ZJM2` 不一致，属基线过期（详见第四节）。
3. 新贴图 `ZJMBackground` 已导入 `/IslandAuctionKing/Asset/TuPian/ZhuJieMian/`，五项 UI 贴图属性全部合规，并已绑定到 `参考图`。
4. 运行时不会被覆盖：`AuctionDressUIService` 的级联定义里 `HubBackground` 行虽把 `Target` 写成 `参考图`，但**代码中没有任何把选中材质应用到 `Target` 的实现**，`ApplyPreviewMaterial` 只作用于装扮界面自身预览图。

---

## 二、资产落位

| 项 | 值 |
| --- | --- |
| 贴图资产 | `/IslandAuctionKing/Asset/TuPian/ZhuJieMian/ZJMBackground`（`Texture2D`） |
| 磁盘文件 | `...\UGCProjects\IslandAuctionKing\Asset\TuPian\ZhuJieMian\ZJMBackground.uasset`（6,292,370 字节） |
| 原图 | 用户提供的 `背景.png`，实际可用副本为剪贴板 JPEG，1671×941（宽高比 1.7758，与 16:9 的 1.7778 相差 0.11%） |
| 绑定控件 | `/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/ZhuJieMian` → WidgetTree → `CanvasPanel_0_Wrapper_Wrapper`(ScaleBox) → `CanvasPanel_0_Wrapper`(SizeBox) → `CanvasPanel_0`(CanvasPanel) → `参考图`(Image) |

导入调用：`ue.import_asset(<暂存英文名 jpg 绝对路径>, '/IslandAuctionKing/Asset/TuPian/ZhuJieMian')`
—— 目标参数只传**资产目录**，不拼接资产名（拼接会建同名子文件夹）。

---

## 三、写入与回读证据

### 3.1 贴图侧（plan_id `plan_16790507_30f41bfa`）

导入后逐项写入并回读，五项与 `ZJM1`–`ZJM11` 完全同构：

| 属性 | 目标值 | 写入前 | 写入后 |
| --- | --- | --- | --- |
| `LODGroup` | 16 | 0 | **16** |
| `CompressionSettings` | 0 | 0 | **0** |
| `MipGenSettings` | 13 | 13 | **13** |
| `SRGB` | True | True | **True** |
| `CompressionQuality` | 5 | 0 | **5** |

跨会话 `load_object` 复读：`(16, 0, 13, True, 5)`，尺寸 `1671x941`，与写入一致。
`tex.save_package()` 成功；磁盘出现 `ZJMBackground.uasset`。

> 注意：`ue.objed_save_asset('ZJMBackground','Texture')` 报 `Asset 'ZJMBackground' not found in Texture editor.`（该资产未在纹理编辑器中打开）。**贴图侧以 `save_package()` 为准**，`objed_save_asset` 仅适用于 .uasset 已在对应编辑器页签打开的情形。

### 3.2 画刷侧（plan_id `plan_16790539_1d9b62f4`）

```python
img.call_function('SetBrushFromTexture', tex, False)   # False = 不按贴图尺寸改控件尺寸
```

| 项 | 写入前 | 写入后 |
| --- | --- | --- |
| `参考图.Brush.ResourceObject` | `None` | **`ZJMBackground` (Texture2D)** |
| `DrawAs` | 3 (Image) | 3 (Image)，未变 |
| `Tiling` | 0 (NoTile) | 0，未变 |
| `ImageType` | 0 (NoImage) | 0，未变 |
| `ColorAndOpacity` | (1,1,1,1) | (1,1,1,1)，未变 |
| Slot 锚点 | (0,0)-(1,1) | (0,0)-(1,1)，未变 |
| Slot Offsets | (0,0,0,0) | (0,0,0,0)，未变 |

`bp.save_package()` 返回对象本身（非布尔，不能当成功判据）；`ue.objed_save_asset('ZhuJieMian','UI')` 返回 `True`。
重新 `load_object` 复读 `ResourceObject == ZJMBackground`，`pkg_dirty == False`，控件树总数 46（14 个 `Image` + 其余文本/按钮/容器），`参考图` 仍在。
磁盘 `ZhuJieMian.uasset` 由 102,260 → 102,489 字节，`mtime` 更新为 14:02。

### 3.3 布局未被改动

`SetBrushFromTexture(..., False)` 不触发 `bMatchSize`，`参考图` 的锚点与 Offsets 保持全屏拉伸，不需要额外补 `Slot` 修正。

---

## 四、与 2026-08-26 画刷基线的差异（基线过期，需订正）

以 2026-09-14 实测为准，[ZhuJieMian 画刷现状基线表](../../知识/通用/UI与交互/ZhuJieMian画刷现状基线表.md) 第 22 节表格存在三处过期：

| 项 | 基线表（2026-08-26） | 2026-09-14 实测 |
| --- | --- | --- |
| 控件树总数 | 23（1 `CanvasPanel` + 14 `Image` + 8 `TextBlock`） | **46**（含 `ScaleBox`/`SizeBox` 适配层、按钮、更多文本） |
| `参考图.Brush.ResourceObject` | `ZJM2` | 写入前为 **`None`**，写入后为 `ZJMBackground` |
| `地图UI`（`ZJM4`） | 存在，右上锚点 | **已不存在**；同区域现为 `Image_160`（`ZJM12`） |

未变化项：`参考图` 的 `ZOrder=-5`、四向拉伸锚点 `(0,0)-(1,1)`、Offsets 全 0 均与基线一致；`ZJM1` 仍被 3 个「上方UI」共用，`ZJM3` 仍被「玩家名称/服务器剩余时间」共用。

另需注意：`ZJM4` 现已**无人引用**（仅占目录）。当次基线表对 `参考图` 贴图名的记录来源是 UAssetAPI JSON，而该项目 JSON 的 import 索引映射存在错位风险（参见基线表自身对 `_JsonOutput` 的说明），**贴图名以 MCP 反射回读为准**。

---

## 五、运行时链路核实（不会被覆盖）

`Script/Function/AuctionDressUIService.lua` 第 56–80 行级联定义中的 `Target` 字段只在主界面/竞拍/结算三处声明（`参考图`、`AuctionRootBackground`、`SettlementBackground` 等），但通读全文件：

- 唯一实际写入画刷的函数是 `ApplyPreviewMaterial(previewImage, ...)`，第 334 行与第 450 行调用点传入的都是**装扮界面自身的预览图**；
- 没有任何函数读取 `Region.Target` 并把材质应用到该控件。

**结论：当前装扮系统不会覆写 `参考图`，设计态绑定的 `ZJMBackground` 会在运行期保留。**

同时暴露一个未接通点：`ImageMaterialTable`（`Data/Table/Customized/ImageMaterialTable`，15 行）**没有 `HubBackground` 行**，而级联定义要求 `TextureRow = "HubBackground"`。即装扮界面「主界面 → 主界面底图」目前既无可选材质、也无应用落点。若要打通，需（a）在表中补 `HubBackground` 行，（b）在服务中实现 Target 应用逻辑 —— 两者都属功能变更，**未在本轮实施，需与需求方确认**。

---

## 六、生效方式与备份

- **生效方式**：**必须重新调试 PIE**（涉及蓝图资产画刷与新增贴图资产）。
- **备份路径**：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260914_主界面背景图导入\`
  - `before\ZhuJieMian.uasset.bak`（写前蓝图，102,260 字节）
  - `staging\ZJMBackground.jpg`（导入用暂存源图）
  - `diagnose\`（拖拽导入受阻的本机取证文件，见 [来源记录](../../知识/通用/来源记录/2026-09-14_主界面底图导入与拖拽导入受阻查证.md)）

---

## 七、预估成功日志

PIE 进入等待阶段、`ZhuJieMian` 被创建时，应看到既有日志：

```
【ZhuJieMian+Construct】入口 self=...
【AuctionHubUIService+Initialize】...
【ZhuJieMian+Construct】出口 success=true error=nil
```

（标注为**预估成功日志**：本轮未启动 PIE，日志格式取自现有脚本，未实测。）

---

## 八、待查证

1. 用户原始 `背景.png` 未在本机常见目录（桌面/下载/图片/文档）检索到，本次使用的是剪贴板导出的 JPEG 副本（1671×941）。若存在更高分辨率或无损原图，应重新导入覆盖以获得更好画质 —— **未与需求方确认**。
2. `参考图` 在 2026-08-26 之后从 `ZJM2` 变为 `None` 的**成因不明**（人工清空？适配层重构时被重置？），未取得改动记录。
3. 本轮未截取编辑器设计态或 PIE 截图做视觉确认：编辑器进程以高完整性级别运行，`SetForegroundWindow` 对其无效，`$oasis-ui-screenshot` 的 GDI 路径要求用户先把目标页签置于前台。视觉验收**待用户在编辑器中自行确认**。
