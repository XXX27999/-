# UAsset 转 JSON 工具

> 类型：概念索引
> 来源：[2026-09-16 工程外置资料迁出知识库](../../raw/知识/通用/来源记录/2026-09-16_工程外置资料迁出知识库.md)
> 正文位置：[UAsset 转 JSON 工具 正文](../../raw/知识/通用/工具与流程/UAsset转JSON工具.md)
> 最近更新：2026-09-16

## 索引摘要

把工程内 `.uasset` 增量导出为只读 JSON 镜像的工具，封装自工程根 `ConvertUAssetToJson.ps1`，现已迁出 UGC 工程、统一从知识库调用。UGCAskQ MCP 未命中目标蓝图或控件时，先跑工具同步，再只读查 JSON 做字段补充与差异定位。

要点：

1. **入口**：`D:\知识库\和平精英绿洲起源\工具\UAssetToJsonConverter\dist\UAssetToJsonConverter.exe`（双击图形界面；`--selftest` / `--mode convert|watch` / `--dry-run` / `--report` 供脚本调用）。
2. **产物**：默认输出到 `D:\知识库\和平精英绿洲起源\raw\<项目名>\_JsonOutput\`，工程目录不再生成 `_JsonOutput`。
3. **依赖**：`C:\Program Files (x86)\UAssetGUI.exe`；UE 版本标记默认 `VER_UE4_24`。
4. **必须保留 `LastWriteTime`**：迁移或重建镜像时用 `copy2` 一类保留时间戳的复制，否则增量跳过全部失效。
5. **JSON 仍是只读**：不保证最新、禁止编辑、禁止覆盖 `.uasset`，蓝图/UI/DataTable 写入只能走 MCP。

- **Raw 正文**：[UAsset 转 JSON 工具](../../raw/知识/通用/工具与流程/UAsset转JSON工具.md)
- **工具目录**：[UAssetToJsonConverter](../../工具/UAssetToJsonConverter/)
- **项目登记**：[IslandAuctionKing 辅助文件索引](../../raw/IslandAuctionKing/开发记录/000_辅助文件索引.md)
- **相关概念**：[蓝图与 MCP 写入流程](./蓝图与MCP写入流程.md)、[非运行辅助文件索引与调用](./非运行辅助文件索引与调用.md)、[调试备份存放](./调试备份存放.md)
