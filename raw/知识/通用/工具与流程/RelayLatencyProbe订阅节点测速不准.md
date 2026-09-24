# RelayLatencyProbe 订阅节点测速不准

> 类型：通用知识
> 主题：Clash Verge / mihomo 订阅节点的 AI 中转站首字延迟测速算法；streaming SSE 停表精度
> 适用范围：`D:\知识库\和平精英绿洲起源\工具\outputs\relay-latency-probe`（源码 `app.py` / `engine.py` / `clash_mihomo.py`，产物 `RelayLatencyProbe.exe`）
> 证据状态：项目实测（2026-09-16 离线自测 `test_pick_best.py` 全绿、`test_compare.py` 新旧对照）；推理归纳（未连真实订阅做端到端验证）
> 来源：`app.py`、`engine.py`、`clash_mihomo.py`；备份 `D:\知识库\和平精英绿洲起源\备份\relay-latency-probe\20260916_node_scan_accuracy\`
> 更新时间：2026-09-16
> 关联主题：工具与流程 / 延迟排查 / mihomo 本地 API
> 排除范围：不覆盖 UGC 工程内玩法脚本；不涉及 VMware / 蓝图
> 官方依据：mihomo External Controller 的 `/proxies`、`/group/{name}/delay`、`/connections` 行为由 `/group` 返回结构实测推断；其余为本地实现，无官方文档约束

## 症状

点「测订阅节点」后结果不稳定：同一批节点多次测量最优节点不同；部分明明能出字的节点被判失败；「切换最优」后再手工探测，最优节点并不快。

## 根因（源码级）

| # | 位置 | 问题 | 后果 |
| --- | --- | --- | --- |
| 1 | `engine.run_model_probe` 旧 `stop_on_first` 判定 | 只要 `first_byte_ms` 被赋值（HTTP body 的第一块数据到达）就 `break`，此时通常只有 `{"choices":[{"delta":{"role":"assistant"}}]}` 角色帧 | `first_output_ms` 恒为 `None`，是否拿到可见首字取决于网络分包，时好时坏 |
| 2 | `clash_mihomo.pick_best_by_model` 的 `ok` 判定 | 要求 `probe["ok"] and first_ms is not None and not probe["error"]`，且 `first_ms` 只取 `first_output_ms` | 能正常推理的节点被误判失败，报「没有测到可用的模型节点」 |
| 3 | 单样本排序 | 每个节点只发 1 次请求就排序 | LLM 首字抖动（排队、冷启动）直接进入排序，结果不可复现 |
| 4 | 按 `delay` 升序串行、无预热 | 本机 DNS/TLS 与中转站首次排队的成本全部落在前 1~2 个节点上 | 排在最前的节点被系统性测慢；对照实验中真值 400ms 的节点被测成 2000ms |
| 5 | `group_delay` 默认 `http://www.gstatic.com/generate_204` | 用与目标链路无关的 Google CDN 做预筛并截断到 `limit` | 真实业务域名快的节点根本没进候选池 |
| 6 | `pick_best()` | 调用 `pick_best_by_model(group_name=...)` 缺 `probe_fn` | 一旦被调用必抛 `TypeError`（当前无调用点） |

## 修复

- `engine.run_model_probe` 新增 `stop_on_first_output` / `min_output_chars` / `max_tail_ms`：只有累计到可见输出 token 才停表。
- `engine.model_first_token_ms()`：取值顺序 `first_output_ms` → `first_reason_ms`，**刻意不回退 `first_byte_ms`** —— 只回一个字节却没有任何 token 的节点（中转站秒回错误体）不能被算作可用，否则死节点会被排到最快。
- `clash_mihomo.pick_best_by_model` 重写为五段：
  1. **预热**：丢弃一次探测，吸收冷启动成本；
  2. **目标感知预筛**：`collect_delay_map()` 按真实中转站域名测延迟，失败才回退通用 204；候选池除前 `limit` 个外，从未入池节点均匀补 `limit//4` 个，防止预筛偏差漏掉好节点；
  3. **粗筛**：全候选池各测 1 次；
  4. **精筛**：粗筛前 `shortlist`(5) 名做 `repeats-1` 轮复测，每轮用 `round_robin()` 蛇形换序，摊平顺序偏差；
  5. **交叉确认**：top2 再各补 `confirm`(2) 次。排名一律取**中位数**，返回 `samples` / `median_ms` / `spread_ms`。
- 切换后固定 `settle_ms=350` 等待再探测；新增 `budget_sec=1200` 总预算兜底。
- `leaf_nodes` 增加 `hidden` 过滤；`group_delay` 默认改 https。
- UI：`app.py` 增加「采样次数」输入（`settings.json` 的 `scan_repeats`，默认 3，1~5），探测超时 15s，「测订阅节点」按钮运行期间变「停止测节点」，结果展示中位数与波动。

## 验证

离线自测脚本（在备份目录，非工程内）：

- `test_pick_best.py`：伪造 SSE 分片与 mihomo API，`[PASS] 可见首字明显晚于首字节 差值=300ms`、19 项全绿。
- `test_compare.py`：同数据跑备份目录里的旧算法 vs 新算法

```
旧算法  最优=MID   FAST=2.0 MID=0.9 SLOW=1.5   ← 真值 FAST=400ms，误判
新算法  最优=FAST  FAST=0.4 MID=0.9 SLOW=1.5   ← 正确
```

- PyInstaller 重建 `RelayLatencyProbe.exe`（12,545,396 字节，2026-09-16 13:17），进程冒烟启动 8 秒无崩溃。

## 待查证

- 未连真实订阅做过端到端测速。若接入后发现 top 节点仍不稳，优先调大 `采样次数`，并把 `测节点数` 从 60 降到 10~20（60 个节点串行粗筛在死节点多时会拖到分钟级）。
- `/group/{name}/delay` 对需要鉴权的业务域名返回的延迟是否包含服务端处理时间，未核实。

## 关联

- 备份与自测：`D:\知识库\和平精英绿洲起源\备份\relay-latency-probe\20260916_node_scan_accuracy\`
- 重建命令：

```bat
cd /d D:\知识库\和平精英绿洲起源\工具\outputs\relay-latency-probe-build
python -m PyInstaller --noconfirm --onefile --windowed --name RelayLatencyProbe ^
  --distpath "D:\知识库\和平精英绿洲起源\工具\outputs\relay-latency-probe" ^
  --workpath "D:\知识库\和平精英绿洲起源\工具\outputs\relay-latency-probe-build\work" ^
  --specpath "D:\知识库\和平精英绿洲起源\工具\outputs\relay-latency-probe-build" ^
  "D:\知识库\和平精英绿洲起源\工具\outputs\relay-latency-probe\app.py"
```
