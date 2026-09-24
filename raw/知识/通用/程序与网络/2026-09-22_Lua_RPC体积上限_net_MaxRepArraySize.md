# Lua RPC 体积红线：`net.MaxRepArraySize = 4096`

- **类型**：通用知识（引擎限制 + 排障范式）
- **主题**：`UnrealNetwork.CallUnrealRPC` 下发的 Lua table 序列化体积上限、超限后的连锁故障与修复范式
- **适用范围**：绿洲起源 Lua 脚本里所有走 `CallUnrealRPC(..., "KHDRPC_Call"/"FWDRPC_Call", ...)` 并携带 table 参数的调用；端侧为 DS + 客户端
- **证据状态**：**项目实测**（IslandAuctionKing 2026-09-22 双人 PIE，DS FullLog/TagLog 硬证据）+ 引擎日志原文；非官方文档条目
- **来源**：
  - 项目日志 `ShadowTrackerExtra\Saved\Logs\IslandAuctionKing\DSlog\FullLog\2026.09.22-11.47.10_ds__dkck7pqy1yikk3_realtime.log`（11:49:31.124 / 11:49:31.129 / 11:49:31.136 / 11:49:37.410）
  - 项目日志 `DSlog\TagLog\..._taglog.log`（第 3533 / 3538 / 3598 / 3600 行）
  - 项目诊断页 [2026-09-22_锁定报价后连接超时_根因诊断](../../../../备份/IslandAuctionKing/20260922_RPCArraySizeLimit/2026-09-22_锁定报价后连接超时_根因诊断.md)（AUX-20260922-001）
- **更新时间**：2026-09-22
- **关联主题**：[RPC分发架构](./RPC分发架构.md)、[2026-07-13_RPC编码规范标准文档](./2026-07-13_RPC编码规范标准文档.md)
- **排除范围**：`RepLazyProperty` 属性复制（不同通道，本文结论不直接套用）；字符串字段本身的长度上限（未实测）

---

## 1. 硬限制到底是什么

引擎在序列化 Lua table 为 RPC 参数时，会把内容摊平进一个 **Content 数组**，并校验：

```
LogNetSerialization: Error: SerializeProperties_DynamicArray_r: ArraySize (6656) > net.MaxRepArraySize(4096) (Content)
LogNetSerialization: Error: Failed to serialize properties
```

- **限制对象是「元素个数」，不是字节数**。实测同一批数据：28 件 × 13 字段 = **6656 元素 / 53297 字节**；私有状态 28 件 = **4290 元素**。
- 上限 4096 是引擎固定值。本地改 ini 只对 PIE 生效，**不能作为线上修复手段**（线上由官方固定）。
- 嵌套 table 会被摊平计入，所以「字段不多」不等于「元素不多」：`Cells` 这类格子数组是主要贡献者。

## 2. 失败后果远比「这次没发成」严重

超限后连续出现三件事：

1. `LogLuaNetwork: Error: ---LuaNetwork: FlushError` —— **writer 进入错误态**；
2. `OnLogLuaStack: Assertion failed:false`；
3. DS 日志不再输出，客户端表现为 **「竞赛服务器响应超时 / 与服务器失去连接」的断线**。

即：**后续所有 RPC 全线失败**，不是单次调用失败。定位时必须按「断线」而不是「某功能失效」排查。

## 3. `pcall` 拦不住

```lua
local rpcOK, rpcError = pcall(UnrealNetwork.CallUnrealRPC, pc, pc, "FWDRPC_Call", "ClientXXX", payload)
```

- 这条 `pcall` **恒返回 true**：序列化发生在引擎侧、调用返回之后，Lua 层看不到失败。
- 引擎侧照旧记 Net Error + 断言，DS 依旧停摆。
- **判定 RPC 成败必须另加「发送前体积自检」**，不能只看 pcall。

## 4. 修复范式（按优先级）

### 方案 1：裁剪字段（首选）

端侧能由本地配置表补全的字段，**一律不随 RPC 下发**。判据是「端侧消费点实际读哪些字段」：

- 逐个找 `payload` 的读取点（UI 刷新 / 估值计算 / 图鉴匹配），列出真实用到的字段名；
- 贴图（`Texture`）、形状（`Shape`）、旋转（`Rotation`）、占位态（`ArtStatus`）等若端侧有同名本地表按 ID/Name 补全，就删；
- 私有状态里仅供图鉴匹配用的持有藏品，可压到 `{ID, Name}`（图鉴 `BuildOwnedSet` 只消费这两个字段）。

### 方案 2：分片下发（字段还要全量时）

- 主包只带**元信息 + 空数组**（如 `Items = {}`），并带上 `ChunkTotal` / `ChunkStateVersion`；
- 另发 N 个轻量 RPC，载荷 `{StateVersion, Index, Total, ItemCount, Items}`；
- 可靠 RPC 按发送顺序到达，**主包先发、分片后发**即可保证客户端先有容器再填内容；
- 客户端按 `StateVersion` 累积：版本变了就清空重来，重复分片用 Index 去重，`已收数 == Total` 时刷新 UI；
- 分片早于主包到达时（GameState 未就绪）要缓存回放，不能丢弃。

### 方案 3：发送前体积自检（必配，不是可选项）

```lua
-- 估算 table 序列化后的元素数（字符串按字符计，标量计 1，防环）
local function EstimateContentElements(value, visited)
    local valueType = type(value)
    if valueType == "table" then
        local seen = visited or {}
        if seen[value] ~= nil then return 0 end
        seen[value] = true
        local total = 0
        for key, item in pairs(value) do
            total = total + EstimateContentElements(key, seen) + EstimateContentElements(item, seen)
        end
        return total
    end
    if valueType == "string" then return #value end
    return 1
end
```

估算值 > 安全阈值（建议 **≤3000**，留 1000 余量）即打错误日志或改走分片。**这是唯一能在 Lua 层发现该故障的手段。**

## 5. 高危点自查清单

凡「一轮/一局只发一次、但数据量随藏品数增长」的 RPC 都是高危：

- 揭晓公共状态（含全量公开藏品）
- 结算 UI 数据（携带仓库明细）
- 私有状态里的 `Collectibles` / `KnownItemDetails`
- 历史/情报数组（轮次累积）

改法：先裁剪 → 仍超限就分片 → 两者都配体积自检。

## 6. 排障手法

1. 客户端报「连接超时/失去连接」且 `Saved\Crashes` **没有**新的崩溃目录 → 优先怀疑 DS 停摆而不是客户端崩溃；
2. 在 DS `FullLog/*_realtime.log` 里搜 `MaxRepArraySize` / `FlushError` / `Assertion failed:false`；
3. 客户端 LuaLog 在**会话进行中为 0 B**，PIE 停止后才落盘 —— 实时只能看 DS 实时日志，客户端侧证据要等 PIE 停。
