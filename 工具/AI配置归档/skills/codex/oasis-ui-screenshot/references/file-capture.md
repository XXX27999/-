# Path-driven UI capture

Use this workflow when the user provides an Oasis asset path and expects the editor to open the asset before capture. It uses the bundled FlaUI helper only; it does not use Windows.Graphics.Capture or an undocumented Oasis export API.

## Command

```powershell
$helper = 'C:\Users\Administrator\.codex\skills\oasis-ui-screenshot\tools\FlaUiCapture'
$title = '<exact title returned by --list>'
dotnet run --project "$helper\FlaUiCapture.csproj" -c Release --no-build -- `
  --process-name 'ShadowTrackerExtraUGCEditor' `
  --title $title `
  --capture-file '/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/CollectibleCodexUI' `
  --output 'D:\知识库\和平精英绿洲起源\Screenshots\CollectibleCodexUI.png' `
  --timeout-ms 15000 `
  --poll-ms 250 `
  --stability-frames 2 `
  --crop-red-box
```

The command prints one JSON result. `Success=true` requires a unique visible target window, every semantic parent folder to be found and safely expanded (or a validated custom-browser result), the target file to be selected and double-clicked, a stable non-loading frame, a detected target-region crop, and a valid non-uniform PNG. `--capture-file` enables `--crop-red-box` by default; the explicit flag documents the requested output mode.

## Input contract

- `captureFile`: required absolute Oasis path in the form `/<ProjectName>/Asset/<folder>/.../<file>`.
- `output`: required absolute `.png` output path.
- `processName` and `title`: use the exact values returned by `--list`; never invent a window identifier.
- `timeoutMs`: total timeout for folder lookup and rendering. Default `15000`.
- `pollMs`: lookup/frame polling interval. Default `250`.
- `stabilityFrames`: consecutive identical PNG frames required after a minimum 500 ms render delay. Default `2`.
- `cropRedBox`: save only the target red-box region. Default `true` for `capture-file`; if no red annotation is present, the helper detects the selected UMG preview's light dashed frame and keeps a small matching margin.

Use `--no-crop-red-box` only when an explicit full-editor capture is required; path-driven captures should keep the default cropped behavior.

The parser accepts Windows separators, an optional leading slash, `.uasset`, and the common `Asset.Asset` suffix. The normalized result always uses `/` and retains the `Asset` folder segment.

## Navigation behavior

1. Parse the path into project, parent folders, and file name.
2. Find each parent folder in the current UI Automation scope from top to bottom.
3. Read `ExpandCollapsePattern` before expanding. An already-expanded folder is not clicked again.
4. Use `TogglePattern` only when it is exposed and reports an off state.
5. If neither state pattern is available and visible descendants do not prove the folder is open, stop with an error instead of blind-clicking.
6. Scroll the file into view, use `SelectionItemPattern` when available, then double-click its measured bounds.
7. Poll UI Automation loading markers and hash fresh FlaUI GDI frames until the view is stable.
8. Capture a fresh frame and save only the red-box interior. A red annotation is preferred; otherwise the selected UMG preview frame is used as the crop boundary. The red outline itself is excluded by a small inset.

### Custom-rendered asset browser

Some Oasis asset panels are drawn on a custom surface and therefore expose neither asset names nor folder expansion patterns to UI Automation. The helper recognizes the current visible browser from a fresh FlaUI frame, selects the `元件` page for the UI asset example, clears and types the exact file name, requires exactly one blue asset result, single-clicks it, verifies the selected row, and double-clicks the same measured point. This is an actual FlaUI interaction path, not a screenshot-only simulation.

The custom fallback searches the currently visible asset page. It does not silently infer or mutate an unexposed parent-folder state. If the requested parent path is not the page currently shown and the search does not yield exactly one result, the helper returns a failure with the current-page diagnostic. Semantic UI Automation trees retain the arbitrary-depth recursive folder behavior described above.

## Result status codes

| Code | Meaning |
| ---: | --- |
| 0 | Captured and verified |
| 2 | Target window is missing or not unique |
| 10 | Asset path is invalid |
| 12 | Parent folder is missing or cannot be safely expanded |
| 13 | Target file is missing |
| 14 | Target cannot be selected or activated |
| 15 | Render timeout or frame never stabilized |
| 16 | PNG signature, dimensions, or non-uniformity check failed |
| 17 | Unexpected navigation/capture error |
| 18 | Target red-box or selected-preview crop region was not detected |

## Examples

### Root-level asset

```powershell
dotnet run --project .\FlaUiCapture.csproj -c Release --no-build -- `
  --process-name 'ShadowTrackerExtraUGCEditor' `
  --title 'ShadowTrackerExtra (64 位，PCD3D_SM5) 23556, Compiled: Jul  8 2026 20:02:25' `
  --capture-file '/IslandAuctionKing/Asset/UI/MainMenu' `
  --output 'C:\captures\MainMenu.png' `
  --crop-red-box
```

### Three-level nested asset

```powershell
dotnet run --project .\FlaUiCapture.csproj -c Release --no-build -- `
  --process-name 'ShadowTrackerExtraUGCEditor' `
  --title 'ShadowTrackerExtra (64 位，PCD3D_SM5) 23556, Compiled: Jul  8 2026 20:02:25' `
  --capture-file '/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/CollectibleCodexUI' `
  --output 'C:\captures\CollectibleCodexUI.png' `
  --timeout-ms 20000 `
  --stability-frames 3 `
  --crop-red-box
```

The title in an actual run must be refreshed with `--list`; the title above is illustrative only.

## Known limitation

Some Oasis editor panels remain custom-rendered and expose no semantic UI Automation names or state patterns. The current helper has a screenshot-validated fallback for the visible asset browser, but it cannot prove an arbitrary hidden parent-folder path through UIA when the editor does not expose that state. It fails closed when the visible page cannot produce one unique result. `Capture.Element(window)` also still requires the target editor window to be visible and unobscured.
