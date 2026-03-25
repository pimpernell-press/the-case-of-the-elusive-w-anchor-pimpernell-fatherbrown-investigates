# Transclude Design Sketch — Flux Capacitor + Corpus Index

**Status:** Design notes only. No build scripts modified. No files embedded.
**Date:** 2026-03-25
**Context:** Experimental documentation for how DoughForge and hom-ixFAIRindex
tools could integrate with the book build pipeline.

---

## The Two Tools

### 1. Flux Capacitor (DoughForge)

**Source:** `C:\Users\peewe\Documents\DoughForge\widgets\flux_capacitor\index.html`

A self-contained HTML widget titled "Flux Capacitor of Strawberry Politics."
It is an AQAL (All Quadrants, All Levels) bias detection and epistemological
grounding tool. Specifically, it:

- Accepts source text, a known bias type, and an external base reference
- Requires a **W-Anchor** (git commit hash) as an epistemological anchor —
  Tarski's meta-language requirement: truth cannot be defined from within
  the system; the commit hash is the external ground
- Runs an AQAL quadrant pre-screener across four dimensions:
  - **I** (Interior Individual) — inner experience, phenomenology
  - **WE** (Interior Collective) — shared meaning, cultural context
  - **IT** (Exterior Individual) — observable, measurable, falsifiable
  - **ITS** (Exterior Collective) — institutional, economic, systemic
- Produces a "Wisdom Optimization Report" with:
  - Contradiction Index (Maimonides Scale)
  - Perspective Score (Anekantavada — Jain many-sidedness)
  - Bias Metric (-100 to +100)
  - AQAL Balance (quadrant coverage percentage)
  - A Peirce Pragmatic Check — does the claim have practical consequences?
- Includes a CLI-equivalent panel showing the PowerShell commands that
  reproduce the same checks in the terminal

**Role in the book:** This is the instrument panel. In Chapter 3a ("The Flux
Capacitor and the Halting Problem"), Father Brown opens it on Thomas's laptop.
It is both the running gag and the real verification tool — the novel's
content can be fed through it to check its own AQAL balance.

### 2. Corpus Index (hom-ixFAIRindex)

**Source:** `C:\Users\peewe\OneDrive\Desktop\homeix\tools\homeix_corpus_index.html`

A tabbed HTML application titled "Home@ix | Corpus Index — Staff Training
Platform." It provides:

- **Overview tab** — platform architecture, FAIR-Index database, BIM catalogue
- **Corpus Index tab** — a structured table mapping every source document to
  its location, category, and external link. Includes:
  - FAIR-Index canonical dataset (GitHub)
  - W-Anchor Protocol (ANCHOR.md)
  - FAIR-Index Dashboard (GitHub Pages)
  - Google Drive 6-year document archive
  - MMC manufacturing documentation
- **Interrogation Tools tab** — a FAIR-Index Query Simulator and Intelligent
  Search Parser that searches across corpus, Drive archive, and web sources
- **Training Resources tab** — guides for the Gemini API, FAIR-Index protocol,
  BIM catalogue, and interrogation prompts

The corpus entries are backed by a JavaScript knowledge base containing
structured facts about Roger G. Lewis, Home@ix Ltd, the FAIR-Index, the
Potton acquisition, and the W-Anchor Protocol.

**Role in the book:** This is the FAIR metadata layer. When chapters cite
housing affordability data, the source is traceable through this index.
The corpus index makes the novel's factual claims discoverable, indexable,
and citable — the book's bibliography as a living, queryable tool.

---

## Conceptual Integration with build_epub.py

The current build pipeline (`tools/build_epub.py`) reads `book.yaml`, collects
chapter markdown files, and runs Pandoc to produce an EPUB. The two tools
would extend this in complementary ways:

### Transformation Layer (Flux Capacitor)

The Flux Capacitor operates as a **pre-build validation step** — analogous to
dough-into-bread, manuscript-into-EPUB. Before the EPUB is built:

1. Each chapter's markdown could be fed through the AQAL analysis
2. The build would record AQAL balance scores per chapter
3. Chapters with extreme bias metrics or low quadrant coverage would be
   flagged (not blocked — flagged) for review
4. The W-Anchor commit hash at build time would be embedded in the EPUB
   metadata, grounding the publication to a specific verified state

**Integration point:** A new `tools/validate_aqal.py` script (future) could
parse each chapter, run the Flux Capacitor's keyword heuristics in Python
(porting the JS logic), and produce a pre-build report. The HTML widget
itself could be included in `dist/` as an interactive companion artefact.

### Discoverability Layer (Corpus Index)

The Corpus Index operates as a **post-build metadata enrichment** — making the
published book FAIR (Findable, Accessible, Interoperable, Reusable):

1. Each chapter's factual claims map to corpus entries in the index
2. The index provides external traceability — from novel assertion to
   source document to canonical dataset
3. Including the corpus index HTML alongside the EPUB means readers can
   verify any claim the book makes

**Integration point:** A future build step could copy `homeix_corpus_index.html`
into `dist/` alongside the EPUB, and generate a `sources.json` mapping
chapter numbers to corpus entry IDs. The EPUB's metadata could include
a `dc:relation` pointing to the corpus index URL.

### Proposed dist/ Layout (Future)

```
dist/
  the-case-of-the-elusive-w-anchor.epub    # The book (existing)
  the-case-of-the-elusive-w-anchor.docx    # The book (existing)
  flux_capacitor/
    index.html                              # Interactive AQAL widget
  corpus_index/
    homeix_corpus_index.html                # FAIR metadata index
  build_report.json                         # AQAL scores per chapter
  sources.json                              # Chapter-to-corpus mapping
```

### What This Does NOT Do

- Does not modify `tools/build_epub.py` — that script is stable and working
- Does not clone or embed external repos — references by local path only
- Does not add dependencies — the HTML widgets are self-contained
- Does not change the manuscript — this is infrastructure documentation

---

## Connection to the Novel's Themes

The integration is not just technical. It enacts the book's argument:

- **The Flux Capacitor** is the novel's answer to the Halting Problem:
  you cannot verify a system from within the system. The commit hash is
  the external oracle. Father Brown understands this as Original Sin —
  you need something outside yourself to check yourself.

- **The Corpus Index** is the novel's answer to the Circle of Blame:
  every accusation is traceable, every number has a source, every claim
  can be checked. Mrs. Ledger blames Dex, Dex blames Fairweather,
  Fairweather blames Siobhan — but the index doesn't blame. It cites.

The form enacts the content. The build pipeline IS the argument.
