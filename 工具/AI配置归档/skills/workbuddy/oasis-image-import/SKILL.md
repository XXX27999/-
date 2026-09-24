---
name: oasis-image-import
description: 批量导入图片到绿洲编辑器项目，支持 PNG/JPG/TGA 格式，自动转换中文文件名为英文开头的合法资产名称，并配置为 UI/场景/特效贴图格式。用于和平精英绿洲起源编辑器的图片资源批量导入工作流。
agent_created: true
---

# 绿洲编辑器图片批量导入

为绿洲起源编辑器提供图片资源批量导入功能，自动处理文件名规范化和贴图配置。

## 功能特性

- ✅ 批量导入 PNG/JPG/TGA 图片到项目 Asset 目录
- ✅ 自动将中文文件名转换为英文开头的合法资产名称（英文字母+数字+下划线）
- ✅ 保持源文件夹的子目录结构
- ✅ 自动配置为 UI/场景/特效贴图格式（符合官方 Wiki 规范）
- ✅ 提供文件名映射表，记录原始中文名与转换后英文名的对应关系
- ✅ 生成导入报告和验证日志

## 使用场景

- 美术资源批量导入到编辑器
- UI 界面图片素材导入
- 场景贴图、特效贴图批量导入
- 第三方素材库图片导入

## 工作流程

1. **准备阶段**：扫描源文件夹，识别所有 PNG/JPG/TGA 图片
2. **文件名规范化**：将中文文件名转换为 Image_ 前缀 + 拼音/序号的英文名称
3. **导入执行**：调用 UE Python API `ue.import_asset(临时英文文件, 目标文件夹)` 导入图片；第二参数只能是目标文件夹，不能拼接资产名
4. **配置应用**：根据贴图类型（UI/场景/特效）自动配置 Texture2D 属性
5. **验证与报告**：生成导入报告、文件名映射表和验证日志

## 调用方式

当用户询问"导入图片"、"批量导入素材"、"图片资源导入"或明确提到绿洲编辑器图片导入时，使用此技能。

### 必需信息

- **源文件夹路径**：Windows 绝对路径，例如 C:\Users\...\素材\UI
- **目标 UE 路径**：项目内路径，例如 /IslandAuctionKing/Asset/TuPian/UI
- **贴图类型**（可选）：UI（默认）、场景、特效

### 执行步骤

1. 调用 scripts/batch_import.mjs 生成导入计划和文件名映射
2. 使用 UGCAskQ MCP 的 ue_py 工具执行实际导入
3. 生成导入报告和验证结果

## 文件名转换规则

### 转换策略

1. **保留英文字母、数字、下划线**：已符合规范的字符直接保留
2. **中文转拼音**：使用 pinyin 库将中文转换为拼音首字母
3. **非法字符替换**：空格、短横线等转为下划线
4. **前缀添加**：如果首字符不是字母，添加 Image_ 前缀
5. **去重处理**：如果转换后名称重复，添加数字后缀 _1、_2 等

### 转换示例

| 原始文件名 | 转换后资产名 | 说明 |
|-----------|-------------|------|
| 金币.png | Image_jinbi | 中文转拼音 + 前缀 |
| 帮助按钮.png | Image_bangzhuanniu | 中文转拼音 + 前缀 |
| MainUI.png | MainUI | 英文名直接保留 |
| 2D背景.png | Image_2D_beijing | 数字开头加前缀 + 中文转拼音 |
| UI-背景 01.png | Image_UI_beijing_01 | 特殊字符替换 + 中文转拼音 |

## 贴图配置规范

基于官方 Wiki 277_资源导入.md 和 300_贴图与材质编辑.md：

### UI 贴图（默认）
- CompressionSettings: 0 (TC_Default)
- LODGroup: 16 (TEXTUREGROUP_UI)
- MipGenSettings: 13 (TMGS_NoMipmaps)
- SRGB: True

### 场景贴图
- CompressionSettings: 0 (TC_Default)
- LODGroup: 0 (TEXTUREGROUP_World)
- MipGenSettings: 0 (TMGS_FromTextureGroup)
- SRGB: True（固有色）/ False（RMA贴图）

### 特效贴图
- CompressionSettings: 0 (TC_Default)
- LODGroup: 13 (TEXTUREGROUP_Effects)
- MipGenSettings: 0 (TMGS_FromTextureGroup)
- SRGB: 根据特效类型

## 输出文件

导入完成后在目标项目根目录生成：

1. **Import_Report_YYYYMMDD_HHMMSS.json**：导入统计报告
2. **Filename_Mapping_YYYYMMDD_HHMMSS.json**：原始文件名与转换后资产名的映射表
3. **导入日志**：记录在 UE 编辑器日志中，以【BatchImportImages+...】开头

## 依据文档

- D:\oasis-skill-plus\docs\wiki\新手入门\资源管理与编辑\277_资源导入.md
- D:\oasis-skill-plus\docs\wiki\新手入门\资源管理与编辑\资源编辑\300_贴图与材质编辑.md
- 绿洲编辑器 Python API 文档（UGCAskQ MCP）

## 限制与注意事项

1. **仅支持 Texture2D**：不支持 RenderTarget、贴图数组等高级类型
2. **需要编辑器运行**：必须在绿洲编辑器打开项目的情况下执行
3. **覆盖行为**：如果目标路径已存在同名资产，会被覆盖（建议先备份）
4. **中文路径支持**：源文件夹可以包含中文路径，但资产名称必须英文；执行脚本会先将源图复制为英文临时文件再导入目标文件夹
5. **目标路径语义**：`ue.import_asset` 的目标参数只能传资产目录，例如 `/IslandAuctionKing/Asset/TuPian/UI`；严禁传入 `/.../UI/AssetName`，否则会创建同名子文件夹并保留源文件名
5. **生效方式**：图片导入后立即生效，无需重新调试 PIE

## 故障排查

### 常见问题

- **导入失败**：检查源文件是否损坏、格式是否支持（仅 PNG/JPG/TGA）
- **编辑器未响应**：大批量导入时编辑器可能卡顿，等待完成即可
- **资产未显示**：刷新编辑器 Content Browser 或重启编辑器
- **配置未生效**：检查 UE Python 日志，确认 save_package() 成功执行

## 技能实现

使用 Node.js 脚本 + UGCAskQ MCP Python API：

1. **Node.js 预处理**（scripts/batch_import.mjs）：
   - 扫描源文件夹
   - 生成文件名映射
   - 创建导入计划

2. **Python 执行**（通过 ue_py 工具）：
   - 调用 ue.import_asset 导入图片
   - 配置 Texture2D 属性
   - 保存资产包

3. **验证与报告**：
   - 读取导入后的资产
   - 验证配置正确性
   - 生成导入报告
