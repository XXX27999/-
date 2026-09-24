# IslandAuctionKing ZhuJieMian 画刷基线说明

> 项目资产：`/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/ZhuJieMian`
> 详细通用字段表：[ZhuJieMian 画刷现状基线表](../../../wiki/概念/ZhuJieMian画刷现状基线表.md)

## 回读摘要

- 控件树共 23 个：1 个 `CanvasPanel`、14 个 `Image`、8 个 `TextBlock`。
- 14 个 `Image` 均使用 `Brush`；`BrushImage` 全部为 `None`。
- `ZJM1` 被 3 个 Image 控件复用，`ZJM3` 被 2 个控件复用。
- `参考图` 使用 `ZJM2`，`ZOrder=-5`，四向拉伸。

## 证据边界

该文件只登记项目侧摘要；字段级控件表与复跑代码维护在全局概念页。画刷运行时改写、参考图是否应在交付前隐藏，仍需单独验证。
