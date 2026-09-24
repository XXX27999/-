# 绿洲编辑器图片批量导入工具

自动将图片批量导入到绿洲编辑器项目，并规范化文件名为英文资产名称。

## 快速开始

### 1. 生成导入计划

```bash
node scripts/batch_import.mjs "C:\Users\Administrator\Desktop\素材\竞拍\可用\主界面UI" "/IslandAuctionKing/Asset/TuPian/ZhuJieMianUI" 16
```

参数说明：
- 参数1：源文件夹（Windows绝对路径）
- 参数2：目标UE路径
- 参数3：纹理组（16=UI, 0=场景, 13=特效）

输出示例：
```json
{
  "sourceFolder": "C:\\Users\\Administrator\\Desktop\\素材\\竞拍\\可用\\主界面UI",
  "targetPath": "/IslandAuctionKing/Asset/TuPian/ZhuJieMianUI",
  "textureGroup": 16,
  "totalFiles": 16,
  "files": [...],
  "mapping": [
    {"original": "金币.png", "asset": "Image_jinbi", "path": "金币.png"},
    {"original": "帮助按钮.png", "asset": "Image_bangzhuanniu", "path": "帮助按钮.png"}
  ]
}
```

### 2. 在 Codex 中执行导入

在 Codex 对话中：

```
请使用 oasis-image-import 技能导入图片：
- 源文件夹：C:\Users\Administrator\Desktop\素材\竞拍\可用\主界面UI
- 目标路径：/IslandAuctionKing/Asset/TuPian/ZhuJieMianUI
- 贴图类型：UI
```

Codex 将自动：
1. 调用 batch_import.mjs 生成导入计划
2. 使用 UGCAskQ MCP 的 ue_py 执行导入
3. 生成导入报告和文件名映射表

## 文件名转换规则

### 转换示例

| 原始文件名 | 转换后资产名 |
|-----------|-------------|
| 金币.png | Image_jinbi |
| 帮助按钮.png | Image_bangzhuanniu |
| MainUI.png | MainUI |
| 2D背景.png | Image_2D_beijing |
| UI-背景 01.png | Image_UI_beijing_01 |
| 技能选择/技能底.png | Image_jinengdi |

### 转换规则

1. **英文保留**：已符合规范的英文字母、数字、下划线直接保留
2. **中文转拼音**：使用内置拼音映射表转换常用汉字
3. **特殊字符替换**：空格、短横线转为下划线
4. **前缀添加**：数字开头或空名称添加 `Image_` 前缀
5. **去重处理**：重名时添加 `_1`、`_2` 等后缀

## 贴图配置

### UI 贴图（默认，textureGroup=16）
- CompressionSettings: 0 (TC_Default)
- LODGroup: 16 (TEXTUREGROUP_UI)
- MipGenSettings: 2 (TMGS_NoMipmaps)
- SRGB: True

### 场景贴图（textureGroup=0）
- LODGroup: 0 (TEXTUREGROUP_World)
- 其他同上

### 特效贴图（textureGroup=13）
- LODGroup: 13 (TEXTUREGROUP_Effects)
- 其他同上

## 输出文件

导入完成后生成：

1. **import_plan_<timestamp>.json**：导入计划（scripts目录）
2. **导入报告**：包含成功/失败统计和文件名映射
3. **UE编辑器日志**：详细的导入过程日志

## 技能集成

此工具已集成为 Codex 技能，可通过以下方式调用：

```
@oasis-image-import 导入图片
源文件夹：C:\素材\UI
目标路径：/IslandAuctionKing/Asset/TuPian/UI
```

或者在对话中自然描述：

```
帮我把桌面的主界面UI图片批量导入到项目的 Asset/TuPian/ZhuJieMianUI 文件夹
```

## 依据文档

- 官方Wiki：277_资源导入.md
- 官方Wiki：300_贴图与材质编辑.md
- UGCAskQ MCP Python API

## 注意事项

1. ✅ 支持中文路径和中文文件名
2. ✅ 自动保持子文件夹结构
3. ⚠️ 会覆盖同名资产（建议先备份）
4. ⚠️ 需要编辑器处于打开状态
5. ⚠️ 大批量导入可能导致编辑器卡顿

## 故障排查

### 文件名映射表在哪里？
在导入报告的 `mapping` 字段中，记录了所有原始文件名与转换后资产名的对应关系。

### 导入后资产名称看不懂？
参考导入报告中的 `mapping` 字段，或在编辑器中按 F2 重命名资产。

### 导入失败？
检查：
- 源文件是否损坏
- 文件格式是否为 PNG/JPG/TGA
- 编辑器是否打开项目
- UE Python 日志中的错误信息

## 开发测试

```bash
# 测试导入计划生成
npm test

# 手动测试
node scripts/batch_import.mjs "测试文件夹路径" "/目标UE路径" 16
```

## 版本历史

- v1.0.0 (2026-08-24)
  - 初始版本
  - 支持 PNG/JPG/TGA 批量导入
  - 自动文件名规范化
  - 支持 UI/场景/特效贴图配置
