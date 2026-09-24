---
类型: 项目约定
主题: IslandAuctionKing PIE 调试启动要求
适用范围: IslandAuctionKing（海岛竞拍王）UGC 工程，所有 PIE 调试场景
证据状态: 项目实测 + 用户明确约定
来源: 用户 2026-09-22 明确指令；工程配置 AuctionConfig.RequiredPlayers = 2
更新时间: 2026-09-22
关联主题: PIE 调试、竞拍流程、双客户端验证
排除范围: 其他 UGC 工程；未经实测的其他进入竞拍的前置条件
官方依据: 无（属项目约定，非官方 API 机制）
---

# IslandAuctionKing PIE 调试启动要求（双客户端）

## 结论（强制）

**本工程启动 PIE 调试必须启动两个客户端（`team_count=2`），单客户端无法进入竞拍。**

任何 AI 助手或开发者在本工程自行开启 PIE 调试前，**必须先查看项目要求**（本页 + 工程根 `AGENTS.md`），
不得默认沿用「单客户端 PIE」的通用习惯。

## 启动前人数检查（强制）

每次启动 PIE 前，先查看当前地图/玩法的正常运行人数要求，再填写 `ue_pie` 参数：

1. 读取 `Script/Function/AuctionConfig.lua` 中的 `AuctionConfig.RequiredPlayers`，并核对 `AuctionGameService.lua` 的人数门禁；当前项目实测要求为 2 人。
2. 计算本次 PIE 的实际客户端总数 `team_count * (players_per_team + spectators_per_team)`，不得低于 `RequiredPlayers`；竞拍验证固定使用两个玩家客户端。
3. `ue_read ctx:` 确认 `is_debug_playing=true`，并确认返回至少两个客户端窗口/日志路径后，才允许执行 `doluastring`、截图或判定竞拍界面验证结果。

此检查是本项目的项目实测流程，不是官方 API 规则；若后续修改地图或玩法人数门槛，必须先更新本页与对应项目证据，再启动 PIE。

## 正确调用

```
ue_pie {
  action: "start",
  submode_id: 0,
  team_count: 2,
  players_per_team: 1,
  spectators_per_team: 0,
  simulation_platform: "mobile"
}
```

- `team_count=2` 为**必须**，其余字段按需。
- 等价写法：`teams: [{players:1},{players:1}]`。

## 根因

工程配置 `AuctionConfig.RequiredPlayers = 2`，进入竞拍阶段要求房间内玩家数达到 2。
单客户端（`team_count=1`）时玩家数恒为 1，无法满足进入条件，表现为「进不去竞拍」。

## 实测现象（2026-09-22）

- 单客户端起 PIE：无法进入竞拍；且 PIE 客户端在等待阶段会自行退出，
  随后 `doluastring` / `reloadlua` 报 `No PIE client window is registered` 或
  `Lua reload was not handled; the PIE client connection may not be ready`。
- 双客户端起 PIE：`ue_read ctx:` 显示 `is_debug_playing: true`、`debug_thread_state: 3`；
  窗口枚举可见 `PIEPlayer_T1_10001` 与 `PIEPlayer_T2_20001`，`doluastring` 正常执行。

## 双客户端下的窗口句柄获取

`doluastring` 的 `client_hwnd` 需传十进制窗口句柄。本机 Git Bash 缺 coreutils，
用 Python312 + `ctypes.windll.user32.EnumWindows` 按标题枚举（含 `PIE` 关键字），
再取 `GetWindowTextW`。实测标题形如：

```
ShadowTrackerExtra (64-bit, PCD3D_ES31)  PIEPlayer_T1_10001  ,14612 , Compiled: Sep 10 2026 15:10:33
ShadowTrackerExtra (64-bit, PCD3D_ES31)  PIEPlayer_T2_20001  ,25440 , Compiled: Sep 10 2026 15:10:33
```

脚本位置：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260922_仓库藏品层级遮挡\`（本页配套）。

## 关联坑

1. **`doluastring` 的代码里不能用 `\n` 换行**：控制台把 `dostring content:` 当作单行处理，
   含 `\n` 的片段只回显不执行。一律写成单行，语句间用 `;` 分隔。
2. **片段过长会被丢弃**：实测超过一定长度的片段只回显、不产生执行输出，也不会报错。
   探针应拆小（每段 1–3 个取值），避免「一次读十几个字段」。
3. **`doluastring` 是单向派发**：工具返回 `{}` 不代表执行成功，必须去客户端日志读结果。
4. **客户端 Lua 日志在会话进行中不落盘**：必须等到 PIE 停止后才会写入
   `Saved\Logs\IslandAuctionKing\Clientlog\FullLog\*_1.log`。
   实测 12:05:52 会话说停就停，之后无法再补读。

## 验证

- `ue_read queries=["ctx:"]` 确认 `is_debug_playing: true`。
- 窗口枚举到 2 个 `PIEPlayer_*` 窗口。
- `doluastring` 后客户端日志出现 `LogUGCClient: [TagLog] <你的标记>`。

## 相关

- 工程根 `AGENTS.md`（功能脚本配置规范）。
- `raw\IslandAuctionKing\日志证据\2026-09-18_单人PIE二次匹配停留在主界面.md`（单客户端相关现象）。
