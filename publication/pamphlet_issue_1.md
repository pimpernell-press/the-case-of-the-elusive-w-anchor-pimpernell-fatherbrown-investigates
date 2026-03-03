---
title: "Reproducible Self‑Pub Kit"
subtitle: "Shipping Without Surprises"
author: "A writer who’s published 11 books via Draft2Digital (since 2018)"
date: "2026-03-03"
lang: en-GB
---

# Reproducible Self‑Pub Kit

## Shipping Without Surprises

### Release notes for writers who’ve been burned by “little quirks”

> “You are not expected to understand this.”

That sentence showed up as a real comment in early UNIX source code—half warning, half wink.  
It wasn’t meant as a challenge. It meant: *this won’t be on the exam.*

So yes: **it’s on the exam.**

Not because you need to become a compiler archaeologist, but because modern publishing tools have the same bad habit as old systems code: they quietly accumulate quirks, and then you lose an afternoon (or a launch date) to something you “weren’t expected to understand.”

This pamphlet is a small act of civil engineering:

- One canonical manuscript.
- A repeatable build that produces PDF + EPUB + DOCX.
- A boring paper trail that prevents drift.

You don’t have to love tooling. You just shouldn’t have to fear it.

You already know how to write. The frustrating part is everything *around* the writing: the title that doesn’t match, the cover that drifts, the EPUB that behaves until a platform preview invents new physics, and the eternal question:

**Which file is the real one?**

This pamphlet is a small answer: **one canonical manuscript + one repeatable build + version history you can trust.** Not glamorous. Just *reliably boring*.

\newpage

# Contents & Foreword

## Contents

1. Origin Story: the quirks that ate publication day
2. Ground Truth: one manuscript, many outputs
3. Versioning with Git: stop selling yourself work you already did
4. Metadata discipline: titles, subtitles, series, and the Great Drift
5. Covers that match reality (outside *and* inside)
6. Flexible by design: kids’ books → technical → academic
7. Quick timeline + first‑ship checklist
8. Micro‑index for tired humans

## Foreword (from a cheerful realist)

I’ve published 11 books through Draft2Digital since 2018. Two more are on deck. That means I’ve had enough “oh no” moments to qualify as a minor weather pattern.

The recurring theme isn’t incompetence. It’s **drift**: titles drift, covers drift, internal title pages drift, versions drift… and suddenly your “final” file has cousins. Loud cousins.

This kit is how you stop drift from running your publishing schedule.

\newpage

# 1) Origin Story: the quirks that ate publication day

Draft2Digital is brilliant at distribution. Reedsy is great for production. And yet—between tools—tiny quirks can hold up publication like a pebble in a train door.

Common culprits:

- Cover title/subtitle doesn’t match the internal title page.
- EPUB respects headings; DOCX decides to improvise.
- Scene breaks turn into mystery blank space (or mystery *no* space).
- Previews look fine… until store conversion does its own thing.
- You fix one thing and accidentally publish a different file than the one you checked.

The fix isn’t heroic. It’s practical:

**Write down reality. Make the tools obey it.**

That’s what an Anchor file is for: a boring little contract that says “these paths are real, these commands work on this machine, this is the source, and these are build outputs.”

### Prompt Box: “Check what’s real (before you fix what isn’t)”

~~~powershell
cd "C:\Users\peewe\OneDrive\Desktop\reproducible-self-pub-kit"
git status -sb
Test-Path .\publication\pamphlet_issue_1.md
pandoc --version
xelatex --version
