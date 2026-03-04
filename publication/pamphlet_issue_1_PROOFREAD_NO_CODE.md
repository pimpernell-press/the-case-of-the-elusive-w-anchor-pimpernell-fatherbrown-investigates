Reproducible SelfPub Kit
Shipping Without Surprises
Release notes for writers whove been burned by little quirks
You are not expected to understand this.

That sentence showed up as a real comment in early UNIX source codehalf warning, half wink.

It wasnt meant as a challenge. It meant: this wont be on the exam.

So yes: its on the exam.

Not because you need to become a compiler archaeologist, but because modern publishing tools have the same bad habit as old systems code: they quietly accumulate quirks, and then you lose an afternoon (or a launch date) to something you werent expected to understand.

This pamphlet is a small act of civil engineering:

One canonical manuscript.
A repeatable build that produces PDF + EPUB + DOCX.
A boring paper trail that prevents drift.
You dont have to love tooling. You just shouldnt have to fear it.

You already know how to write. The frustrating part is everything around the writing: the title that doesnt match, the cover that drifts, the EPUB that behaves until a platform preview invents new physics, and the eternal question:

Which file is the real one?

This pamphlet is a small answer: one canonical manuscript + one repeatable build + version history you can trust. Not glamorous. Just reliably boring.

Contents & Foreword
Contents
Origin Story: the quirks that ate publication day
Ground Truth: one manuscript, many outputs
Versioning with Git: stop selling yourself work you already did
Metadata discipline: titles, subtitles, series, and the Great Drift
Covers that match reality (outside and inside)
Flexible by design: kids books  technical  academic
Quick timeline + firstship checklist
Microindex for tired humans
Foreword (from a cheerful realist)
Ive published 11 books through Draft2Digital since 2018. Two more are on deck. That means Ive had enough oh no moments to qualify as a minor weather pattern.

The recurring theme isnt incompetence. Its drift: titles drift, covers drift, internal title pages drift, versions drift and suddenly your final file has cousins. Loud cousins.

This kit is how you stop drift from running your publishing schedule.

1) Origin Story: the quirks that ate publication day
Draft2Digital is brilliant at distribution. Reedsy is great for production. And yetbetween toolstiny quirks can hold up publication like a pebble in a train door.

Common culprits:

Cover title/subtitle doesnt match the internal title page.
EPUB respects headings; DOCX decides to improvise.
Scene breaks turn into mystery blank space (or mystery no space).
Previews look fine until store conversion does its own thing.
You fix one thing and accidentally publish a different file than the one you checked.
The fix isnt heroic. Its practical:

Write down reality. Make the tools obey it.

Thats what an Anchor file is for: a boring little contract that says these paths are real, these commands work on this machine, this is the source, and these are build outputs.

Prompt Box: Check whats real (before you fix what isnt)
Pitfall: Notepad + OneDrive + Markdown fences (how people lose hours)
If Notepad offers to clear all and save new or says it cant find the file, stop and verify youre editing the file you think you are. In synced folders (e.g., OneDrive), the file can change while Notepad is open.

Also: Markdown code fences are literal. If you start a fenced block with ``` and forget the closing, the rest of the document becomes code.

Two checks:

Confirm the manuscript file is real and non-empty:

Confirm code fences are balanced (even count):

2) Ground Truth: one manuscript, many outputs
Publishing pain usually comes from one root cause:

You stop knowing which file is the truth.

So we pick a truth and make everything else a rebuildable product of that truth.

The Ground Truth rule
One canonical manuscript (this Markdown file).

Everything else is generated: PDF, EPUB, DOCX, cover embeds, metadata exports.

If an output looks wrong, you do not fix the output. You fix the manuscript (or the build rules) and rebuild.

This isnt ideology. Its how you keep launch day boring.

What counts as canonical (and what doesnt)
Canonical (edit these):

publication/pamphlet_issue_1.md

any images referenced by the manuscript (covers, diagrams)

build scripts/templates you actually control (if used)

Artifacts (rebuild these):

outputs/.pdf

outputs/.epub

outputs/*.docx

If you can regenerate it, dont treat it like source.

The Anchor connection (no mysticism, just receipts)
Your ANCHOR.md is the contract that keeps you honest:

the repo layout you expect
the commands that should work
the checks you run when reality starts drifting
When youre tired, obvious becomes expensive. Anchor files are cheap insurance.

3) Versioning with Git: stop selling yourself work you already did
Git is not here to turn you into a developer. Its here to prevent these disasters:

I fixed it yesterday. Where did it go?
Which draft did I upload?
I changed one tiny thing and now everything is different.
I need the previous subtitle back. The good one.
The writer-friendly Git minimum
You can get 90% of the value with three commands:

Thats it. No branching epic required.

What to commit (a sensible default)
Commit:

manuscripts (publication/*.md)
Anchor + logs (ANCHOR.md, publication/INTERIM_PROGRESS_LOG.md)
build scripts (tools/*)
templates/styles you own (if any)
referenced images
Avoid committing:

generated outputs (outputs/*) unless you explicitly want release artifacts in the repo
If you do commit outputs, do it deliberately (and ideally in a separate commit) so history stays readable.

A good commit message formula
Use: verb + object + reason

Examples:

Add epigraph and replace HTML breaks with \newpage
Clarify Anchor contract and add build checks
Fix heading levels to improve EPUB navigation
Your future self doesnt need poetry. They need context.

4) Metadata discipline: titles, subtitles, series, and the Great Drift
Metadata is the most boring part of publishinguntil it costs you hours.

Drift happens when these dont match:

cover text
internal title page text (inside the book)
platform metadata fields (Draft2Digital, etc.)
filenames and folders
what you think you shipped
The One Sheet of Reality trick
Maintain one place where the current truth lives. YAML at the top of the manuscript is ideal.

Your YAML is already doing the job:

Practical rules that prevent drift
Change metadata in one place first (YAML), then update the cover/title page if needed.
Treat store dashboards as outputs, not the source of truth.
Decide your public title policy and stick to it:
subtitle everywhere vs cover-only
series name formatting
author name spelling/punctuation (yes, it matters)
EPUB note (quiet but important)
EPUB readers and libraries surface metadata aggressively. If your EPUB looks wrong in a device library, its often metadatanot layout.

5) Covers that match reality (outside and inside)
Covers are where drift becomes visible and embarrassing.

The classic mismatch:

cover says Title: Subtitle
title page inside says Title (or an older subtitle)
store listing says something else entirely
Minimum cover alignment checklist
cover text matches YAML (title/subtitle/author)
internal title page matches YAML (or you intentionally omit subtitle and document that choice)
EPUB metadata matches YAML
filenames are boring and consistent (no final_final_REAL2)
Where people lose time
exporting multiple cover sizes and forgetting which is live
tweaking cover text after upload but not updating the manuscript
tiny subtitle change turning into four separate edits across tools
Time-saving principle:
Make metadata edits once, then rebuild and re-export.

6) Flexible by design: kids books  technical  academic
Different writers have different habits. Good. The workflow should adapt without breaking.

This kit is deliberately permissive:

write in Markdown from an LLM, a text editor, Obsidian, VS Code, Notepadwhatever
keep structure simple: headings, lists, blockquotes, code fences
avoid format-fragile tricks that only one output understands
A safe subset of Markdown for predictable builds
Use freely:

/ ## / ### headings
bullet/numbered lists
blockquotes (>)
code fences (triple backticks)
emphasis (italic, bold)
links
Be cautious with:

raw HTML for layout (varies by output)
manual spacing tricks (multiple blank lines; renderers differ)
forcing pagination for EPUB/DOCX (they dont have pages in the same way)
Formatting philosophy (for tired humans)
If you cant explain why a formatting trick exists in one sentence, it doesnt belong in the canonical manuscript.

7) Quick timeline + firstship checklist
Getting to shipped is mostly reducing avoidable surprises.

A sane timeline (pamphlet edition)
Write in the canonical Markdown
Build PDF/EPUB/DOCX locally
Spot-check the usual failure points
Commit the changes that produced the shippable build
Upload/distribute
Tag the release (optional, but helpful)
Firstship checklist (fast, not fancy)
Content sanity

Title/subtitle/author match YAML and cover
Contents list matches headings (or is clearly manual and accurate)
No accidental everything is code sections (unclosed fences)
Build sanity

PDF opens, fonts look normal, headings look right
EPUB opens in at least one reader (Calibre is fine)
DOCX opens and headings are real headings (not bold paragraphs)
Common output gotchas

Scene breaks are consistent (pick one style and stick to it)
Images (if any) render and are correctly sized
Smart punctuation renders cleanly (XeLaTeX usually behaves)
The two-minute preview rule
If you only have two minutes, check:

the title/first page
the contents/nav
one code block
one major section break
Most disasters show up right there.

8) Microindex for tired humans
This is the Im panicking, where is that thing section.

Anchor file: the contract for whats real (paths, tools, commands, outputs)
Canonical manuscript: the one source you edit; everything else is generated
Drift: mismatches across cover, title page, stores, files, versions
Outputs: PDF/EPUB/DOCX artifacts built from the canonical manuscript
Pandoc: converter that turns Markdown into the three formats
XeLaTeX: PDF engine (good with fonts and smart punctuation)
Code fence: triple-backticks that must always be closed
Which file is real? Answer: the canonical manuscript + the commit history
Closing note (cheerful, realistic)
Youre not trying to become a tool expert. Youre trying to ship writing without losing days to nonsense.

This kit doesnt remove quirks from the world.

It makes them repeatable, diagnosable, and  eventually  boring.

Note: This Reproducible Self-Pub Kit is based on the architecture and patterns from the Home@ix FAIR project (see https://github.com/tonefreqhz/hom-ixFAIRindex), which established the foundational workflow for reproducible builds, PROJECT_ROOT anchoring, build invariants, and the Build Notes Anchor to prevent AI/human drift in long-running development.