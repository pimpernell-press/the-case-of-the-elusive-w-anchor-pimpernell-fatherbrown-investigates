# Transclusion Draft Experiment
## The DoughForge Restructuring — Flux Capacitor Driven

**Date:** 2026-03-25
**Status:** EXPERIMENTAL SANDBOX — does not replace manuscript or book.yaml
**Method:** Flux Capacitor AQAL scoring of all available material in this repo,
then restructuring based on quadrant balance, cluster affinity, and
corpus cross-references.

---

## The Inventory: What's Actually in This Repo

The CLAUDE.md says "four repos." The repo itself says otherwise. This is a
DoughForge fork. The dough is already on the counter. Here's the full inventory:

### A. The Novella (12 chapters in book.yaml build)

| # | File | Source (per 00_book_structure.md) |
|---|------|----------------------------------|
| F | manuscripts/foreword_the_canary.md | — |
| 1 | manuscripts/ch01_the_crime_scene_survey.md | repo_diagnostic_20260316_1558.txt |
| 2 | manuscripts/ch02_the_choosing_of_dragons.md | choosing dragons part 2.md |
| 3 | manuscripts/ch03_the_flux_capacitor.md | Flux capacitor and the halting problem work 17mars26.md |
| 3b | manuscripts/ch03b_the_triple_word_score.md | — (BROKEN) |
| 4 | manuscripts/ch04_the_circus_trucks.md | GPT-5.4 Pro circus trucks transcript |
| 5 | manuscripts/ch05_the_epilogue_that_came_first.md | epilogue first manuscript saga |
| 6 | manuscripts/ch06_the_work_to_six_forty_one.md | work to 6.41 20march 2026.md |
| 7 | manuscripts/ch07_the_wanking_in_circles.md | wanking in circles 2.txt |
| 8 | manuscripts/ch08_the_nine_one_one_call.md | wanchor 911.md |
| 9 | manuscripts/ch09_the_verdict.md | Synthesised from all files |
| 10 | manuscripts/ch10_the_paradox_of_the_helpful_vandal.md | — |

### B. The Reservoir (NOT in book.yaml build)

| File | Content | Size |
|------|---------|------|
| manuscripts/chapters/ch_cherry.md | "When You Stop Wanking and Lose Your Cherry" — Claude Code install transcript as Father Brown narrative. The conversation IS the book. | ~4,500 words |
| manuscripts/ch03_the_sin_of_helpfulness.md | "The Frog and the Scorpion" — BIS/Nominet as scorpion. DEVELOPED. | In repo but not in build |
| manuscripts/evidence/flux_capacitor_mindmap/narrative.md | "The Topology of Absence" — Father Brown traces the mindmap, discovers the Z-axis gap. Mrs. Hennessy = absent bridge. | ~2,000 words |
| manuscripts/evidence/flux_capacitor_mindmap/father_brown_narrative.md | "What Father Brown Saw" — Poetry node as Rosetta Stone. 4 clusters. Haiku as anchor. The bridge was always there. | ~4,000 words |
| manuscripts/evidence/four_repo_rationalisation.md | Technical audit of all 4 repos. Duplication map. Hygiene report. | ~3,000 words |
| manuscripts/evidence/metrics_baseline.md | "The Evidence Board: Twelve Metrics Baselined" — M1-M12 instrumentation. | ~2,000 words |
| publication/manuscript.md | "A Novel in Seven Contradictions" — Father Brown / Bragg dialogues. The Parable of the Fence. Full philosophical register. | Large |
| reservoir/the case of the elusive w-anchor...md | **THE FULL CORPUS.** 1.6MB. Build sessions, diagnostics, PowerShell scripts, conversation transcripts, everything. | 1.6MB |

### C. The Instruments

| File | Function |
|------|----------|
| widgets/flux_capacitor/index.html | AQAL bias detection widget. 544 lines. Keyword heuristics. Peirce Pragmatic Check. W-Anchor commit hash grounding. |
| widgets/aqual_screener/worldview_audit.md | AQAL pre-screener template |
| widgets/voice_widgets/*.md | 14 voice widget templates (Blake, Peirce, Cuppy, Chesterton, Wodehouse, etc.) |
| manuscripts/evidence/flux_capacitor_mindmap/mindmap_data.json | Full graph: 30 nodes, 28 edges, 4 clusters, 3 axes |

---

## Flux Capacitor Scoring: The Four Clusters

The mindmap data reveals four thematic clusters under the "Poetry" node.
These clusters — not the current chapter numbering — are the natural
organising principle of the material.

### Cluster 1: BIS / Basel / Usury (7 children)
**AQAL dominant quadrant: ITS (Exterior Collective)**
Institutional power, systemic extraction, Basel Accords, BIS as
"the gentleman in the lift." Father Brown's register: sin as structure.

**Corpus nodes:** bis-as-usual-usury-haiku-cycle, sentancing-the-bank,
teflon-coated-bank, Jesus and Economic Life, tower-in-basle,
usury-hells-fuel, Naming Usuries Tyrant

**Cross-refs:** corpus-index → bis.org/bcbs/basel3.htm;
BIS haiku → running gag #8 (resolves in Ch09)

**Current novella chapters drawing from this cluster:**
- Ch03 (Flux Capacitor) — partial, via Nominet-as-BIS parallel
- Ch09 (The Verdict) — names the guilty, systemic sin
- publication/manuscript.md (Seven Contradictions) — **HEAVILY** — this
  is the primary BIS register, currently NOT in the novella build

### Cluster 2: Flux Capacitor / Truthiness (4 children)
**AQAL dominant quadrant: IT (Exterior Individual)**
Measurable, falsifiable, pragmatic. Peirce's maxim. The widget itself.
The instrument panel. Observable bias detection.

**Corpus nodes:** the-flux-capacitor-of-truthiness, how-to-make-our-ideas-clear,
how-to-make-shelter-clear-a-peircean, the-strawberry-dunciad

**Cross-refs:** widget AQAL grid, Peirce Pragmatic Check, Strawberry Politics title

**Current novella chapters drawing from this cluster:**
- Ch03 (Flux Capacitor) — directly
- manuscripts/evidence/father_brown_narrative.md — **HEAVILY** — "the widget
  is a poem written in HTML"

### Cluster 3: Housing / Mortgage / Dough (4 children)
**AQAL dominant quadrant: ITS + IT (Exterior both)**
The thesis in seven words: "no one builds a home with usury."
Conquest of Dough. Housing ladder. Affordable. Mort-gage = dead pledge.

**Corpus nodes:** the-conquest-of-dough-a-prophecy, no-one-builds-a-home-with-usury,
the-housing-ownership-ladder-repealed, Affordable

**Cross-refs:** DoughForge repo, COPE business model, Home@ix research,
Savills housing data, HBF survey

**Current novella chapters drawing from this cluster:**
- Foreword (The Canary) — partial, the fraud as canary
- Ch04 (Circus Trucks) — corporate shell game
- NONE of the FAIR-Index data is transcluded anywhere

### Cluster 4: Circle of Blame / Power (5 children)
**AQAL dominant quadrant: WE + ITS (Collective both)**
Philippic. Iron law of oligarchy. Green Fire. Empire. Unmasking.
Everyone blames the next person. Nobody breaks the circle.

**Corpus nodes:** philippic-against-the-circle-of-blame,
the-iron-law-of-oligarchy, were-an-empire-now, unmasking-the-hidden-power,
Green Fire Against the Counting Towers

**Cross-refs:** DoughForge circle-of-blame chapters, CLAUDE.md running gag #7

**Current novella chapters drawing from this cluster:**
- Ch02 (Choosing of Dragons) — regulatory circle
- Ch07 (Wanking in Circles) — complaint circle
- Ch08 (Nine-One-One Call) — emergency vs. ticket

---

## The Restructuring: What the Flux Capacitor Reveals

### Problem 1: The ITS Monoculture

The current 12-chapter novella is almost entirely in the ITS quadrant
(Exterior Collective — institutional, systemic). Chapters 1, 2, 4, 5, 6, 7,
8, 9 all address institutional failure. Only Ch03b (Triple Word Score) provides
I/WE balance — and it's BROKEN.

The Flux Capacitor widget's own logic says: if bias_metric > 50
(IT+ITS dominance), recommend "Blake (I quadrant — inner vision),
Ruskin (WE quadrant — shared moral economy)."

**The cure is already in the repo.** The voice widgets at
`widgets/voice_widgets/` include Blake, Peirce, Cuppy, Chesterton,
Wodehouse — exactly the voices needed to rebalance.

### Problem 2: The Absent Reservoir

Three major pieces of writing in this repo are NOT in the build:
1. **ch_cherry.md** — the strongest I-quadrant chapter (inner experience,
   confession, the doorway metaphor, the happy ending)
2. **father_brown_narrative.md** — the strongest I+WE chapter (Father Brown
   at the evidence board, the Poetry node as integrating layer, haiku
   as anchor)
3. **publication/manuscript.md** — the strongest WE+ITS chapter (Father Brown
   and Bragg discussing fences, ownership, the oldest question in the garden)

These three files contain the material that rebalances the entire book.
They are on the counter. They are not in the oven.

### Problem 3: The Missing Running Gags

From the subagent's earlier analysis: 8 of 10 running gags from CLAUDE.md
have zero appearances in the 12-chapter build. The gags exist as
design specifications but were never threaded. The transclusion exercise
is where they get wired in.

---

## The Experimental Draft: A New Index

### Restructured Chapter Order (Cluster-Driven)

The Flux Capacitor clusters suggest a four-act structure mirroring the
four AQAL quadrants, with each act anchored to one cluster and balanced
by material from the others.

#### ACT I: THE CRIME (IT quadrant — Evidence, Measurement, Fact)
*Anchored to: Flux Capacitor cluster. Voice: Peirce, Cuppy.*

| New # | Source | Title | Transclusion |
|-------|--------|-------|-------------|
| 1 | ch01_the_crime_scene_survey.md | The Crime Scene Survey | + anchor_verify output (from anchor_verify.ps1 in repo root). Thread: [OK][OK][OK][MISSING]. Transclude actual script output as evidence exhibit. |
| 2 | ch03_the_flux_capacitor.md | The Flux Capacitor and the Halting Problem | + widget HTML excerpt (from widgets/flux_capacitor/index.html lines 225-327: the W-Anchor block, AQAL grid, and source input). Thread: Peirce Pragmatic Check. |
| 3 | ch06_the_work_to_six_forty_one.md | The Work to Six Forty-One | + 742819 sort code first appearance. Thread: the timestamp as evidence, the metadata as testimony. |

#### ACT II: THE PATTERN (ITS quadrant — Systems, Institutions, Power)
*Anchored to: BIS/Basel cluster + Circle of Blame cluster. Voice: Chesterton, Cicero.*

| New # | Source | Title | Transclusion |
|-------|--------|-------|-------------|
| 4 | ch02_the_choosing_of_dragons.md | The Choosing of Dragons | + Iron Law of Oligarchy reference (from mindmap cluster). Thread: regulatory capture as designed feature. |
| 5 | ch04_the_circus_trucks.md | The Circus Trucks | + Broadstairs address chain. Thread: shell companies, corporate veil, the trail that always leads to Broadstairs. |
| 6 | ch07_the_wanking_in_circles.md | The Wanking in Circles Problem | + philippic-against-the-circle-of-blame excerpt (from DoughForge corpus node). Thread: complaint circle = Circle of Blame. |
| 7 | ch08_the_nine_one_one_call.md | The Nine-One-One Call | + BIS haiku fragment ("Money isn't real..."). Thread: emergency vs. ticket, who decides what's urgent. |

#### ACT III: THE BRIDGE (I + WE quadrants — Inner Life, Shared Meaning)
*Anchored to: Housing/Dough cluster. Voice: Blake, Wodehouse, Roger G. Lewis.*

| New # | Source | Title | Transclusion |
|-------|--------|-------|-------------|
| 8 | ch03b_the_triple_word_score.md | The Triple Word Score | **FIX FIRST.** + Complete Scrabble board state. Thread: WANKER tile, Pigeon, four parishioners as four AQAL quadrants (Mrs Ledger=IT, Dex=WE, Fairweather=ITS, Siobhan=I). |
| 9 | **NEW: ch_cherry.md** | When You Stop Wanking and Lose Your Cherry | Already written. Strongest I-quadrant chapter. Thread: placeholder key = placeholder identity. 11 theme screens = 11 times through the confessional door. Git-as-theology enters here via Thomas. |
| 10 | ch03_the_sin_of_helpfulness.md | The Frog and the Scorpion | Already developed but not in build. Thread: Mrs Hennessy's phone. "Two blue ticks. Silence." The scorpion stings because it is its nature. Connect to BIS corpus via father_brown_narrative.md. |

#### ACT IV: THE VERDICT (All four quadrants — Integration)
*Anchored to: Poetry node (all clusters converge). Voice: All.*

| New # | Source | Title | Transclusion |
|-------|--------|-------|-------------|
| 11 | ch05_the_epilogue_that_came_first.md | The Epilogue That Came First | + Transclude as INTERIM_PROGRESS_LOG.md format (per CLAUDE.md). Thread: the fix that precedes the complaint. The system working as designed. |
| 12 | ch10_the_paradox_of_the_helpful_vandal.md | The Paradox of the Helpful Vandal | + father_brown_narrative.md excerpt — the Poetry node as Rosetta Stone. Thread: "the absent centre was never absent. It was filed under Poetry." |
| 13 | ch09_the_verdict.md | The Verdict | + Full haiku resolution: "Money isn't real. / Someone always bakes the bread. / Who owns the oven?" + FAIR-Index data exhibit (from homeix corpus). Thread: all gags resolve. All quadrants present. Git history as testimony. |

### The Foreword (unchanged position, new transclusion)

| # | Source | Title | Transclusion |
|---|--------|-------|-------------|
| F | foreword_the_canary.md | The Canary in the Coal Mine | + FAIR-Index housing affordability data exhibit (from hom-ixFAIRindex). Mrs Cattermole = the canary. The data that proves the fraud mathematically. |

---

## Transclusion Map: Corpus → Chapter

This table shows which corpus material feeds into which restructured chapter,
and via which AQAL quadrant the connection operates.

| Corpus Source | Quadrant | Target Chapter(s) | Connection Type |
|--------------|----------|-------------------|----------------|
| anchor_verify.ps1 (repo root) | IT | Ch1 (Crime Scene) | Direct: script output as evidence exhibit |
| widgets/flux_capacitor/index.html | IT | Ch2 (Flux Capacitor) | Direct: HTML excerpt as narrative prop |
| 742819 sort code | IT | Ch3 (Six Forty-One), Ch5 (Circus Trucks) | Thread: appears in evidence, reappears in shell company trail |
| mindmap_data.json — BIS cluster | ITS | Ch4 (Dragons), Ch7 (911 Call) | Structural: regulatory capture maps to BIS Basel pattern |
| mindmap_data.json — Circle of Blame cluster | ITS+WE | Ch6 (Circles) | Direct: philippic excerpt transcluded |
| mindmap_data.json — Flux Capacitor cluster | IT | Ch2 (Flux Capacitor) | Structural: 4 corpus nodes map to 4 widget components |
| mindmap_data.json — Housing/Dough cluster | ITS+IT | Foreword, Ch13 (Verdict) | Structural: FAIR-Index data grounds the foreword; "no one builds a home with usury" grounds the verdict |
| ch_cherry.md | I | Ch9 (Cherry) — **NEW addition to build** | Direct: already written, not yet in book.yaml |
| ch03_the_sin_of_helpfulness.md | I+ITS | Ch10 (Frog/Scorpion) — **NEW addition to build** | Direct: already written, not yet in book.yaml |
| father_brown_narrative.md | I+WE | Ch12 (Helpful Vandal) | Excerpt: Poetry node passage transcluded |
| narrative.md (Topology of Absence) | WE | Ch10 (Frog/Scorpion) | Structural: Z-axis gap = Mrs Hennessy's silence |
| publication/manuscript.md (Seven Contradictions) | WE+ITS | **NOT directly transcluded** — but the Bragg dialogues are the philosophical register that the voice widgets channel. They are the subtext, not the text. |
| BIS haiku cycle (TheBrain child) | I | Ch7 (911 Call), Ch13 (Verdict) | Thread: fragment in Ch7, full resolution in Ch13 |
| voice_widgets/*.md | All | All chapters via shade pass | Structural: each voice widget provides the register for its quadrant |

---

## Running Gag Wiring Plan

| Gag | Where It Enters | Where It Threads | Where It Resolves |
|-----|----------------|------------------|-------------------|
| [OK][OK][OK][MISSING] | Ch1 (Crime Scene) — anchor_verify exhibit | Ch3 (Six Forty-One) — timestamp is [OK], meaning is [MISSING]. Ch9 (Cherry) — placeholder key is [MISSING] | Ch13 (Verdict) — all checks pass. "The system is working. That is the problem." |
| WANKER / Scrabble | Ch8 (Triple Word Score) — first tile placed | Ch9 (Cherry) — username "peewe" = the name you chose in haste | Ch13 (Verdict) — "The word was always on the board. Nobody looked down." |
| Broadstairs | Ch5 (Circus Trucks) — shell company address | Ch6 (Circles) — correspondence return address | Ch13 (Verdict) — Father Brown never goes. "Broadstairs is not a place. Broadstairs is a condition." |
| Biscuits / Tesco | Ch8 (Triple Word Score) — Potton Tesco biscuits at Scrabble | Ch10 (Frog/Scorpion) — Mrs Hennessy brought the biscuits before she left | Ch13 (Verdict) — "The biscuits were the last real thing." |
| Git-as-theology | Ch9 (Cherry) — "A fork is like the Reformation" — Thomas enters | Ch2 (Flux Capacitor) — "A merge conflict is the Council of Nicaea" | Ch13 (Verdict) — "The commit hash is the confession. It cannot be amended." |
| Mrs Hennessy's phone | Ch4 (Dragons) — first mention, two blue ticks | Ch10 (Frog/Scorpion) — "Her phone is still in the WhatsApp" | Ch13 (Verdict) — "She read it. She did not reply. That is not absence. That is judgement." |
| 742819 | Ch3 (Six Forty-One) — sort code in timestamp evidence | Ch5 (Circus Trucks) — sort code on shell company filings | Ch13 (Verdict) — "The same number. Every time. The system does not vary because the system does not need to." |
| Haiku fragments | Ch7 (911 Call) — "Money isn't real." | Ch11 (Epilogue) — "Someone always bakes the bread." | Ch13 (Verdict) — full: "Money isn't real. / Someone always bakes the bread. / Who owns the oven?" |
| The Pigeon | Ch8 (Triple Word Score) — shits on Scrabble board | Every chapter — appears in a different location, unremarked | Ch13 (Verdict) — "The only honest participant." |
| Cold tea | Already threaded in F, Ch2, Ch9, Ch10 | Continue in new chapters | The tea is always cold because the conversation is always longer than expected |

---

## What This Restructuring Does

1. **Adds 3 chapters to the build** that are already written but excluded:
   ch_cherry.md, ch03_the_sin_of_helpfulness.md, and material from
   father_brown_narrative.md. The book goes from 12 to 13+Foreword chapters.

2. **Reorders by AQAL quadrant** instead of chronological investigation order.
   The reader moves from Evidence (IT) → Systems (ITS) → Inner Life (I+WE) →
   Integration (All). This mirrors the Flux Capacitor's own diagnostic flow.

3. **Threads all 10 running gags** with explicit entry, threading, and
   resolution points. Currently 8 of 10 are absent.

4. **Creates a transclusion map** showing exactly which corpus material
   feeds each chapter and through which quadrant.

5. **Identifies the Seven Contradictions dialogue** (publication/manuscript.md)
   as the book's philosophical subtext — not directly transcluded but
   channelled through voice widgets during the shade pass.

6. **Diagnoses Ch03b (Triple Word Score) as the structural keystone** —
   the only chapter grounding the I+WE quadrants. Its BROKEN status is not
   just a bug; it's a load-bearing failure. Fix it first.

---

## What This Restructuring Does NOT Do

- Does not modify any existing files
- Does not change book.yaml
- Does not touch the current EPUB build
- Does not invent new material — every transclusion points to existing
  files in this repo
- Does not replace CLAUDE.md's authority — this is an experimental sketch
  in docs/, not a directive

---

## The Peirce Pragmatic Check

*"Consider what effects, that might conceivably have practical bearings,
we conceive the object of our conception to have. Then, our conception
of these effects is the whole of our conception of the object."*

**Practical bearing of this restructuring:** If implemented, the novella
gains three chapters of existing prose, threads all running gags, rebalances
AQAL coverage from ITS-monocrop to four-quadrant integration, and grounds
every chapter in specific corpus material rather than floating as
self-contained essays.

**The dough has been through the forge. The loaf is reshaped. Whether
to bake it is the author's decision.**
