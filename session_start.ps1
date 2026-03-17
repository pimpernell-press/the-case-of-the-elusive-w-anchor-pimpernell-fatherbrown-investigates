# =============================================================
#  W-ANCHOR PROTOCOL — SESSION START  (4-repo coordinator)
#  Works from ANY of the 4 repo roots — run as .\session_start.ps1
#  2026-03-17 — Phase 5 added: progress log read at session open
# =============================================================

$ErrorActionPreference = "Continue"

$REPOS = @(
    [ordered]@{ Name = "reproducible-self-pub-kit"; Path = "C:\Users\peewe\OneDrive\Desktop\reproducible-self-pub-kit";                                               Anchor = "anchor_verify.ps1"; Remote = "https://github.com/tonefreqhz/reproducible-self-pub-kit" },
    [ordered]@{ Name = "hom-ixFAIRindex";           Path = "C:\Users\peewe\OneDrive\Desktop\homeix";                                                                   Anchor = "anchor_verify.ps1"; Remote = "https://github.com/tonefreqhz/hom-ixFAIRindex" },
    [ordered]@{ Name = "DoughForge";                Path = "C:\Users\peewe\Documents\DoughForge";                                                                      Anchor = "anchor_verify.ps1"; Remote = "https://github.com/tonefreqhz/DoughForge" },
    [ordered]@{ Name = "pimpernell-fatherbrown";    Path = "C:\Users\peewe\OneDrive\Desktop\the-case-of-the-elusive-w-anchor-pimpernell-fatherbrown-investigates";     Anchor = "anchor_verify.ps1"; Remote = "https://github.com/pimpernell-press/the-case-of-the-elusive-w-anchor-pimpernell-fatherbrown-investigates" }
)

# ── Helpers ───────────────────────────────────────────────────
function Banner($t) {
    $line = "=" * 62
    Write-Host ""; Write-Host $line -ForegroundColor Cyan
    Write-Host "  $t" -ForegroundColor Cyan
    Write-Host $line -ForegroundColor Cyan
}

function Row($label, $val, $col = "Green") {
    Write-Host ("  [{0}] {1}" -f $label.PadRight(28), $val) -ForegroundColor $col
}

# ── Collect results ───────────────────────────────────────────
$results = @{}
foreach ($r in $REPOS) { $results[$r.Name] = @{ anchor="?"; pull="?"; diff=""; ahead=0; push="?" } }

# ═══════════════════════════════════════════════════════════════
Banner "PHASE 1  --  ANCHOR VERIFY"

foreach ($repo in $REPOS) {
    Write-Host ""
    Write-Host "  >> $($repo.Name)" -ForegroundColor Yellow
    if (-not (Test-Path $repo.Path)) {
        Row "MISSING" $repo.Path "Red"
        $results[$repo.Name].anchor = "MISSING"; continue
    }
    $script = Join-Path $repo.Path $repo.Anchor
    if (-not (Test-Path $script)) {
        Row "NO ANCHOR" $script "Red"
        $results[$repo.Name].anchor = "NO ANCHOR"; continue
    }
    Push-Location $repo.Path
    & ".\$($repo.Anchor)" 2>&1 | ForEach-Object { Write-Host "    $_" }
    $results[$repo.Name].anchor = "OK"
    Pop-Location
}

# ═══════════════════════════════════════════════════════════════
Banner "PHASE 2  --  GIT PULL"

foreach ($repo in $REPOS) {
    if (-not (Test-Path $repo.Path)) { $results[$repo.Name].pull = "SKIP"; continue }
    Write-Host ""; Write-Host "  >> $($repo.Name)" -ForegroundColor Yellow
    Push-Location $repo.Path
    git pull 2>&1 | ForEach-Object { Write-Host "    $_" }
    $results[$repo.Name].pull = if ($LASTEXITCODE -eq 0) { "OK" } else { "ERROR" }
    Pop-Location
}

# ═══════════════════════════════════════════════════════════════
Banner "PHASE 3  --  GIT DIFF / STATUS"

foreach ($repo in $REPOS) {
    if (-not (Test-Path $repo.Path)) { $results[$repo.Name].diff = "SKIP"; continue }
    Write-Host ""; Write-Host "  >> $($repo.Name)" -ForegroundColor Yellow
    Push-Location $repo.Path

    $branch = (git branch --show-current 2>&1) -join ""
    $short  = git status --short 2>&1
    $ahead  = (git rev-list --count "@{u}..HEAD" 2>&1) -join ""
    if ($ahead -notmatch "^\d+$") { $ahead = "0" }

    Write-Host "    Branch : $branch"
    Write-Host "    Ahead  : $ahead commit(s) unpushed"

    if ($short) {
        Write-Host "    Diff   :" -ForegroundColor Yellow
        $short | ForEach-Object { Write-Host "      $_" -ForegroundColor Yellow }
        git diff --stat 2>&1 | ForEach-Object { Write-Host "      $_" }
    } else {
        Write-Host "    Diff   : (clean)" -ForegroundColor Green
    }

    $results[$repo.Name].diff  = if ($short) { ($short -join "; ") } else { "clean" }
    $results[$repo.Name].ahead = [int]$ahead
    Pop-Location
}

# ═══════════════════════════════════════════════════════════════
Banner "PHASE 4  --  GIT ADD / COMMIT / PUSH"

$STAMP = Get-Date -Format "yyyy-MM-dd HH:mm"

foreach ($repo in $REPOS) {
    if (-not (Test-Path $repo.Path)) { $results[$repo.Name].push = "SKIP"; continue }
    Write-Host ""; Write-Host "  >> $($repo.Name)" -ForegroundColor Yellow
    Push-Location $repo.Path

    $short = git status --short 2>&1
    $ahead = $results[$repo.Name].ahead

    if ($short) {
        Write-Host "    Staging all changes..." -ForegroundColor Yellow
        git add -A 2>&1 | ForEach-Object { Write-Host "    $_" }
        $msg = "chore: session sync $STAMP [W-Anchor auto-commit]"
        git commit -m $msg 2>&1 | ForEach-Object { Write-Host "    $_" }
        $ahead = [int]((git rev-list --count "@{u}..HEAD" 2>&1) -join "")
    }

    if ($ahead -gt 0) {
        Write-Host "    Pushing $ahead commit(s)..." -ForegroundColor Yellow
        git push 2>&1 | ForEach-Object { Write-Host "    $_" }
        $results[$repo.Name].push = if ($LASTEXITCODE -eq 0) { "PUSHED $ahead" } else { "PUSH ERROR" }
    } else {
        Write-Host "    Nothing to push." -ForegroundColor Green
        $results[$repo.Name].push = "UP TO DATE"
    }
    Pop-Location
}

# ═══════════════════════════════════════════════════════════════
Banner "PHASE 5  --  PROGRESS LOGS"

foreach ($repo in $REPOS) {
    $logPath = Join-Path $repo.Path "INTERIM_PROGRESS_LOG.md"
    Write-Host ""
    Write-Host "  >> $($repo.Name)" -ForegroundColor Yellow
    if (Test-Path $logPath) {
        Write-Host "  [OK] $logPath" -ForegroundColor Green
        Get-Content $logPath | Select-Object -First 20 | ForEach-Object {
            Write-Host "       $_"
        }
    } else {
        Write-Host "  [MISSING] INTERIM_PROGRESS_LOG.md" -ForegroundColor Red
    }
}

# ═══════════════════════════════════════════════════════════════
Banner "SESSION STATE SUMMARY  --  paste to AI"

Write-Host ""
Write-Host "  ------- COPY FROM HERE -------" -ForegroundColor Magenta
Write-Host ""
Write-Host "  SESSION  : $STAMP"
Write-Host "  MACHINE  : $env:COMPUTERNAME"
Write-Host ""
Write-Host "  REPO STATUS:"
foreach ($repo in $REPOS) {
    $r = $results[$repo.Name]
    $line = "    {0}  anchor={1}  pull={2}  push={3}  diff={4}" -f `
        $repo.Name.PadRight(36), $r.anchor, $r.pull, $r.push, $r.diff
    $col = if ($r.anchor -eq "OK" -and $r.pull -ne "ERROR") { "Green" } else { "Red" }
    Write-Host $line -ForegroundColor $col
}
Write-Host ""
Write-Host "  PROGRESS LOGS:"
foreach ($repo in $REPOS) {
    $logPath = Join-Path $repo.Path "INTERIM_PROGRESS_LOG.md"
    if (Test-Path $logPath) {
        Write-Host "    [OK     ] $($repo.Name.PadRight(36)) $logPath" -ForegroundColor Green
        Get-Content $logPath | Select-Object -First 20 | ForEach-Object {
            Write-Host "             $_"
        }
    } else {
        Write-Host "    [MISSING] $($repo.Name)" -ForegroundColor Red
    }
    Write-Host ""
}
Write-Host "  ACTIVE PROJECTS:"
Write-Host "    DoughForge           -- philosoetry audio ch03-ch25 COMPLETE (23/23)"
Write-Host "    DoughForge           -- publisher bundle: tools\build_publisher_bundle.py"
Write-Host "    reproducible-kit     -- session_start.ps1 4-repo coordinator LIVE"
Write-Host "    hom-ixFAIRindex      -- FAIR housing index pipeline"
Write-Host "    pimpernell-press     -- Father Brown / W-Anchor book"
Write-Host ""
Write-Host "  REMOTE REPOS:"
foreach ($repo in $REPOS) {
    Write-Host "    $($repo.Name.PadRight(36)) $($repo.Remote)"
}
Write-Host ""
Write-Host "  ------- COPY TO HERE -------" -ForegroundColor Magenta
Write-Host ""
Banner "SESSION OPEN  --  ALL 4 REPOS ANCHORED"
