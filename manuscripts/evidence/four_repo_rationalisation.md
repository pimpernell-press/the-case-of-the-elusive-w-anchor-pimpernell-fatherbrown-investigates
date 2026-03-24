# Four-Repo Rationalisation Report

**Date:** 2026-03-24
**Auditor:** Claude Opus 4.6 (build agent, not writer)
**Scope:** All four W-Anchor Protocol repositories

---

## 1. Repository Overview

| Repo | Files | Last Commit | Status | Attestation |
|------|-------|-------------|--------|-------------|
| DoughForge | ~1,907 | `ccab6f2` session sync | clean | PASS (24 sources, 2 outputs) |
| Father Brown | 91 | `fcfa270` instrumentation | clean | PASS (14 sources, 2 outputs) |
| reproducible-self-pub-kit | ~160 | `4da12f4` anchor pointer | clean | PASS (16 sources, 4 outputs) |
| hom-ixFAIRindex | ~3,515 | `273f323` anchor pointer | clean | PASS (8 sources, 7 outputs) |

---

## 2. Duplication Map

### Files duplicated across repos

| File | DoughForge | Father Brown | Kit | HomeIx | Canonical Home |
|------|-----------|--------------|-----|--------|----------------|
| `anchor.py` | Yes (182 lines, DoughForge-specific) | Yes (103 lines, FB-specific) | Yes (42 lines, Kit-specific) | Yes (4 lines, stub) | **Each repo has its own** — correct. Not truly duplicated; each defines repo-specific paths. |
| `anchor_verify.ps1` | Yes (35 lines) | Yes (43 lines) | Yes (different) | No | **Kit** should be canonical but each has diverged. Father Brown's is most complete. |
| `session_start.ps1` | No | Yes (189 lines, 4-repo coord) | Yes (same file) | No | **Kit** — it's the 4-repo coordinator. Father Brown has a copy. |
| `CLAUDE.md` | No | Yes (master) | Yes (satellite) | Yes (satellite) | **Father Brown** is the master. Kit and HomeIx have satellite pointers. |
| `widgets/voice_widgets/` (14 files) | No | Yes | Yes | No | **Kit** — these are templates. Father Brown's are copies. |
| `widgets/aqual_screener/worldview_audit.md` | No | Yes | Yes | No | **Kit** |
| `scripts/build.ps1` | Yes (different) | Yes (44 lines) | Yes (44 lines) | No | **Kit** — Father Brown's is byte-identical to Kit's. DoughForge has its own. |
| `scripts/build_cover.py` | Yes | Yes | Yes | No | **Kit** — all three should reference the canonical version. |
| `publish/*.ps1` (7 scripts) | No | Yes | Yes | No | **Kit** — Father Brown has copies of all 7. |

### Verdict on duplication

**Low risk:** `anchor.py` — each repo's version is intentionally different (defines local paths). This is correct.

**Medium risk:** `anchor_verify.ps1` — three versions, each slightly different. Should converge on a single canonical version in the Kit, with satellite repos sourcing it or running it remotely.

**High risk:** `publish/*.ps1` (7 scripts), `scripts/build.ps1`, `scripts/build_cover.py`, `widgets/voice_widgets/` (14 files) — these are byte-identical or near-identical between Father Brown and the Kit. When one is updated, the other drifts silently. **These should live in the Kit only.** Father Brown should either symlink, submodule, or `session_start.ps1` should verify hash parity.

---

## 3. Hygiene Issues

### DoughForge
| Issue | Path | Severity | Recommendation |
|-------|------|----------|----------------|
| Loose files at root | `.from anchorto wanker 16 nmarch.md`, `8 march commit sequence.txt` | Low | Move to `archive/` or delete |
| `E Pubs New/` at root | 10 EPUBs | Medium | Move to `catalogue/published/` |
| `covers/` at root | Generated covers | Low | Already gitignored — confirm |
| `All components of book and paths/` | 80+ files, session transcripts mixed with chapters | High | **Triage needed.** Canonical chapters are in `chapters/`. Everything else is archive material. Move non-chapter files to `archive/sessions/` |
| `.anchor_hash` at root | Stale? | Low | Check if still used; if not, delete |
| `__pycache__/` committed | 2 `.pyc` files | Medium | Add `__pycache__/` to `.gitignore`, `git rm --cached` |

### reproducible-self-pub-kit
| Issue | Path | Severity | Recommendation |
|-------|------|----------|----------------|
| `.venv/` committed to git | Entire pip installation | **Critical** | `.venv/` IS in `.gitignore` but was committed before the ignore rule. Run `git rm -r --cached .venv/` |
| `__pycache__/` committed | `tools/__pycache__/`, root `__pycache__/` | Medium | `git rm -r --cached __pycache__/ tools/__pycache__/` |
| Lock files committed | `manuscripts/catalogue staging/docx/.~lock.*` | Low | Already in `.gitignore` pattern — remove cached copies |
| `archive/backups/` | Multiple dated backup dirs | Low | Expected — archive pattern is fine |
| `temp_anchor_readme.txt` | Root | Low | Delete — superseded by `ANCHOR.md` |
| `inputs/canonical/chapters/` and `chunks/` | FAIR paper drafts as HTML | Medium | These are HomeIx material. Should be fetched from HomeIx, not stored here. |

### hom-ixFAIRindex
| Issue | Path | Severity | Recommendation |
|-------|------|----------|----------------|
| 10 `outputs_archive_*` dirs | Dated output snapshots | High | **3,000+ files of stale output snapshots.** These inflate the repo massively. Archive to a separate branch or delete. Keep only the latest `outputs/`. |
| `_audit_20260228_102356/` | One-time audit data | Medium | Move to `archive/` or delete — audit is a point-in-time snapshot |
| `_epub_extract/` | Unzipped EPUB contents | Medium | Delete — can be regenerated |
| `backup_inbox_py_*/`, `backup_savefig_patch_*/` | Safety backups | Low | Already gitignored pattern — remove cached if tracked |
| `sweep_up/` | Dedup quarantine dirs | Medium | Purpose served — can be deleted |
| `anchor.py` is a 4-line stub | Just `BASE_COVER` and `FINAL_COVER` | Low | Should be expanded to match other repos' anchor.py pattern, or deleted if cover logic lives elsewhere |
| `pandas`/`matplotlib` not on system Python | `.venv` has them | Low | Attestation correctly reports "not installed" — add note that `.venv` activation is required |

### Father Brown
| Issue | Path | Severity | Recommendation |
|-------|------|----------|----------------|
| `The W-Anchor CLAUDE.md` at root | Stray copy | Low | Delete or move to `docs/` |
| `tools/OK so the special offer By The Conq.txt` | Misplaced note | Low | Move to `reservoir/` or delete |
| `whenyoustopwanking andloseyourCherrythe happyending.md` at root | 2,097-line transcript | Medium | Move to `manuscripts/evidence/` — it's source material for ch_cherry |

---

## 4. Cross-Repo Dependency Map

```
┌─────────────────────────────────────────────────────────┐
│                   session_start.ps1                      │
│              (lives in Kit + Father Brown)                │
│         Coordinates all 4 repos at session open          │
└──────────┬──────────┬──────────┬──────────┬─────────────┘
           │          │          │          │
     ┌─────▼────┐ ┌──▼────────┐ ┌▼────────┐ ┌▼──────────┐
     │ DoughForge│ │Father Brown│ │  Kit    │ │  HomeIx   │
     │          │ │           │ │         │ │           │
     │chapters/ │ │manuscripts/│ │tools/   │ │src/       │
     │widgets/  │◄┤widgets/   │◄┤widgets/ │ │tools/     │
     │assets/   │ │publish/   │◄┤publish/ │ │outputs/   │
     │dist/     │ │scripts/   │◄┤scripts/ │ │           │
     │          │ │dist/      │ │outputs/ │ │           │
     └──────────┘ └───────────┘ └─────────┘ └───────────┘
                        │              │            │
                        │    ◄─────────┘            │
                        │  (build toolchain)        │
                        │                           │
                        ▼                           │
                  book.yaml ──────── cross-refs ────┘
                  (ch03 cites FAIR data from HomeIx)
                  (ch01 transcludes anchor_verify from Kit)
                  (ch03 embeds flux_capacitor from DoughForge)
```

### Key dependencies:
1. **Kit → all repos:** `tools/build_book.py` is the build entry point. `scripts/build.ps1` in Father Brown delegates to Kit's `tools/build_book.py`.
2. **Father Brown → DoughForge:** `widgets/flux_capacitor/index.html` is forked from DoughForge. Currently byte-identical.
3. **Father Brown → HomeIx:** Chapter cross-references cite `tools/homeix_corpus_index.html`.
4. **Father Brown → Kit:** `publish/` directory is duplicated from Kit. `session_start.ps1` is copied.

---

## 5. Recommended Actions (Priority Order)

### Immediate (this session)
- [x] Install instrumentation in all 4 repos (done)
- [x] Run first attestation in all 4 repos (done — all PASS)
- [x] Update `.gitignore` in all 4 repos (done)

### Next session
1. **Kit: Remove `.venv/` from tracking** — `git rm -r --cached .venv/` (saves ~50MB in repo history)
2. **Kit: Remove `__pycache__/` from tracking** — `git rm -r --cached __pycache__/ tools/__pycache__/`
3. **HomeIx: Delete `outputs_archive_*` dirs** — `git rm -r outputs_archive_*/` (saves ~3,000 files)
4. **HomeIx: Delete `_epub_extract/`** — regeneratable
5. **Father Brown: Move `whenyoustopwanking...md` to `manuscripts/evidence/`**

### Future sessions
6. **Consolidate `publish/` scripts** — Father Brown should reference Kit's copies, not maintain duplicates
7. **Consolidate `widgets/voice_widgets/`** — canonical in Kit, referenced from Father Brown
8. **DoughForge: Triage `All components of book and paths/`** — separate chapters from session transcripts
9. **Add hash-parity check to `session_start.ps1`** — verify that duplicated files match across repos
10. **HomeIx: Expand `anchor.py`** to match the pattern used by the other three repos

---

## 6. Attestation Summary

All four repos now have identical instrumentation:

| Component | DoughForge | Father Brown | Kit | HomeIx |
|-----------|-----------|--------------|-----|--------|
| `scripts/build_attestation.py` | M1,M2,M3,M7,M11 | M1,M2,M3,M7,M11 | M1,M2,M3,M7,M11 | M1,M2,M3,M7,M11 |
| `scripts/verify_build.ps1` | M9,M12 | M9,M12 | M9,M12 | M9,M12 |
| `scripts/session_anchor.ps1` | M4 | M4 | M4 | M4 |
| `logs/DRIFT_LOG.csv` | M5,M6 | M5,M6 | M5,M6 | M5,M6 |
| `.githooks/pre-commit` | M8 | M8 | M8 | M8 |
| First attestation | PASS | PASS | PASS | PASS |
| Output dir | `dist/` | `dist/` | `outputs/` | `outputs/` |
| Sources hashed | 24 | 14 | 16 | 8 |
| Outputs hashed | 2 | 2 | 4 | 7 |

**To activate hooks in each repo:** `git config core.hooksPath .githooks`
