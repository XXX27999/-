# AuctionTestUI 画布溢出修复

> 类型：项目事实 / 蓝图与 UI / MCP 写入与 FlaUI 截图验证
> 主题：`AuctionTestUI` 根 `ScaleBox` 的画布适配
> 适用范围：`IslandAuctionKing` 项目，`AuctionTestUI` 设计态
> 证据状态：MCP Resolve/Plan/Execute、编译保存、重新加载回读和 FlaUI 完整编辑器截图已完成；未启动 PIE
> 来源：用户反馈截图、UGCAskQ MCP 回读与写入、项目既有 UI 记录、FlaUI 截图
> 更新时间：2026-09-02
> 关联主题：[竞拍 UI 编辑器设计态与网页预览对比](./2026-09-01_AuctionTestUI_编辑器设计态与网页预览对比.md)、[竞拍 UI 布局与按钮画刷修复](./2026-08-31_竞拍UI布局与按钮画刷修复.md)、[IslandAuctionKing 项目资料索引](../000_项目索引.md)
> 排除范围：本页不证明 PIE 运行态像素、不同分辨率运行态和输入事件链；不修改 Lua、配置表、控件树、按钮事件或素材
> 官方依据：`D:\oasis-skill-plus\docs\api\class\Others\UScaleBox.md`、`D:\oasis-skill-plus\docs\api\cppenum\E\ES\EStretch.md`

## 问题与根因

用户反馈 `UI 超出画布`。MCP 只读回读目标资产确认控件树为：

`ScaleBox_0 -> SizeBox_0 -> CanvasPanel_0`

写入前状态为：

- `ScaleBox_0.Stretch=1`，即官方 `EStretch.Fill`，非等比填充整个可用区域
- `ScaleBox_0.UsePcParams=False`
- `SizeBox_0.bOverride_WidthOverride=True`
- `SizeBox_0.bOverride_HeightOverride=True`
- `SizeBox_0.WidthOverride=1620`
- `SizeBox_0.HeightOverride=971`

项目网页设计基准和 Canvas 子控件坐标均按 `1620x971` 设计舞台建立。`Fill` 会破坏该固定设计舞台的比例契约，导致设计器展示范围出现越界/拉伸观感。

## 修复记录

目标资产：

`/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/AuctionTestUI`

写入前备份：

`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\_Backup\2026-09-02_AuctionTestUI_ContainmentFix\AuctionTestUI_before_ContainmentFix.uasset`

MCP 计划：`plan_16778700_d4296da8`

只修改根控件属性：

- `ScaleBox_0.Stretch: 1 (Fill) -> 2 (ScaleToFit)`
- 保留 `StretchDirection=0 (Both)`
- 保留 `UsePcParams=False`
- 保留 `SizeBox_0=1620x971` 及两个 Override 开关

官方 `EStretch` 定义确认：`Fill=1` 为非等比填充；`ScaleToFit=2` 为保持比例缩放，直到不再发生裁切。该修复没有改动业务坐标和控件层级。

## 回读与截图证据

重新加载资产后的 MCP 回读：

- `ScaleBox_0.Stretch=2`
- `ScaleBox_0.StretchPc=1`，但 `UsePcParams=False`，因此 PC 参数未接管
- `SizeBox_0.WidthOverride=1620.0`
- `SizeBox_0.HeightOverride=971.0`
- `bOverride_WidthOverride=True`
- `bOverride_HeightOverride=True`
- 控件树头部仍为 `ScaleBox_0 -> SizeBox_0 -> CanvasPanel_0`

FlaUI 完整编辑器截图：

`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Screenshots\20260902_AuctionTestUI_editor_after_fix.png`

截图验证通过，PNG 尺寸 `1936x1056`、文件大小 `419152` 字节。目视确认 UI 完整收敛在设计画布内，主框架、玩家卡、竞拍情报区、仓库区和底部栏均保留。尝试 `--crop-red-box` 因当前编辑器窗口无可识别红框/选中 UMG 帧失败，未将失败结果当作裁剪截图证据。

## 生效方式与风险

该修改涉及蓝图根控件属性，需重新打开/刷新 UI 设计器查看，并在正式运行时重新调试 PIE；不能用 Lua 热更新替代。若后续明确要求铺满非同宽高比的展示区，需要在 `ScaleToFit` 与 `Fill` 之间重新确认“保持比例”还是“无留白”的视觉取舍。

## 预估成功日志

本轮未启动 PIE，以下仅为重新 PIE 后应观察的预估状态，不是实际运行日志：

```text
AuctionTestUI 资产加载成功，ScaleBox_0 Stretch=ScaleToFit
AuctionTestUI 设计舞台尺寸 Width=1620 Height=971
```
