Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# Always resolve PROJECT_ROOT relative to this script, not your current directory.
$PROJECT_ROOT = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path

# Prefer a repo-local venv Python if present (more reproducible than system Python).
$venvPython = Join-Path $PROJECT_ROOT ".venv\Scripts\python.exe"

if (Test-Path $venvPython) {
    $pythonExe = $venvPython
} else {
    $py = Get-Command py -ErrorAction SilentlyContinue
    if (-not $py) { throw "Python launcher 'py' not found, and no .venv detected. Install Python for Windows or create .venv." }
    # Use the launcher but target a consistent Python (tweak -3.11 to your chosen version).
    $pythonExe = $py.Source
}

$buildScript = Join-Path $PROJECT_ROOT "tools\build_book.py"
if (-not (Test-Path $buildScript)) { throw "Build script not found: $buildScript" }

# Forward any additional CLI args passed to this .ps1 (e.g. --all, --pdf-only, etc.)
if ($pythonExe -like "*\py.exe") {
    & $pythonExe -3.11 $buildScript --project-root $PROJECT_ROOT @args
} else {
    & $pythonExe $buildScript --project-root $PROJECT_ROOT @args
}
