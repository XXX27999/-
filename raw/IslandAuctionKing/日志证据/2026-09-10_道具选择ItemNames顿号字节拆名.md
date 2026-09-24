# 2026-09-10 道具选择 ItemNames 顿号字节拆名

> 类型：项目日志证据
> 主题：AuctionPropSelectUI 道具名显示「鉴仪器」「金??」、介绍为空
> 适用范围：IslandAuctionKing 客户端 `AuctionPropSelectUIService.SplitItemNames`
> 证据状态：项目实测（客户端 LuaLog）
> 来源：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\Saved\Logs\IslandAuctionKing\Clientlog\LuaLog\2026.09.10-12.38.29_client__dkck7pgf7nkitq_2.log`
> 更新时间：2026-09-10
> 关联主题：[道具组默认未拥有与控制器金币拥有态](../开发记录/2026-09-10_道具组默认未拥有与控制器金币拥有态.md)
> 排除范围：不证明道具表 Description 列缺失；道具表 40 行 Name 已读到
> 官方依据：知识库未覆盖 Lua 字符类对 UTF-8 多字节顿号的拆分；本页只记录项目实测

## 会话

DebugID：`dkck7pgf7nkitq`（客户端）/ `dkck7pgf7nkitr`（DS）。分析器默认只扫到 DS，客户端证据来自 LuaLog 定向检索。

## 证据

`LoadPropDescriptions` 出口 `count=40`，含完整名 `微型品鉴仪器`、`大型品鉴仪器`、`金品估值仪器`。

同一次 `Refresh`：

- `slot=1 itemName=微型?? desc=`
- `slot=2 itemName=鉴仪器 desc=`
- `slot=3 itemName=微型尺寸仪器 desc=随机显示4件藏品的轮廓。`
- 高级泛用：`slot=1 itemName=大型??`，`slot=5 itemName=金?? desc=`，`itemCount=13`

购买后服务端 `AuctionOwnedProps=九格均价仪器,大型品鉴仪器,...` 名称完整，说明权威库存没拆，只是 UI 拆名错。

## 根因

`string.gmatch(text, "[^,，、]+")` 的 `[、]` 按字节匹配。UTF-8 `、`=`E3 80 81`，`品`=`E5 93 81`，末字节都是 `81`，于是「微型品鉴仪器」在「品」处被切开。切开后的残名对不上道具表，介绍为空。

## 修复

`SplitItemNames` 与购买回退拆名先 `gsub("、", ",")` 再按 ASCII 逗号切。可热更新。
