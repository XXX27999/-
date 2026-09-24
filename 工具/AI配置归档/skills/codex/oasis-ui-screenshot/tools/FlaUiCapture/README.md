# FlaUI capture helper

This helper uses the official FlaUI NuGet packages FlaUI.Core and FlaUI.UIA3 to enumerate visible top-level Windows UI Automation elements and capture one selected window to PNG.

## Build

    dotnet restore .\FlaUiCapture.csproj
    dotnet build .\FlaUiCapture.csproj -c Release --no-restore

## Use

    dotnet run --project .\FlaUiCapture.csproj -c Release -- --list
    dotnet run --project .\FlaUiCapture.csproj -c Release -- --process-name ShadowTrackerExtraUGCEditor --title "<exact title from --list>" --output "C:\absolute\path\oasis-ui.png" --activate

The matcher must resolve exactly one window. --activate is optional and brings that returned window to the foreground before capture. FlaUI's capture implementation reads the desktop rectangle with GDI, so the target must be visible and unobscured; this is different from Windows.Graphics.Capture.

## Path-driven file capture

Use `--capture-file` for an absolute Oasis asset path. The helper parses the path, walks each parent folder from top to bottom, checks `ExpandCollapsePattern` or `TogglePattern` before opening a folder, selects and double-clicks the target asset, waits for loading markers to clear and the captured frame to stabilize, then verifies the PNG and prints JSON.

```powershell
dotnet run --project .\FlaUiCapture.csproj -c Release --no-build -- `
  --process-name 'ShadowTrackerExtraUGCEditor' `
  --title '<exact title from --list>' `
  --capture-file '/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/CollectibleCodexUI' `
  --output 'C:\captures\CollectibleCodexUI.png' `
  --timeout-ms 15000 `
  --poll-ms 250 `
  --stability-frames 2
```

The full input schema, result codes, failure policy, and root/nested examples are in `references/file-capture.md` and `references/file-capture.schema.json`.
