# 2026-09-24 CodexTokenGlass 大会话删除失效修复

> 类型：来源记录
> 主题：CodexTokenGlass 大会话删除后界面无响应/疑似删除失效的性能修复
> 适用范围：`D:\知识库\和平精英绿洲起源\工具\CodexTokenGlass\`
> 证据状态：项目实测（本地接口计时、文件存在性复验、并发删除回归）
> 来源：用户反馈“删除失效”；工具运行实例 `http://127.0.0.1:9912`；抓包数据 `C:\Users\Administrator\.ccglass\codex-desktop`
> 更新时间：2026-09-24
> 关联主题：[CodexTokenGlass 正文](../工具与流程/CodexToken消耗查询工具.md)
> 排除范围：不涉及 UGC 工程、Lua、蓝图或 PIE

## 问题

用户反馈 CodexTokenGlass 左侧历史删除失效。检查运行实例与磁盘后确认：

- `DELETE /api/delete` 路由存在，GET 返回 405；
- `POST /api/delete-batch` 返回 200；
- CLI `rm-entry` 对真实文件可删除，二次删除返回 not found。

因此“失效”不是接口不存在，也不是文件没删，而是删除后前端触发的整会话重载极慢，界面长时间无响应，表现为删除没有生效。

## 根因证据

会话 `2026-09-24T11-08-38-398` 当时有 1818 个清单、约 627 MB。

| 接口 | 修复前实测 |
| --- | ---: |
| `/api/requests?session=...` | 约 66 秒 |
| `/api/session-stats?session=...` | 约 101 秒 |
| `/api/delete-batch` 单条 | 约 109 ms（文件立即消失） |

旧流程是删除成功后立即重拉列表与统计，两者都调用 `loadSessionMulti` 全量解包所有消息 blob；627 MB 数据反复 JSON 解析会把事件循环占满，并曾触发 Node 4 GB 堆上限崩溃（`service.log`）。

## 修复

1. `ccglass\src\store.js`
   - 新增按 `mtime+size` 的会话摘要缓存；
   - 新增 `summarizeSessionMultiAsync`，每批 24 个文件并 `setImmediate` 让出事件循环；
   - 轻量摘要只读 v2 清单、不展开消息 blob；
   - 旧清单缺少 `metrics` 时后台串行回填 `estInput` / `estOutput` / `nToolUse`。
2. `ccglass\src\blobs.js`
   - 新增 `gcBlobsAsync`，删除后的孤儿 blob 回收改为后台执行。
3. `ccglass\src\store.js` / `ccglass\src\server.js`
   - 新增 `rmEntriesMultiFast`：先删文件并立即返回；
   - `/api/requests`、`/api/session-stats` 改用异步摘要路径；
   - 删除批量接口在响应后调度后台 GC。
4. `ccglass\web\app.js` / `index.html`
   - 删除成功后按返回 id 本地移除并轻量扣减统计，不再同步全量重载；
   - 静态资源版本更新为 `app.js?v=20260924-delete-fast`。
5. 后续加固（同日第二轮）
   - `METRICS_BACKFILL_QUEUE` 改为只保存 `{ file, id, root }`，回填时重新读取清单，避免队列长期持有 1818 份大响应正文；
   - 新增 `rmSessionFast`，单条删除（`DELETE /api/delete?id=`）与整会话删除（`?session=`）也改走“先落盘、响应后后台 GC”，不再让 HTTP 响应等待全量 GC。

## 验证

- 大会话列表接口：`283 ms`。
- 大会话统计接口：`283 ms`。
- 大会话统计进行中并发删除：`119 ms` 返回 `{"deleted":[".../0003"],"removed":1}`，文件立即消失。
- 单条删除：`109 ms` 返回，磁盘复核 `AFTER_EXISTS=False`。
- 删除后列表：`168 ms` 返回空列表，确认刷新能反映删除。
- 前端资源版本：`APP_VERSION=20260924-delete-fast`。
- `node --check`：`store.js`、`server.js`、`blobs.js`、`app.js` 全部通过。
- 第二轮重启后复测（PID `20384`）：大会话列表热态 `303 ms`、统计 `335 ms`；`GET /api/delete` 返回 `405`；缺失 id 单条删除探测 `173 ms` 返回 404、缺失 id 批量删除探测 `80 ms` 返回 `{"deleted":[],"removed":0}`。

## 回归测试删除的真实抓包

为验证删除确实落盘，回归过程中删除了三条真实抓包，必须如实披露：

- `2026-09-23T13-42-27-356/0001`：已删除，删除前未单独备份。
- `2026-09-23T13-13-09-977/0002`：已删除；原内容副本见 `D:\知识库\和平精英绿洲起源\备份\CodexTokenGlass\20260924_delete_regression\data2\2026-09-23T13-13-09-977\`。
- `2026-09-23T13-13-09-977/0003`：已删除；原内容副本同上一目录。

## 备份

- 源码写前备份：`D:\知识库\和平精英绿洲起源\备份\CodexTokenGlass\20260924_delete_large_session_fix\`
- 重启前进程记录：同目录 `restart_note.txt`

## 关联

- [CodexTokenGlass 正文](../工具与流程/CodexToken消耗查询工具.md)
- [CodexTokenGlass 删除与 Token 估算来源记录](./2026-09-23_CodexTokenGlass封装与中文化.md)
