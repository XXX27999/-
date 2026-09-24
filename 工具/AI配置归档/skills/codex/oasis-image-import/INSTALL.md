# oasis-image-import 技能 - 安装与使用指南

## ✓ 安装完成

技能已成功安装到全局 Codex skills 目录：
- 源目录：`D:\工具\oasis-image-import`
- 全局目录：`C:\Users\Administrator\.codex\skills\oasis-image-import`

## 核心功能

### 1. 文件名自动规范化

**问题**：绿洲编辑器资产名称只能包含英文字母、数字、下划线，且必须以字母开头。

**解决方案**：自动将中文文件名转换为合法的英文资产名称。

**转换示例**：
```
金币.png           → Image_jinbi
帮助按钮.png       → Image_bangzhuanniu
大厅右侧.png       → Image_datingyouce
MainUI.png         → MainUI (英文保留)
2D背景.png         → Image_2D_beijing (数字开头加前缀)
UI-背景 01.png     → Image_UI_beijing_01 (特殊字符替换)
```

### 2. 批量导入配置

自动配置贴图属性（符合官方 Wiki 规范）：

**UI 贴图**（textureGroup=16，默认）
- CompressionSettings: 0 (TC_Default)
- LODGroup: 16 (TEXTUREGROUP_UI)
- MipGenSettings: 2 (TMGS_NoMipmaps)
- SRGB: True

**场景贴图**（textureGroup=0）
- LODGroup: 0 (TEXTUREGROUP_World)

**特效贴图**（textureGroup=13）
- LODGroup: 13 (TEXTUREGROUP_Effects)

### 3. 文件名映射表

导入完成后生成映射表，记录原始中文名与转换后英文名的对应关系，方便后续查找。

## 使用方式

### 方式一：在 Codex 对话中使用（推荐）

直接在对话中描述需求：

```
帮我导入图片：
- 源文件夹：C:\素材\UI
- 目标路径：/IslandAuctionKing/Asset/TuPian/UI
- 贴图类型：UI
```

或者：

```
使用 oasis-image-import 技能批量导入桌面的主界面UI图片
```

Codex 将自动：
1. 调用 Node.js 脚本生成导入计划（文件名转换）
2. 使用 UGCAskQ MCP 的 ue_py 工具执行导入
3. 生成导入报告和文件名映射表

### 方式二：命令行测试

```bash
# 进入脚本目录
cd C:\Users\Administrator\.codex\skills\oasis-image-import\scripts

# 生成导入计划（仅测试，不实际导入）
node test_import.mjs "C:\素材\UI" "/IslandAuctionKing/Asset/TuPian/UI" 16

# 参数说明：
# - 参数1：源文件夹（Windows 绝对路径）
# - 参数2：目标 UE 路径
# - 参数3：纹理组（16=UI, 0=场景, 13=特效）
```

### 方式三：在项目中直接使用 Python 脚本

之前创建的 `Script/Tools/BatchImportImages.py` 仍然可用，但不包含文件名规范化功能。

## 完整工作流程

### 1. 准备阶段
- 准备好图片文件（PNG/JPG/TGA）
- 确定目标 UE 路径
- 选择贴图类型（UI/场景/特效）

### 2. 生成导入计划
```bash
node test_import.mjs "源文件夹" "目标UE路径" 16
```

输出示例：
```json
{
  "totalFiles": 16,
  "mapping": [
    {"original": "金币.png", "asset": "Image_jinbi"},
    {"original": "帮助按钮.png", "asset": "Image_bangzhuanniu"}
  ]
}
```

### 3. 在 Codex 中执行导入

告诉 Codex：
```
使用 oasis-image-import 技能导入图片，
源文件夹：[你的路径]，
目标路径：[UE路径]
```

### 4. 验证结果
- 打开编辑器 Content Browser
- 导航到目标路径
- 检查导入的 Texture2D 资产
- 查看导入报告中的文件名映射表

## 技能结构

```
D:\工具\oasis-image-import\
├── SKILL.md                      # 技能描述（Codex 读取）
├── README.md                     # 使用说明
├── package.json                  # Node.js 配置
└── scripts\
    ├── batch_import.mjs          # 导入计划生成器（文件名转换）
    ├── test_import.mjs           # 测试脚本
    └── execute_import.py         # Python 执行模板
```

## 文件名转换规则详解

### 支持的中文拼音映射

脚本内置了常用汉字的拼音映射表，覆盖了 UI、游戏、特效等常见词汇：

```javascript
{
  '金': 'jin', '币': 'bi', '帮': 'bang', '助': 'zhu',
  '大': 'da', '厅': 'ting', '右': 'you', '侧': 'ce',
  '技': 'ji', '能': 'neng', '选': 'xuan', '择': 'ze',
  // ... 更多映射
}
```

### 未映射汉字的处理

如果遇到未在映射表中的汉字，会被替换为 'x'，并添加 `Image_` 前缀确保合法性。

**建议**：如需支持更多汉字，编辑 `scripts/batch_import.mjs` 的 `pinyinMap` 对象。

## 依据文档

本技能基于以下官方文档开发：

1. **D:\oasis-skill-plus\docs\wiki\新手入门\资源管理与编辑\277_资源导入.md**
   - 支持格式：PNG、JPG、TGA
   - 导入方式：拖动或 ue.import_asset API

2. **D:\oasis-skill-plus\docs\wiki\新手入门\资源管理与编辑\资源编辑\300_贴图与材质编辑.md**
   - UI 贴图配置规范
   - 场景/特效贴图配置

## 测试用例

### 成功案例

之前已成功测试：
- ✓ 16 张主界面 UI 图片
- ✓ 包含子文件夹（技能选择）
- ✓ 中文文件名自动转换
- ✓ 配置为 UI 贴图格式

导入结果位于：
`/IslandAuctionKing/Asset/TuPian/ZhuJieMianUI/`

### 验证方法

在编辑器中：
1. 打开 Content Browser
2. 导航到导入路径
3. 双击任意贴图查看 Details
4. 确认：
   - Compression Settings = Default
   - LOD Group = UI
   - Mip Gen Settings = NoMipmaps

## 常见问题

### Q: 中文文件名转换后不认识怎么办？

A: 查看导入报告中的 `mapping` 字段，里面记录了所有原始文件名与转换后资产名的对应关系。

### Q: 能否自定义拼音映射？

A: 可以，编辑 `scripts/batch_import.mjs` 中的 `pinyinMap` 对象，添加你需要的汉字映射。

### Q: 为什么有些文件名变成了 Image_xxx？

A: 当文件名不以字母开头，或转换后为空时，会自动添加 `Image_` 前缀确保合法性。

### Q: 支持其他图片格式吗？

A: 目前仅支持 PNG、JPG、JPEG、TGA，这是绿洲编辑器官方支持的格式。

### Q: 会覆盖已存在的资产吗？

A: 是的，如果目标路径已存在同名资产，会被覆盖。建议先备份重要资产。

## 后续改进计划

- [ ] 集成更完整的拼音库（支持所有汉字）
- [ ] 支持自定义文件名转换规则
- [ ] 导入前预览转换结果
- [ ] 支持批量重命名已导入的资产
- [ ] 生成更详细的导入报告（包含预览图）

## 版本信息

- **版本**：v1.0.0
- **创建时间**：2026-08-24
- **测试状态**：✅ 已验证（16 张图片导入成功）
- **兼容性**：绿洲启源编辑器 + UGCAskQ MCP

---

**技能位置**：
- 源目录：`D:\工具\oasis-image-import`
- 全局目录：`C:\Users\Administrator\.codex\skills\oasis-image-import`
- 项目工具：`IslandAuctionKing/Script/Tools/BatchImportImages.py`
