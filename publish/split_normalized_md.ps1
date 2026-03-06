param(
  [Parameter(Mandatory=$true)][string]$NormalizedMdPath,
  [string]$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path,
  [string]$OutDir      = "inputs\canonical\chapters",
  [switch]$WipeOutDir
)

$ErrorActionPreference = "Stop"

function Slugify([string]$s) {
  $t = $s.ToLowerInvariant().Trim()
  $t = $t -replace "[^a-z0-9\s\-]", ""
  $t = $t -replace "\s+", "-"
  $t = $t -replace "\-+", "-"
  if ([string]::IsNullOrWhiteSpace($t)) { return "chapter" }
  return $t
}

$normPath = Resolve-Path -LiteralPath $NormalizedMdPath
$outPath  = Join-Path $ProjectRoot $OutDir

if (-not (Test-Path $normPath)) { throw "Normalized markdown not found: $NormalizedMdPath" }

New-Item -ItemType Directory -Force -Path $outPath | Out-Null

if ($WipeOutDir) {
  Get-ChildItem -LiteralPath $outPath -File -Filter "*.md" | Remove-Item -Force
}

$text = Get-Content -LiteralPath $normPath -Raw

# Find H1 headings (# Title)
$matches = [regex]::Matches($text, "(?m)^(#\s+.+)\s*$")
if ($matches.Count -eq 0) {
  $one = Join-Path $outPath "0001-manuscript.md"
  Set-Content -LiteralPath $one -Encoding UTF8 -Value ($text.Trim() + "`r`n")
  Write-Host "No H1 headings found. Wrote single chapter:" $one
  return
}

# Split keeping headings
$indices = @()
foreach ($m in $matches) { $indices += $m.Index }
$indices += $text.Length

for ($i = 0; $i -lt $matches.Count; $i++) {
  $start = $matches[$i].Index
  $end   = $indices[$i + 1]
  $chunk = $text.Substring($start, $end - $start).Trim()

  $titleLine = $matches[$i].Groups[1].Value.Trim()
  $title = ($titleLine -replace "^\#\s+", "").Trim()
  $slug = Slugify $title

  $n = "{0:D4}" -f ($i + 1)
  $fileName = "$n-$slug.md"
  $dest = Join-Path $outPath $fileName

  Set-Content -LiteralPath $dest -Encoding UTF8 -Value ($chunk + "`r`n")
  Write-Host "Wrote:" $fileName
}

Write-Host "Split complete ->" $outPath
