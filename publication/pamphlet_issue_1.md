# Reproducible SelfPub Kit

---



---

## Shipping Without Surprises

---



---

### Release notes for writers whove been burned by little quirks

---



---

This pamphlet is a small act of civil engineering:

---



---

- One canonical manuscript.

---

- A repeatable build that produces PDF + EPUB + DOCX.

---

- A boring paper trail that prevents drift.

---



---

------------------------------------------------------------------------

---

# Contents & Foreword

---



---

## Contents

---



---

1.  Origin Story: the quirks that ate publication day

---

2.  Ground Truth: one manuscript, many outputs

---

3.  Versioning with Git: stop selling yourself work you already did

---

4.  Metadata discipline: titles, subtitles, series, and the Great Drift

---

5.  Covers that match reality (outside *and* inside)

---

6.  Flexible by design: kids books technical academic

---

7.  Quick timeline + firstship checklist

---

8.  Microindex for tired humans

---



---

## Foreword (from a cheerful realist)

---



---

Ive published 11 books through Draft2Digital since 2018. Two more are on

---

deck.

---



---

The recurring theme isnt incompetence. Its **drift**.

---



---

------------------------------------------------------------------------

---

# 1) Origin Story: the quirks that ate publication day

---



---

Between tools, tiny quirks can hold up publication like a pebble in a

---

train door.

---



---

### Prompt Box: Check whats real (before you fix what isnt)

---



---

git status -sb

---

Test-Path .\publication\pamphlet_issue_1.md

---

pandoc --version

---

xelatex --version

---



---

------------------------------------------------------------------------

---

# 2) Ground Truth: one manuscript, many outputs

---



---

Pick a truth, then make everything else a rebuildable product of that

---

truth.

---



---

**Canonical:** the manuscript + metadata you edit.

---



---

**Artifacts:** PDF/EPUB/DOCX you rebuild.

---

# 3) Versioning with Git: stop selling yourself work you already did

---



---

git status -sb

---

git add .\publication\pamphlet_issue_1.md

---

git commit -m "Explain what changed in one sentence"

---

# 4) Metadata discipline: titles, subtitles, series, and the Great Drift

---



---

Keep one place where the current truth lives (YAML/metadata), and make

---

everything else follow.

---

# 5) Covers that match reality (outside and inside)

---



---

- Cover text matches metadata

---

- Internal title page matches metadata

---

- EPUB metadata matches metadata

---

# 6) Flexible by design: kids books technical academic

---



---

Use a safe subset of Markdown to keep builds predictable.

---

# 7) Quick timeline + firstship checklist

---



---

- Build locally

---

- Spot-check

---

- Commit

---

- Ship

---

# 8) Microindex for tired humans

---



---

- **Anchor:** the contract for whats real

---

- **Canonical manuscript:** the one file you edit

---

- **Outputs:** rebuildable artifacts

---



---

*Make the process boring.*
