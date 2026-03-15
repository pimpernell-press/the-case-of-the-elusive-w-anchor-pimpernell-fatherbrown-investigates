Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# Always resolve PROJECT_ROOT relative to this script, not your current directory.
$PROJECT_ROOT = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path

$buildScript = Join-Path $PROJECT_ROOT "tools\build_book.py"
if (-not (Test-Path $buildScript)) { throw "Build script not found: $buildScript" }

# Prefer a repo-local venv Python if present (more reproducible than system Python).
$venvPython = Join-Path $PROJECT_ROOT ".venv\Scripts\python.exe"
if (Test-Path $venvPython) {
    & $venvPython $buildScript --project-root $PROJECT_ROOT @args
    exit $LASTEXITCODE
}

# Fall back to the Windows Python launcher.
$py = Get-Command py -ErrorAction SilentlyContinue
if (-not $py) {
    throw "Python launcher 'py' not found, and no .venv detected. Install Python for Windows or create .venv."
}

# Try a few common Python versions, newest first.
$versionsToTry = @("3.12", "3.11", "3.10", "3")
$ran = $false

foreach ($v in $versionsToTry) {
    try {
        if ($v -eq "3") {
            & $py.Source -3 $buildScript --project-root $PROJECT_ROOT @args
        } else {
            & $py.Source "-$v" $buildScript --project-root $PROJECT_ROOT @args
        }
        $ran = $true
        exit $LASTEXITCODE
    } catch {
        # keep trying
    }
}

Write-Host "`nNo usable Python found via 'py'. Detected environments:" -ForegroundColor Yellow
& $py.Source --list

throw "Install Python (recommended: winget install -e --id Python.Python.3.12) or create a .venv in the repo."
