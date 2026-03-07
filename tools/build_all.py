import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # Add repo root to path for anchor import
$ErrorActionPreference = "Stop"

# Always resolve PROJECT_ROOT relative to this script (not the current directory).
$PROJECT_ROOT = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path

# Locate Python launcher
$py = Get-Command py -ErrorAction SilentlyContinue
if (-not $py) { throw "Python launcher 'py' not found. Install Python for Windows (adds 'py')." }

# Target script (fail fast if it moved/renamed)
$script = Join-Path $PROJECT_ROOT "tools\build_book.py"
if (-not (Test-Path $script)) { throw "Build script not found: $script" }

# Execute
Write-Host "PROJECT_ROOT=$PROJECT_ROOT"
Write-Host "RUN: $($py.Source) `"$script`" --project-root `"$PROJECT_ROOT`""
& $py.Source $script --project-root $PROJECT_ROOT

