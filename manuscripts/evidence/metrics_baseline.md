# The Evidence Board: Twelve Metrics Baselined

## What Father Brown Pinned to the Wall

Father Brown stood before the evidence board in the parish hall. It had grown.
Where once there were chapters and corkboard and red string, there were now
twelve cards — each bearing a metric designation — pinned in two columns.

"Twelve measurements," he said. "Not of the crime. Of the *investigation itself*.
Because the first thing a competent detective measures is whether his own
instruments are working."

Thomas looked up. "Like anchor_verify."

"Exactly like anchor_verify. Except anchor_verify checks *existence* — is the
file there? These twelve check *integrity* — is the file what it claims to be?
Has it changed when it shouldn't have? Has it *not* changed when it should have?"

---

## The Twelve Metrics

| ID | Metric | Status | Instrument |
|----|--------|--------|------------|
| M1 | **Source File Hashing** | IMPLEMENTED | `build_attestation.py` — SHA-256 of every source file in `book.yaml` |
| M2 | **Output File Hashing** | IMPLEMENTED | `build_attestation.py` — SHA-256 of EPUB, PDF, DOCX in `dist/` |
| M3 | **Manifest Consistency** | IMPLEMENTED | `build_attestation.py` — compares `book.yaml` chapters to files on disk |
| M4 | **Session Anchor** | IMPLEMENTED | `session_anchor.ps1` — prints git state, drift log, attestation at session start |
| M5 | **Drift Incident Logging** | PARTIAL | `logs/DRIFT_LOG.csv` — structure exists, requires human entries per session |
| M6 | **Minutes Lost to Drift** | PARTIAL | `logs/DRIFT_LOG.csv` — `minutes_lost` column, requires honest self-reporting |
| M7 | **Dirty Output Detection** | IMPLEMENTED | `build_attestation.py` — flags outputs modified without source changes |
| M8 | **Pre-Commit Gate** | IMPLEMENTED | `.githooks/pre-commit` — blocks output commits without attestation |
| M9 | **Build Verification** | IMPLEMENTED | `verify_build.ps1` — runs build + attestation + prints summary |
| M10 | **Mean Time to Recovery** | NOT YET | Requires CI pipeline — track time between build failure and next green |
| M11 | **Tool Version Capture** | IMPLEMENTED | `build_attestation.py` — records Python, Pandoc, LuaLaTeX versions |
| M12 | **Environment Check** | IMPLEMENTED | `verify_build.ps1` — verifies required tools are installed before build |

---

## What This Commit Addresses

This commit instruments **nine of twelve metrics** (M1–M4, M7–M9, M11–M12).

Three remain:
- **M5 and M6** (drift logging) have the *structure* but require *human input*.
  The CSV exists. The columns exist. The first entry exists. But only the author
  can record when drift happened and how many minutes it cost. The instrument
  is built; the observation is the author's responsibility.
- **M10** (MTTR) requires a CI pipeline that does not yet exist. When `scripts/build.ps1`
  runs in GitHub Actions, M10 becomes measurable automatically.

---

## The Evidence Board: Before and After

### Before this session

The evidence board had:
- `anchor_verify.ps1` — checked path existence. [OK] or [MISSING]. Binary.
- `anchor.py` — Python path constants. The map of where things should be.
- `session_start.ps1` — 4-repo coordinator. Git pull, diff, push. The ritual.
- `book.yaml` — chapter manifest. The list of what the book contains.

These instruments answered one question: *"Is the thing where it should be?"*

### After this session

The evidence board now also has:
- `build_attestation.py` — hashes sources and outputs. Compares manifest to reality.
- `verify_build.ps1` — runs the build and checks the result.
- `session_anchor.ps1` — prints the state of everything at session start.
- `logs/DRIFT_LOG.csv` — records when the investigation went off track.
- `.githooks/pre-commit` — blocks commits that ship unverified outputs.

These instruments answer a different question: *"Is the thing what it claims to be?"*

---

## Father Brown's Observation

Father Brown pinned the last card — M12, Environment Check — and stepped back.

"The difference," he said, "between the old board and the new board is the
difference between a census and an audit. A census counts heads. An audit
checks the books. Before today, we were counting heads — is the file present?
Is the directory present? Is the repo present? All important questions. All
answerable with a simple [OK] or [MISSING]."

He turned to Thomas.

"But Mrs. Hennessy was *present* in the WhatsApp group. Her phone was there.
Two blue ticks. Silence. Presence is not proof of participation. A file can
be present and *wrong*. An output can be present and *stale*. A build can
succeed and produce something that no longer matches its sources."

He tapped the M7 card — Dirty Output Detection.

"This is the one that matters most. Not because dirty outputs are common, but
because they are *invisible*. The EPUB looks the same. The filename is the same.
The commit message says 'build.' But the hash has changed and nobody changed the
source. That is not a build. That is a forgery. And the only way to catch a
forgery is to measure what nobody thought to measure."

He folded his hands.

"Twelve metrics. Nine instrumented. Three requiring human honesty. Which is,
I suppose, the ratio one expects in any parish."
