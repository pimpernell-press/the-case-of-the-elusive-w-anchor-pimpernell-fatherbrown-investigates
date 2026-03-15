# publish\diagnose_title_and_metadata.ps1
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

Write-Host "=== PROJECT ROOT ==="
$root = (git rev-parse --show-toplevel).Trim()
Set-Location $root
pwd

$canonManuscript = ".\publication\pamphlet_issue_1.md"
$canonMetadata   = ".\publication\metadata_pamphlet_issue_1.md"

Write-Host "`n=== CANONICAL PATHS (per PRINT_AND_BUILD_NOTES.md) ==="
"{0} -> {1}" -f $canonManuscript, (Test-Path $canonManuscript)
"{0} -> {1}" -f $canonMetadata,   (Test-Path $canonMetadata)

Write-Host "`n=== TOP OF CANONICAL METADATA (first 40 lines) ==="
if (Test-Path $canonMetadata) { Get-Content $canonMetadata -TotalCount 40 } else { Write-Host "MISSING: $canonMetadata" }

Write-Host "`n=== TOP OF CANONICAL MANUSCRIPT (first 60 lines) ==="
if (Test-Path $canonManuscript) { Get-Content $canonManuscript -TotalCount 60 } else { Write-Host "MISSING: $canonManuscript" }

Write-Host "`n=== TITLE LEAK SEARCH (repo-wide) ==="
Get-ChildItem -Path . -Recurse -File | Select-String -Pattern `
  "title\s*:\s*.*Manuscript|SelfPub Kit - Manuscript|title=manuscript|--metadata(\s|=)title|display_title\s*=|manuscript\.pdf|manuscript\.epub|manuscript\.docx" `
  -Context 2,2

Write-Host "`n=== PANDOC CALL SITES (repo-wide) ==="
Get-ChildItem -Path . -Recurse -File | Select-String -Pattern "pandoc\s" -Context 2,2

Write-Host "`n=== BUILD (current pipeline) ==="
.\publish\rebuild_publish.ps1

Write-Host "`n=== OPEN PDF (for quick eyeball) ==="
if (Test-Path ".\outputs\pdf\manuscript.pdf") { Start-Process .\outputs\pdf\manuscript.pdf } else { Write-Host "Missing outputs\pdf\manuscript.pdf" }

