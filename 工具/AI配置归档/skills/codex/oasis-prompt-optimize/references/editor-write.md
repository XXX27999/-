# 编辑器写入提示词

仅在任务改蓝图、UMG、DataTable、结构体或资源导入时读取本页。

## 读写入口

提示词必须把读和写拆开：

- 读蓝图/UI 属性：优先 UGCAskQ MCP。MCP 未查到时，先在项目根执行 `powershell -ExecutionPolicy Bypass -File ".\ConvertUAssetToJson.ps1"`，再只读 `_JsonOutput`。
- 改蓝图结构、组件、UI 属性、事件入口、DataTable：必须 UGCAskQ MCP 的 `Resolve → Plan → Execute`。
- `_JsonOutput` 只用于核查和差异定位。禁止编辑 JSON、用 JSON 覆盖 `.uasset`，或据此声称已改编辑器蓝图。
- 脚本不存在、转换失败或版本不明时，停止把旧 JSON 当确定性依据。

资产路径一律 `/<ProjectName>/Asset/...`，不用 `/Game/`。写前备份到 `D:\知识库\和平精英绿洲起源\备份\<项目名>\<YYYYMMDD>_<主题>\`，并在提示词里要求把该绝对路径告诉用户。禁止写进 UGC 工程 Backup/、Saved/Backup、`_JsonOutput/Backup`。

写后立即 MCP 回读。成功返回 `None` 的 API 不能当成功判据。MCP 和同步后的 JSON 都查不到目标属性时，提示词必须要求停止写入并报告「未查询到/未验证」。

## MCP 实测陷阱

这些条目会改变写法，需要写进相关提示词：

- PRV 当前是 observe 等级，无 plan 也可能 `warn_pass`。规范靠自律，不能指望服务端拦截。
- `objed_*` 必须先 `objed_open_editor(<类型>)`。
- UI/物编复制用 `objed_duplicate_asset`，不用 `duplicate_asset`。
- `widget_slot` 只稳写 `ZOrder` / `bAutoSize`。位置尺寸用 `Slot.SetPosition` / `SetSize` / `SetAnchors` / `SetAlignment`。
- struct 优先就地改字段，整体替换会清空未赋值字段。
- `data_table_find_row` 查不存在的行会抛异常，必须包裹。
- 新建/复制后先 `save_package()` 再 `load_object`；找不到时用 `resolve_asset`，禁止凭命名拼路径。

## 新 UI

新页面/控件提示词必须写成：

1. `$ui-ux-pro-max` 设计并给出可运行网页预览
2. 等用户明确说「预览没问题」
3. MCP 回读现有蓝图/组件
4. MCP 写入并回读
5. `$oasis-ui-screenshot` 截图对照，不要盲改下一轮

格子/背景/图标位图走 `$ergouzi-image-gen`，记录提示词、模型、任务 ID、绝对路径。导入按 Wiki `277_资源导入.md`：仅 PNG/JPG/TGA，文件名英文开头，拖入 `Asset` 指定文件夹。批量导入可指向 `$oasis-image-import`。UI 贴图回读五项：`LODGroup=16`、`MipGenSettings=13`、`CompressionSettings=0`、`CompressionQuality=5`、`SRGB=True`。不要把历史记录里的 `MipGenSettings=2` 写进提示词。

固定布局先确认设计舞台、锚点和父容器，再写 Position/Size。被框的一格只是模板，要按相对偏移复制到同名序号全族，并回读首个、标注个、末个。图片层、点击层、文本层、状态叠加层分开量、一起验收。长文本必须要求 `AutoWrapText` 并固定宽度。

## 配置表

按功能分表，禁止堆进一张大表：

```text
Asset/Data/Table/Customized/<功能模块名>/<功能模块名>ConfigTable
```

四列全是字符串：`ValueType`、`Value`、`Description`、`ModificationNotes`。行名用稳定英文点号路径。新表必须在配置加载器中注册。Lua 嵌套表和数组展开成标量行。修改后必须重新 PIE。

## 蓝图事件

绿洲蓝图没有事件图表，事件默认启用，靠函数名触发。提示词改事件名等于要求同步改 Lua 调用，否则断开。
