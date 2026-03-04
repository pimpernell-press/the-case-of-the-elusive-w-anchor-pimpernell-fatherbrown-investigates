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
---

##  User Manual Note  How writing + assembling + building works here

This repo is designed so you can write in small, easy-to-edit chapter files, then automatically assemble them into a single manuscript for publishing builds (EPUB/PDF/DOCX).

###  What you edit (human-friendly source)
You write and revise chapter files here:

`inputs/canonical/chapters/`

Each file is plain Markdown. A typical chapter starts with a top-level heading:

```md
# Chapter Title
```

This is the only place you should be writing prose day-to-day.

###  What gets generated (machine-friendly build input)
When youre ready to compile everything into one manuscript, the repo generates:

`publication/manuscript.md`

Think of this as the print/export master file that is always reproducible from the chapters. You usually dont hand-edit this file; its assembled from the chapter folder.

###  What gets built (deliverables)
The build pipeline reads the assembled manuscript and produces:

- `outputs/pdf/manuscript.pdf`
- `outputs/epub/manuscript.epub`
- `outputs/docx/manuscript.docx`

These are the files you upload to services like Draft2Digital.

###  Standard workflow (the mental model)
1. **Edit:** change one chapter Markdown file  
2. **Assemble:** regenerate `publication/manuscript.md` from chapters  
3. **Build:** regenerate EPUB/PDF/DOCX from `publication/manuscript.md`  
4. **Version:** commit changes + add a progress log entry  

### Why this is better than one big doc
- Chapters are easier to navigate and review.
- You avoid mystery edits inside large files.
- Builds become consistent and repeatable across machines.


---

##  Git workflow (new user guidance)

### Quick daily commands
```powershell
git status -sb
git pull --ff-only
git add -A
git commit -m "Describe your change"
git push
```

### Write a repo state report
```powershell
.\tools\write_repo_state_report.ps1
```

Reports are written to: `publication/_reports/`.
Latest repo state report: `publication/_reports/repo_state_2026-03-04_193619.md`





