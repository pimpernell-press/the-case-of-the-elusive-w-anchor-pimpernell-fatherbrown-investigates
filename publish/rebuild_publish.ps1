$ErrorActionPreference = "Stop"

# Always resolve PROJECT_ROOT relative to this script, not your current directory.
$PROJECT_ROOT = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
Write-Host "PROJECT_ROOT = $PROJECT_ROOT"

$py = (Get-Command py -ErrorAction SilentlyContinue)
if (-not $py) { throw "Python launcher 'py' not found. Install Python for Windows." }

& $py.Source (Join-Path $PROJECT_ROOT "tools\build_book.py") --project-root $PROJECT_ROOT
