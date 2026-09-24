param(
    [string]$Root = 'D:\知识库\和平精英绿洲起源'
)

$ErrorActionPreference = 'Stop'
$utf8 = [System.Text.UTF8Encoding]::new($false)
$wikiRoot = Join-Path $Root 'wiki'
$rawRoot = Join-Path $Root 'raw\知识\通用'

function Write-Utf8NoBom {
    param([string]$Path, [string]$Content)

    $directory = [System.IO.Path]::GetDirectoryName($Path)
    if (-not (Test-Path -LiteralPath $directory)) {
        New-Item -ItemType Directory -Path $directory -Force | Out-Null
    }
    [System.IO.File]::WriteAllText($Path, $Content, $utf8)
}

function Get-RelativePath {
    param([string]$FromDirectory, [string]$ToPath)

    $fromUri = [System.Uri]::new(([System.IO.Path]::GetFullPath($FromDirectory) + [System.IO.Path]::DirectorySeparatorChar))
    $toUri = [System.Uri]::new([System.IO.Path]::GetFullPath($ToPath))
    return [System.Uri]::UnescapeDataString($fromUri.MakeRelativeUri($toUri).ToString())
}

$conceptModules = @{
    '3DUI挂载方案.md' = '程序与网络'
    '存档与数据持久化.md' = '程序与网络'
    '端侧权威与HasAuthority.md' = '程序与网络'
    'RPC分发架构.md' = '程序与网络'
    '蓝图与MCP写入流程.md' = '工具与流程'
    '配置表与结构体的MCP编辑.md' = '工具与流程'
    'UGCAskQ-MCP能力矩阵.md' = '工具与流程'
    'UGCAskQ-MCP实测陷阱清单.md' = '工具与流程'
    'PIE调试与热更新边界.md' = '工具与流程'
    '日志与错误保护规范.md' = '工具与流程'
    '配置表驱动开发.md' = '配置与数据'
    '资源导入与路径规范.md' = '配置与数据'
    '绿洲UI枚举与结构体速查.md' = 'UI与交互'
    '模型渲染与缩放问题.md' = 'UI与交互'
    '图鉴UI高保真还原.md' = 'UI与交互'
    'MCP-UI编辑与高保真还原知识库.md' = 'UI与交互'
    'UI页面切换与Widget生命周期.md' = 'UI与交互'
    'ZhuJieMian画刷现状基线表.md' = 'UI与交互'
    '知识库分层与索引隔离.md' = '知识库治理'
}

$mapping = @{}
foreach ($item in $conceptModules.GetEnumerator()) {
    $source = Join-Path $wikiRoot ('概念\' + $item.Key)
    $target = Join-Path $rawRoot ($item.Value + '\' + $item.Key)
    $mapping[$source] = $target
}

Get-ChildItem -LiteralPath (Join-Path $wikiRoot '来源') -File -Filter '*.md' | ForEach-Object {
    $mapping[$_.FullName] = Join-Path $rawRoot ('来源记录\' + $_.Name)
}

foreach ($source in $mapping.Keys) {
    $target = $mapping[$source]
    $content = [System.IO.File]::ReadAllText($source)
    $content = [regex]::Replace($content, '(?<prefix>\[[^]]+\]\()(?<target>[^)#]+)(?<suffix>(?:#[^)]*)?\))', {
        param($match)
        $linkTarget = $match.Groups['target'].Value
        if ($linkTarget -match '^(https?:|mailto:|file:)' -or $linkTarget -notmatch '\.md$') {
            return $match.Value
        }
        $resolved = [System.IO.Path]::GetFullPath([System.IO.Path]::Combine([System.IO.Path]::GetDirectoryName($source), $linkTarget))
        if ($mapping.ContainsKey($resolved)) {
            $relative = Get-RelativePath -FromDirectory ([System.IO.Path]::GetDirectoryName($target)) -ToPath $mapping[$resolved]
            return $match.Groups['prefix'].Value + $relative + $match.Groups['suffix'].Value
        }
        return $match.Value
    })
    Write-Utf8NoBom -Path $target -Content $content
}

$moduleIndex = @{
    '程序与网络' = '网络与端侧'
    'UI与交互' = 'UI'
    '配置与数据' = '工程规范'
    '工具与流程' = 'UGCAskQ MCP 工具链'
    '知识库治理' = '知识库工程约定'
    '来源记录' = '来源页'
}

foreach ($module in $moduleIndex.Keys) {
    $directory = Join-Path $rawRoot $module
    $files = Get-ChildItem -LiteralPath $directory -File -Filter '*.md' | Sort-Object Name
    $entries = ($files | ForEach-Object { '- [' + $_.BaseName + '](./' + $_.Name + ')' }) -join [Environment]::NewLine
    $content = '# ' + $module + ' 内容目录' + [Environment]::NewLine + [Environment]::NewLine +
        '> 内容层目录。详细正文、代码、教程与证据保存在当前目录；Wiki 仅提供导航。' + [Environment]::NewLine + [Environment]::NewLine +
        $entries + [Environment]::NewLine
    Write-Utf8NoBom -Path (Join-Path $directory '000_目录.md') -Content $content
}

$overview = @'
# 通用知识内容总览

> 职责：保存详细技术正文、代码、操作步骤、实测记录与原始资料摘要。
> Wiki 导航：[wiki/000_索引.md](../../../wiki/000_索引.md)
> 更新：2026-08-26

| 模块 | Raw 内容目录 | Wiki 导航 |
| --- | --- | --- |
| 程序与网络 | [目录](./程序与网络/000_目录.md) | [网络与端侧](../../../wiki/000_索引.md#网络与端侧) |
| UI与交互 | [目录](./UI与交互/000_目录.md) | [UI](../../../wiki/000_索引.md#ui) |
| 配置与数据 | [目录](./配置与数据/000_目录.md) | [工程规范](../../../wiki/000_索引.md#工程规范) |
| 工具与流程 | [目录](./工具与流程/000_目录.md) | [UGCAskQ MCP 工具链](../../../wiki/000_索引.md#ugcaskq-mcp-工具链) |
| 知识库治理 | [目录](./知识库治理/000_目录.md) | [知识库工程约定](../../../wiki/000_索引.md#知识库工程约定) |
| 来源记录 | [目录](./来源记录/000_目录.md) | [来源页](../../../wiki/000_索引.md#来源页) |
'@
Write-Utf8NoBom -Path (Join-Path $rawRoot '000_内容总览.md') -Content $overview

foreach ($source in $mapping.Keys) {
    $target = $mapping[$source]
    $original = [System.IO.File]::ReadAllText($target)
    $titleMatch = [regex]::Match($original, '(?m)^#\s+(.+)$')
    $title = if ($titleMatch.Success) { $titleMatch.Groups[1].Value.Trim() } else { [System.IO.Path]::GetFileNameWithoutExtension($source) }
    $sourceMatch = [regex]::Match($original, '(?m)^>\s*来源[：:].+$')
    $sourceLine = if ($sourceMatch.Success) { $sourceMatch.Value } else { '> 来源：迁移前 Wiki 正文（2026-08-26）' }
    $relativeRaw = Get-RelativePath -FromDirectory ([System.IO.Path]::GetDirectoryName($source)) -ToPath $target
    $stubType = if ($source -like '*\概念\*') { '概念索引' } else { '来源索引' }
    $stub = '# ' + $title + [Environment]::NewLine + [Environment]::NewLine +
        '> 类型：' + $stubType + [Environment]::NewLine + $sourceLine + [Environment]::NewLine +
        '> 正文位置：[' + $title + ' 正文](' + $relativeRaw + ')' + [Environment]::NewLine +
        '> 最近迁移：2026-08-26' + [Environment]::NewLine + [Environment]::NewLine +
        '## 索引摘要' + [Environment]::NewLine + [Environment]::NewLine +
        '详细结论、代码、步骤、证据和待查证项已迁入 Raw 内容层；本页只保留导航。' + [Environment]::NewLine + [Environment]::NewLine +
        '- **Raw 正文**：[' + $title + ' 正文](' + $relativeRaw + ')' + [Environment]::NewLine +
        '- **内容层总览**：[raw/知识/通用/000_内容总览.md](../../raw/知识/通用/000_内容总览.md)' + [Environment]::NewLine
    Write-Utf8NoBom -Path $source -Content $stub
}
