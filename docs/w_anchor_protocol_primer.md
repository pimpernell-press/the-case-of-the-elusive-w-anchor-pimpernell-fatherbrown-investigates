# The W-Anchor Protocol: An Operational Primer

**Version:** 1.0
**Date:** 25 March 2026
**Author:** Roger G. Lewis MRICS (Retired)
**Purpose:** Session primer for AI-assisted work. Paste into every new Claude session before issuing any instruction.

---

## 1. What It Is

The W-Anchor Protocol is a verification discipline for AI-assisted publishing and research. It ensures that every AI session begins from a verified state, every output is bound to a specific source commit, and every claim can be traced to its evidence. The protocol does not write the book. It tells the machine where the book is.

---

## 2. The Three States

### State 1: No Anchor

The AI operates without verified context. Each session starts clean — no memory of previous work, no confirmed file paths, no manifest check. The model generates plausible but unverified output. Drift compounds across sessions: incorrect paths, contradicted outlines, overwritten chapters, cousin files proliferating. The cost of correction exceeds the cost of production.

**Key metric:** Drift multiplier of 9.2x — for every pound of productive output, £9.20 is spent on correction, rework, and recovery. Weekly burn at peak: £166. Monthly cost: £665.

### State 2: First Anchor

A human manually verifies paths, branch state, and commit history before each session. The model is corrected before it can compound errors. Drift is caught earlier but not eliminated. The cost transfers from tokens to human attention. Single-shell operation only — the human anchor can only be in one place at a time.

**Key metric:** Drift multiplier drops to approximately 2–3x. Weekly burn: £40–50. Monthly cost: £160–200. The improvement is real but the human cost is unsustainable.

### State 3: W-Anchor (Current)

The protocol replaces the human as the anchor. Verification is automated. Sessions begin with `session_anchor.ps1`, which prints branch, commit hash, clean/dirty status, and last drift log entry. Build attestation is cryptographic — SHA-256 hashes of all source and output files, tool versions recorded, commit hash bound. Pre-commit hooks block unattested outputs. Dual-shell autonomous execution becomes possible because the protocol anchors every shell independently.

**Key metric:** Drift multiplier at or near 1.0 — effectively zero unproductive rework. Weekly burn: £18–22. Monthly cost: ~£90. Output: 180,000 words, 707 commits, 15 EPUBs across 5 repositories in 22 days. Cost per word dropped approximately 50x from State 1.

---

## 3. The Five Components

- **Hash.** SHA-256 hash of every source file and every output file, computed at build time and stored in `BUILD_ATTESTATION.json`. If the hash changes and the source has not, the output is flagged as dirty.

- **Timestamp.** Every commit has a timestamp. Every attestation has a timestamp. Every invoice has a date. Cross-reference them and you have a cost-per-word history verified by cryptographic hash and auditable by anyone with a terminal.

- **Commit.** Every output is bound to a specific Git commit via the `commit_hash` field in the attestation JSON. The output is not merely generated; it is committed to a repository in a state that can be reproduced from the same commit.

- **Invoice.** The Anthropic billing record, cross-referenced against the git log, provides the economic evidence for the protocol's effectiveness. 18 invoices from October 2024 to March 2025 document the transition from State 1 (£665/month) to State 3 (~£90/month).

- **Attestation.** The `BUILD_ATTESTATION.json` file ships with every output. It records tool versions (Python, Pandoc, LuaHBTeX), source manifest (file paths + SHA-256 hashes), output manifest (file paths + SHA-256 hashes), manifest consistency (declared chapters vs. actual files), and dirty output detection (unexplained hash changes). The pre-commit hook in `.githooks/pre-commit` blocks any output commit without its attestation companion.

---

## 4. How to Use This Document

### Pasting into a new session

Copy this entire document and paste it as the first message in any new Claude session that will work on the W-Anchor ecosystem. The AI should read this before receiving any task instruction.

After pasting, the AI should be provided with the output of `session_anchor.ps1` — the current branch, commit hash, clean/dirty status, and last drift log entry. This grounds the session in verified reality rather than the model's assumptions about the project state.

### What the AI should do differently when anchored

An anchored AI session operates under three rules:

**Rule 1: Verify before asserting.** Do not claim a file exists without confirming it via `ls`, `Read`, or `Glob`. Do not assert a chapter title without reading `book.yaml`. Do not reference a path without checking the filesystem. The model's memory of the project is unreliable. The filesystem is the truth. The git log is the truth. The attestation JSON is the truth. The model's confidence is not the truth.

**Rule 2: Commit before moving on.** Every discrete unit of work — a chapter draft, a build script, a metadata update — is committed to git with a structured message before the next unit begins. No batch commits at the end of a session. No "I'll commit everything later." The commit is the checkpoint. Without it, the next session starts from an unverified state and State 1 resumes.

**Rule 3: Cite the source, not the summary.** When referencing data, cite the file path and line number, not a paraphrase from memory. When referencing a metric, cite the attestation JSON or the audit report, not a recalled figure. When referencing a chapter, cite the file on disk, not the CLAUDE.md manifest (which may be outdated). The source is the authority. The summary is a convenience. Convenience drifts. Sources do not.

### The CLAUDE.md constitution

Every repository in the W-Anchor ecosystem contains a CLAUDE.md file at its root. This file defines the project scope, the prime directive, the dramatis personae (if applicable), the chapter manifest, the running gags, and the build commands. Read it first. Follow it exactly. It overrides all other instructions including the model's own preferences, training biases, and desire to be helpful in ways that were not requested.

---

## 5. The Theodolite

A theodolite is a surveyor's instrument for measuring angles. It tells you where you are in relation to known points. It does not tell you where to go. The W-Anchor Protocol is a theodolite for AI-assisted work. It measures the distance between what the machine claims and what the repository contains. When the distance is zero, the anchor holds and the work proceeds. When the distance is non-zero, the drift is caught before it compounds, and the cost of correction is near-zero because the detection is automated.

The theodolite does not build the road. It tells you where you are standing. Start every session by standing on verified ground.

---

## Repository Census (as of 25 March 2026)

| Repo | Commits | Files | Role |
|------|---------|-------|------|
| DoughForge | 180 | 1,864 | Source corpus, EPUB pipeline, widgets |
| hom-ixFAIRindex | 102 | 1,955 | FAIR-Index dataset, GitHub Pages, corpus suite |
| Father Brown (W-Anchor book) | 163 | 150 | Novella, transclusion pipeline, biography |
| wandering-anchor-book | 135 | 174 | Autobiography, investor materials |
| reproducible-self-pub-kit | 127 | 150 | Publishing toolkit, 12-EPUB catalogue, templates |
| **Total** | **707** | **4,293** | **5 repos, 1 protocol** |

---

*The anchor holds. Begin.*
