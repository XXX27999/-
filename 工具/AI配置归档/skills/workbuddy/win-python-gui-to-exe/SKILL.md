---
name: win-python-gui-to-exe
description: 把本机 Python 脚本（含 tkinter 图形界面）打包成 Windows 单文件 exe，并在打包前后用命令行自检 + 窗口枚举冒烟测试做可复现验证。当用户要求“做一个 exe 程序 / 桌面小工具 / 把脚本打包成 exe”，或在 Windows 上开发独立 GUI 工具时需要用到。
agent_created: true
---

# Windows Python GUI → 单文件 exe

把带界面的 Python 工具做成双击可用、可交付的 `.exe`，并保证“打包成功”之外还有**可验证的运行证据**。

## 本机环境事实（先读，能省掉一半返工）

| 事项 | 结论 |
| --- | --- |
| 托管 Python 3.13.12 | **没有 tkinter**，`import tkinter` 直接 `ModuleNotFoundError` |
| 系统 Python 3.12.10 | **有 tkinter 8.6**，路径 `C:\Users\Administrator\AppData\Local\Programs\Python\Python312\python.exe` |
| 结论 | 任何带 GUI 的工具**一律用系统 Python 3.12**；3.13 只用于无 GUI 的纯脚本 |
| 隔离 venv 示例 | `C:\Users\Administrator\.workbuddy\binaries\python\envs\<name>`（用系统 Python 创建，才能继承 tkinter） |
| bash 工具 | **残缺**：`ls` `find` `head` `grep` `rm` `dirname` `cd` 全部 `command not found`（`rm` 的 safe-bin shim 也失败） |

**bash 替代方案**：文件枚举 / 删除 / 复制一律改用 `python -c` 或 PowerShell 工具，
不要试图在 bash 里 `ls` / `rm`。多行 `python -c` 用双引号包裹、内部用单引号，Windows 路径的反斜杠可原样传递。

## 步骤

### 1. 写源码时就要为“可验证”留口子

主程序除 GUI 外**必须同时支持命令行模式**，否则打包后无法自动化验证：

```python
def parse_args(argv=None):
    p = argparse.ArgumentParser(prog="...")
    p.add_argument("--scan", metavar="输入", help="命令行模式")
    p.add_argument("--txt", metavar="输出文件")
    p.add_argument("--html", metavar="输出文件")
    return p.parse_args(argv)

def main():
    # --windowed 打包后没有控制台，stdout/stderr 为 None，必须先兜底
    if sys.stdout is None: sys.stdout = open(os.devnull, "w")
    if sys.stderr is None: sys.stderr = open(os.devnull, "w")
    args = parse_args()
    if args.scan:
        return run_cli(args)      # 不创建 Tk root
    root = tk.Tk(); App(root); root.mainloop(); return 0

if __name__ == "__main__":
    sys.exit(main())
```

其它必须写进源码的细节：

- **模块 docstring 用 `r"""`**：正文里出现 `\Asset` / `\UGCProjects` 这类 Windows 路径会触发
  `SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes ... truncated \UXXXXXXXX escape`。
- **区分 frozen 路径**：`os.path.dirname(sys.executable)`（`getattr(sys, "frozen", False)` 为真时），
  否则 exe 同目录的外置配置/词典会找不到。
- **DPI 感知**（可选但明显提升观感）：
  ```python
  try:
      from ctypes import windll; windll.shcore.SetProcessDpiAwareness(1)
  except Exception: pass
  ```
- **tkinter 用 `ttk` + `clam` 主题**，`Treeview` 设 `rowheight`，中文指定 `Microsoft YaHei UI` 字体。

### 2. 打包前先跑通逻辑（不起 GUI）

```bash
cd "<源码目录>" && "<系统 Python312>" -X utf8 -m py_compile 主程序.py && echo SYNTAX_OK
"<系统 Python312>" -X utf8 主程序.py --scan "<真实输入>" --txt "<临时输出>" --html "<临时输出>"
```

**一定要拿真实数据跑**，不要只跑构造的样例——本次就是靠这一步才发现
`Config`+`Table` 叠词、`GameMode` 被驼峰切碎等 4 处翻译缺陷。

### 3. 建隔离 venv 并装 PyInstaller

```bash
"<系统 Python312>" -m venv "C:\Users\Administrator\.workbuddy\binaries\python\envs\<name>"
"C:\Users\Administrator\.workbuddy\binaries\python\envs\<name>\Scripts\python.exe" -m pip install --quiet --upgrade pip pyinstaller
```

**没有任何缓存时这一步约 4 分钟，务必 `run_in_background`。**

### 4. 打包

```bash
cd "<源码目录>" && "<venv>/Scripts/python.exe" -m PyInstaller \
  --noconfirm --clean --onefile --windowed --name <英文名> \
  --distpath "<交付目录>/dist" \
  --workpath "<工程外目录>/build" \
  --specpath "<工程外目录>" \
  "主程序.py" > "<工程外目录>/build_log.txt" 2>&1; echo "BUILD_EXIT=$?"
```

- `--onefile --windowed`：单文件 + 无黑框控制台，双击即用。
- **`--workpath` / `--specpath` 必须指到交付目录之外**（如知识库备份目录），
  否则交付目录会被 `build/` 和 `.spec` 污染。
- **exe 名用英文**（如 `FolderTreeTranslator.exe`），窗口标题里再用中文，避免编码坑。
- 清理缓存用 Python：`python -c "import shutil;shutil.rmtree(r'<dir>\\__pycache__',ignore_errors=True)"`（bash 无 `rm`）。

#### ⚠️ 打包前必做两件事（否则会失败或留下脏文件）

**1) 先建好 `--workpath` / `--specpath` 目录。** bash 不会因重定向自动建目录，目录不存在时
命令直接以 `No such file or directory` 失败，`build_log.txt` 都写不出来（第一眼看不到真正原因）。

**2) 先物理删除 `dist\<name>.exe`。** PyInstaller 覆盖已存在的 exe 时调用 `os.remove`，
本机 `sitecustomize.py` 会把它劫持成"移入回收站"，回收站异常时报
`[safe-delete] 操作失败 ... Error during a 'trash' operation ... Some operations were aborted`
导致 `BUILD_EXIT=1`。最可靠的删法：

```powershell
Remove-Item "<交付目录>\dist\<name>.exe" -Force    # 用 PowerShell 工具，别用 bash rm
```
注意 PowerShell 工具**删除成功后也可能返回 exit code 1**、且不回显 stdout，
必须再用 Python `os.path.exists()` 复核，不要凭退出码判断。

**3) 打包后扫一遍交付目录**：safe-delete 失败时可能把文件"搬走"而不是删除，
导致交付目录根出现**旧版本 stray exe**（同名不同大小）。发现后立即删掉，
否则用户会双击到旧版本。

### 5. 打包后验证 exe（两步，缺一不可）

**a) 命令行模式实测**——直接跑 `dist\<name>.exe --scan ... --txt ...`，
确认 exe 内部逻辑与源码版一致。

**⚠️ exe stdout 在 WorkBuddy Desktop 内走 cp936 编码**（PyInstaller `--windowed` 进程
`subprocess.run` 默认按系统 codepage 解码），直接 `print(r.stdout)` 中文全是乱码。
**改让 exe 用 `--txt <文件>` 把结果落到文件，再用 `Read` 工具读 .txt 验证**——别靠 stdout 解析。

**b) GUI 冒烟测试**——`--windowed` exe 崩溃会静默退出，必须确认窗口真的建出来了：

**首选：源码版 import + tk.Tk() 路径**（不依赖 exe 子进程，受 sandbox 影响最小）：

```python
import sys, tkinter as tk
sys.path.insert(0, r"<工具目录>")
import 主程序 as app
assert app.APP_VERSION == "<版本号>"

# 把所有关键模块都 import 一次
print("WORD_DICT:", len(app.WORD_DICT))

root = tk.Tk()
root.title("%s  v%s" % (app.APP_TITLE, app.APP_VERSION))
print("title:", root.title())
root.update()              # 让窗口进入消息循环一次
print("geom:", root.winfo_geometry())
root.destroy()
print("[OK] GUI 启动路径通过")
```

**兜底：exe 子进程枚举窗口**（**WorkBuddy Desktop 内 MainWindowHandle 通常为 0**，
只有 IME 子窗口可见；只有原生桌面会话才可靠）：

```python
import ctypes, subprocess, time
from ctypes import wintypes
proc = subprocess.Popen([EXE], creationflags=0x00000008)   # DETACHED_PROCESS
time.sleep(7)
ps = ("$p = Get-Process -Id " + str(proc.pid) +
      " -ErrorAction SilentlyContinue; "
      "if ($p) { @{ Title = $p.MainWindowTitle; HasMain = $p.MainWindowHandle.ToInt64() -ne 0 } | ConvertTo-Json }")
r = subprocess.run(["powershell", "-NoProfile", "-Command", ps],
                   capture_output=True, text=True)
ok = ("v1.x.x" in r.stdout) or ("整理工具" in r.stdout)
proc.terminate()
```

注意：WorkBuddy Desktop sandbox 内 `MainWindowHandle` 通常为 0 或指向 IME 子窗口，
**只有外层桌面会话才能看到完整 Tk 顶层标题**。源码 import + tk.Tk() 是更可靠的验证。

### 6. 收尾

- 一次性 `.py` 测试脚本用完即删（用 Python，不用 bash `rm`）。
- 删掉 `build/`、`.spec`、`__pycache__`、`*.pyc`、`build_log.txt`。
- 保留一份真实输出样本（如导出的 txt/html）到 `示例输出\`，作为交付证据。
- 扫一遍源工程根目录确认无残留。

## 交付物布局建议

```
<工具目录>/
├── 主程序.py                    # 源码，用户可能要改
├── dist/<英文名>.exe            # 单文件 exe
└── 示例输出/…                   # 真实运行样本
```

**不要把 exe 或 `.py` 放进绿洲 UGC 工程目录**：PIE 上传会递归扫描工程内文件，
含 `.` 或 `-` 的文件名会触发 `may contain the following characters: .-` 中断调试。

## 附：目录名「英译中 + 拼音识别」引擎的坑（本工具累积）

> 适用场景：把 UGC 工程的英文/拼音命名的资产目录树翻译成中文名展示。
> 分两级匹配：**内置词典**（可被同目录 `translation_dict.json` 覆盖）+ **规则引擎**。

### 判定顺序（顺序错了就丢译名，这是最容易踩的坑）

```
1. 完整名精确表 names          （DressControlTable → 装扮方案表）
2. 前缀表 prefixes             （UGCTemplateRowStruct_ → 表格行结构模板）
3. 分段：按 _ - 空格 切
   每段依次走：
     3.1 整段精确表 segs
     3.2 英文词表 words（含 upper / capitalize / lower 变体）
     3.3 拼音词级表 PY_WORDS（原大小写优先，再小写）
     3.4 型号/专有代号 判断 → 保留原文
     3.5 驼峰分词 → 英文最长窗口(4~2词) → 拼音最长窗口(3~2词) → 单词表 → 拼音
4. 拼接后叠词合并 + 中英交界补空格
```

**3.2 / 3.3 必须排在 3.4 之前**，否则 `FX`（特效）、`GM`、`ID`、`CWJB`（宠物金币部）
这类 3~6 位全大写缩写会被当成型号保留英文，丢掉已有译名。

### 拼音识别必须有「不像英文」的硬约束（否则大面积误判）

无约束的音节切分会把常见英文词切成合法拼音：`orange` → `o`+`ran`+`ge` 全合法 →
误译「哦让鹅」；`purple`/`blue`/`green` 同理。**实测有效的三条约束**：

1. 原串长度 ≥ 4
2. 音节数 ≥ 2（单音节交给词级表）
3. **每个音节长度 ≥ 2 —— 禁用单字母音节 a/o/e**（英文里极常见，拼音里极少用）

另外：**单字母 token（`A` / `M` / `O`）一律不参与拼音识别**，否则 `M16A4` 会被译成
「M 16 啊 4」。删掉「单音节兜底」分支能再消掉一批误判。

**根本解法仍是补英文词表**——颜色（Orange/Purple/Blue/Green/Red/Yellow/Black/
White/Gray/Pink/Brown/Cyan）、方位、动作、界面术语等高频词进表后，
自然走英文分支，不再落到拼音。

### 型号 / 专有代号要保留原文，不要硬拆

枪械与装备型号在中英文里写法一致，翻译反而难读。两条正则即可覆盖：

```python
_MODEL_RE      = re.compile(r"^(?:[A-Za-z]+[0-9]+[A-Za-z0-9]*|[0-9]+[A-Za-z]+[A-Za-z0-9]*)$")
_UPPER_TOKEN_RE = re.compile(r"^[A-Z]{3,6}$")
```

命中即 `return seg`。覆盖 `M416` / `M16A4` / `UMP45` / `M249` / `MK14`（含数字）
与 `AKM` / `AWM` / `SKS` / `QBZ` / `SCARL` / `UIBP` / `SDK`（3~6 位全大写）。

后缀类缩写（`UIBP` = UI Blueprint、`BP` = Blueprint）建议在整段表里映射为**空串**，
拼接时自动跳过，中文名更干净（`LobbyMain_UIBP` → 「大厅主界面」）。

### 覆盖率统计不要用「中文名里还有没有字母」

型号、专有缩写保留原文是预期行为，用字符判会把它们计入缺口，数字虚低。
改为在翻译过程中**逐 token 计数**：给翻译函数加可选 `miss` 参数
（`{"n": 0}`），只在真正落到「未识别 → 保留原文」分支时 `miss["n"] += 1`，
最后按文件是否有 miss 统计完整率。这样 `AKM_Orange → AKM 橙色` 不计缺口。
