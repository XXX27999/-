# Oasis Editor Capture Workflow

This reference describes the FlaUI-only capture route used by `oasis-ui-screenshot`.

## Build and enumerate

```powershell
Set-Location -LiteralPath 'C:\Users\Administrator\.codex\skills\oasis-ui-screenshot\tools\FlaUiCapture'
dotnet restore .\FlaUiCapture.csproj
dotnet build .\FlaUiCapture.csproj -c Release --no-restore
dotnet run --project .\FlaUiCapture.csproj -c Release --no-build -- --list
```

Require exactly one visible `ShadowTrackerExtraUGCEditor` window. Use the exact process name and title returned by `--list`; never construct a window identifier or reuse an old process title.

## Direct capture

```powershell
dotnet run --project .\FlaUiCapture.csproj -c Release --no-build -- `
  --process-name 'ShadowTrackerExtraUGCEditor' `
  --title '<exact title from --list>' `
  --output 'C:\absolute\path\oasis-ui.png' `
  --activate
```

FlaUI's `Capture.Element(window).ToFile(...)` is a desktop GDI capture. The target must be visible and unobscured. The helper does not claim to export a native UMG canvas.

For an already-open widget that needs the same target-region output as a path-driven capture, add `--crop-red-box`. The helper prefers a visible red annotation and otherwise crops the selected UMG preview frame; without this flag, the direct command remains a full-editor capture.

## Path-driven capture

For a target file path, use [file-capture.md](file-capture.md) and [file-capture.schema.json](file-capture.schema.json). The `--capture-file` command handles recursive parent-folder navigation, expansion-state detection, selection, double-click activation, render waiting, stable-frame detection, and JSON result reporting.

## 当 `--list` 漏掉编辑器窗口时（2026-09-14 实测）

FlaUI `--list` 在本机**会漏掉正在运行的编辑器**：进程确实存在且窗口 `IsWindowVisible=True`，
但 `--list` 只返回 ChatGPT / 资源管理器 / WinRAR 等无关窗口。同源现象是
High IL 下 `SetForegroundWindow` 对编辑器无效。此时不要据此判定「编辑器未运行」。

绕法（Windows PowerShell + `user32` P/Invoke，不依赖 FlaUI）：

```powershell
# 1) 按 PID 枚举顶层窗口，拿到 UnrealWindow 的 HWND
#    本机典型结果：
#      hwnd=<A> class=UnrealWindow title=UI编辑器
#      hwnd=<B> class=UnrealWindow title=ShadowTrackerExtra (64 位，PCD3D_SM5) <pid>, Compiled: ...
# 2) IsIconic -> ShowWindow(h,9) 还原；ShowWindow(h,5) + SetForegroundWindow(h)
# 3) Start-Sleep -Milliseconds 1500 后 GetWindowRect + Graphics.CopyFromScreen 落 PNG
```

已验证可用的最小实现（`C:\Users\Administrator\AppData\Local\Temp\oasis_shot\` 下有现成脚本
`enum.ps1` / `cap.ps1` 可复用）：`EnumWindows` + `GetWindowThreadProcessId` 过滤 PID →
`SetForegroundWindow` → `CopyFromScreen`。抓 `UI编辑器` 那个 HWND 得到的是完整的 UMG 设计器画面。

注意（本机通用）：**PowerShell 工具不回传 stdout**。任何 PowerShell 步骤的结果都要
`Set-Content`/`Out-File` 落盘，再用 Read 读文件确认；`.ps1` 放在 ASCII 路径下避免编码问题。

## 当 `--list` 能列出编辑器窗口、但画面里**没有目标 UI** 时（2026-09-15 实测）

与上一节相反的另一类失败：窗口**列出来了**，但抓下来的画面里没有要截的 UI。

实测背景：`AuctionDressUI` 已用 MCP `open_editor_for_asset(wbp)` 在设计器打开（返回 True），
`--list` 也返回了该 PID 的编辑器窗口，但两个候选窗口的画面都不是 UMG 设计器：

| 标题 | 尺寸 | 均值亮度 | 白像素占比 | 判断 |
| --- | --- | --- | --- | --- |
| `ShadowTrackerExtra (64 位，PCD3D_SM5) <pid>, Compiled: ...` | 1936×1048 | 73.6 | 7.4% | 关卡编辑器主窗（推断） |
| `调试游戏` | 1000×600 | 251.75 | 95.8% | 空白/占位窗 |

`FlaUI.Core.Capturing.Capture.Element(window).ToFile(...)` 读的是**桌面矩形**，
所以遮挡窗口会一起被抓进来，窗口"存在"不等于"设计器画面可见"。

**判据不要靠肉眼，用像素反查设计 token**（PIL + numpy，确定性）：

```python
a = np.asarray(Image.open(png).convert('RGB')).astype(np.int16)
m = (abs(a[:,:,0]-245)<=14) & (abs(a[:,:,1]-163)<=14) & (abs(a[:,:,2]-59)<=14)  # 金色 #F5A33B
print(int(m.sum()))   # 命中 0 → 目标 UI 不在画面内
```
`abs(...)` 需写成 `np.abs(...)`；`m.sum()==0` 即判定未命中。

处置：**不要**把这类 PNG 当成功截图交付；按 `SKILL.md` 失败策略返回状态码与日志，
并把文件重命名为 `capture_fail_*.png` 留存证据。另外：本机可能同时存在 PIE player 窗口
（标题含 `PIEPlayer_T1_...`）与模态「调试游戏」窗，抓屏前先确认它们已关闭。

## Verification

```powershell
$Path = 'C:\absolute\path\oasis-ui.png'
& powershell -NoProfile -ExecutionPolicy Bypass -File 'C:\Users\Administrator\.codex\skills\oasis-ui-screenshot\scripts\verify_png.ps1' -Path $Path
```

Also inspect the saved PNG with the local image viewer. Confirm that the intended widget or editor view is visible, the image is not blank, and no dialog or selection overlay hides important content.

## Evidence boundary

Local evidence at `D:\知识库\和平精英绿洲起源\wiki\概念\绿洲编辑器UI截图与验证.md` and `D:\知识库\和平精英绿洲起源\raw\知识\通用\来源记录\2026-08-27_FlaUI安装与编辑器截图.md` records the observed FlaUI helper behavior and its unobscured-window limitation. Local official material does not confirm a dedicated Oasis UMG editor-canvas PNG export API.
