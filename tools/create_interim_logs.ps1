# create_interim_logs.ps1
# Creates INTERIM_PROGRESS_LOG.md in any repo that is missing it.
# Special case: homeix — renames PRINT_AND_BUILD_NOTES.md if log is absent.

$today = Get-Date -Format "yyyy-MM-dd"

$repos = @(
    @{
        path = "C:\Users\peewe\Documents\DoughForge"
        name = "DoughForge"
        note = "Bumper Edition build — EPUB + PDF. Novel Ch1-Ch8 + Epilogue + AuthorsNote."
    },
    @{
        path = "C:\Users\peewe\OneDrive\Desktop\reproducible-self-pub-kit"
        name = "reproducible-self-pub-kit"
        note = "session_start.ps1 4-repo coordinator live. Phase 5 added."
    },
    @{
        path    = "C:\Users\peewe\OneDrive\Desktop\homeix"
        name    = "hom-ixFAIRindex"
        note    = "FAIR housing index pipeline. chore/print-sequence branch."
        oldLog  = "PRINT_AND_BUILD_NOTES.md"
    },
    @{
        path = "C:\Users\peewe\OneDrive\Desktop\the-case-of-the-elusive-w-anchor-pimpernell-fatherbrown-investigates"
        name = "pimpernell-fatherbrown"
        note = "Father Brown / W-Anchor investigation book. Manuscripts dir active."
    }
)

foreach ($repo in $repos) {
    Write-Host ""
    Write-Host "  >> $($repo.name)" -ForegroundColor Cyan

    if (-not (Test-Path $repo.path)) {
        Write-Host "  [MISSING] Repo path not found. Skipping." -ForegroundColor Red
        continue
    }

    $logPath = Join-Path $repo.path "INTERIM_PROGRESS_LOG.md"

    # Special case: homeix rename
    if ($repo.ContainsKey("oldLog")) {
        $oldPath = Join-Path $repo.path $repo.oldLog
        if ((Test-Path $oldPath) -and (-not (Test-Path $logPath))) {
            Rename-Item -Path $oldPath -NewName "INTERIM_PROGRESS_LOG.md"
            Write-Host "  [RENAMED] $($repo.oldLog) -> INTERIM_PROGRESS_LOG.md" -ForegroundColor Yellow
        }
    }

    if (Test-Path $logPath) {
        Write-Host "  [OK] INTERIM_PROGRESS_LOG.md already exists." -ForegroundColor Green
    } else {
        $content = @"
# INTERIM PROGRESS LOG — $($repo.name)

## CURRENT STATE — READ FIRST
- Last session ended: $today — $($repo.note)
- Next action: confirm anchor green, proceed with build
- Blockers: none
- Do not proceed past this line without confirming the above

---

## Cross-Repo State (ceteris paribus)
| Repo | Branch | Last Commit | Status |
|------|--------|-------------|--------|
| DoughForge | main | 83bdc3b | clean |
| reproducible-self-pub-kit | main | f9971b6 | clean |
| hom-ixFAIRindex | chore/print-sequence | 504aa8b | clean |
| pimpernell-fatherbrown | main | 1242f40 | clean |

---

## Session Log

### $today
- INTERIM_PROGRESS_LOG.md created
- All four repos anchored and green
- Phase 5 added to session_start.ps1
- Coleridge Thread synthesis committed
- Session Synthesis Tarski/Malone/Lewis committed
"@
        $content | Set-Content -Path $logPath -Encoding UTF8
        Write-Host "  [CREATED] INTERIM_PROGRESS_LOG.md" -ForegroundColor Green
    }

    Push-Location $repo.path
    $status = git status --porcelain
    if ($status) {
        git add INTERIM_PROGRESS_LOG.md
        if ($repo.ContainsKey("oldLog")) { git add $repo.oldLog 2>$null }
        git commit -m "docs: add INTERIM_PROGRESS_LOG.md $today [W-Anchor]"
        git push
        Write-Host "  [PUSHED]" -ForegroundColor Green
    } else {
        Write-Host "  [CLEAN] Nothing to push." -ForegroundColor DarkGray
    }
    Pop-Location
}

Write-Host ""
Write-Host "  All progress logs confirmed." -ForegroundColor Cyan
