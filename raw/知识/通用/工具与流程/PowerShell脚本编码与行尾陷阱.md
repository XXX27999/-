# PowerShell 脚本编码与行尾陷阱（ACP 936 环境）

- **类型**：经验归纳 + 本机实测
- **主题**：无 BOM UTF-8 的 `.ps1` 在本机 PowerShell 5.1（ACP=936）下按 GBK 解码所引发的解析失败与假报错
- **适用范围**：本机（`C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe`，PSVersion 5.1.26100.9444，`[System.Text.Encoding]::Default.WebName = gb2312`，注册表 `HKLM:\SYSTEM\CurrentControlSet\Control\Nls\CodePage\ACP = 936`）执行的一切 `.ps1`，含知识库归档脚本、技能脚本、一次性工具脚本
- **证据状态**：已实测（2026-09-20，`ugc-log-bug-analyzer` 技能补丁）
- **来源**：本地实测；技能脚本 `C:\Users\Administrator\.workbuddy\skills\ugc-log-bug-analyzer\scripts\analyze_ugc_logs.ps1`；验证记录 `D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260918_DressTheme\skill_verify_final.txt`、`skill_smoke_final.txt`
- **更新时间**：2026-09-20
- **关联主题**：[调试备份存放](./调试备份存放.md)、[日志与错误保护规范](./日志与错误保护规范.md)、`$ugc-log-bug-analyzer`
- **排除范围**：不涉及 PowerShell 7（`pwsh`）默认 UTF-8 行为；不涉及 `.psm1` 模块清单；未验证在 ACP=65001 机器上的差异
- **官方依据**：无（属本机运行时行为，非绿洲官方文档内容）

## 1. 现象

给一个原本纯 ASCII 的 `.ps1` 补丁加入**以中文字符结尾**的注释行后，脚本整份解析失败：

```
Parser::ParseFile → 6 个语法错误
  表达式或语句中包含意外的标记"crash"。
  字符串缺少终止符: '。
  Try 语句缺少自己的 Catch 或 Finally 块。
```

但同一份字节用 UTF-8 解码后 `Parser::ParseInput` 报 **0 错误**，脚本实际执行也正常。即：**错误不来自脚本本身，而来自解码方式。**

## 2. 根因（实测）

1. Windows PowerShell 5.1 读取无 BOM 的 `.ps1` 时按 **ANSI 代码页（本机 936/GB2312）** 解码，而不是 UTF-8。

2. GB2312 解码对 UTF-8 中文的字节流是「按对吞字节」的：前导字节（0x81–0xFE）会吃掉下一个字节。
   - ASCII 字节（< 0x80）永远是单字节字符 → **引号、括号、反引号的数量不会因误码改变**，所以字符串字面量出问题一般不致命；
   - 但中文字符的 UTF-8 末字节常常是前导字节，若该行行尾是**裸 LF**，`末字节 + 0x0A` 会被当成一对消费 → **换行被吃掉，本行与下一行合并**。

3. 实例：注释行以 `。` 结尾（UTF-8 `E3 80 82`，末字节 `0x82` 是合法 GBK 前导字节）+ 裸 LF → 下一行 `$crashForensics = [ordered]@{...}` 被并入注释 → `try` 块结构断裂 → 整份脚本报错。若合并进注释的是赋值语句，在 `Set-StrictMode -Version Latest` 下还会变成运行期变量未定义错误。
   - 实测该文件全文 **只有 1 行** 以非 ASCII 字符结尾（就是新加的补丁行），`ANSI 解码行数 684` vs `UTF-8 解码行数 685`，正好少 1 行。
   - 行尾为 CRLF 时被吞的是 CR、LF 保留，因此不产生合并——**致命组合是「CJK 结尾 + 裸 LF」**。

4. `Parser::ParseFile(path)` 在本机也按 ANSI 读，所以它会给出**假报错**；不能拿它当语法校验依据。

## 3. 规则（可直接照做）

1. **`.ps1` 源码保持纯 ASCII**（字节层面 0 个 >0x7F）。
   - 中文输出用码点构造：`[string]::Concat(([char]0x5BA2),([char]0x6237))`；
   - 长中文文案用 UTF-8 base64：`[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('...'))`。
2. 校验语法时必须**两种解码各测一次**，都要 0 错误：
   ```powershell
   $bytes = [System.IO.File]::ReadAllBytes($p)
   $e1=$null; $null=[System.Management.Automation.Language.Parser]::ParseInput([System.Text.Encoding]::UTF8.GetString($bytes),[ref]$null,[ref]$e1)
   $e2=$null; $null=[System.Management.Automation.Language.Parser]::ParseInput([System.Text.Encoding]::GetEncoding(936).GetString($bytes),[ref]$null,[ref]$e2)
   ```
   更直接的自检：`@($bytes | Where-Object { $_ -gt 127 }).Count` 必须为 0。
3. **不要用点源 `. .\x.ps1` 去测试脚本**：脚本内的 `exit` 会终止当前会话、`Set-StrictMode` 会污染当前作用域，导致其后的校验命令整体失败且看不到原因。用 `& .\x.ps1 -Args`。
4. 写回脚本内容用 UTF-8 **无 BOM**（与知识库文本一致）；若确需中文源码，则必须写 UTF-8 **带 BOM**，并重新确认 `-File` 调用方不额外做 ANSI 解码。
5. 引用 `&` 调用结果时用 `2>&1` 捕获，并对输出做 `ConvertFrom-Json` 之类的一次性可用性校验，避免「无输出」被当成「无问题」。

## 4. 常见误判

| 表现 | 误判 | 实际 |
| --- | --- | --- |
| `ParseFile` 报多处语法错 | 脚本写错了 | 按 ANSI 解码导致的假报错，换 `ParseInput`+UTF-8 即 0 错 |
| 引号/括号看起来没少 | 应该是别的原因 | ASCII 字节不受误码影响，问题在**行合并**，不在引号 |
| 注释里写中文无关紧要 | 只是注释 | 注释行的 CJK 结尾同样能吞换行，把下一行代码并进注释 |
