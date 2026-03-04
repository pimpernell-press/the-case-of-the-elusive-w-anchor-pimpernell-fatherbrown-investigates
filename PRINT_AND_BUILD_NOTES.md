# Reproducible Self-Pub Kit  PRINT_AND_BUILD_NOTES (Anchor)

## Build invariant (must hold)
All canonical paths resolve from **PROJECT_ROOT** (repo root), not from:

- the script directory
- the current working directory (CWD)

This repo is allowed to be run from anywhere; it is not allowed to be confused about where it lives.

---

## Intended one-line rebuild (Windows)
~~~powershell
.\publish\rebuild_publish.ps1
~~~

---

## Canonical locations (current  enforced by build scripts)
These are the current source-of-truth paths used by the build commands/scripts today.

- Canonical manuscript:
  - publication/pamphlet_issue_1.md
- Canonical metadata:
  - publication/metadata_pamphlet_issue_1.md
- Build artefacts:
  - outputs/pdf/
  - outputs/epub/
  - outputs/docx/

---

## Target layout (not yet enforced)
This is the planned organization. It is a roadmap, not a guarantee, until build scripts enforce it.

- Author inputs:
  - manuscript_md/
  - manuscript_docx/book.docx
  - ssets/
  - inputs/canonical/metadata.yml
- Build artefacts:
  - outputs/...
  - publication/print_*
  - publication/release_*

---

## Non-negotiables
- **No hard-coded machine paths.**
- **Fail fast** with clear errors when expected folders/files are missing.
- Print resolved **PROJECT_ROOT** and key directories at runtime.

---

## Recent changes
- 2026-03-03: Public repo created; initial skeleton committed.