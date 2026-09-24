using System.Diagnostics;
using System.Drawing;
using System.Drawing.Imaging;
using System.Security.Cryptography;
using System.Text.Json;
using FlaUI.Core.AutomationElements;
using FlaUI.Core.Capturing;
using FlaUI.Core.Definitions;
using FlaUI.Core.Input;
using FlaUI.Core.WindowsAPI;
using FlaUI.UIA3;

const string defaultProcessName = "ShadowTrackerExtraUGCEditor";

try
{
    var options = CaptureOptions.Parse(args);
    using var automation = new UIA3Automation();
    var windows = EnumerateWindows(automation);

    if (options.ListOnly)
    {
        foreach (var window in windows.OrderBy(item => item.ProcessName).ThenBy(item => item.Title))
        {
            Console.WriteLine($"pid={window.ProcessId} process={window.ProcessName} handle=0x{window.Handle.ToInt64():X} title={window.Title}");
        }

        return 0;
    }

    var selected = SelectWindow(windows, options, defaultProcessName);
    if (selected is null)
    {
        if (!string.IsNullOrWhiteSpace(options.CaptureFilePath))
        {
            var logs = new List<string> { "[error] target window is missing or not unique" };
            var failure = CaptureFileResult.Failed(2, options.CaptureFilePath, options.OutputPath, logs, Stopwatch.GetTimestamp());
            Console.WriteLine(JsonSerializer.Serialize(failure, new JsonSerializerOptions { WriteIndented = true }));
        }

        return 2;
    }

    if (options.DumpNames)
    {
        foreach (var element in selected.Element.FindAllDescendants())
        {
            try
            {
                if (!string.IsNullOrWhiteSpace(element.Name))
                {
                    Console.WriteLine($"name={element.Name} type={element.ControlType} bounds={element.BoundingRectangle}");
                }
            }
            catch
            {
                // Controls can disappear while the custom editor refreshes.
            }
        }

        return 0;
    }

    if (options.ClickX.HasValue && options.ClickY.HasValue)
    {
        Activate(selected.Element);
        var point = new Point(selected.Bounds.X + options.ClickX.Value, selected.Bounds.Y + options.ClickY.Value);
        Mouse.Click(point);
        Console.WriteLine($"clicked={options.ClickX.Value},{options.ClickY.Value}");
        return 0;
    }

    if (options.DoubleClickX.HasValue && options.DoubleClickY.HasValue)
    {
        Activate(selected.Element);
        var point = new Point(selected.Bounds.X + options.DoubleClickX.Value, selected.Bounds.Y + options.DoubleClickY.Value);
        Mouse.DoubleClick(point);
        Console.WriteLine($"double-clicked={options.DoubleClickX.Value},{options.DoubleClickY.Value}");
        return 0;
    }

    if (options.TypeX.HasValue && options.TypeY.HasValue)
    {
        Activate(selected.Element);
        var point = new Point(selected.Bounds.X + options.TypeX.Value, selected.Bounds.Y + options.TypeY.Value);
        Mouse.Click(point);
        Keyboard.TypeSimultaneously(VirtualKeyShort.CONTROL, VirtualKeyShort.KEY_A);
        Keyboard.Type(options.TypeText!);
        Console.WriteLine($"typed-at={options.TypeX.Value},{options.TypeY.Value} text={options.TypeText}");
        return 0;
    }

    if (options.ClearX.HasValue && options.ClearY.HasValue)
    {
        Activate(selected.Element);
        var point = new Point(selected.Bounds.X + options.ClearX.Value, selected.Bounds.Y + options.ClearY.Value);
        Mouse.Click(point);
        Keyboard.TypeSimultaneously(VirtualKeyShort.CONTROL, VirtualKeyShort.KEY_A);
        Keyboard.Press(VirtualKeyShort.BACK);
        Console.WriteLine($"cleared-at={options.ClearX.Value},{options.ClearY.Value}");
        return 0;
    }

    if (options.BackX.HasValue && options.BackY.HasValue)
    {
        Activate(selected.Element);
        var point = new Point(selected.Bounds.X + options.BackX.Value, selected.Bounds.Y + options.BackY.Value);
        Mouse.Click(point);
        Keyboard.Press(VirtualKeyShort.BACK);
        Console.WriteLine($"back-at={options.BackX.Value},{options.BackY.Value}");
        return 0;
    }

    if (!string.IsNullOrWhiteSpace(options.InvokeName))
    {
        var matches = AutomationSearch.FindByName(selected.Element, options.InvokeName).ToArray();
        if (matches.Length != 1)
        {
            Console.Error.WriteLine($"Expected exactly one control named '{options.InvokeName}', found {matches.Length}.");
            return 5;
        }

        try
        {
            matches[0].Patterns.Invoke.Pattern.Invoke();
        }
        catch
        {
            matches[0].Click();
        }

        Console.WriteLine($"invoked={options.InvokeName}");
        return 0;
    }

    if (!string.IsNullOrWhiteSpace(options.CaptureFilePath))
    {
        var result = CaptureFile(selected, options);
        Console.WriteLine(JsonSerializer.Serialize(result, new JsonSerializerOptions { WriteIndented = true }));
        return result.StatusCode;
    }

    Activate(selected.Element);
    Directory.CreateDirectory(Path.GetDirectoryName(options.OutputPath)!);
    var directLogs = new List<string>();
    using var image = Capture.Element(selected.Element);
    if (!TrySaveCapture(image.Bitmap, options, directLogs))
    {
        foreach (var log in directLogs)
        {
            Console.Error.WriteLine(log);
        }

        return 18;
    }

    var file = new FileInfo(options.OutputPath);
    Console.WriteLine($"path={file.FullName}");
    Console.WriteLine($"process={selected.ProcessName}");
    Console.WriteLine($"pid={selected.ProcessId}");
    Console.WriteLine($"title={selected.Title}");
    Console.WriteLine($"bytes={file.Length}");
    Console.WriteLine($"bounds={selected.Bounds.Width}x{selected.Bounds.Height}");
    return file.Length > 0 ? 0 : 4;
}
catch (ArgumentException error)
{
    Console.Error.WriteLine(error.Message);
    return 64;
}
catch (Exception error)
{
    Console.Error.WriteLine($"FlaUI capture failed: {error.GetType().Name}: {error.Message}");
    return 1;
}

static WindowInfo[] EnumerateWindows(UIA3Automation automation)
{
    var desktop = automation.GetDesktop();
    return desktop.FindAllChildren(automation.ConditionFactory.ByControlType(ControlType.Window))
        .Select(element => element.AsWindow())
        .Where(window => window != null && window.IsAvailable)
        .Cast<Window>()
        .Select(WindowInfo.TryFrom)
        .Where(info => info != null)
        .Cast<WindowInfo>()
        .Where(info => info.Bounds.Width > 0 && info.Bounds.Height > 0)
        .ToArray();
}

static WindowInfo? SelectWindow(WindowInfo[] windows, CaptureOptions options, string defaultProcessName)
{
    var candidates = windows.AsEnumerable();
    if (!string.IsNullOrWhiteSpace(options.ProcessName))
    {
        candidates = candidates.Where(window => string.Equals(window.ProcessName, options.ProcessName, StringComparison.OrdinalIgnoreCase));
    }

    if (!string.IsNullOrWhiteSpace(options.Title))
    {
        candidates = candidates.Where(window => string.Equals(window.Title, options.Title, StringComparison.Ordinal));
    }

    if (string.IsNullOrWhiteSpace(options.ProcessName) && string.IsNullOrWhiteSpace(options.Title))
    {
        candidates = candidates.Where(window => string.Equals(window.ProcessName, defaultProcessName, StringComparison.OrdinalIgnoreCase));
    }

    var selected = candidates.ToArray();
    if (selected.Length == 1)
    {
        return selected[0];
    }

    Console.Error.WriteLine($"Expected exactly one target window, found {selected.Length}.");
    Console.Error.WriteLine("Use --list, then pass --process-name and --title with values from that output.");
    return null;
}

static CaptureFileResult CaptureFile(WindowInfo window, CaptureOptions options)
{
    // 输入是已唯一匹配的编辑器窗口和完整 Oasis 资产路径；所有失败都返回可机器读取的状态码与日志。
    var logs = new List<string>();
    var started = Stopwatch.GetTimestamp();
    try
    {
        var assetPath = AssetPath.Parse(options.CaptureFilePath!);
        logs.Add($"[path] project={assetPath.ProjectName} folders={string.Join("/", assetPath.FolderSegments)} file={assetPath.FileName}");
        Activate(window.Element);

        var navigator = new FileHierarchyNavigator(window.Element, options, logs);
        if (!navigator.Navigate(assetPath))
        {
            return CaptureFileResult.Failed(navigator.FailureCode, assetPath.Normalized, options.OutputPath, logs, started);
        }

        if (!navigator.CustomTargetActivated)
        {
            var target = navigator.Target;
            if (target is null)
            {
                logs.Add($"[error] target file not found: {assetPath.FileName}");
                return CaptureFileResult.Failed(13, assetPath.Normalized, options.OutputPath, logs, started);
            }

            if (!SelectAndActivate(target, logs))
            {
                return CaptureFileResult.Failed(14, assetPath.Normalized, options.OutputPath, logs, started);
            }
        }
        else
        {
            logs.Add("[activate] custom-rendered asset result was selected and double-clicked with FlaUI");
        }

        MovePointerAway(window.Element);
        logs.Add("[capture] moved FlaUI pointer away from the selected asset to dismiss hover UI");
        var waiter = new RenderWaiter(window.Element, options, logs);
        if (!waiter.WaitForReady(assetPath.FileName))
        {
            return CaptureFileResult.Failed(15, assetPath.Normalized, options.OutputPath, logs, started);
        }

        Directory.CreateDirectory(Path.GetDirectoryName(options.OutputPath)!);
        using (var image = Capture.Element(window.Element))
        {
            if (!TrySaveCapture(image.Bitmap, options, logs))
            {
                return CaptureFileResult.Failed(18, assetPath.Normalized, options.OutputPath, logs, started);
            }
        }

        var verification = PngVerification.Verify(options.OutputPath);
        logs.Add($"[capture] path={verification.Path} bytes={verification.Bytes} size={verification.Width}x{verification.Height} nonUniform={verification.NonUniformPixels}");
        if (!verification.Valid)
        {
            logs.Add($"[error] PNG verification failed: {verification.Error}");
            return CaptureFileResult.Failed(16, assetPath.Normalized, options.OutputPath, logs, started);
        }

        logs.Add("[done] selected asset rendered and captured with FlaUI GDI");
        return CaptureFileResult.Ok(assetPath.Normalized, options.OutputPath, verification, logs, started);
    }
    catch (AssetPathException error)
    {
        logs.Add($"[error] invalid asset path: {error.Message}");
        return CaptureFileResult.Failed(10, options.CaptureFilePath!, options.OutputPath, logs, started);
    }
    catch (Exception error)
    {
        logs.Add($"[error] {error.GetType().Name}: {error.Message}");
        return CaptureFileResult.Failed(17, options.CaptureFilePath!, options.OutputPath, logs, started);
    }
}

static bool TrySaveCapture(Bitmap source, CaptureOptions options, List<string> logs)
{
    // 路径驱动截图默认只保存目标红框内部；直接截图仍可显式使用 --crop-red-box。
    if (!options.CropRedBox)
    {
        source.Save(options.OutputPath, ImageFormat.Png);
        return true;
    }

    if (!UiCropper.TryFindTargetRegion(source, out var crop, out var mode, out var error))
    {
        logs.Add($"[error] target crop region was not found: {error}");
        return false;
    }

    using var cropped = source.Clone(crop, PixelFormat.Format32bppArgb);
    cropped.Save(options.OutputPath, ImageFormat.Png);
    logs.Add($"[crop] mode={mode} source={source.Width}x{source.Height} region={crop.X},{crop.Y},{crop.Width}x{crop.Height}");
    return true;
}

static bool SelectAndActivate(AutomationElement target, List<string> logs)
{
    // 先选中再双击，避免只获得焦点却没有触发编辑器的资产加载动作。
    try
    {
        ScrollIntoView(target);
        if (target.Patterns.SelectionItem.IsSupported)
        {
            target.Patterns.SelectionItem.Pattern.Select();
            logs.Add($"[select] selected '{target.Name}' through SelectionItemPattern");
        }
        else
        {
            target.Click();
            logs.Add($"[select] clicked '{target.Name}' because SelectionItemPattern is unavailable");
        }

        var bounds = target.BoundingRectangle;
        if (bounds.Width <= 0 || bounds.Height <= 0)
        {
            logs.Add("[error] target file has no visible bounds");
            return false;
        }

        Mouse.DoubleClick(new Point(bounds.X + bounds.Width / 2, bounds.Y + bounds.Height / 2));
        logs.Add("[activate] double-clicked target file to render its editor view");
        return true;
    }
    catch (Exception error)
    {
        logs.Add($"[error] target activation failed: {error.GetType().Name}: {error.Message}");
        return false;
    }
}

static void Activate(Window window)
{
    window.SetForeground();
    Thread.Sleep(250);
}

static void MovePointerAway(AutomationElement window)
{
    // 鼠标停留在自绘资产行会触发路径 tooltip；移到工具栏空白区后再开始稳定帧检测。
    var bounds = window.BoundingRectangle;
    var x = bounds.X + Math.Max(1, bounds.Width / 2);
    var y = bounds.Y + Math.Clamp(90, 1, Math.Max(1, bounds.Height - 1));
    Mouse.MoveTo(new Point(x, y));
    Thread.Sleep(150);
}

static void ScrollIntoView(AutomationElement element)
{
    if (element.Patterns.ScrollItem.IsSupported)
    {
        element.Patterns.ScrollItem.Pattern.ScrollIntoView();
        Thread.Sleep(100);
    }
}

static class AutomationSearch
{
    public static IEnumerable<AutomationElement> FindByName(AutomationElement root, string name)
    {
        if (ReadName(root).Equals(name, StringComparison.OrdinalIgnoreCase))
        {
            yield return root;
        }

        foreach (var element in root.FindAllDescendants())
        {
            if (ReadName(element).Equals(name, StringComparison.OrdinalIgnoreCase))
            {
                yield return element;
            }
        }
    }

    public static IEnumerable<AutomationElement> FindFileSystemCandidates(AutomationElement root, string name)
    {
        var named = FindByName(root, name).ToArray();
        var preferred = named.Where(element => element.ControlType is ControlType.TreeItem or ControlType.ListItem or ControlType.DataItem or ControlType.Button or ControlType.Custom).ToArray();
        return preferred.Length > 0 ? preferred : named;
    }

    private static string ReadName(AutomationElement element)
    {
        try
        {
            return element.Name ?? string.Empty;
        }
        catch
        {
            // Ignore controls that disappear during a refresh.
            return string.Empty;
        }
    }
}

sealed class FileHierarchyNavigator
{
    private readonly AutomationElement window;
    private readonly CaptureOptions options;
    private readonly List<string> logs;

    public FileHierarchyNavigator(AutomationElement window, CaptureOptions options, List<string> logs)
    {
        this.window = window;
        this.options = options;
        this.logs = logs;
    }

    public AutomationElement? Target { get; private set; }
    public bool CustomTargetActivated { get; private set; }
    public int FailureCode { get; private set; } = 12;

    public bool Navigate(AssetPath path)
    {
        // Oasis 当前资产树是自绘控件时，UIA 不会返回 Asset、文件夹或文件节点；先走经过截图验证的 FlaUI 交互兜底。
        if (CustomAssetBrowserNavigator.TryDetect(window, logs, out var geometry))
        {
            var customNavigator = new CustomAssetBrowserNavigator(window, options, logs, geometry);
            if (!customNavigator.Navigate(path))
            {
                FailureCode = customNavigator.FailureCode;
                return false;
            }

            CustomTargetActivated = true;
            return true;
        }

        // 每一层都重新在当前 UIA scope 内查找，支持任意深度且不会依赖固定坐标。
        AutomationElement scope = window;
        var traversed = new List<string>();
        foreach (var segment in path.FolderSegments)
        {
            traversed.Add(segment);
            var folder = WaitForElement(() => AutomationSearch.FindFileSystemCandidates(scope, segment).FirstOrDefault(), $"folder '{segment}'");
            if (folder is null)
            {
                FailureCode = 12;
                logs.Add($"[error] folder not found at '{string.Join("/", traversed)}'");
                return false;
            }

            if (!EnsureExpanded(folder, segment))
            {
                return false;
            }

            scope = folder;
        }

        Target = WaitForElement(() => AutomationSearch.FindFileSystemCandidates(scope, path.FileName).FirstOrDefault() ?? AutomationSearch.FindFileSystemCandidates(window, path.FileName).FirstOrDefault(), $"file '{path.FileName}'");
        if (Target is null)
        {
            FailureCode = 13;
            logs.Add($"[error] file not found: {path.FileName}");
            return false;
        }

        logs.Add($"[locate] target visible: {Target.Name} bounds={Target.BoundingRectangle}");
        return true;
    }

    private bool EnsureExpanded(AutomationElement folder, string segment)
    {
        // 读取状态后再展开，保护已展开目录不被第二次点击折叠。
        try
        {
            if (folder.Patterns.ExpandCollapse.IsSupported)
            {
                var state = folder.Patterns.ExpandCollapse.Pattern.ExpandCollapseState.ToString();
                if (state.Equals("Expanded", StringComparison.OrdinalIgnoreCase))
                {
                    logs.Add($"[expand] '{segment}' already expanded");
                    return true;
                }

                folder.Patterns.ExpandCollapse.Pattern.Expand();
                logs.Add($"[expand] expanded '{segment}' with ExpandCollapsePattern");
                return WaitForElement(() => folder.FindAllDescendants().FirstOrDefault(), $"children of '{segment}'") is not null;
            }

            if (folder.Patterns.Toggle.IsSupported)
            {
                var state = folder.Patterns.Toggle.Pattern.ToggleState.ToString();
                if (state.Equals("On", StringComparison.OrdinalIgnoreCase))
                {
                    logs.Add($"[expand] '{segment}' already expanded through TogglePattern");
                    return true;
                }

                folder.Patterns.Toggle.Pattern.Toggle();
                logs.Add($"[expand] toggled '{segment}' open with TogglePattern");
                return true;
            }

            var hasVisibleChildren = folder.FindAllDescendants().Any(child => child.BoundingRectangle.Width > 0 && child.BoundingRectangle.Height > 0);
            if (hasVisibleChildren)
            {
                logs.Add($"[expand] '{segment}' treated as expanded because visible descendants exist");
                return true;
            }

            logs.Add($"[error] '{segment}' exposes neither ExpandCollapsePattern nor TogglePattern; refusing blind toggle");
            return false;
        }
        catch (Exception error)
        {
            logs.Add($"[error] cannot inspect folder '{segment}': {error.GetType().Name}: {error.Message}");
            return false;
        }
    }

    private AutomationElement? WaitForElement(Func<AutomationElement?> probe, string description)
    {
        var deadline = DateTime.UtcNow.AddMilliseconds(options.TimeoutMs);
        while (DateTime.UtcNow < deadline)
        {
            var element = probe();
            if (element is not null)
            {
                return element;
            }

            Thread.Sleep(options.PollMs);
        }

        logs.Add($"[timeout] {description} was not visible within {options.TimeoutMs}ms");
        return null;
    }
}

sealed class CustomAssetBrowserNavigator
{
    private readonly AutomationElement window;
    private readonly CaptureOptions options;
    private readonly List<string> logs;
    private readonly CustomAssetBrowserGeometry geometry;

    public CustomAssetBrowserNavigator(AutomationElement window, CaptureOptions options, List<string> logs, CustomAssetBrowserGeometry geometry)
    {
        this.window = window;
        this.options = options;
        this.logs = logs;
        this.geometry = geometry;
    }

    public int FailureCode { get; private set; } = 12;

    public static bool TryDetect(AutomationElement window, List<string> logs, out CustomAssetBrowserGeometry geometry)
    {
        geometry = null!;
        try
        {
            using var image = Capture.Element(window);
            if (!CustomAssetBrowserGeometry.TryCreate(image.Bitmap, out geometry))
            {
                return false;
            }

            logs.Add($"[detect] custom-rendered Oasis asset browser detected size={image.Bitmap.Width}x{image.Bitmap.Height}");
            return true;
        }
        catch (Exception error)
        {
            logs.Add($"[detect] custom asset browser probe failed: {error.GetType().Name}: {error.Message}");
            return false;
        }
    }

    public bool Navigate(AssetPath path)
    {
        // WidgetLayout 使用“界面布局”页，其余 UI 资产使用“元件”页；点击页签是幂等操作，已选中时不会重复切换。
        var useElementTab = !path.FolderSegments.Any(segment => segment.Equals("WidgetLayout", StringComparison.OrdinalIgnoreCase));
        try
        {
            logs.Add($"[custom] target page={(useElementTab ? "元件" : "界面布局")} expectedParent=/{path.ProjectName}/{string.Join('/', path.FolderSegments)}");
            if (!EnsureTab(useElementTab))
            {
                FailureCode = 14;
                return false;
            }

            ClearSearch();
            TypeSearch(path.FileName);
            if (!WaitForFrame(frame => geometry.CountVisibleResultRows(frame) == 1, $"unique result '{path.FileName}'"))
            {
                using var image = Capture.Element(window);
                var visibleRows = geometry.CountVisibleResultRows(image.Bitmap);
                logs.Add($"[error] custom asset search did not produce exactly one result for '{path.FileName}', visibleRows={visibleRows}; current browser folder cannot be changed through exposed FlaUI state");
                FailureCode = 13;
                return false;
            }

            var targetPoint = ToScreenPoint(geometry.FirstResultPoint);
            Mouse.Click(targetPoint);
            logs.Add($"[select] clicked unique custom asset result '{path.FileName}' at relative={geometry.FirstResultPoint.X},{geometry.FirstResultPoint.Y}");
            if (!WaitForFrame(frame => geometry.IsOnlyResultSelected(frame), $"selected result '{path.FileName}'"))
            {
                FailureCode = 14;
                return false;
            }

            Mouse.DoubleClick(targetPoint);
            logs.Add($"[activate] double-clicked custom asset result '{path.FileName}' at relative={geometry.FirstResultPoint.X},{geometry.FirstResultPoint.Y}");
            if (!WaitForEditor(path.FileName))
            {
                FailureCode = 15;
                return false;
            }

            return true;
        }
        catch (Exception error)
        {
            logs.Add($"[error] custom asset navigation failed: {error.GetType().Name}: {error.Message}");
            FailureCode = 17;
            return false;
        }
    }

    private bool EnsureTab(bool useElementTab)
    {
        if (WaitForFrame(frame => geometry.IsTabSelected(frame, useElementTab), $"{(useElementTab ? "元件" : "界面布局")} tab"))
        {
            logs.Add($"[tab] {(useElementTab ? "元件" : "界面布局")} tab already selected");
            return true;
        }

        Mouse.Click(ToScreenPoint(useElementTab ? geometry.ElementsTabPoint : geometry.InterfaceLayoutTabPoint));
        logs.Add($"[tab] clicked {(useElementTab ? "元件" : "界面布局")} tab with FlaUI");
        return WaitForFrame(frame => geometry.IsTabSelected(frame, useElementTab), $"{(useElementTab ? "元件" : "界面布局")} tab after click");
    }

    private void ClearSearch()
    {
        Mouse.Click(ToScreenPoint(geometry.SearchPoint));
        Keyboard.TypeSimultaneously(VirtualKeyShort.CONTROL, VirtualKeyShort.KEY_A);
        Keyboard.Press(VirtualKeyShort.BACK);
        logs.Add("[search] cleared custom asset search box with FlaUI keyboard input");
    }

    private void TypeSearch(string fileName)
    {
        Mouse.Click(ToScreenPoint(geometry.SearchPoint));
        Keyboard.TypeSimultaneously(VirtualKeyShort.CONTROL, VirtualKeyShort.KEY_A);
        Keyboard.Type(fileName);
        logs.Add($"[search] typed exact custom asset file name '{fileName}' with FlaUI keyboard input");
    }

    private bool WaitForEditor(string fileName)
    {
        var deadline = DateTime.UtcNow.AddMilliseconds(options.TimeoutMs);
        var minimumReadyAt = DateTime.UtcNow.AddMilliseconds(Math.Min(500, options.TimeoutMs));
        while (DateTime.UtcNow < deadline)
        {
            var hasNameMarker = HasEditorNameMarker(fileName);
            var hasEditorSurface = false;
            try
            {
                using var image = Capture.Element(window);
                hasEditorSurface = geometry.HasEditorSurface(image.Bitmap);
            }
            catch
            {
                // The editor can rebuild the canvas while the asset is opening; the next poll retries capture.
            }

            if (DateTime.UtcNow >= minimumReadyAt && (hasNameMarker || hasEditorSurface))
            {
                logs.Add($"[wait] custom editor view visible for '{fileName}', nameMarker={hasNameMarker} surface={hasEditorSurface}");
                return true;
            }

            Thread.Sleep(options.PollMs);
        }

        logs.Add($"[timeout] custom editor view for '{fileName}' was not visible within {options.TimeoutMs}ms");
        return false;
    }

    private bool HasEditorNameMarker(string fileName)
    {
        try
        {
            return window.FindAllDescendants().Any(element =>
            {
                try
                {
                    return (element.Name ?? string.Empty).Contains(fileName, StringComparison.OrdinalIgnoreCase);
                }
                catch
                {
                    return false;
                }
            });
        }
        catch
        {
            return false;
        }
    }

    private bool WaitForFrame(Func<Bitmap, bool> predicate, string description)
    {
        var deadline = DateTime.UtcNow.AddMilliseconds(options.TimeoutMs);
        while (DateTime.UtcNow < deadline)
        {
            try
            {
                using var image = Capture.Element(window);
                if (predicate(image.Bitmap))
                {
                    return true;
                }
            }
            catch
            {
                // Retry transient capture failures while the custom editor is refreshing.
            }

            Thread.Sleep(options.PollMs);
        }

        logs.Add($"[timeout] {description} was not confirmed by a fresh FlaUI frame within {options.TimeoutMs}ms");
        return false;
    }

    private Point ToScreenPoint(Point relativePoint)
    {
        var bounds = window.BoundingRectangle;
        return new Point(bounds.X + relativePoint.X, bounds.Y + relativePoint.Y);
    }
}

sealed class CustomAssetBrowserGeometry
{
    private const int ReferenceWidth = 1936;
    private const int ReferenceHeight = 1056;

    private CustomAssetBrowserGeometry(int width, int height, int searchLeft, int searchRight)
    {
        InterfaceLayoutTabPoint = ScalePoint(width, height, 100, 60);
        ElementsTabPoint = ScalePoint(width, height, 100, 96);
        var searchY = ScalePoint(width, height, 0, 54).Y;
        var panelRight = Math.Min(width - 1, searchRight + ScaleValue(width, ReferenceWidth, 115));
        SearchPoint = new Point((searchLeft + searchRight) / 2, searchY);
        FirstResultPoint = new Point(searchLeft + ScaleValue(width, ReferenceWidth, 145), ScalePoint(width, height, 0, 134).Y);
        ResultIconRegion = new Rectangle(searchLeft + ScaleValue(width, ReferenceWidth, 13), ScalePoint(width, height, 0, 112).Y, ScaleValue(width, ReferenceWidth, 58), ScaleValue(height, ReferenceHeight, 42));
        ResultRowRegion = new Rectangle(searchLeft, ScalePoint(width, height, 0, 112).Y, Math.Max(1, panelRight - searchLeft), ScaleValue(height, ReferenceHeight, 45));
        EditorSurfaceRegion = ScaleRectangle(width, height, 1040, 112, 600, 650);
        RowHeight = Math.Max(1, ScaleValue(height, ReferenceHeight, 44));
        SelectionSamplePoint = new Point(Math.Max(searchLeft, panelRight - ScaleValue(width, ReferenceWidth, 20)), FirstResultPoint.Y);
    }

    public Point InterfaceLayoutTabPoint { get; }
    public Point ElementsTabPoint { get; }
    public Point SearchPoint { get; }
    public Point FirstResultPoint { get; }
    public Rectangle ResultIconRegion { get; }
    public Rectangle ResultRowRegion { get; }
    public Rectangle EditorSurfaceRegion { get; }
    public int RowHeight { get; }
    public Point SelectionSamplePoint { get; }

    public static bool TryCreate(Bitmap bitmap, out CustomAssetBrowserGeometry geometry)
    {
        geometry = null!;
        if (bitmap.Width < 1000 || bitmap.Height < 600)
        {
            return false;
        }

        if (!TryFindSearchBox(bitmap, out var searchLeft, out var searchRight))
        {
            return false;
        }

        var interfaceBand = ReadPixel(bitmap, ScalePoint(bitmap.Width, bitmap.Height, 150, 60));
        var elementsBand = ReadPixel(bitmap, ScalePoint(bitmap.Width, bitmap.Height, 150, 96));
        if (!IsEditorBand(interfaceBand) && !IsEditorBand(elementsBand))
        {
            return false;
        }

        geometry = new CustomAssetBrowserGeometry(bitmap.Width, bitmap.Height, searchLeft, searchRight);
        return true;
    }

    public bool IsTabSelected(Bitmap bitmap, bool useElementTab)
    {
        var selectedPoint = useElementTab ? ElementsTabPoint : InterfaceLayoutTabPoint;
        var otherPoint = useElementTab ? InterfaceLayoutTabPoint : ElementsTabPoint;
        return IsSelectedBand(ReadPixel(bitmap, selectedPoint))
            && !IsSelectedBand(ReadPixel(bitmap, otherPoint));
    }

    public int CountVisibleResultRows(Bitmap bitmap)
    {
        var count = 0;
        for (var row = 0; row < 20; row++)
        {
            var centerY = FirstResultPoint.Y + row * RowHeight;
            var region = new Rectangle(ResultIconRegion.X, centerY - ResultIconRegion.Height / 2, ResultIconRegion.Width, ResultIconRegion.Height);
            if (CountPixels(bitmap, region, IsAssetIconBlue) >= 12)
            {
                count++;
            }
        }

        return count;
    }

    public bool IsOnlyResultSelected(Bitmap bitmap)
    {
        if (CountVisibleResultRows(bitmap) != 1)
        {
            return false;
        }

        return IsSelectedBand(ReadPixel(bitmap, SelectionSamplePoint));
    }

    public bool HasEditorSurface(Bitmap bitmap)
    {
        var region = ScaleRectangle(bitmap.Width, bitmap.Height, 1040, 112, 600, 650);
        var signal = CountPixels(bitmap, region, color => color.R > 20 || color.G > 20 || color.B > 20);
        return signal >= Math.Max(100, region.Width * region.Height / 100);
    }

    private static Point ScalePoint(int width, int height, int x, int y)
        => new(Math.Clamp((int)Math.Round(x * width / (double)ReferenceWidth), 0, Math.Max(0, width - 1)), Math.Clamp((int)Math.Round(y * height / (double)ReferenceHeight), 0, Math.Max(0, height - 1)));

    private static Rectangle ScaleRectangle(int width, int height, int x, int y, int rectangleWidth, int rectangleHeight)
    {
        var topLeft = ScalePoint(width, height, x, y);
        var bottomRight = ScalePoint(width, height, x + rectangleWidth, y + rectangleHeight);
        return new Rectangle(topLeft.X, topLeft.Y, Math.Max(1, bottomRight.X - topLeft.X), Math.Max(1, bottomRight.Y - topLeft.Y));
    }

    private static int ScaleValue(int actualDimension, int referenceDimension, int referenceValue)
        => (int)Math.Round(referenceValue * actualDimension / (double)referenceDimension);

    private static bool TryFindSearchBox(Bitmap bitmap, out int searchLeft, out int searchRight)
    {
        searchLeft = 0;
        searchRight = 0;
        var firstCandidate = bitmap.Width;
        var lastCandidate = -1;
        var scanLeft = Math.Max(0, ScaleValue(bitmap.Width, ReferenceWidth, 180));
        var scanRight = Math.Min(bitmap.Width, ScaleValue(bitmap.Width, ReferenceWidth, 680));
        for (var x = scanLeft; x < scanRight; x++)
        {
            var lightPixels = 0;
            for (var y = ScaleValue(bitmap.Height, ReferenceHeight, 46); y <= ScaleValue(bitmap.Height, ReferenceHeight, 66); y += 2)
            {
                var color = bitmap.GetPixel(x, Math.Min(bitmap.Height - 1, y));
                if (color.R >= 180 && color.G >= 180 && color.B >= 180 && ColorDistance(color, Color.White) < 90)
                {
                    lightPixels++;
                }
            }

            if (lightPixels < 5)
            {
                continue;
            }

            firstCandidate = Math.Min(firstCandidate, x);
            lastCandidate = Math.Max(lastCandidate, x);
        }

        if (lastCandidate < firstCandidate || lastCandidate - firstCandidate < ScaleValue(bitmap.Width, ReferenceWidth, 120))
        {
            return false;
        }

        searchLeft = Math.Max(0, firstCandidate - ScaleValue(bitmap.Width, ReferenceWidth, 4));
        searchRight = Math.Min(bitmap.Width - 1, lastCandidate + ScaleValue(bitmap.Width, ReferenceWidth, 2));
        return searchRight > searchLeft;
    }

    private static Color ReadPixel(Bitmap bitmap, Point point)
        => bitmap.GetPixel(Math.Clamp(point.X, 0, bitmap.Width - 1), Math.Clamp(point.Y, 0, bitmap.Height - 1));

    private static int CountPixels(Bitmap bitmap, Rectangle region, Func<Color, bool> predicate)
    {
        var left = Math.Clamp(region.Left, 0, bitmap.Width - 1);
        var top = Math.Clamp(region.Top, 0, bitmap.Height - 1);
        var right = Math.Clamp(region.Right, left + 1, bitmap.Width);
        var bottom = Math.Clamp(region.Bottom, top + 1, bitmap.Height);
        var count = 0;
        for (var y = top; y < bottom; y += 2)
        {
            for (var x = left; x < right; x += 2)
            {
                if (predicate(bitmap.GetPixel(x, y)))
                {
                    count++;
                }
            }
        }

        return count;
    }

    private static bool IsAssetIconBlue(Color color)
        => color.B >= 100 && color.B - color.R >= 35 && color.B - color.G >= 20;

    private static bool IsEditorBand(Color color)
        => color.R < 110 && color.G < 115 && color.B < 120 && Math.Abs(color.R - color.G) <= 12;

    private static bool IsSelectedBand(Color color)
        => color.R >= 45 && color.R <= 100 && Math.Abs(color.R - color.G) <= 5 && Math.Abs(color.G - color.B) <= 5;

    private static int ColorDistance(Color left, Color right)
        => Math.Abs(left.R - right.R) + Math.Abs(left.G - right.G) + Math.Abs(left.B - right.B);
}

static class UiCropper
{
    // 红框通常来自用户标注；编辑器本身没有红框时，退回到已选 UMG 预览的浅色虚线边界。
    public static bool TryFindTargetRegion(Bitmap bitmap, out Rectangle crop, out string mode, out string error)
    {
        crop = Rectangle.Empty;
        mode = string.Empty;
        error = string.Empty;

        if (TryFindRedBorder(bitmap, out var redBorder))
        {
            crop = Inset(redBorder, 3, 3, 3, 3, bitmap.Size);
            mode = "red-border-interior";
            return crop.Width > 0 && crop.Height > 0;
        }

        if (TryFindSelectionFrame(bitmap, out var selectionFrame))
        {
            // 没有红色标注时保留少量画布边距，使输出与用户标注的红框范围一致。
            crop = Expand(selectionFrame, 12, 13, 12, 20, bitmap.Size);
            mode = "selection-frame-fallback";
            return crop.Width > 0 && crop.Height > 0;
        }

        error = "no red annotation or selected UMG preview frame was detected in the fresh FlaUI capture";
        return false;
    }

    private static bool TryFindRedBorder(Bitmap bitmap, out Rectangle border)
    {
        border = Rectangle.Empty;
        var scan = new Rectangle(
            Math.Clamp((int)Math.Round(bitmap.Width * 0.35), 0, bitmap.Width - 1),
            Math.Clamp((int)Math.Round(bitmap.Height * 0.10), 0, bitmap.Height - 1),
            Math.Max(1, Math.Min(bitmap.Width, (int)Math.Round(bitmap.Width * 0.55))),
            Math.Max(1, Math.Min(bitmap.Height, (int)Math.Round(bitmap.Height * 0.75))));
        scan = ClampRectangle(scan, bitmap.Size);

        var horizontal = FindLineClusters(bitmap, scan, true, IsRedBorderPixel, Math.Max(80, scan.Width / 4));
        var vertical = FindLineClusters(bitmap, scan, false, IsRedBorderPixel, Math.Max(60, scan.Height / 4));
        if (!TryFindRectangle(horizontal, vertical, bitmap.Size, 200, 100, 1.20, 2.60, out border))
        {
            border = Rectangle.Empty;
            return false;
        }

        return true;
    }

    private static bool TryFindSelectionFrame(Bitmap bitmap, out Rectangle frame)
    {
        frame = Rectangle.Empty;
        var scan = new Rectangle(
            Math.Clamp((int)Math.Round(bitmap.Width * 0.45), 0, bitmap.Width - 1),
            Math.Clamp((int)Math.Round(bitmap.Height * 0.20), 0, bitmap.Height - 1),
            Math.Max(1, Math.Min(bitmap.Width, (int)Math.Round(bitmap.Width * 0.45))),
            Math.Max(1, Math.Min(bitmap.Height, (int)Math.Round(bitmap.Height * 0.52))));
        scan = ClampRectangle(scan, bitmap.Size);

        var horizontal = FindLineClusters(bitmap, scan, true, IsSelectionFramePixel, Math.Max(120, scan.Width / 4));
        // 虚线竖边的亮像素密度低于横边，但仍需高于普通网格线，使用约五分之一作为门槛。
        var vertical = FindLineClusters(bitmap, scan, false, IsSelectionFramePixel, Math.Max(60, scan.Height / 5));
        return TryFindRectangle(horizontal, vertical, bitmap.Size, 250, 140, 1.20, 2.60, out frame);
    }

    private static List<LineCluster> FindLineClusters(
        Bitmap bitmap,
        Rectangle scan,
        bool horizontal,
        Func<Color, bool> predicate,
        int minimumStrength)
    {
        var candidates = new List<LineEvidence>();
        var coordinateStart = horizontal ? scan.Top : scan.Left;
        var coordinateEnd = horizontal ? scan.Bottom : scan.Right;
        var spanStart = horizontal ? scan.Left : scan.Top;
        var spanEnd = horizontal ? scan.Right : scan.Bottom;

        for (var coordinate = coordinateStart; coordinate < coordinateEnd; coordinate++)
        {
            var points = new List<int>();
            for (var span = spanStart; span < spanEnd; span++)
            {
                var point = horizontal ? new Point(span, coordinate) : new Point(coordinate, span);
                if (predicate(bitmap.GetPixel(point.X, point.Y)))
                {
                    points.Add(span);
                }
            }

            if (points.Count < minimumStrength)
            {
                continue;
            }

            points.Sort();
            var trim = Math.Max(0, (int)Math.Floor(points.Count * 0.05));
            candidates.Add(new LineEvidence(
                coordinate,
                points[Math.Min(trim, points.Count - 1)],
                points[Math.Max(trim, points.Count - trim - 1)],
                points.Count));
        }

        var clusters = new List<LineCluster>();
        foreach (var candidate in candidates)
        {
            if (clusters.Count == 0 || candidate.Coordinate - clusters[^1].LastCoordinate > 3)
            {
                clusters.Add(new LineCluster(candidate.Coordinate, candidate.Coordinate, candidate.Start, candidate.End, candidate.Strength));
                continue;
            }

            var previous = clusters[^1];
            clusters[^1] = new LineCluster(
                previous.FirstCoordinate,
                candidate.Coordinate,
                Math.Min(previous.Start, candidate.Start),
                Math.Max(previous.End, candidate.End),
                previous.Strength + candidate.Strength);
        }

        return clusters;
    }

    private static bool TryFindRectangle(
        IReadOnlyList<LineCluster> horizontal,
        IReadOnlyList<LineCluster> vertical,
        Size bitmapSize,
        int minimumWidth,
        int minimumHeight,
        double minimumAspect,
        double maximumAspect,
        out Rectangle rectangle)
    {
        rectangle = Rectangle.Empty;
        var bestScore = double.MinValue;

        for (var topIndex = 0; topIndex < horizontal.Count; topIndex++)
        {
            for (var bottomIndex = topIndex + 1; bottomIndex < horizontal.Count; bottomIndex++)
            {
                var top = horizontal[topIndex];
                var bottom = horizontal[bottomIndex];
                var topY = top.FirstCoordinate;
                var bottomY = bottom.LastCoordinate;
                var height = bottomY - topY;
                if (height < minimumHeight || height > bitmapSize.Height * 0.55)
                {
                    continue;
                }

                for (var leftIndex = 0; leftIndex < vertical.Count; leftIndex++)
                {
                    for (var rightIndex = leftIndex + 1; rightIndex < vertical.Count; rightIndex++)
                    {
                        var left = vertical[leftIndex];
                        var right = vertical[rightIndex];
                        var leftX = left.FirstCoordinate;
                        var rightX = right.LastCoordinate;
                        var width = rightX - leftX;
                        var aspect = width / (double)height;
                        if (width < minimumWidth || width > bitmapSize.Width * 0.60 || aspect < minimumAspect || aspect > maximumAspect)
                        {
                            continue;
                        }

                        var horizontalAlignment =
                            Math.Abs(top.Start - leftX)
                            + Math.Abs(top.End - rightX)
                            + Math.Abs(bottom.Start - leftX)
                            + Math.Abs(bottom.End - rightX);
                        var verticalAlignment =
                            Math.Abs(left.Start - topY)
                            + Math.Abs(left.End - bottomY)
                            + Math.Abs(right.Start - topY)
                            + Math.Abs(right.End - bottomY);
                        var aspectPenalty = Math.Abs(aspect - 1.75) * 80;
                        var score = top.Strength + bottom.Strength + left.Strength + right.Strength
                            - horizontalAlignment * 2.0
                            - verticalAlignment * 1.5
                            - aspectPenalty;
                        if (score <= bestScore)
                        {
                            continue;
                        }

                        bestScore = score;
                        rectangle = Rectangle.FromLTRB(leftX, topY, rightX + 1, bottomY + 1);
                    }
                }
            }
        }

        return !rectangle.IsEmpty;
    }

    private static Rectangle Inset(Rectangle rectangle, int left, int top, int right, int bottom, Size bounds)
        => ClampRectangle(Rectangle.FromLTRB(rectangle.Left + left, rectangle.Top + top, rectangle.Right - right, rectangle.Bottom - bottom), bounds);

    private static Rectangle Expand(Rectangle rectangle, int left, int top, int right, int bottom, Size bounds)
        => ClampRectangle(Rectangle.FromLTRB(rectangle.Left - left, rectangle.Top - top, rectangle.Right + right, rectangle.Bottom + bottom), bounds);

    private static Rectangle ClampRectangle(Rectangle rectangle, Size bounds)
    {
        var left = Math.Clamp(rectangle.Left, 0, Math.Max(0, bounds.Width - 1));
        var top = Math.Clamp(rectangle.Top, 0, Math.Max(0, bounds.Height - 1));
        var right = Math.Clamp(rectangle.Right, left + 1, bounds.Width);
        var bottom = Math.Clamp(rectangle.Bottom, top + 1, bounds.Height);
        return Rectangle.FromLTRB(left, top, right, bottom);
    }

    private static bool IsRedBorderPixel(Color color)
        => color.R >= 180 && color.G <= 105 && color.B <= 105 && color.R - color.G >= 90 && color.R - color.B >= 90;

    private static bool IsSelectionFramePixel(Color color)
    {
        var maximum = Math.Max(color.R, Math.Max(color.G, color.B));
        var minimum = Math.Min(color.R, Math.Min(color.G, color.B));
        return maximum >= 210 && maximum - minimum <= 18;
    }

    private readonly record struct LineEvidence(int Coordinate, int Start, int End, int Strength);

    private readonly record struct LineCluster(int FirstCoordinate, int LastCoordinate, int Start, int End, int Strength);
}

sealed class RenderWaiter
{
    private static readonly string[] loadingMarkers = ["加载中", "正在加载", "读取中", "渲染中", "Loading", "Please wait"];
    private readonly AutomationElement window;
    private readonly CaptureOptions options;
    private readonly List<string> logs;

    public RenderWaiter(AutomationElement window, CaptureOptions options, List<string> logs)
    {
        this.window = window;
        this.options = options;
        this.logs = logs;
    }

    public bool WaitForReady(string fileName)
    {
        // 加载标记优先；标记消失后仍要求连续相同帧，过滤异步渲染残帧。
        var deadline = DateTime.UtcNow.AddMilliseconds(options.TimeoutMs);
        string? previousHash = null;
        var stableFrames = 0;
        var hasReportedLoading = false;
        var minimumReadyAt = DateTime.UtcNow.AddMilliseconds(Math.Min(500, options.TimeoutMs));

        while (DateTime.UtcNow < deadline)
        {
            var loading = FindLoadingMarkers().ToArray();
            if (loading.Length > 0)
            {
                if (!hasReportedLoading)
                {
                    logs.Add($"[wait] loading markers visible: {string.Join(", ", loading)}");
                    hasReportedLoading = true;
                }

                stableFrames = 0;
                Thread.Sleep(options.PollMs);
                continue;
            }

            var frameHash = CaptureFrameHash();
            if (frameHash == previousHash)
            {
                stableFrames++;
            }
            else
            {
                stableFrames = 0;
                previousHash = frameHash;
            }

            if (DateTime.UtcNow >= minimumReadyAt && stableFrames >= options.StabilityFrames)
            {
                logs.Add($"[wait] render ready for '{fileName}', stableFrames={stableFrames + 1}");
                return true;
            }

            Thread.Sleep(options.PollMs);
        }

        logs.Add($"[timeout] render did not stabilize within {options.TimeoutMs}ms");
        return false;
    }

    private IEnumerable<string> FindLoadingMarkers()
    {
        foreach (var element in window.FindAllDescendants())
        {
            string name;
            try
            {
                name = element.Name ?? string.Empty;
            }
            catch
            {
                continue;
            }

            if (loadingMarkers.Any(marker => name.Contains(marker, StringComparison.OrdinalIgnoreCase)))
            {
                yield return name;
            }
        }
    }

    private string CaptureFrameHash()
    {
        // 绿洲编辑器存在低对比度动态水印；对高信号像素量化后再指纹，避免水印让稳定帧永远无法收敛。
        using var image = Capture.Element(window);
        var bitmap = image.Bitmap;
        var fingerprint = new List<byte>(bitmap.Width * bitmap.Height / 16 + 8);
        fingerprint.AddRange(BitConverter.GetBytes(bitmap.Width));
        fingerprint.AddRange(BitConverter.GetBytes(bitmap.Height));
        for (var y = 0; y < bitmap.Height; y += 4)
        {
            for (var x = 0; x < bitmap.Width; x += 4)
            {
                var color = bitmap.GetPixel(x, y);
                var maximum = Math.Max(color.R, Math.Max(color.G, color.B));
                var minimum = Math.Min(color.R, Math.Min(color.G, color.B));
                if (maximum >= 96 || maximum - minimum >= 45)
                {
                    fingerprint.Add((byte)(color.R / 16));
                    fingerprint.Add((byte)(color.G / 16));
                    fingerprint.Add((byte)(color.B / 16));
                }
                else
                {
                    fingerprint.Add(0);
                    fingerprint.Add(0);
                    fingerprint.Add(0);
                }
            }
        }

        return Convert.ToHexString(SHA256.HashData(fingerprint.ToArray()));
    }
}

sealed record AssetPath(string ProjectName, string[] FolderSegments, string FileName, string Normalized)
{
    public static AssetPath Parse(string input)
    {
        // 统一处理斜杠、可选前导斜杠、uasset 扩展名和 UObject 对象后缀。
        var normalized = input.Trim().Replace('\\', '/');
        while (normalized.StartsWith('/'))
        {
            normalized = normalized[1..];
        }

        var parts = normalized.Split('/', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);
        if (parts.Length < 3 || string.IsNullOrWhiteSpace(parts[0]) || string.IsNullOrWhiteSpace(parts[^1]))
        {
            throw new AssetPathException("expected /<ProjectName>/Asset/<folder>/.../<file>");
        }

        if (!parts[1].Equals("Asset", StringComparison.OrdinalIgnoreCase))
        {
            throw new AssetPathException("the second path segment must be Asset");
        }

        var fileName = parts[^1];
        if (fileName.EndsWith(".uasset", StringComparison.OrdinalIgnoreCase))
        {
            fileName = fileName[..^7];
        }

        if (fileName.Contains('.') && fileName.Split('.').Length == 2)
        {
            fileName = fileName.Split('.')[0];
        }

        if (string.IsNullOrWhiteSpace(fileName))
        {
            throw new AssetPathException("target file name is empty");
        }

        return new AssetPath(parts[0], parts[1..^1], fileName, "/" + string.Join('/', parts[..^1]) + "/" + fileName);
    }
}

sealed class AssetPathException : Exception
{
    public AssetPathException(string message) : base(message) { }
}

sealed record PngVerification(string Path, long Bytes, int Width, int Height, bool Valid, bool NonUniformPixels, string? Error)
{
    public static PngVerification Verify(string path)
    {
        // 文件签名和尺寸不足以证明画面有效，因此额外抽样检查是否为单色空白图。
        if (!File.Exists(path))
        {
            return new PngVerification(path, 0, 0, 0, false, false, "file does not exist");
        }

        var file = new FileInfo(path);
        if (file.Length <= 0)
        {
            return new PngVerification(path, file.Length, 0, 0, false, false, "file is empty");
        }

        var bytes = File.ReadAllBytes(path);
        var signature = Convert.ToHexString(bytes.Take(8).ToArray());
        if (signature != "89504E470D0A1A0A")
        {
            return new PngVerification(path, file.Length, 0, 0, false, false, $"unexpected signature {signature}");
        }

        try
        {
            using var image = Image.FromFile(path);
            if (image.Width <= 0 || image.Height <= 0)
            {
                return new PngVerification(path, file.Length, image.Width, image.Height, false, false, "invalid dimensions");
            }

            using var bitmap = new Bitmap(image);
            var reference = bitmap.GetPixel(0, 0);
            var nonUniform = false;
            var stepX = Math.Max(1, bitmap.Width / 32);
            var stepY = Math.Max(1, bitmap.Height / 32);
            for (var y = 0; y < bitmap.Height && !nonUniform; y += stepY)
            {
                for (var x = 0; x < bitmap.Width; x += stepX)
                {
                    var pixel = bitmap.GetPixel(x, y);
                    if (pixel.ToArgb() != reference.ToArgb())
                    {
                        nonUniform = true;
                        break;
                    }
                }
            }

            return new PngVerification(path, file.Length, image.Width, image.Height, nonUniform, nonUniform, nonUniform ? null : "image is a single color");
        }
        catch (Exception error)
        {
            return new PngVerification(path, file.Length, 0, 0, false, false, error.Message);
        }
    }
}

sealed record CaptureFileResult(int StatusCode, bool Success, string AssetPath, string OutputPath, long ElapsedMs, PngVerification? Verification, IReadOnlyList<string> Logs)
{
    public static CaptureFileResult Ok(string assetPath, string outputPath, PngVerification verification, List<string> logs, long started)
        => new(0, true, assetPath, outputPath, ElapsedMilliseconds(started), verification, logs);

    public static CaptureFileResult Failed(int code, string assetPath, string outputPath, List<string> logs, long started)
        => new(code, false, assetPath, outputPath, ElapsedMilliseconds(started), null, logs);

    private static long ElapsedMilliseconds(long started)
        => (long)Stopwatch.GetElapsedTime(started).TotalMilliseconds;
}

sealed record CaptureOptions(bool ListOnly, string? ProcessName, string? Title, string? InvokeName, bool DumpNames, int? ClickX, int? ClickY, int? DoubleClickX, int? DoubleClickY, int? TypeX, int? TypeY, string? TypeText, int? ClearX, int? ClearY, int? BackX, int? BackY, string OutputPath, bool Activate, string? CaptureFilePath, int TimeoutMs, int PollMs, int StabilityFrames, bool CropRedBox)
{
    public static CaptureOptions Parse(string[] args)
    {
        var listOnly = false;
        string? processName = null;
        string? title = null;
        string? invokeName = null;
        var dumpNames = false;
        int? clickX = null;
        int? clickY = null;
        int? doubleClickX = null;
        int? doubleClickY = null;
        int? typeX = null;
        int? typeY = null;
        string? typeText = null;
        int? clearX = null;
        int? clearY = null;
        int? backX = null;
        int? backY = null;
        string? outputPath = null;
        var activate = false;
        string? captureFilePath = null;
        var timeoutMs = 15000;
        var pollMs = 250;
        var stabilityFrames = 2;
        bool? cropRedBox = null;

        for (var index = 0; index < args.Length; index++)
        {
            switch (args[index])
            {
                case "--list": listOnly = true; break;
                case "--process-name": processName = ReadValue(args, ref index, args[index]); break;
                case "--title": title = ReadValue(args, ref index, args[index]); break;
                case "--invoke-name": invokeName = ReadValue(args, ref index, args[index]); break;
                case "--dump-names": dumpNames = true; break;
                case "--click-x": clickX = int.Parse(ReadValue(args, ref index, args[index])); break;
                case "--click-y": clickY = int.Parse(ReadValue(args, ref index, args[index])); break;
                case "--double-click-x": doubleClickX = int.Parse(ReadValue(args, ref index, args[index])); break;
                case "--double-click-y": doubleClickY = int.Parse(ReadValue(args, ref index, args[index])); break;
                case "--type-x": typeX = int.Parse(ReadValue(args, ref index, args[index])); break;
                case "--type-y": typeY = int.Parse(ReadValue(args, ref index, args[index])); break;
                case "--text": typeText = ReadValue(args, ref index, args[index]); break;
                case "--clear-x": clearX = int.Parse(ReadValue(args, ref index, args[index])); break;
                case "--clear-y": clearY = int.Parse(ReadValue(args, ref index, args[index])); break;
                case "--back-x": backX = int.Parse(ReadValue(args, ref index, args[index])); break;
                case "--back-y": backY = int.Parse(ReadValue(args, ref index, args[index])); break;
                case "--output": outputPath = ReadValue(args, ref index, args[index]); break;
                case "--activate": activate = true; break;
                case "--capture-file": captureFilePath = ReadValue(args, ref index, args[index]); break;
                case "--timeout-ms": timeoutMs = int.Parse(ReadValue(args, ref index, args[index])); break;
                case "--poll-ms": pollMs = int.Parse(ReadValue(args, ref index, args[index])); break;
                case "--stability-frames": stabilityFrames = int.Parse(ReadValue(args, ref index, args[index])); break;
                case "--crop-red-box": cropRedBox = true; break;
                case "--no-crop-red-box": cropRedBox = false; break;
                case "--help":
                case "-h": PrintHelp(); Environment.Exit(0); break;
                default: throw new ArgumentException($"Unknown argument: {args[index]}");
            }
        }

        if (!listOnly && !dumpNames && string.IsNullOrWhiteSpace(invokeName) && string.IsNullOrWhiteSpace(outputPath))
        {
            throw new ArgumentException("--output is required unless --list, --dump-names, or --invoke-name is used.");
        }

        if (!string.IsNullOrWhiteSpace(outputPath) && !Path.IsPathFullyQualified(outputPath))
        {
            throw new ArgumentException("--output must be an absolute path.");
        }

        if (!string.IsNullOrWhiteSpace(captureFilePath) && string.IsNullOrWhiteSpace(outputPath))
        {
            throw new ArgumentException("--capture-file requires --output.");
        }

        if ((clickX.HasValue || clickY.HasValue) && (!clickX.HasValue || !clickY.HasValue))
        {
            throw new ArgumentException("--click-x and --click-y must be provided together.");
        }

        if ((doubleClickX.HasValue || doubleClickY.HasValue) && (!doubleClickX.HasValue || !doubleClickY.HasValue))
        {
            throw new ArgumentException("--double-click-x and --double-click-y must be provided together.");
        }

        if ((typeX.HasValue || typeY.HasValue || typeText is not null) && (!typeX.HasValue || !typeY.HasValue || typeText is null))
        {
            throw new ArgumentException("--type-x, --type-y, and --text must be provided together.");
        }

        if ((clearX.HasValue || clearY.HasValue) && (!clearX.HasValue || !clearY.HasValue))
        {
            throw new ArgumentException("--clear-x and --clear-y must be provided together.");
        }

        if ((backX.HasValue || backY.HasValue) && (!backX.HasValue || !backY.HasValue))
        {
            throw new ArgumentException("--back-x and --back-y must be provided together.");
        }

        if (timeoutMs <= 0 || pollMs <= 0 || stabilityFrames < 1)
        {
            throw new ArgumentException("--timeout-ms and --poll-ms must be positive; --stability-frames must be at least 1.");
        }

        // 路径驱动调用按用户约定只输出红框内部；整窗截图可继续使用无该参数的直接截图入口。
        cropRedBox ??= !string.IsNullOrWhiteSpace(captureFilePath);
        return new CaptureOptions(listOnly, processName, title, invokeName, dumpNames, clickX, clickY, doubleClickX, doubleClickY, typeX, typeY, typeText, clearX, clearY, backX, backY, outputPath ?? string.Empty, activate, captureFilePath, timeoutMs, pollMs, stabilityFrames, cropRedBox.Value);
    }

    private static string ReadValue(string[] args, ref int index, string option)
    {
        if (++index >= args.Length || string.IsNullOrWhiteSpace(args[index]))
        {
            throw new ArgumentException($"{option} requires a value.");
        }

        return args[index];
    }

    private static void PrintHelp()
    {
        Console.WriteLine("FlaUI UI screenshot helper");
        Console.WriteLine("  --list");
        Console.WriteLine("  --process-name <name> --title <exact title> --dump-names");
        Console.WriteLine("  --process-name <name> --title <exact title> --click-x <x> --click-y <y> --output <absolute path>");
        Console.WriteLine("  --process-name <name> --title <exact title> --double-click-x <x> --double-click-y <y> --output <absolute path>");
        Console.WriteLine("  --process-name <name> --title <exact title> --type-x <x> --type-y <y> --text <text> --output <absolute path>");
        Console.WriteLine("  --process-name <name> --title <exact title> --clear-x <x> --clear-y <y> --output <absolute path>");
        Console.WriteLine("  --process-name <name> --title <exact title> --back-x <x> --back-y <y> --output <absolute path>");
        Console.WriteLine("  --process-name <name> --title <exact title> --invoke-name <control name>");
        Console.WriteLine("  --process-name <name> --title <exact title> --output <absolute .png> [--activate]");
        Console.WriteLine("  --process-name <name> --title <exact title> --capture-file <asset path> --output <absolute .png> [--timeout-ms 15000] [--crop-red-box|--no-crop-red-box]");
    }
}

sealed record WindowInfo(int ProcessId, string ProcessName, string Title, IntPtr Handle, Rectangle Bounds, Window Element)
{
    public static WindowInfo? TryFrom(Window window)
    {
        try
        {
            var processId = window.Properties.ProcessId.ValueOrDefault;
            var processName = "<exited>";
            try
            {
                processName = Process.GetProcessById(processId).ProcessName;
            }
            catch
            {
                // The process can exit while the desktop tree is inspected.
            }

            return new WindowInfo(processId, processName, window.Title ?? string.Empty, window.Properties.NativeWindowHandle.ValueOrDefault, window.BoundingRectangle, window);
        }
        catch
        {
            return null;
        }
    }
}
