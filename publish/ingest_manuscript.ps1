param(
  [Parameter(Mandatory=$true)][string]$InputPath,
  [string]$Title = "Manuscript",
  [string]$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path,
  [switch]$WipeCanonicalChapters
)

$ErrorActionPreference = "Stop"

function Get-FileHashHex([string]$p) {
  return (Get-FileHash -Algorithm SHA256 -LiteralPath $p).Hash.ToLowerInvariant()
}

function New-JobId() {
  return (Get-Date -Format "yyyy-MM-dd_HHmmss") + "_" + ([guid]::NewGuid().ToString("N").Substring(0,8))
}

$inputFull = Resolve-Path -LiteralPath $InputPath
$ext = [IO.Path]::GetExtension($inputFull.Path).ToLowerInvariant()

$jobId = New-JobId
$incomingDir = Join-Path $ProjectRoot ("manuscripts\incoming\" + $jobId)
$stagingDir  = Join-Path $ProjectRoot ("manuscripts\staging\"  + $jobId)
$reportsDir  = Join-Path $ProjectRoot "publication\_reports"

New-Item -ItemType Directory -Force -Path $incomingDir, $stagingDir, $reportsDir | Out-Null

$originalName = "original" + $ext
$originalPath = Join-Path $incomingDir $originalName
Copy-Item -LiteralPath $inputFull.Path -Destination $originalPath -Force

$hash = Get-FileHashHex $originalPath
$normalizedMd = Join-Path $stagingDir "normalized.md"
$reportPath   = Join-Path $reportsDir ("ingest_" + $jobId + ".txt")

# Tool checks
Get-Command pandoc -ErrorAction Stop | Out-Null

$notes = New-Object System.Collections.Generic.List[string]
$notes.Add("INGEST JOB: $jobId")
$notes.Add("Title:      $Title")
$notes.Add("Input:      $($inputFull.Path)")
$notes.Add("Copied To:  $originalPath")
$notes.Add("SHA256:     $hash")
$notes.Add("Time:       $(Get-Date -Format o)")
$notes.Add("")

switch ($ext) {
  ".md" {
    Copy-Item -LiteralPath $originalPath -Destination $normalizedMd -Force
    $notes.Add("Normalize: md -> normalized.md (copy)")
  }
  ".html" {
    pandoc $originalPath -f html -t gfm --wrap=none -o $normalizedMd
    $notes.Add("Normalize: html -> gfm (pandoc)")
  }
  ".htm"  {
    pandoc $originalPath -f html -t gfm --wrap=none -o $normalizedMd
    $notes.Add("Normalize: html -> gfm (pandoc)")
  }
  ".docx" {
    pandoc $originalPath -f docx -t gfm --wrap=none -o $normalizedMd
    $notes.Add("Normalize: docx -> gfm (pandoc)")
  }
  ".pdf" {
    $pdftotext = Get-Command pdftotext -ErrorAction SilentlyContinue
    if (-not $pdftotext) {
      throw "PDF input requires 'pdftotext' (Poppler). Install Poppler and ensure pdftotext is on PATH."
    }

    $txtPath = Join-Path $stagingDir "extracted.txt"
    & $pdftotext.Source "-layout" $originalPath $txtPath | Out-Null

    if (-not (Test-Path $txtPath)) { throw "pdftotext failed to produce: $txtPath" }

    $raw = Get-Content -LiteralPath $txtPath -Raw
    $md = @(
      "# $Title",
      "",
      "<!-- SOURCE: PDF text extraction; review formatting carefully -->",
      "",
      $raw.Trim()
    ) -join "`r`n"

    Set-Content -LiteralPath $normalizedMd -Encoding UTF8 -Value ($md + "`r`n")
    $notes.Add("Normalize: pdf -> text (pdftotext) -> normalized.md (wrapped)")
    $notes.Add("WARNING: PDF normalization is best-effort; headings/splitting may require manual cleanup.")
  }
  default {
    throw "Unsupported input type: $ext (supported: .docx .pdf .md .html)"
  }
}

$notes.Add("Normalized: $normalizedMd")
$notes | Set-Content -LiteralPath $reportPath -Encoding UTF8

# Split into canonical chapters
$splitArgs = @{
  NormalizedMdPath = $normalizedMd
  ProjectRoot      = $ProjectRoot
}
if ($WipeCanonicalChapters) { $splitArgs["WipeOutDir"] = $true }

& (Join-Path $PSScriptRoot "split_normalized_md.ps1") @splitArgs

# Assemble to build input
& (Join-Path $PSScriptRoot "assemble_chapters.ps1") -ProjectRoot $ProjectRoot

Write-Host "Ingest complete. Report:" $reportPath
