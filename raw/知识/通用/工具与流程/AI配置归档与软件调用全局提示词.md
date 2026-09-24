# AI 配置归档与软件调用全局提示词

> 类型：通用知识 / 工具与流程
> 主题：AI 工具链能力（技能、插件、MCP）在知识库中的统一归档契约；预留给软件调用的标准化全局提示词
> 适用范围：本机所有 AI 客户端（WorkBuddy、Codex、cc-switch 等）接入《和平精英》绿洲起源 UGC 开发时的技能 / 插件 / MCP / 提示词管理
> 证据状态：项目实测（2026-09-16 全量冷扫描，3016 个文件逐文件 SHA256，回校 `ALL OK`；2026-09-24 全局提示词增补 `$null` 强制禁止）
> 来源：2026-09-16 会话。用户原文——「请在知识库中对与"和平精英"项目编辑相关的所有技能及MCP配置进行完整备份存档。（后续创建的新技能，插件，MCP都存放于知识库）同时检索并查看当前系统正在使用的全局提示词内容，并基于查看结果在知识库中新建一份专门预留给软件调用的全局提示词文本，包含适用于软件使用的标准化指令与上下文说明。」
> 更新时间：2026-09-24
> 关联主题：非运行辅助文件索引与调用规范、调试备份存放、蓝图与 MCP 写入流程、绿洲编辑器提示词优化、知识库准确性与关联性读取写回
> 排除范围：UGC 工程内运行文件（`.uasset` / Lua / 导入资产）本体；插件市场缓存正文；`raw/docs/` 官方原始资料
> 官方依据：官方未覆盖；本条为仓库工程约定 + 本机实测

## 一、核心结论

1. **AI 工具链能力也必须进知识库。** 技能包、插件清单、MCP 配置和全局提示词此前只存在于客户端私有目录（`~\.workbuddy\`、`~\.codex\`、`~\.cc-switch\`），既不在知识库检索范围内，也无法在客户端重装、更新覆盖或误删后恢复。2026-09-16 起统一归档到：

   `D:\知识库\和平精英绿洲起源\工具\AI配置归档\`

2. **「先归档，后部署」是新增资产的强制顺序**：任何新技能 / 插件 / MCP 先在归档目录落权威副本、按模板登记、算哈希，再复制到客户端运行位置。契约见 `…\AI配置归档\存放约定_新增技能插件MCP.md`；该流程本身已固化为技能 `oasis-ai-config-archive`（`~\.workbuddy\skills\oasis-ai-config-archive\SKILL.md`，已同步归档）。

3. **四层技能来源必须分层归档**，不能只存一份：本机技能分布在四个互不相同的宿主目录，且**已存在版本漂移**（同一技能在不同宿主字节数不同）。只保留一份会在恢复时选错版本。

4. **全局提示词要区分「原件」与「可注入版」**：原件依赖各客户端特定的规则目录与条件生效机制（如 WorkBuddy 的 `alwaysApply` / `paths`、Codex 的 `AGENTS.md`），无法直接搬到别的客户端；因此另建一份客户端无关、可整文件注入的「软件调用版」，把路径、技能、MCP、输出契约全部显式化。

5. **「与和平精英项目编辑相关」的判定**采用三条并行标准：① 技能描述直接指向绿洲编辑器 / UGC 资产 / 官方文档；② 被全局规则显式 `$技能名` 点名；③ 本机实际参与绿洲工作流。未命中的同目录技能一并镜像，避免恢复缺口。

6. **2026-09-24 增补 `$null` 强制禁止**：PowerShell 的 `>$null` / `2>$null` 在 UGC 工程目录被当成路径时会生成 0 字节 `$null`，触发 `CheckUploadFileNameFailed Result 10001` 并中断 PIE。全局提示词、项目规则和软件调用版均已加入「禁止创建或残留 `$null`、禁止在工程目录使用 `>$null` / `2>$null`、收尾复扫为 0」条款；项目实测与替代命令见 [调试备份存放](./调试备份存放.md) 和 [PIE 调试非法字符校验失败](./PIE调试非法字符校验失败.md)。

## 二、归档位置与分层

| 资产类型 | 归档位置 | 客户端运行位置 |
| --- | --- | --- |
| WorkBuddy 用户级技能 | `…\AI配置归档\skills\workbuddy\` | `C:\Users\Administrator\.workbuddy\skills\` |
| Codex 侧技能 | `…\AI配置归档\skills\codex\` | `C:\Users\Administrator\.codex\skills\` |
| cc-switch 共享技能 | `…\AI配置归档\skills\shared_cc-switch\` | `C:\Users\Administrator\.cc-switch\skills\` |
| 绿洲仓库自带技能 | `…\AI配置归档\skills\repo_oasis-skill-plus\` | `D:\oasis-skill-plus\skills\` |
| WorkBuddy MCP / 连接器 | `…\AI配置归档\mcp\workbuddy\` | `…\.workbuddy\mcp.json`、`…\.workbuddy\connectors\` |
| Codex MCP | `…\AI配置归档\mcp\codex\` | `…\.codex\config.toml` 的 `[mcp_servers.*]` |
| 插件与市场清单 | `…\AI配置归档\plugins\workbuddy\` | `…\.workbuddy\plugins\`、`…\.workbuddy\settings.json` |
| 全局提示词 | `…\AI配置归档\全局提示词\` | `…\.workbuddy\rules\`、`…\.codex\AGENTS.md` |

**排除项（明确不入档）**：`__pycache__` 与 `*.pyc`（可再生缓存）、客户端 `plugins\cache` 内置插件正文（市场可重装）、会话历史与状态库（`workbuddy.db`、`*.sqlite`）。

## 三、软件调用版全局提示词的定位

| 项 | 值 |
| --- | --- |
| 文件 | `D:\知识库\和平精英绿洲起源\工具\AI配置归档\全局提示词\软件调用版_绿洲全局提示词.md` |
| 版本 | `1.1.0`（2026-09-24） |
| 结构 | YAML 元数据 → 0 加载与拼装约定 → 1 身份与目标 → 2 运行环境上下文 → 3 标准化指令（3.1–3.15）→ 4 技能调用矩阵 → 5 MCP 调用契约 → 6 输出契约 → 7 硬约束与禁止项 → 8 版本与变更 → 9 相关页面 → 10 待查证 |
| 合并来源 | `oasis-global.md`（WorkBuddy 全局规则）+ `island-auction-king-config.md`（项目级配置规范）+ `CODEBUDDY.md`（用户记忆速查）+ `AGENTS.md`（Codex 全局提示词） |
| 设计取舍 | ① **保留原表述**：指令正文沿用原件措辞，只做编号结构化，不做同义改写；② **前后加契约**：文件头 YAML 可被解析，正文含加载契约与输出契约；③ **客户端无关**：Codex 专属的线程派发、具体模型名、本地代理端口全部抽成第 0.3 节「可选模块」并标注启用条件；④ **路径单一真相**：所有路径集中在第 2 节，指令正文只引用 `{{...}}` 符号 |

四份原件的关系（逐字对比结论）：

- **原件04（Codex `AGENTS.md`）是超集**：额外含【多开对话派发】【当前模型】【主任务统筹与持续监听】三章线程派发专属内容，以及 Sol + Luna 授权条款与具体模型名。
- **原件01（WorkBuddy `oasis-global.md`）是通用化子集**：删除上述 Codex 专属章节，把 `$oasis-official-docs` / `$oasis-ui-screenshot` / `$oasis-image-import` / `$oasis-dev-record` 的触发条件补入【全局技能】，并新增 4k/gpt-image-2 的三条硬约束与耗时事实。
- **原件02 与原件04 第 132–355 行内容等价**（IslandAuctionKing 功能脚本配置规范），在 WorkBuddy 侧被拆成独立规则文件按项目路径条件生效。
- **原件03 只做速查**，指向原件01、原件02。

## 四、可执行步骤

### 4.1 检索归档（先查索引，不扫目录）

```powershell
$root = 'D:\知识库\和平精英绿洲起源\工具\AI配置归档'
# L0：读总索引与归档登记记录
Get-Content "$root\000_归档索引.md"
Get-Content "$root\归档记录\20260916_技能与MCP全量归档.md"
# L1：按精确实体定位（技能名 / MCP 服务名 / 端口 / 触发词）
Select-String -Path "$root\000_归档索引.md","$root\归档记录\*.md" -Pattern 'ugcaskq|12463|oasis-prompt-optimize'
```

### 4.2 校验归档完整性

```powershell
$root = 'D:\知识库\和平精英绿洲起源\工具\AI配置归档'
Get-Content "$root\归档记录\校验清单_SHA256.txt" | Where-Object { $_ -notmatch '^#' -and $_.Trim() } | ForEach-Object {
  $p = $_ -split '\s+'
  $f = Join-Path $root $p[1]
  if (-not (Test-Path $f)) { "MISSING $($p[1])" }
  elseif ((Get-FileHash $f -Algorithm SHA256).Hash -ne $p[0]) { "FAIL    $($p[1])" }
}
# 期望输出：无 MISSING / 无 FAIL
```

### 4.3 恢复技能

```powershell
robocopy 'D:\知识库\和平精英绿洲起源\工具\AI配置归档\skills\workbuddy' `
         "$env:USERPROFILE\.workbuddy\skills" /E /XD __pycache__ /XF *.pyc
# 恢复后重启客户端；UGCAskQ 端口用 $oasis-mcp-port-discover 复核
```

### 4.4 恢复 MCP 配置

```powershell
Copy-Item 'D:\知识库\和平精英绿洲起源\工具\AI配置归档\mcp\workbuddy\01_workbuddy_mcp.json' `
          "$env:USERPROFILE\.workbuddy\mcp.json" -Force
# Codex 侧：把 mcp\codex\01_codex_config.toml 的 [mcp_servers.ugcaskq] 段手工合并进现网 config.toml，
# 不要整文件覆盖（现网还有 [projects.*] 信任列表与 [windows] 段）
```

### 4.5 以软件调用版作为系统提示词前缀

```powershell
Get-Content 'D:\知识库\和平精英绿洲起源\工具\AI配置归档\全局提示词\软件调用版_绿洲全局提示词.md' -Raw
```

调用方按该文件第 0.1 节选最小注入集，按 0.2 节替换 `{{...}}` 符号；若不做替换，须把符号按字面语义理解为对应绝对路径。

### 4.6 新增技能 / 插件 / MCP

按 `…\AI配置归档\存放约定_新增技能插件MCP.md` 五步执行：建前查重 → 写入归档 → 按固定字段登记 → 算 SHA256 → 部署到客户端。登记项字段固定为：资产类型、归档绝对路径、来源绝对路径、部署目标绝对路径、关联实体、用途、调用入口、输入/输出、依赖、版本、证据状态、生命周期、更新时间。

## 五、常见错误

- ❌ **只把技能留在客户端目录**，认为「装好了就行」。→ 客户端更新会静默覆盖自研技能，重装即丢失。
- ❌ **只归档一份技能**。→ 本机四个宿主目录已有字节级差异，单份归档会在恢复时选错版本。
- ❌ **把插件缓存或会话数据库也塞进归档**。→ `plugins\cache` 体积大且可重装；`*.sqlite` 是历史数据不是配置资产。
- ❌ **用 Codex `AGENTS.md` 直接当通用提示词注入别的客户端**。→ 其中【多开对话派发】【当前模型】依赖 Codex 专有工具，注入后会产出无效指令，甚至复现历史模型名硬编码问题。
- ❌ **把软件调用版当原件维护**。→ 原件更新后须同步第 8 节版本表；路径变更只改第 2 节；客户端专属内容一律进第 0.3 节，不得写进第 3 节指令主体。
- ❌ **归档内留下 `__pycache__` / `*.pyc` / 临时脚本**。→ 破坏哈希校验的稳定性。
- ❌ **用归档整文件覆盖 Codex `config.toml`**。→ 会丢掉 `[projects.*]` 信任列表与 `[windows] sandbox` 段。

## 六、相关页面

- [../知识库治理/非运行辅助文件索引与调用规范.md](../知识库治理/非运行辅助文件索引与调用规范.md)
- [调试备份存放](./调试备份存放.md)
- [蓝图与MCP写入流程](./蓝图与MCP写入流程.md)
- [UGCAskQ-MCP能力矩阵](./UGCAskQ-MCP能力矩阵.md)
- [UGCAskQ-MCP实测陷阱清单](./UGCAskQ-MCP实测陷阱清单.md)
- [绿洲编辑器提示词优化](./绿洲编辑器提示词优化.md)
- [Codex-Sol与Luna分工模式](./Codex-Sol与Luna分工模式.md)
- [AI配置归档索引（归档目录）](../../../../工具/AI配置归档/000_归档索引.md)
- [软件调用版_绿洲全局提示词](../../../../工具/AI配置归档/全局提示词/软件调用版_绿洲全局提示词.md)

## 七、待查证

1. `~\.codex\skills` 与 `~\.workbuddy\skills` 的同步机制未查证：`oasis-official-docs` 是软链到 `~\.cc-switch\skills`，其余是独立副本且已有字节差异，尚不清楚是人工同步还是某个工具在做单向复制。
2. 「先归档后部署」是否会导致客户端读到旧副本，取决于各客户端技能扫描策略，未实测。
3. 插件正文能否从 `~\.workbuddy\plugins\cache` 稳定抽出并离线固化，未验证。
4. ~~UGCAskQ 端口 `12463` 是否为编辑器固定端口（三处配置均硬编码），未做跨启动实测。~~ **已确认（用户确认，2026-09-16）**：`12463` 是本机编辑器的**固定端口**，三处硬编码即为正确写法，无需自动发现。剩余未查证项：与官方默认 `33444` 的取值差异成因。
5. Codex 链路应走 `57321`（现网 `config.toml` 的 `base_url`）还是 `8787`（`AGENTS.md` 硬性要求），两处结论冲突，需实测判定。
