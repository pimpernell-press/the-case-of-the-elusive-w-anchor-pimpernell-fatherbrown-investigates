param(
  [string]$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path,
  [string]$ChaptersDir = "inputs\canonical\chapters",
  [string]$OutFile     = "publication\pamphlet_issue_1.md"
)

$ErrorActionPreference = "Stop"

$chaptersPath = Join-Path $ProjectRoot $ChaptersDir
$outPath      = Join-Path $ProjectRoot $OutFile

if (-not (Test-Path $chaptersPath)) { throw "Missing chapters folder: $chaptersPath" }

$files = Get-ChildItem -LiteralPath $chaptersPath -File -Filter "*.md" | Sort-Object Name
if (-not $files) { throw "No chapter .md files found in: $chaptersPath" }

New-Item -ItemType Directory -Force -Path (Split-Path $outPath -Parent) | Out-Null

$header = @(
  "<!-- AUTO-GENERATED FILE: do not hand-edit -->",
  "<!-- Source: inputs/canonical/chapters/*.md -->",
  "<!-- Built:  $(Get-Date -Format o) -->",
  ""
) -join "`r`n"

Set-Content -LiteralPath $outPath -Encoding UTF8 -Value $header

foreach ($f in $files) {
  Add-Content -LiteralPath $outPath -Encoding UTF8 -Value ("`r`n<!-- BEGIN: " + $f.Name + " -->`r`n")
  Get-Content -LiteralPath $f.FullName -Raw | Add-Content -LiteralPath $outPath -Encoding UTF8
  Add-Content -LiteralPath $outPath -Encoding UTF8 -Value ("`r`n<!-- END: " + $f.Name + " -->`r`n`r`n---`r`n")
}

Write-Host "Assembled" $files.Count "chapters ->" $outPath
