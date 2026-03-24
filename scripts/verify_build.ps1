Set-StrictMode -Version Latest
$ErrorActionPreference = "Continue"

# ─── Resolve paths ─────────────────────────────────────────
$SCRIPT_DIR = $PSScriptRoot
$PROJECT_ROOT = (Resolve-Path (Join-Path $SCRIPT_DIR "..")).Path
$ATTESTATION = Join-Path $PROJECT_ROOT "scripts\build_attestation.py"
$BUILD_PS1 = Join-Path $PROJECT_ROOT "scripts\build.ps1"
$SUMMARY = Join-Path $PROJECT_ROOT "dist\BUILD_SUMMARY.md"

Write-Host ""
Write-Host "================================================================"
Write-Host " DOUGHFORGE BUILD VERIFICATION — M9, M12"
Write-Host "================================================================"
Write-Host ""

# ─── Phase 1: Environment Check ───────────────────────────
Write-Host "  PHASE 1: Environment" -ForegroundColor Cyan
$allTools = $true

# Python
$py = Get-Command python -ErrorAction SilentlyContinue
if (-not $py) { $py = Get-Command py -ErrorAction SilentlyContinue }
if ($py) {
    $pyVer = & $py.Source --version 2>&1
    Write-Host "  [OK     ] Python        $pyVer"
} else {
    Write-Host "  [MISSING] Python        not found" -ForegroundColor Red
    $allTools = $false
}

# Pandoc
$pandoc = Get-Command pandoc -ErrorAction SilentlyContinue
if ($pandoc) {
    $pVer = (& pandoc --version 2>&1) | Select-Object -First 1
    Write-Host "  [OK     ] Pandoc        $pVer"
} else {
    Write-Host "  [MISSING] Pandoc        not found (EPUB/PDF build will fail)" -ForegroundColor Yellow
}

# LuaLaTeX
$lua = Get-Command lualatex -ErrorAction SilentlyContinue
if ($lua) {
    $lVer = (& lualatex --version 2>&1) | Select-Object -First 1
    Write-Host "  [OK     ] LuaLaTeX      $lVer"
} else {
    Write-Host "  [MISSING] LuaLaTeX      not found (PDF build will fail)" -ForegroundColor Yellow
}

if (-not $allTools) {
    Write-Host ""
    Write-Host "  STOP: Required tools missing. Cannot proceed." -ForegroundColor Red
    exit 1
}

Write-Host ""

# ─── Phase 2: Run Build (if build script exists) ──────────
Write-Host "  PHASE 2: Build" -ForegroundColor Cyan
if (Test-Path $BUILD_PS1) {
    Write-Host "  Running scripts\build.ps1 ..."
    Push-Location $PROJECT_ROOT
    try {
        & $BUILD_PS1 2>&1 | ForEach-Object { Write-Host "    $_" }
        if ($LASTEXITCODE -ne 0) {
            Write-Host "  [WARN] Build returned exit code $LASTEXITCODE" -ForegroundColor Yellow
        } else {
            Write-Host "  [OK] Build completed."
        }
    } catch {
        Write-Host "  [WARN] Build error: $_" -ForegroundColor Yellow
    }
    Pop-Location
} else {
    Write-Host "  [SKIP] scripts\build.ps1 not found — running attestation only."
}
Write-Host ""

# ─── Phase 3: Run Build Attestation ───────────────────────
Write-Host "  PHASE 3: Attestation" -ForegroundColor Cyan
if (-not (Test-Path $ATTESTATION)) {
    Write-Host "  [MISSING] build_attestation.py not found at $ATTESTATION" -ForegroundColor Red
    exit 1
}

Push-Location $PROJECT_ROOT
$pyCmd = if ($py) { $py.Source } else { "python" }
& $pyCmd $ATTESTATION 2>&1 | ForEach-Object { Write-Host "    $_" }
$attExit = $LASTEXITCODE
Pop-Location

Write-Host ""

# ─── Phase 4: Print Summary ──────────────────────────────
Write-Host "  PHASE 4: Summary" -ForegroundColor Cyan
if (Test-Path $SUMMARY) {
    Get-Content $SUMMARY | ForEach-Object { Write-Host "    $_" }
} else {
    Write-Host "  [MISSING] BUILD_SUMMARY.md was not generated." -ForegroundColor Red
}

Write-Host ""
if ($attExit -eq 0) {
    Write-Host "  ════════════════════════════════════════" -ForegroundColor Green
    Write-Host "  BUILD VERIFICATION: PASS" -ForegroundColor Green
    Write-Host "  ════════════════════════════════════════" -ForegroundColor Green
} else {
    Write-Host "  ════════════════════════════════════════" -ForegroundColor Red
    Write-Host "  BUILD VERIFICATION: FAIL" -ForegroundColor Red
    Write-Host "  ════════════════════════════════════════" -ForegroundColor Red
}
Write-Host ""

exit $attExit
