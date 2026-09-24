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

## Verification

```powershell
$Path = 'C:\absolute\path\oasis-ui.png'
& powershell -NoProfile -ExecutionPolicy Bypass -File 'C:\Users\Administrator\.codex\skills\oasis-ui-screenshot\scripts\verify_png.ps1' -Path $Path
```

Also inspect the saved PNG with the local image viewer. Confirm that the intended widget or editor view is visible, the image is not blank, and no dialog or selection overlay hides important content.

## Evidence boundary

Local evidence at `D:\知识库\和平精英绿洲起源\wiki\概念\绿洲编辑器UI截图与验证.md` and `D:\知识库\和平精英绿洲起源\raw\知识\通用\来源记录\2026-08-27_FlaUI安装与编辑器截图.md` records the observed FlaUI helper behavior and its unobscured-window limitation. Local official material does not confirm a dedicated Oasis UMG editor-canvas PNG export API.
