# Reproducible Self-Pub Kit  PRINT_AND_BUILD_NOTES (Anchor)

## Build invariant (must hold)
All canonical paths resolve from PROJECT_ROOT (repo root), not from:
- the script directory
- the current working directory (CWD)

## Intended one-line rebuild (Windows)
.\publish\rebuild_publish.ps1

## Canonical locations (planned)
- Author inputs:
  - manuscript_md/
  - manuscript_docx/book.docx
  - assets/
  - inputs/canonical/metadata.yml
- Build artefacts:
  - outputs/...
  - publication/print_*
  - publication/release_*

## Non-negotiables
- No hard-coded machine paths.
- Fail fast with clear errors when expected folders/files are missing.
- Print resolved PROJECT_ROOT and key directories at runtime.

## Recent changes
- 2026-03-03: Public repo created; initial skeleton committed.
