param(
    [string]$OasisSyncRoot = "D:\oasis-skill-plus",
    [string]$NodePath = "node",
    [switch]$SkipRemote,
    [switch]$WhatIf
)

$ErrorActionPreference = "Stop"
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$knowledgeRoot = Split-Path -Parent $scriptDir

$destinations = @{
    "api" = Join-Path $knowledgeRoot "raw\docs\api"
    "wiki" = Join-Path $knowledgeRoot "raw\docs\wiki"
}

function Get-FileManifest {
    param([string]$Root)

    $resolvedRoot = (Resolve-Path -LiteralPath $Root).Path.TrimEnd('\')
    $manifest = @{}
    Get-ChildItem -LiteralPath $Root -Recurse -File | ForEach-Object {
        $relativePath = $_.FullName.Substring($resolvedRoot.Length + 1).Replace('\', '/')
        $manifest[$relativePath] = $_.Length
    }
    return $manifest
}

function Assert-MirrorComplete {
    param(
        [string]$Source,
        [string]$Destination
    )

    $sourceManifest = Get-FileManifest -Root $Source
    $destinationManifest = Get-FileManifest -Root $Destination
    $missing = @($sourceManifest.Keys | Where-Object { -not $destinationManifest.ContainsKey($_) })
    $unexpected = @($destinationManifest.Keys | Where-Object { -not $sourceManifest.ContainsKey($_) })
    $sizeMismatch = @(
        $sourceManifest.Keys |
            Where-Object {
                $destinationManifest.ContainsKey($_) -and $destinationManifest[$_] -ne $sourceManifest[$_]
            }
    )

    if ($missing.Count -gt 0 -or $unexpected.Count -gt 0 -or $sizeMismatch.Count -gt 0) {
        throw (
            "Mirror verification failed for '$Destination'. " +
            "missing=$($missing.Count), unexpected=$($unexpected.Count), sizeMismatch=$($sizeMismatch.Count)"
        )
    }

    Write-Output "[INFO] Mirror verified: $($sourceManifest.Count) files"
}

# 1. Search for Node path
if ($NodePath -eq "node") {
    if (-not (Get-Command "node" -ErrorAction SilentlyContinue)) {
        $standardPaths = @(
            "C:\Program Files\nodejs\node.exe",
            "C:\Program Files (x86)\nodejs\node.exe",
            "C:\Users\Administrator\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe"
        )
        foreach ($p in $standardPaths) {
            if (Test-Path -LiteralPath $p) {
                $NodePath = $p
                break
            }
        }
        if (-not (Test-Path -LiteralPath $NodePath -ErrorAction SilentlyContinue)) {
            throw "Node.js not found in PATH or standard installation folders. Please specify NodePath parameter."
        }
    }
}

Write-Output "[INFO] Node executable: $NodePath"
Write-Output "[INFO] Sync repository root: $OasisSyncRoot"

# 2. Verify sync source
$cliScript = Join-Path $OasisSyncRoot "src\cli.mjs"
if (-not (Test-Path -LiteralPath $cliScript)) {
    throw "src/cli.mjs not found. Please ensure D:\oasis-skill-plus exists and is complete."
}

if ($WhatIf) {
    Write-Output "[WhatIf] Command to run: & $NodePath src/cli.mjs sync-all"
    foreach ($key in $destinations.Keys) {
        Write-Output ("[WhatIf] Ready to mirror: {0} -> {1}" -f (Join-Path $OasisSyncRoot "docs\$key"), $destinations[$key])
    }
    return
}

if ($SkipRemote) {
    Write-Output "[INFO] Skipping remote fetch; mirroring existing oasis-skill-plus docs."
} else {
    # 3. Execute sync command with direct console inheritance to avoid stream deadlock
    Write-Output "[INFO] Starting remote Wiki and API sync..."
    $processInfo = New-Object System.Diagnostics.ProcessStartInfo
    $processInfo.FileName = $NodePath
    $processInfo.Arguments = "src/cli.mjs sync-all"
    $processInfo.WorkingDirectory = $OasisSyncRoot
    $processInfo.UseShellExecute = $false
    $processInfo.RedirectStandardOutput = $false
    $processInfo.RedirectStandardError = $false
    $processInfo.CreateNoWindow = $false

    $process = New-Object System.Diagnostics.Process
    $process.StartInfo = $processInfo
    $process.Start() | Out-Null
    $process.WaitForExit()

    if ($process.ExitCode -ne 0) {
        throw "Sync process failed with exit code: $($process.ExitCode)"
    }
}

# 4. Mirror files to content layers
Write-Output "[INFO] Mirroring synced files to raw/docs..."
foreach ($key in $destinations.Keys) {
    $src = Join-Path $OasisSyncRoot "docs\$key"
    $dest = $destinations[$key]

    if (-not (Test-Path -LiteralPath $src)) {
        throw "Sync output directory missing: $src"
    }

    if (Test-Path -LiteralPath $dest) {
        Write-Output "[INFO] Cleaning stale mirror: $dest"
        Remove-Item -LiteralPath $dest -Recurse -Force
    }

    New-Item -ItemType Directory -Path (Split-Path -Parent $dest) -Force | Out-Null
    Write-Output "[INFO] Mirroring: $src -> $dest"
    Copy-Item -LiteralPath $src -Destination $dest -Recurse -Force
    Assert-MirrorComplete -Source $src -Destination $dest
}

Write-Output "[DONE] Local official docs synced and mirrored successfully!"
