# PIE 等待阶段未创建 ZhuJieMian 主界面

> 类型：项目日志证据与 Lua 修复
> 主题：PIE 等待阶段没有加载主界面大厅
> 适用范围：IslandAuctionKing，Waiting 阶段客户端 UI 创建
> 证据状态：项目实测；最新 PIE Lua 日志已核对；Lua 语法检查通过；本轮未再启动 PIE
> 来源：`Saved/Logs/IslandAuctionKing/Clientlog/LuaLog/2026.09.08-12.34.36_client__dkck7peo2lu6hj_1.log` 与 `_2.log`
> 更新时间：2026-09-08
> 关联主题：AuctionHubUIService、UGCGameState、UGCPlayerController、ZhuJieMian
> 排除范围：未改 ZhuJieMian.uasset 布局；未改三个选择层；未改二次匹配服务
> 官方依据：`UserWidget.NewWidgetObjectBP`、`UUserWidget.AddToViewport`；工程内已证路径 `AuctionTestUIService.CreateAndShow`

## 日志结论

最新 PIE 客户端 Lua 日志（2026-09-08 12:37:06）两侧都有：

```
【UGCPlayerController+ReceiveBeginPlay】分支 等待阶段保留主界面大厅，不创建竞拍测试UI Phase=Waiting
【UGCGameState+ReceiveBeginPlay】分支 等待阶段保留主界面大厅，不创建竞拍测试UI Phase=Waiting
```

全文件没有 `【ZhuJieMian+Construct】`，也没有 `AuctionHubUIService+Initialize` / `CreateAndShow`。

项目实测：等待阶段被改成“不要创建 AuctionTestUI”，但没有任何脚本创建 `ZhuJieMian`。蓝图只在 Construct 里初始化，PIE 不会自动把该 UI 挂到视口。

## 修复

写前备份：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260908_ZhuJieMianNotCreatedInPIE\`

1. `AuctionHubUIService.CreateAndShow(worldContext)`：客户端加载 `ZhuJieMian_C`，`NewWidgetObjectBP` + `AddToViewport`；Construct 未完成时补 `Initialize`。
2. `AuctionHubUIService.Hide()`：离开等待阶段关闭大厅。
3. `UGCGameState:ReceiveBeginPlay` / `OnRep_AuctionPublicState`：Waiting 创建大厅；离开 Waiting 关闭大厅并创建竞拍 UI。
4. `UGCPlayerController:ReceiveBeginPlay`：Waiting 兜底创建大厅。

## 验证

- `luaparser`：三个改动文件 SYNTAX OK
- 未再启动 PIE
- MCP 未调用（纯 Lua）

## 生效方式

重新调试 PIE。涉及 BeginPlay 创建 UI，不能热更新。

## 预估成功日志

```
【UGCPlayerController+ReceiveBeginPlay】分支 等待阶段已创建主界面大厅 widget=...
【AuctionHubUIService+CreateAndShow】出口 success=true
【ZhuJieMian+Construct】入口
【AuctionHubUIService+Initialize】出口 success=true
```
