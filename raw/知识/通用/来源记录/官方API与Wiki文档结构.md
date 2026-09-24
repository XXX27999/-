# 官方 API 与 Wiki 文档结构

> 来源：`raw/docs/api`、`raw/docs/wiki`、`raw/docs/skills/oasis-official-docs.md`  
> 用途：说明官方资料在本仓库中的组织方式，以及查证时该去哪个目录
> 最新镜像校验：2026-09-11，Wiki 329 篇 Markdown + 3444 张图片，API 6201 个文件

---

## 一、API 文档（`raw/docs/api`）

入口：`raw/docs/api/000_索引.md`

| 分区 | 条目数 | 索引 | 内容 |
| --- | --- | --- | --- |
| `class` | 1401 | `raw/docs/api/class/000_索引.md` | 类与全局接口 |
| `cppenum` | 3692 | `raw/docs/api/cppenum/000_索引.md` | 枚举，按首字母两级分目录 |
| `cppstruct` | 1100 | `raw/docs/api/cppstruct/000_索引.md` | 结构体，按首字母两级分目录 |
| `globalfunc` | 3 | `raw/docs/api/globalfunc/000_索引.md` | 全局函数 |

`class` 下按来源再分四类：

- `和平全局接口/`：绿洲自有的系统级接口，按业务域分子目录——基础功能、角色系统、物品与背包、技能系统、怪物系统、UI 界面、载具、场景与环境、社交系统、玩法规则、商业化与功能模板、工具库。
- `和平类事件/`：可覆写的类事件，按宿主类分目录——GameMode、PlayerController、PlayerPawn、Pawn、武器、载具基类、背包组件、地面可拾取物、技能、Buff。
- `引擎/`：引擎侧常用全局类。
- `Others/`：其余 UE 类，如 `AActor.md`、`UAnimInstance.md`、`UWidgetComponent.md`。

### 常用查证入口

| 需要确认的内容 | 文档位置 |
| --- | --- |
| RPC 调用（`CallUnrealRPC` / `_Unreliable` / `_Multicast`） | `class/和平全局接口/基础功能/UnrealNetwork.md` |
| 资源路径、`SpawnEmitterAttached`、玩家查询 | `class/和平全局接口/基础功能/UGCGameSystem.md` |
| 对象位置 UI（`AddObjectPositionUI` 等） | `class/和平全局接口/UI 界面/UGCWidgetManagerSystem.md` |
| 玩家存档读写 | `class/和平全局接口/角色系统/UGCPlayerStateSystem.md` |
| Actor 附着、碰撞、位置 | `class/Others/AActor.md` |
| World 空间 UI 组件 | `class/Others/UWidgetComponent.md` |

API 文档条目通常带「生效范围：服务器&客户端 / 客户端 / 服务器」标注，这是判断端侧限制的官方依据，见 [端侧权威与 HasAuthority](../程序与网络/端侧权威与HasAuthority.md)。

---

## 二、Wiki 文档（`raw/docs/wiki`）

入口：`raw/docs/wiki/000_索引.md`。正文 329 篇，图片资源集中在 `_assets/images`（3444 张）。

| 顶级分类 | 正文篇数 | 代表内容 |
| --- | --- | --- |
| `绿洲编辑器基础内容` | 27 | 编辑器安装、脚本编写、调试游戏、匹配系统、上传发布、UGCAskQ MCP 使用说明 |
| `新手入门` | 25 | HelloWorld、资源导入与编辑、游戏场景、关卡编辑 |
| `进阶内容` | 142 | 网络同步系统、开发框架介绍、存档、GamePlay 系统（怪物/技能/角色/物资/载具/属性与伤害）、UI 系统、输入系统、模式编辑器、和平精英集成功能 |
| `玩法案例及模板` | 31 | 团竞 2.0、多人 PVE、俯视角生存、经典海岛、3D 预览显示系统 |
| `性能优化及异常处理` | 18 | 性能检测、渲染剔除、网络裁剪、异步加载、弱网重连、PIE 日志面板 |
| `常用实战教学` | 18 | 复活配置、粒子挂载、骨骼缩放、3D 转 2D 预览、坐标转换 |
| `商业化及功能模板` | 18 | 礼包、商业化组件 |
| `常见问题` | 9 | PIE 调试失败原因、上传失败排查、GamePlay/UI/脚本逻辑 FAQ |
| `通用功能` | 13 | 实体类型、Tween、公告系统、场景破坏物 |
| `版本日志` | 10 | 1.28 ~ 1.37 Release Notes |
| `AI工具` | 3 | AI 生成图片、AI 资源检索、视频生成 3D 动画 |
| `交互物` / `开发者须知` | 2 | 交互组件、开发者须知 |

### 高频排查入口

- `常见问题/20391_PIE调试失败原因与解决方案.md`：按九个阶段（入口、权限与版本、压缩上传、上传凭证、上传流程、DS 启动、调试状态、账号限制、Job 任务）逐条列出错误码原文与含义，是 PIE 失败排查的第一站，见 [PIE 调试与热更新边界](../工具与流程/PIE调试与热更新边界.md)。
- `进阶内容/203_网络同步系统介绍.md`：属性同步与 RPC 的官方说明，见 [RPC 分发架构](../程序与网络/RPC分发架构.md)。
- `进阶内容/352_绿洲启元玩法开发框架介绍.md`：DS/Client 划分、GameMode/GameState/PlayerController/PlayerPawn/PlayerState 职责、UID/PlayerKey/TeamID 概念。
- `进阶内容/存档/20052_玩家数据存档.md`：存档 API 与注意事项，见 [存档与数据持久化](../程序与网络/存档与数据持久化.md)。
- `新手入门/资源管理与编辑/277_资源导入.md`：静态模型、贴图、骨骼动画、音效的格式与导入选项，见 [资源导入与路径规范](../配置与数据/资源导入与路径规范.md)。
- `绿洲编辑器基础内容/20414_UGCAskQ MCP 使用说明.md`：MCP 支持的编辑器能力范围，见 [蓝图与 MCP 写入流程](../工具与流程/蓝图与MCP写入流程.md)。

---

## 三、查询工具（`raw/docs/skills/oasis-official-docs.md`）

`oasis-official-docs` 是查询型 skill，供其他工程以 `oasis-skill-plus` 子模块形式接入，从本地 Markdown 检索官方 API 与 Wiki。

| 模式 | 用途 |
| --- | --- |
| `--mode verify-api` | 写代码前先确认 API 是否真实存在 |
| `--mode search --scope wiki` | 先查官方 Wiki 再总结排查方法 |
| `--mode search --scope all` | 跨 API 与 Wiki 综合检索 |

返回 JSON 包含命中来源（`api`/`wiki`）、命中方式（`exact-title`/`title`/`content`）、相对与绝对路径、命中片段。

默认只读本地已同步的 Markdown；仅在用户明确要求「最新」时才执行 `sync` / `sync-api` / `sync-all` 刷新。

**边界**：没有本地文档时不得凭记忆把 API 当成官方事实。

---

## 四、相关页面

- [2026-08-26 raw 资料入库总结](2026-08-26_raw资料入库总结.md)
- [官方文档本地同步](../工具与流程/官方文档本地同步.md)
- [2026-09-11 官方文档 API 同步崩溃修复](2026-09-11_官方文档API同步崩溃修复.md)
- [Wiki 索引](../../../../wiki/000_索引.md)
> 最新镜像校验：2026-09-11，Wiki 329 篇 Markdown + 3444 张图片，API 6201 个文件
