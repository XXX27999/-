# RPC 分发架构

> 来源：`raw/docs/ai/2026-07-13_RPC编码规范标准文档.md`、`raw/docs/ai/2026-08-03_GM私有实体碰撞血条伤害隔离.md`、`raw/docs/ai/2026-07-20_跳楼机本地玩家宠物附着与客户端座位同步修复记录.md`  
> 官方依据：`raw/docs/api/class/和平全局接口/基础功能/UnrealNetwork.md`、`raw/docs/wiki/进阶内容/203_网络同步系统介绍.md`

---

## 一、核心思想

所有跨端调用只走两个固定入口，业务函数按**字符串名称**在模块内分发。`UGCPlayerController` 不承载业务 RPC，只保留分发器，避免 RPC 属性无限膨胀。

| 方向 | 分发器 | 实现文件 | 实际执行端 |
| --- | --- | --- | --- |
| 客户端 → 服务端 | `KHDRPC_Call` | `Script/Blueprint/CF_KHDRPC.lua` | 服务端 |
| 服务端 → 客户端 | `FWDRPC_Call` | `Script/Blueprint/CF_FWDRPC.lua` | 客户端 |

命名含义：KHDRPC = 客户端到服务端；FWDRPC = 转发到客户端。

---

## 二、固定分发器

```lua
--- 服务端 RPC 分发器：客户端调用后在服务端执行
function UGCPlayerController:KHDRPC_Call(funcName, ...)
    CF_KHDRPC(funcName, self, ...)
end

--- 客户端 RPC 分发器：服务端调用后在客户端执行
function UGCPlayerController:FWDRPC_Call(funcName, ...)
    CF_FWDRPC(funcName, self, ...)
end
```

分发依赖 Lua metatable 的 `__call`：

```lua
setmetatable(CF_KHDRPC, {
    __call = function(t, funcName, ...)
        local fn = t[funcName]
        if fn then
            fn(...)
        else
            ugcprint("[CF_KHDRPC] 未知函数: " .. tostring(funcName))
        end
    end
})
```

RPC 白名单的通用官方示例由 `GetAvailableServerRPCs()` 注册客户端到服务端的 RPC 名称；旧版本页曾将双入口写成固定返回 `"KHDRPC_Call"` / `"FWDRPC_Call"`，该表述不能覆盖所有项目，现标记为历史经验，具体项目必须以实际注册契约和 PIE 验证为准。

---

## 三、调用方式

```lua
-- 客户端 → 服务端
UnrealNetwork.CallUnrealRPC(pc, pc, "KHDRPC_Call", "ServerRPC_BuyPet", rowName, price)

-- 服务端 → 客户端
UnrealNetwork.CallUnrealRPC(pc, pc, "FWDRPC_Call", "ClientShowTiShi", tipText)
```

官方 `UnrealNetwork` 提供三个变体，语义不同，不能混用：

| API | 语义 |
| --- | --- |
| `CallUnrealRPC` | 可靠单播 |
| `CallUnrealRPC_Unreliable` | 不可靠单播 |
| `CallUnrealRPC_Multicast` | 可靠广播，目标为 Actor 或 Component |

---

## 四、命名约定

| 方向 | 前缀 | 示例 |
| --- | --- | --- |
| 客户端 → 服务端 | `ServerRPC_` + PascalCase | `ServerRPC_ApplyAreaCare`、`ServerRPC_BuyPetFromPool` |
| 服务端 → 客户端 | `Client` + PascalCase | `ClientOpenWorkingAreaUI`、`ClientShowTiShi`、`ClientUpdateUI3D` |

历史遗留存在无前缀函数（`StartWork`、`Warehouse`、`Map`）与 `C_` 前缀（`C_ShowOfflineWorkGoldTips`），新代码统一使用标准前缀。

函数签名要求完整 LuaDoc 注释：一句话功能说明 + 每个 `@param` 的类型与含义 + `@return`（如有）。

---

## 五、禁止事项

1. 在 `UGCPlayerController` 上新增其他 RPC 属性。
2. 直接调用 `pc:RPC` 绕过分发器。
3. 在 KHDRPC 函数中调用客户端专用 API（如 `AddToViewport`）。
4. 在 FWDRPC 函数中调用服务端专用 API（如 `SpawnActor`、属性写入）。
5. 用 `if not self:HasAuthority() then return end` 静默跳过某一端，详见 [端侧权威与 HasAuthority](端侧权威与HasAuthority.md)。

---

## 六、实战验证案例

- **私有实体隔离**（`2026-08-03`）：服务端判定后通过 `FWDRPC` 通知 Owner 客户端受伤与死亡，Controller 始终只有两个入口。
- **载具附着同步**（`2026-07-20`）：服务端 `K2_AttachToActor` 建立权威状态后，用 `FWDRPC_Call` 让客户端对本地 Pawn 与宠物显式附着，再 `GetAttachParentActor` 回读验证。

## 八、项目注册契约修订

> 类型：项目差异记录
> 主题：Lua / RPC / 端侧
> 适用范围：IslandAuctionKing；仅在该项目完成新格式 PIE 验证后作为项目规范使用
> 证据状态：项目实测、冲突、待查证
> 来源：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Script\Blueprint\UGCPlayerController.lua`、IslandAuctionKing 2026-08-31 PIE 日志及用户明确修订
> 更新时间：2026-08-31
> 关联主题：蓝图函数遮蔽、端侧权威、PIE 调试与热更新边界
> 排除范围：不修改官方 `raw/docs/`，不将该项目契约升格为所有项目的官方 API 结论
> 官方依据：`D:\oasis-skill-plus\docs\wiki\进阶内容\203_网络同步系统介绍.md` 仅确认 `GetAvailableServerRPCs` 为注册入口，不确认本项目双包装器格式

IslandAuctionKing 当前采用唯一 RPC 注册函数，函数体必须保持纯注册内容，不添加打印或其他业务逻辑：

```lua
function UGCPlayerController:GetAvailableServerRPCs()
    return "KHDRPC_Call","FWDRPC_Call";
end
```

项目修订原因：控制器蓝图曾存在同名普通 `KHDRPC_Call` 函数，且缺少 `FUNC_Net`，导致客户端调用 Lua 包装器时出现 `Function[KHDRPC_Call] is forbidden to call on client`。该蓝图函数已通过 UGCAskQ MCP 的 Resolve → Plan → Execute 删除并回读确认函数图移除；旧注册格式的 PIE 日志仍保留为历史失败证据。新注册格式尚未完成一次独立 PIE 成功验证，不能提前宣称 RPC 已恢复。

项目证据：[IslandAuctionKing 角色道具选择后未进入竞拍日志分析](../../../IslandAuctionKing/日志证据/2026-08-28_角色道具选择未跳转竞拍日志分析.md)

---

## 七、相关页面

- [端侧权威与 HasAuthority](端侧权威与HasAuthority.md)
- [日志与错误保护规范](../工具与流程/日志与错误保护规范.md)
- [PIE 调试与热更新边界](../工具与流程/PIE调试与热更新边界.md)
- 来源：[2026-08-26 raw 资料入库总结](../来源记录/2026-08-26_raw资料入库总结.md)
