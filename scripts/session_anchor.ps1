Set-StrictMode -Version Latest
$ErrorActionPreference = "Continue"

# ─── Resolve paths ─────────────────────────────────────────
$SCRIPT_DIR = $PSScriptRoot
$PROJECT_ROOT = (Resolve-Path (Join-Path $SCRIPT_DIR "..")).Path
$DRIFT_LOG = Join-Path $PROJECT_ROOT "logs\DRIFT_LOG.csv"
$ATTESTATION_JSON = Join-Path $PROJECT_ROOT "dist\BUILD_ATTESTATION.json"

Write-Host ""
Write-Host "================================================================"
Write-Host " SESSION ANCHOR — M4"
Write-Host "================================================================"
Write-Host ""

# ─── Git state ─────────────────────────────────────────────
Push-Location $PROJECT_ROOT

$branch = (git branch --show-current 2>&1) -join ""
$lastHash = (git rev-parse --short HEAD 2>&1) -join ""
$lastMsg = (git log -1 --format="%s" 2>&1) -join ""
$status = git status --porcelain 2>&1
$clean = if ($status) { "DIRTY" } else { "CLEAN" }
$untracked = ($status | Where-Object { $_ -match "^\?\?" }).Count

Write-Host "  Branch   : $branch"
Write-Host "  Commit   : $lastHash — $lastMsg"
Write-Host "  Status   : $clean"
if ($untracked -gt 0) {
    Write-Host "  Untracked: $untracked file(s)" -ForegroundColor Yellow
}

Pop-Location
Write-Host ""

# ─── Key paths ─────────────────────────────────────────────
Write-Host "  Key Paths:" -ForegroundColor Cyan
$keyPaths = @{
    "manuscripts/" = Join-Path $PROJECT_ROOT "manuscripts"
    "scripts/"     = Join-Path $PROJECT_ROOT "scripts"
    "dist/"        = Join-Path $PROJECT_ROOT "dist"
    "logs/"        = Join-Path $PROJECT_ROOT "logs"
    "widgets/"     = Join-Path $PROJECT_ROOT "widgets"
}

foreach ($label in $keyPaths.Keys | Sort-Object) {
    $p = $keyPaths[$label]
    if (Test-Path $p) {
        Write-Host ("    [OK     ] {0}" -f $label)
    } else {
        Write-Host ("    [MISSING] {0}" -f $label) -ForegroundColor Red
    }
}
Write-Host ""

# ─── Drift Log (last 3 entries) ───────────────────────────
Write-Host "  Drift Log (last 3):" -ForegroundColor Cyan
if (Test-Path $DRIFT_LOG) {
    $lines = Get-Content $DRIFT_LOG
    $dataLines = $lines | Select-Object -Skip 1  # skip header
    $last3 = $dataLines | Select-Object -Last 3
    if ($last3) {
        $last3 | ForEach-Object { Write-Host "    $_" }
    } else {
        Write-Host "    (no entries yet)"
    }
} else {
    Write-Host "    [MISSING] logs/DRIFT_LOG.csv" -ForegroundColor Yellow
}
Write-Host ""

# ─── Build Attestation ────────────────────────────────────
Write-Host "  Build Attestation:" -ForegroundColor Cyan
if (Test-Path $ATTESTATION_JSON) {
    try {
        $att = Get-Content $ATTESTATION_JSON -Raw | ConvertFrom-Json
        $pass = if ($att.overall_pass) { "PASS" } else { "FAIL" }
        $col = if ($att.overall_pass) { "Green" } else { "Red" }
        Write-Host "    Status    : $pass" -ForegroundColor $col
        Write-Host "    Timestamp : $($att.timestamp)"
        Write-Host "    Commit    : $($att.commit_hash.Substring(0,12))"
    } catch {
        Write-Host "    [ERROR] Could not parse BUILD_ATTESTATION.json" -ForegroundColor Red
    }
} else {
    Write-Host "    [not yet] No build attestation. Run: python scripts/build_attestation.py" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "  ─────── SESSION ANCHOR BLOCK (paste to LLM) ───────" -ForegroundColor Magenta

Push-Location $PROJECT_ROOT
$stamp = Get-Date -Format "yyyy-MM-dd HH:mm"
$commitFull = (git rev-parse HEAD 2>&1) -join ""
Pop-Location

Write-Host ""
Write-Host "  SESSION: $stamp"
Write-Host "  REPO: the-case-of-the-elusive-w-anchor"
Write-Host "  BRANCH: $branch"
Write-Host "  COMMIT: $commitFull"
Write-Host "  STATUS: $clean"

if (Test-Path $ATTESTATION_JSON) {
    try {
        $att2 = Get-Content $ATTESTATION_JSON -Raw | ConvertFrom-Json
        Write-Host "  ATTESTATION: $($att2.overall_pass) ($($att2.timestamp))"
    } catch {}
}

if (Test-Path $DRIFT_LOG) {
    $lastEntry = (Get-Content $DRIFT_LOG | Select-Object -Last 1)
    Write-Host "  LAST_DRIFT: $lastEntry"
}

Write-Host ""
Write-Host "  ─────── END ANCHOR BLOCK ───────" -ForegroundColor Magenta
Write-Host ""
