param(
    [Parameter(Mandatory = $true)]
    [ValidateNotNullOrEmpty()]
    [string]$Path
)

function Read-BigEndianUInt32([byte[]]$Data, [int]$Offset) {
    return [uint32](
        ([uint32]$Data[$Offset] * 16777216) +
        ([uint32]$Data[$Offset + 1] * 65536) +
        ([uint32]$Data[$Offset + 2] * 256) +
        [uint32]$Data[$Offset + 3])
}

$resolved = Resolve-Path -LiteralPath $Path -ErrorAction Stop
$file = Get-Item -LiteralPath $resolved.Path -ErrorAction Stop
if ($file.PSIsContainer -or $file.Length -le 0) {
    throw "PNG file is missing or empty: $($resolved.Path)"
}

$bytes = [IO.File]::ReadAllBytes($resolved.Path)
$signature = [byte[]](137, 80, 78, 71, 13, 10, 26, 10)
if ($bytes.Length -lt 24) {
    throw "PNG file is too short: $($resolved.Path)"
}

for ($i = 0; $i -lt $signature.Length; $i++) {
    if ($bytes[$i] -ne $signature[$i]) {
        throw "Invalid PNG signature: $($resolved.Path)"
    }
}

$ihdrLength = Read-BigEndianUInt32 $bytes 8
$ihdrType = [Text.Encoding]::ASCII.GetString($bytes, 12, 4)
if ($ihdrLength -ne 13 -or $ihdrType -ne 'IHDR') {
    throw "PNG IHDR chunk is invalid: $($resolved.Path)"
}

$width = Read-BigEndianUInt32 $bytes 16
$height = Read-BigEndianUInt32 $bytes 20
if ($width -eq 0 -or $height -eq 0) {
    throw "PNG dimensions must be positive: $($resolved.Path)"
}

[pscustomobject]@{
    Path = $resolved.Path
    Bytes = $file.Length
    Width = $width
    Height = $height
    Format = 'PNG'
}
