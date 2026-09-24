param(
    [string]$Root = 'D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\Saved\Logs\UGCRepository',
    [int]$ContextLines = 4,
    [int64]$MaxBytesPerFile = 8388608,
    [string[]]$FocusKeyword = @(),
    [switch]$FullScan,
    [switch]$Json
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$ClientLabel = [string]::Concat(([char]0x5BA2),([char]0x6237),([char]0x7AEF))
$ServerLabel = [string]::Concat(([char]0x670D),([char]0x52A1),([char]0x5668))
$InitMarker = [string]::Concat(([char]0x521D),([char]0x59CB),([char]0x5316),([char]0x5B8C),([char]0x6210))
$TagRegex = '\[UGC\]\[(' + [regex]::Escape($ClientLabel) + '|' + [regex]::Escape($ServerLabel) + ')\]\[(?<tag>[^\]]+)\]'

$CriticalPatterns = @(
    @{ Pattern = 'stack traceback'; Title = 'Lua stack traceback'; Severity = 'critical'; Confidence = 0.98; RootCause = 'Lua execution failed and exposed a stack trace. Start from the first business frame near the hit.'; Suggestions = @('Inspect the first stack traceback block and the lines immediately above it.', 'Add require("Script.UGCLog") and UGCLog.Log() around function entry, branch choice, and return values.') },
    @{ Pattern = 'a nil value'; Title = 'Lua nil access'; Severity = 'critical'; Confidence = 0.98; RootCause = 'A table field, object reference, or function value is nil at runtime.'; Suggestions = @('Check object creation timing and callback return values.', 'Log object validity, owner, key config values, and state transitions before access.') },
    @{ Pattern = 'call a nil'; Title = 'Lua called nil'; Severity = 'critical'; Confidence = 0.97; RootCause = 'A function reference is nil or a module was not loaded as expected.'; Suggestions = @('Verify module loading and method names.', 'Check colon-call versus dot-call usage.') },
    @{ Pattern = 'LuaException'; Title = 'LuaException'; Severity = 'critical'; Confidence = 0.95; RootCause = 'The engine captured a Lua-side exception.'; Suggestions = @('Inspect the log line right before the LuaException block.', 'Add logging for API inputs and return values around the failing path.') },
    @{ Pattern = 'attempt to index'; Title = 'Lua attempt to index'; Severity = 'critical'; Confidence = 0.97; RootCause = 'Code attempted to read a field from nil or from an unexpected value type.'; Suggestions = @('Review lifecycle timing such as BeginPlay, delayed callbacks, and replicated object readiness.', 'Log object FullName, validity, and runtime side before field access.') },
    @{ Pattern = 'attempt to call'; Title = 'Lua attempt to call'; Severity = 'critical'; Confidence = 0.97; RootCause = 'Code attempted to call a non-function value or a missing method.'; Suggestions = @('Confirm the method exists on the target object.', 'Validate inheritance, hot reload references, and module exports.') },
    @{ Pattern = 'Fatal error'; Title = 'Fatal runtime error'; Severity = 'high'; Confidence = 0.98; RootCause = 'A fatal runtime error occurred and should be treated as the top-priority failure.'; Suggestions = @('Focus on the first fatal block before later cascade errors.', 'Compare custom UGC logs right before the fatal timestamp.') },
    @{ Pattern = 'Ensure condition failed'; Title = 'Ensure failed'; Severity = 'high'; Confidence = 0.90; RootCause = 'A runtime precondition was violated.'; Suggestions = @('Check required preconditions before the call.', 'Log the variables involved in the ensure and compare client versus DS timing.') },
    @{ Pattern = 'Accessed None'; Title = 'Accessed None'; Severity = 'high'; Confidence = 0.92; RootCause = 'An object was missing, destroyed, or not replicated yet.'; Suggestions = @('Review object lifecycle and ownership.', 'Log object path and owning actor before use.') },
    @{ Pattern = 'Script Stack'; Title = 'Script stack'; Severity = 'high'; Confidence = 0.90; RootCause = 'A script stack was emitted. Start from the earliest business frame.'; Suggestions = @('Trace the first business script frame.', 'Compare with recent UGCLog tag output to find the broken branch.') }
)

function New-AnalysisResult {
    param([string]$Status, [object]$Session, [System.Collections.IList]$Issues, [object]$Signals)
    [ordered]@{ analysis_status = $Status; session = $Session; issues = $Issues; signals = $Signals }
}

function Get-SeverityRank {
    param([string]$Severity)
    switch ($Severity) { 'critical' { 4 } 'high' { 3 } 'medium' { 2 } 'low' { 1 } default { 0 } }
}

function Test-ShutdownNoise {
    param([string]$Line)
    return ($Line -match 'RequestExit|EngineExit|PreExit|BeginDestroy|EndPlay|Shutdown|ShutDown|LogExit|Close|TearingDown|GameThread timed out waiting for RenderThread')
}

function Get-DebugIdFromName {
    param([string]$Name)
    $match = [regex]::Match($Name, '_(?<id>[A-Za-z0-9]+?)_(?:\d+_TagLog\.log|\d+\.log|realtime\.log)$')
    if ($match.Success) { return $match.Groups['id'].Value }
    return $null
}

function Get-SessionCandidates {
    param([string]$BaseRoot)
    $candidates = @()
    $scanTargets = @(
        @{ Side = 'client'; Kind = 'TagLog'; Path = Join-Path $BaseRoot 'Clientlog\TagLog' },
        @{ Side = 'client'; Kind = 'LuaLog'; Path = Join-Path $BaseRoot 'Clientlog\LuaLog' },
        @{ Side = 'client'; Kind = 'FullLog'; Path = Join-Path $BaseRoot 'Clientlog\FullLog' },
        @{ Side = 'ds'; Kind = 'FullLog'; Path = Join-Path $BaseRoot 'DSlog\FullLog' }
    )
    foreach ($target in $scanTargets) {
        if (-not (Test-Path -LiteralPath $target.Path)) { continue }
        Get-ChildItem -LiteralPath $target.Path -File | ForEach-Object {
            $foundId = Get-DebugIdFromName -Name $_.Name
            if ($null -ne $foundId) {
                $candidates += [pscustomobject]@{ DebugId = $foundId; Side = $target.Side; Kind = $target.Kind; LastWriteTime = $_.LastWriteTime; File = $_.FullName }
            }
        }
    }
    return $candidates
}

function Select-PreferredDebugId {
    param([System.Collections.IList]$Candidates)
    $scored = foreach ($group in ($Candidates | Group-Object DebugId)) {
        $items = @($group.Group)
        $hasClient = [bool]($items | Where-Object { $_.Side -eq 'client' })
        $hasDs = [bool]($items | Where-Object { $_.Side -eq 'ds' })
        [pscustomobject]@{
            DebugId = $group.Name
            Completeness = if ($hasClient -and $hasDs) { 2 } elseif ($hasClient -or $hasDs) { 1 } else { 0 }
            FileCount = $items.Count
            LastWriteTime = ($items | Sort-Object LastWriteTime -Descending | Select-Object -First 1).LastWriteTime
        }
    }
    return ($scored | Sort-Object @{ Expression = { $_.LastWriteTime }; Descending = $true }, @{ Expression = { $_.Completeness }; Descending = $true }, @{ Expression = { $_.FileCount }; Descending = $true } | Select-Object -First 1).DebugId
}

function Resolve-SessionFiles {
    param([string]$BaseRoot, [string]$ResolvedDebugId)
    $map = [ordered]@{
        client_tag = Join-Path $BaseRoot 'Clientlog\TagLog'
        client_lua = Join-Path $BaseRoot 'Clientlog\LuaLog'
        client_full = Join-Path $BaseRoot 'Clientlog\FullLog'
        ds_full = Join-Path $BaseRoot 'DSlog\FullLog'
    }
    $resolved = [ordered]@{}
    foreach ($entry in $map.GetEnumerator()) {
        $resolved[$entry.Key] = @()
        if (-not (Test-Path -LiteralPath $entry.Value)) { continue }
        $matches = Get-ChildItem -LiteralPath $entry.Value -File | Where-Object { $_.Name -like "*_${ResolvedDebugId}_*" } | Sort-Object LastWriteTime
        foreach ($match in $matches) { $resolved[$entry.Key] += $match.FullName }
    }
    return $resolved
}

function Get-TimestampFromLine {
    param([string]$Line)
    if ([string]::IsNullOrEmpty($Line) -or $Line[0] -ne '[') { return $null }
    $end = $Line.IndexOf(']')
    if ($end -gt 1) { return $Line.Substring(1, $end - 1) }
    return $null
}

function Get-TagLabelFromLine {
    param([string]$Line)
    if ($Line.IndexOf('[UGC]', [System.StringComparison]::Ordinal) -lt 0) { return $null }
    $match = [regex]::Match($Line, $script:TagRegex)
    if ($match.Success) { return $match.Groups['tag'].Value }
    return $null
}

function Try-ParseNumbersFromLine {
    param([string]$Line)
    $pairs = [regex]::Matches($Line, '(?<name>[A-Za-z][A-Za-z0-9_]*)=\s*(?<value>-?\d+(?:\.\d+)?)')
    $parsed = @()
    foreach ($pair in $pairs) { $parsed += [pscustomobject]@{ Name = $pair.Groups['name'].Value; Value = [double]$pair.Groups['value'].Value } }
    return $parsed
}

function Get-ScanPlan {
    param([string]$File, [int64]$MaxBytes, [bool]$ReadFullFile)
    $item = Get-Item -LiteralPath $File
    $startOffset = [int64]0
    $scannedBytes = [int64]$item.Length
    $truncated = $false
    if (-not $ReadFullFile -and $MaxBytes -gt 0 -and $item.Length -gt $MaxBytes) {
        $startOffset = [Math]::Max([int64]0, [int64]$item.Length - $MaxBytes)
        $scannedBytes = [int64]$item.Length - $startOffset
        $truncated = $true
    }
    return [ordered]@{ file = $File; bytes = [int64]$item.Length; scanned_bytes = $scannedBytes; scan_start_offset = $startOffset; truncated = $truncated }
}

function Read-LogLines {
    param([string]$File, [int64]$StartOffset = 0)
    $stream = [System.IO.FileStream]::new($File, [System.IO.FileMode]::Open, [System.IO.FileAccess]::Read, [System.IO.FileShare]::ReadWrite)
    $reader = $null
    try {
        if ($StartOffset -gt 0) { [void]$stream.Seek($StartOffset, [System.IO.SeekOrigin]::Begin) }
        $reader = [System.IO.StreamReader]::new($stream, [System.Text.UTF8Encoding]::new($false, $false), $true, 65536)
        if ($StartOffset -gt 0) { [void]$reader.ReadLine() }
        while (-not $reader.EndOfStream) { $reader.ReadLine() }
    }
    finally {
        if ($null -ne $reader) { $reader.Dispose() }
        else { $stream.Dispose() }
    }
}

function Test-AnyKeyword {
    param([string]$Line, [string[]]$Keywords)
    if ($Keywords.Count -eq 0) { return $false }
    foreach ($keyword in $Keywords) {
        if ([string]::IsNullOrWhiteSpace($keyword)) { continue }
        if ($Line.IndexOf($keyword, [System.StringComparison]::OrdinalIgnoreCase) -ge 0) { return $true }
    }
    return $false
}

function Get-RecentContextExcerpt {
    param([System.Collections.Generic.Queue[string]]$RecentLines, [string]$Line)
    if ($RecentLines.Count -eq 0) { return $Line }
    $parts = New-Object 'System.Collections.Generic.List[string]'
    foreach ($recentLine in $RecentLines) { $parts.Add($recentLine) | Out-Null }
    $parts.Add($Line) | Out-Null
    return ($parts.ToArray() -join "`n")
}

function New-Sample {
    param([string]$Key, [string]$File, [int]$ScanLine, [object]$ScanPlan, [string]$Timestamp, [string]$Excerpt)
    $absoluteLine = if ($ScanPlan.truncated) { $null } else { $ScanLine }
    return [pscustomobject][ordered]@{
        key = $Key
        file = $File
        line = $absoluteLine
        scan_line = $ScanLine
        scan_start_offset = $ScanPlan.scan_start_offset
        timestamp = $Timestamp
        excerpt = $Excerpt
    }
}

function Get-LineContexts {
    param([string]$File, [System.Collections.IList]$Targets, [int]$Radius)
    $ranges = @()
    foreach ($target in $Targets) {
        if ($target.file -ne $File) { continue }
        $ranges += [pscustomobject]@{ key = $target.key; start = [Math]::Max(1, [int]$target.line - $Radius); finish = [int]$target.line + $Radius; lines = New-Object 'System.Collections.Generic.List[string]' }
    }
    if ($ranges.Count -eq 0) { return @{} }
    $lineNumber = 0
    Read-LogLines -File $File | ForEach-Object {
        $lineNumber++
        foreach ($range in $ranges) {
            if ($lineNumber -ge $range.start -and $lineNumber -le $range.finish) { $range.lines.Add($_) | Out-Null }
        }
    }
    $result = @{}
    foreach ($range in $ranges) { $result[$range.key] = ($range.lines.ToArray() -join "`n") }
    return $result
}

function Add-Issue {
    param(
        [System.Collections.Generic.List[object]]$Bucket,
        [string]$Severity,
        [double]$Confidence,
        [string]$Title,
        [string]$Summary,
        [System.Collections.IList]$Evidence,
        [string]$RootCause,
        [string[]]$Suggestions,
        [string[]]$MatchedPatterns = @(),
        [bool]$RequiresMcpConfirmation = $false,
        [string[]]$McpQueryHints = @()
    )
    $Bucket.Add([ordered]@{
        severity = $Severity
        confidence = $Confidence
        title = $Title
        summary = $Summary
        evidence = $Evidence
        root_cause = $RootCause
        suggestions = $Suggestions
        matched_patterns = $MatchedPatterns
        requires_mcp_confirmation = $RequiresMcpConfirmation
        mcp_query_hints = $McpQueryHints
    }) | Out-Null
}

function Analyze-Logs {
    param([string[]]$Files, [int]$WindowRadius, [int64]$MaxBytes, [bool]$ReadFullFile, [string[]]$FocusKeywords)
    $issues = New-Object 'System.Collections.Generic.List[object]'
    $explicitGroups = @{}
    $warningGroups = @{}
    $tagCounts = @{}
    $valueTrack = @{}
    $phaseSeen = [ordered]@{ init = $false; battle_begin = $false; loading_hide = $false }
    $sideSignals = [ordered]@{ client_hits = 0; ds_hits = 0 }
    $fileStats = @{}
    $fileLineHits = @{}
    $shutdownNoise = [ordered]@{ count = 0; samples = New-Object 'System.Collections.Generic.List[object]' }
    $focusKeywordList = @($FocusKeywords | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })
    $focusSignals = [ordered]@{ count = 0; samples = New-Object 'System.Collections.Generic.List[object]' }
    $truncatedFiles = New-Object 'System.Collections.Generic.List[object]'
    $clusterGapLines = 30
    $sampleLimit = 3
    $focusSampleLimit = 10
    $evidenceLimit = 5
    $repeatThreshold = 12

    foreach ($file in $Files) {
        if ([string]::IsNullOrWhiteSpace($file) -or -not (Test-Path -LiteralPath $file)) { continue }
        $scanPlan = Get-ScanPlan -File $file -MaxBytes $MaxBytes -ReadFullFile $ReadFullFile
        if ($scanPlan.truncated) { $truncatedFiles.Add($scanPlan) | Out-Null }
        $fileStats[$file] = [ordered]@{ lines = 0; bytes = $scanPlan.bytes; scanned_bytes = $scanPlan.scanned_bytes; scan_start_offset = $scanPlan.scan_start_offset; truncated = $scanPlan.truncated; hits = 0; focus_hits = 0 }
        $lineNumber = 0
        $recentLines = New-Object 'System.Collections.Generic.Queue[string]'
        Read-LogLines -File $file -StartOffset $scanPlan.scan_start_offset | ForEach-Object {
            $lineNumber++
            $fileStats[$file].lines++
            $line = $_
            $timestamp = $null
            $side = if ($file -like '*\DSlog\*') { 'ds' } else { 'client' }

            if ($line.Contains($InitMarker)) { $phaseSeen.init = $true }
            if ($line.IndexOf('OnBattleBeginPlay', [System.StringComparison]::OrdinalIgnoreCase) -ge 0 -or $line.IndexOf('enter battle success', [System.StringComparison]::OrdinalIgnoreCase) -ge 0) { $phaseSeen.battle_begin = $true }
            if ($line.IndexOf('HideLoading', [System.StringComparison]::OrdinalIgnoreCase) -ge 0) { $phaseSeen.loading_hide = $true }

            $lineMatched = $false
            if ($focusKeywordList.Count -gt 0 -and (Test-AnyKeyword -Line $line -Keywords $focusKeywordList)) {
                $lineMatched = $true
                if ($null -eq $timestamp) { $timestamp = Get-TimestampFromLine -Line $line }
                $focusSignals.count++
                $fileStats[$file].focus_hits++
                if ($focusSignals.samples.Count -lt $focusSampleLimit) {
                    $focusSignals.samples.Add((New-Sample -Key ($file + '|focus|' + $lineNumber) -File $file -ScanLine $lineNumber -ScanPlan $scanPlan -Timestamp $timestamp -Excerpt (Get-RecentContextExcerpt -RecentLines $recentLines -Line $line))) | Out-Null
                }
            }

            $tag = Get-TagLabelFromLine -Line $line
            if ($null -ne $tag) {
                $lineMatched = $true
                if ($null -eq $timestamp) { $timestamp = Get-TimestampFromLine -Line $line }
                if (-not $tagCounts.ContainsKey($tag)) { $tagCounts[$tag] = [ordered]@{ count = 0; first = $timestamp; last = $timestamp } }
                $tagCounts[$tag].count++
                $tagCounts[$tag].last = $timestamp
            }

            foreach ($pattern in $script:CriticalPatterns) {
                if ($line.IndexOf($pattern.Pattern, [System.StringComparison]::OrdinalIgnoreCase) -ge 0) {
                    $lineMatched = $true
                    if ($null -eq $timestamp) { $timestamp = Get-TimestampFromLine -Line $line }
                    $groupKey = $file + '|' + $pattern.Pattern
                    if (-not $explicitGroups.ContainsKey($groupKey)) {
                        $explicitGroups[$groupKey] = [pscustomobject][ordered]@{
                            key = $groupKey; file = $file; pattern = $pattern.Pattern; severity = $pattern.Severity; confidence = $pattern.Confidence; title = $pattern.Title
                            root_cause = $pattern.RootCause; suggestions = $pattern.Suggestions; count = 0; firstTimestamp = $timestamp; lastTimestamp = $timestamp
                            firstLine = $lineNumber; lastLine = $lineNumber; samples = New-Object 'System.Collections.Generic.List[object]'
                        }
                    }
                    $group = $explicitGroups[$groupKey]
                    $group.count++
                    $group.lastTimestamp = $timestamp
                    $group.lastLine = $lineNumber
                    if ($null -eq $group.firstTimestamp) { $group.firstTimestamp = $timestamp }
                    if ($group.samples.Count -lt $sampleLimit) {
                        $group.samples.Add((New-Sample -Key ($groupKey + '|' + $lineNumber) -File $file -ScanLine $lineNumber -ScanPlan $scanPlan -Timestamp $timestamp -Excerpt (Get-RecentContextExcerpt -RecentLines $recentLines -Line $line))) | Out-Null
                    }
                    if ($side -eq 'client') { $sideSignals.client_hits++ } else { $sideSignals.ds_hits++ }
                }
            }

            if ($line.IndexOf('Warning:', [System.StringComparison]::OrdinalIgnoreCase) -ge 0 -or $line.IndexOf('Error:', [System.StringComparison]::OrdinalIgnoreCase) -ge 0) {
                if ($null -eq $timestamp) { $timestamp = Get-TimestampFromLine -Line $line }
                if (Test-ShutdownNoise -Line $line) {
                    $shutdownNoise.count++
                    if ($shutdownNoise.samples.Count -lt $sampleLimit) {
                        $shutdownNoise.samples.Add((New-Sample -Key ($file + '|shutdown|' + $lineNumber) -File $file -ScanLine $lineNumber -ScanPlan $scanPlan -Timestamp $timestamp -Excerpt (Get-RecentContextExcerpt -RecentLines $recentLines -Line $line))) | Out-Null
                    }
                    $lineMatched = $true
                }
                else {
                    $lineMatched = $true
                    if (-not $warningGroups.ContainsKey($file)) { $warningGroups[$file] = [pscustomobject][ordered]@{ file = $file; count = 0; samples = New-Object 'System.Collections.Generic.List[object]' } }
                    $warningGroup = $warningGroups[$file]
                    $warningGroup.count++
                    if ($warningGroup.samples.Count -lt $sampleLimit) { $warningGroup.samples.Add((New-Sample -Key ($file + '|warning|' + $lineNumber) -File $file -ScanLine $lineNumber -ScanPlan $scanPlan -Timestamp $timestamp -Excerpt (Get-RecentContextExcerpt -RecentLines $recentLines -Line $line))) | Out-Null }
                    if ($side -eq 'client') { $sideSignals.client_hits++ } else { $sideSignals.ds_hits++ }
                }
            }

            if ($lineMatched) {
                $fileStats[$file].hits++
                if (-not $fileLineHits.ContainsKey($file)) { $fileLineHits[$file] = New-Object 'System.Collections.Generic.List[int]' }
                $fileLineHits[$file].Add($lineNumber) | Out-Null
            }

            if ($null -ne $tag -and $line.IndexOf('=', [System.StringComparison]::OrdinalIgnoreCase) -ge 0) {
                foreach ($entry in @(Try-ParseNumbersFromLine -Line $line)) {
                    if (-not $valueTrack.ContainsKey($tag)) { $valueTrack[$tag] = @{} }
                    if (-not $valueTrack[$tag].ContainsKey($entry.Name)) { $valueTrack[$tag][$entry.Name] = New-Object 'System.Collections.Generic.List[double]' }
                    $valueTrack[$tag][$entry.Name].Add($entry.Value) | Out-Null
                }
            }
            if ($WindowRadius -gt 0) {
                $recentLines.Enqueue($line)
                while ($recentLines.Count -gt $WindowRadius) { [void]$recentLines.Dequeue() }
            }
        }
    }

    $fileTargets = @{}
    foreach ($group in $explicitGroups.Values) {
        foreach ($sample in $group.samples) {
            if ($null -eq $sample.line) { continue }
            if (-not $fileTargets.ContainsKey($group.file)) { $fileTargets[$group.file] = New-Object 'System.Collections.Generic.List[object]' }
            $fileTargets[$group.file].Add($sample) | Out-Null
        }
    }
    $contextsByFile = @{}
    foreach ($file in $fileTargets.Keys) { $contextsByFile[$file] = Get-LineContexts -File $file -Targets $fileTargets[$file] -Radius $WindowRadius }

    $clusters = New-Object 'System.Collections.Generic.List[object]'
    foreach ($group in ($explicitGroups.Values | Sort-Object file, firstLine, lastLine)) {
        $cluster = if ($clusters.Count -gt 0) { $clusters[$clusters.Count - 1] } else { $null }
        if ($null -eq $cluster -or $cluster.file -ne $group.file -or $group.firstLine -gt ($cluster.lastLine + $clusterGapLines)) {
            $clusters.Add([pscustomobject]@{ file = $group.file; firstLine = $group.firstLine; lastLine = $group.lastLine; groups = New-Object 'System.Collections.Generic.List[object]' }) | Out-Null
            $cluster = $clusters[$clusters.Count - 1]
        }
        $cluster.groups.Add($group) | Out-Null
        if ($group.lastLine -gt $cluster.lastLine) { $cluster.lastLine = $group.lastLine }
    }

    foreach ($cluster in $clusters) {
        $primary = @($cluster.groups | Sort-Object @{ Expression = { Get-SeverityRank -Severity $_.severity }; Descending = $true }, @{ Expression = { $_.confidence }; Descending = $true }, @{ Expression = { $_.firstLine }; Descending = $false } | Select-Object -First 1)[0]
        $contexts = $contextsByFile[$primary.file]
        $evidence = New-Object 'System.Collections.Generic.List[object]'
        $seen = New-Object 'System.Collections.Generic.HashSet[string]'
        foreach ($group in $cluster.groups) {
            foreach ($sample in $group.samples) {
                $excerpt = $sample.excerpt
                if ($null -ne $contexts -and $contexts.ContainsKey($sample.key) -and -not [string]::IsNullOrWhiteSpace($contexts[$sample.key])) { $excerpt = $contexts[$sample.key] }
                $evidenceKey = $sample.file + '|' + [string]$sample.scan_line + '|' + $group.pattern
                if (-not $seen.Add($evidenceKey)) { continue }
                $evidence.Add([ordered]@{ file = $sample.file; line = $sample.line; scan_line = $sample.scan_line; scan_start_offset = $sample.scan_start_offset; timestamp = $sample.timestamp; pattern = $group.pattern; excerpt = $excerpt }) | Out-Null
                if ($evidence.Count -ge $evidenceLimit) { break }
            }
            if ($evidence.Count -ge $evidenceLimit) { break }
        }
        $matchedPatterns = @($cluster.groups | ForEach-Object { $_.pattern } | Sort-Object -Unique)
        $clusterHitCount = @($cluster.groups | ForEach-Object { $_.count } | Measure-Object -Sum).Sum
        $summary = if ($cluster.groups.Count -gt 1) { 'Matched related error block: ' + ($matchedPatterns -join ', ') + " (hits=$clusterHitCount)" } else { 'Matched critical error keyword: ' + $primary.pattern + " (hits=$clusterHitCount)" }
        Add-Issue -Bucket $issues -Severity $primary.severity -Confidence $primary.confidence -Title $primary.title -Summary $summary -Evidence $evidence -RootCause $primary.root_cause -Suggestions $primary.suggestions -MatchedPatterns $matchedPatterns -RequiresMcpConfirmation $true -McpQueryHints @('Confirm Oasis lifecycle/object validity rules if the fix depends on timing or replicated object readiness.', 'Confirm client versus DS responsibility before moving logic between sides.')
    }

    foreach ($tagEntry in $tagCounts.GetEnumerator() | Sort-Object { $_.Value.count } -Descending) {
        if ($tagEntry.Value.count -lt $repeatThreshold) { continue }
        $scope = $tagEntry.Key
        $suggestions = New-Object 'System.Collections.Generic.List[string]'
        $suggestions.Add("Check whether [$scope] is logged from Tick, a timer, repeated event binding, or a loop.") | Out-Null
        $suggestions.Add('Add logs for state transitions, enter conditions, and exit conditions instead of only repeating the same line.') | Out-Null
        if ($valueTrack.ContainsKey($scope)) {
            foreach ($name in $valueTrack[$scope].Keys) {
                $values = $valueTrack[$scope][$name]
                if ($values.Count -lt 2) { continue }
                $min = ($values | Measure-Object -Minimum).Minimum
                $max = ($values | Measure-Object -Maximum).Maximum
                if ([Math]::Abs($max - $min) -ge 3) { $suggestions.Add("Variable $name changes noticeably under the same tag ($min -> $max). Check for stacking, rollback, or display-side desync.") | Out-Null }
            }
        }
        Add-Issue -Bucket $issues -Severity 'medium' -Confidence 0.72 -Title "High-frequency tag [$scope]" -Summary "The same business tag was printed $($tagEntry.Value.count) times, which suggests looping, rebinding, or state thrashing." -Evidence @([ordered]@{ file = $null; line = $null; timestamp = $tagEntry.Value.first; pattern = 'high-frequency-tag'; excerpt = "tag=$scope count=$($tagEntry.Value.count) first=$($tagEntry.Value.first) last=$($tagEntry.Value.last)" }) -RootCause 'Frequent repeated logs usually mean repeated execution paths, missing unbinds, no throttling in Tick, or a state machine bouncing between values.' -Suggestions @($suggestions) -MatchedPatterns @('high-frequency-tag') -RequiresMcpConfirmation $true -McpQueryHints @('Confirm whether the repeated callback should run on Tick, timer, client, DS, or both sides.')
    }

    if ($phaseSeen.init -and -not $phaseSeen.battle_begin) {
        Add-Issue -Bucket $issues -Severity 'medium' -Confidence 0.66 -Title 'Init marker without later phase marker' -Summary 'An init-complete marker appeared, but no later battle-begin marker was found.' -Evidence @([ordered]@{ file = $null; line = $null; timestamp = $null; pattern = 'missing-follow-up'; excerpt = 'Init marker exists but battle begin markers do not.' }) -RootCause 'The flow may stop during resource loading, UI setup, network sync, or object readiness without throwing a hard exception.' -Suggestions @('Add logs after init for preload completion, pawn ready, and UI creation finished.', 'Add logs on early-return branches that can stop the flow.') -MatchedPatterns @('missing-follow-up') -RequiresMcpConfirmation $true -McpQueryHints @('Confirm expected Oasis battle lifecycle markers for this game mode.')
    }
    if ($phaseSeen.battle_begin -and -not $phaseSeen.loading_hide) {
        Add-Issue -Bucket $issues -Severity 'low' -Confidence 0.55 -Title 'Battle begin without loading-hide marker' -Summary 'Battle start was observed, but loading-hide was not.' -Evidence @([ordered]@{ file = $null; line = $null; timestamp = $null; pattern = 'loading-sequence'; excerpt = 'Battle-begin markers exist, but HideLoading was not found.' }) -RootCause 'This can indicate missing UI cleanup, a loading-state issue, or insufficient logging.' -Suggestions @('Inspect HUD init and loading close logic.', 'Add logs right before and after HideLoading.') -MatchedPatterns @('loading-sequence')
    }
    if ($sideSignals.client_hits -gt 0 -and $sideSignals.ds_hits -eq 0) {
        Add-Issue -Bucket $issues -Severity 'medium' -Confidence 0.68 -Title 'Signals appear only on the client side' -Summary 'Current abnormal signals appear on the client side only.' -Evidence @([ordered]@{ file = $null; line = $null; timestamp = $null; pattern = 'client-only'; excerpt = 'client_hits > 0 and ds_hits == 0' }) -RootCause 'This points more strongly to client-only UI, FX, input, asset, or client-owned object lifecycle problems.' -Suggestions @('Inspect client-only logic first.', 'Add logs for runtime side, asset state, and UI lifecycle.') -MatchedPatterns @('client-only') -RequiresMcpConfirmation $true -McpQueryHints @('Confirm whether the suspected logic is expected to execute on client, DS, or both.')
    }
    if ($issues.Count -eq 0 -and $warningGroups.Count -gt 0) {
        $evidence = @()
        foreach ($warningGroup in ($warningGroups.Values | Sort-Object count -Descending | Select-Object -First 1)) {
            foreach ($sample in $warningGroup.samples) { $evidence += [ordered]@{ file = $sample.file; line = $sample.line; scan_line = $sample.scan_line; scan_start_offset = $sample.scan_start_offset; timestamp = $sample.timestamp; pattern = 'warning-or-error'; excerpt = $sample.excerpt } }
        }
        Add-Issue -Bucket $issues -Severity 'low' -Confidence 0.45 -Title 'Warnings or non-fatal errors present' -Summary 'No high-confidence script error was found, but warning/error lines still exist.' -Evidence $evidence -RootCause 'This looks more like config, resource, mount, or environment noise until correlated with the exact bug time.' -Suggestions @('Check whether the warning is stable and reproducible.', 'If it aligns with the bug timestamp, add business logs around the same path.') -MatchedPatterns @('warning-or-error')
    }

    if ($issues.Count -eq 0 -and $focusKeywordList.Count -gt 0 -and $focusSignals.count -gt 0) {
        Add-Issue -Bucket $issues -Severity 'low' -Confidence 0.40 -Title 'Focus keyword evidence present' -Summary "Matched focus keywords $($focusKeywordList -join ', ') without a high-confidence runtime error." -Evidence @($focusSignals.samples.ToArray()) -RootCause 'The focused subsystem is active in the selected log window, but the current evidence is not enough to prove a runtime failure.' -Suggestions @('Correlate these focus samples with the user-visible bug time.', 'Add UGCLog.Log() around entry, branch decisions, return values, and side checks in the focused subsystem.') -MatchedPatterns @('focus-keyword')
    }

    if ($issues.Count -eq 0 -and $shutdownNoise.count -gt 0) {
        Add-Issue -Bucket $issues -Severity 'low' -Confidence 0.20 -Title 'Shutdown noise only' -Summary "Only shutdown/exit-like warnings were found (x$($shutdownNoise.count)); treat as low-priority unless it matches the bug timestamp." -Evidence @($shutdownNoise.samples.ToArray()) -RootCause 'Engine shutdown and teardown logs are common after stopping PIE/client sessions and often appear after the real failure.' -Suggestions @('Look earlier in the same DebugID for the first gameplay-side error.', 'Add UGCLog.Log() before stop/cleanup paths only if the bug occurs during shutdown.') -MatchedPatterns @('shutdown-noise')
    }

    $coverageWarnings = @()
    foreach ($path in $fileStats.Keys) {
        if ($fileStats[$path].lines -gt 0 -and $fileStats[$path].hits -eq 0) {
            $coverageWarnings += [ordered]@{ file = $path; reason = 'scanned but no suspicious line matched' }
        }
    }

    $warningSum = if ($warningGroups.Count -gt 0) { @($warningGroups.Values | ForEach-Object { $_.count }) | Measure-Object -Sum | Select-Object -ExpandProperty Sum } else { 0 }
    return [ordered]@{
        Issues = $issues
        Signals = [ordered]@{
            critical_keyword_hits = $explicitGroups.Count
            warning_or_error_hits = $warningSum
            shutdown_noise_hits = $shutdownNoise.count
            focus_keywords = $focusKeywordList
            focus_keyword_hits = $focusSignals.count
            focus_samples = @($focusSignals.samples.ToArray())
            repeated_tags = @($tagCounts.GetEnumerator() | Where-Object { $_.Value.count -ge $repeatThreshold } | Sort-Object { $_.Value.count } -Descending | ForEach-Object { [ordered]@{ tag = $_.Key; count = $_.Value.count; first = $_.Value.first; last = $_.Value.last } })
            client_hits = $sideSignals.client_hits
            ds_hits = $sideSignals.ds_hits
            phase_markers = $phaseSeen
            scan_policy = [ordered]@{ full_scan = $ReadFullFile; max_bytes_per_file = $MaxBytes; truncated_files = @($truncatedFiles.ToArray()) }
            scanned_files = @($fileStats.Keys | ForEach-Object { [ordered]@{ file = $_; lines = $fileStats[$_].lines; bytes = $fileStats[$_].bytes; scanned_bytes = $fileStats[$_].scanned_bytes; scan_start_offset = $fileStats[$_].scan_start_offset; truncated = $fileStats[$_].truncated; hits = $fileStats[$_].hits; focus_hits = $fileStats[$_].focus_hits } })
            file_coverage = @($fileStats.Keys | ForEach-Object { [ordered]@{ file = $_; lines = $fileStats[$_].lines; bytes = $fileStats[$_].bytes; scanned_bytes = $fileStats[$_].scanned_bytes; truncated = $fileStats[$_].truncated; matched_lines = $fileStats[$_].hits } })
            coverage_warnings = $coverageWarnings
            matched_windows = @($fileLineHits.GetEnumerator() | ForEach-Object {
                $minLine = ($_.Value | Measure-Object -Minimum).Minimum
                $maxLine = ($_.Value | Measure-Object -Maximum).Maximum
                $stats = $fileStats[$_.Key]
                $firstLine = if ($stats.truncated) { $null } else { $minLine }
                $lastLine = if ($stats.truncated) { $null } else { $maxLine }
                [ordered]@{ file = $_.Key; hit_line_count = $_.Value.Count; first_hit_line = $firstLine; last_hit_line = $lastLine; first_hit_scan_line = $minLine; last_hit_scan_line = $maxLine; scan_start_offset = $stats.scan_start_offset }
            })
        }
    }
}

try {
    $session = [ordered]@{ debug_id = $null; root = $Root; selected_files = [ordered]@{}; time_range = [ordered]@{ start = $null; end = $null }; missing_sides = @(); candidate_count = 0 }
    if (-not (Test-Path -LiteralPath $Root)) {
        New-AnalysisResult -Status 'no_logs' -Session $session -Issues @() -Signals ([ordered]@{ message = 'Log root not found.'; root = $Root }) | ConvertTo-Json -Depth 10
        exit 0
    }
    $candidates = @(Get-SessionCandidates -BaseRoot $Root)
    $session.candidate_count = $candidates.Count
    if ($candidates.Count -eq 0) {
        New-AnalysisResult -Status 'no_logs' -Session $session -Issues @() -Signals ([ordered]@{ message = 'No session candidates found.'; root = $Root }) | ConvertTo-Json -Depth 10
        exit 0
    }
    $DebugId = Select-PreferredDebugId -Candidates $candidates
    $resolvedFiles = Resolve-SessionFiles -BaseRoot $Root -ResolvedDebugId $DebugId
    $selectedFiles = New-Object 'System.Collections.Generic.List[string]'
    foreach ($bucket in @($resolvedFiles.client_tag, $resolvedFiles.client_lua, $resolvedFiles.client_full, $resolvedFiles.ds_full)) {
        foreach ($path in @($bucket)) {
            if (-not [string]::IsNullOrWhiteSpace($path)) { $selectedFiles.Add($path) | Out-Null }
        }
    }
    $session.debug_id = $DebugId
    $session.selected_files = $resolvedFiles
    if ($selectedFiles.Count -eq 0) {
        New-AnalysisResult -Status 'no_logs' -Session $session -Issues @() -Signals ([ordered]@{ message = 'DebugID resolved but no matching files were found.'; debug_id = $DebugId }) | ConvertTo-Json -Depth 10
        exit 0
    }
    $fileInfos = $selectedFiles | ForEach-Object { Get-Item -LiteralPath $_ }
    $session.time_range.start = ($fileInfos | Sort-Object LastWriteTime | Select-Object -First 1).LastWriteTime.ToString('s')
    $session.time_range.end = ($fileInfos | Sort-Object LastWriteTime -Descending | Select-Object -First 1).LastWriteTime.ToString('s')
    $missing = New-Object 'System.Collections.Generic.List[string]'
    if ($resolvedFiles.client_tag.Count -eq 0 -and $resolvedFiles.client_lua.Count -eq 0 -and $resolvedFiles.client_full.Count -eq 0) { $missing.Add('client') | Out-Null }
    if ($resolvedFiles.ds_full.Count -eq 0) { $missing.Add('ds') | Out-Null }
    $session.missing_sides = @($missing)
    $analysis = Analyze-Logs -Files $selectedFiles -WindowRadius $ContextLines -MaxBytes $MaxBytesPerFile -ReadFullFile ([bool]$FullScan) -FocusKeywords $FocusKeyword
    $status = 'ok'
    if ($missing.Count -gt 0) { $status = 'partial_logs' }
    if ($analysis.Issues.Count -eq 0) { $status = if ($missing.Count -gt 0) { 'partial_logs' } else { 'no_clear_issue' } }
    $orderedIssues = @($analysis.Issues | Sort-Object @{ Expression = { Get-SeverityRank -Severity $_.severity }; Descending = $true }, @{ Expression = { $_.confidence }; Descending = $true })
    New-AnalysisResult -Status $status -Session $session -Issues $orderedIssues -Signals $analysis.Signals | ConvertTo-Json -Depth 12
}
catch {
    $session = [ordered]@{ debug_id = $null; root = $Root; selected_files = [ordered]@{}; time_range = [ordered]@{ start = $null; end = $null }; missing_sides = @() }
    New-AnalysisResult -Status 'scan_failed' -Session $session -Issues @() -Signals ([ordered]@{ error = $_.Exception.Message; stack = $_.ScriptStackTrace }) | ConvertTo-Json -Depth 10
    exit 1
}
