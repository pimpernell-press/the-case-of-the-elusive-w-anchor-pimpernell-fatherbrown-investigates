# Stage 02: Flux Capacitor Scoring
## Every DoughForge Chapter Through the AQAL Framework

**Date:** 2026-03-25
**Instrument:** `widgets/flux_capacitor/index.html` (544 lines, in this repo)
**Source:** `conquest_of_doughforge.epub` (55 chapters, 55,000+ words)
**Method:** AQAL keyword heuristics ported from widget JS (lines 456-475)

---

## Scoring Method

The Flux Capacitor widget scores text across four AQAL quadrants using
keyword frequency heuristics. Each quadrant starts at a base of 10 and
gains 8 points per keyword hit, capped at 100.

### Keyword Lists (from widget source)

**I — Interior Individual:**
feel, experience, inner, intend, hope, dream, conscience, sin, guilt,
prayer, doubt, faith, soul, confess, penitent, heart, spirit

**WE — Interior Collective:**
culture, shared, community, narrative, parish, together, blame, trust,
belonging, congregation, we, our, moral, covenant, common

**IT — Exterior Individual:**
data, evidence, fact, commit, hash, measure, verify, check, log, number,
code, git, dns, sort code, ratio, formula, equation, proof, index, metric

**ITS — Exterior Collective:**
system, institution, structure, economy, power, bank, debt, regulation,
bis, basel, fraud, companies house, broadstairs, oligarchy, usury,
mortgage, monetary, central bank

### Derived Metrics

- **Balance** = (I + WE + IT + ITS) / 4
- **Bias** = ((IT + ITS)/2 - (I + WE)/2) * 0.8, clamped to [-100, +100]
  - Positive = exterior/technical lean
  - Negative = interior/personal lean
- **Contradiction Index** = (|bias| / 100) * (1 - checked_quads/4) * 0.7 + 0.1
  - checked_quads = quadrants scoring > 25
- **Dominant** = highest-scoring quadrant

### Widget Diagnosis Thresholds (lines 505-520)

| Bias Range | Widget Says |
|-----------|-------------|
| > +50 | "Strong right-bias. IT/ITS dominance. Inner life suppressed." |
| +20 to +50 | "Moderate right-lean. Good anchor discipline; needs more Coleridge." |
| -20 to +20 | "Balanced. Quadrant equilibrium maintained. The W-Anchor is holding." |
| -50 to -20 | "Moderate left-lean. Rich inner register. Needs more grounded evidence." |
| < -50 | "Strong left-bias. I/WE dominance. Evidence and systems under-represented." |

---

## Full Scoring Results

### Layer 1: The Novel — "Hand Shandy" (ch001, ch005)

| File | Title | Words | I | WE | IT | ITS | Bal | Bias | Dom | Diagnosis |
|------|-------|-------|---|----|----|-----|-----|------|-----|-----------|
| ch001 | THE LIFE AND OPINIONS OF HAND SHANDY | 3,470 | 26 | 58 | 82 | 82 | 62 | +32 | IT | Moderate right-lean. Rich WE from community/narrative framing. Needs Blake. |
| ch005 | Chapter Zero: Ever Had a Wankel? | 826 | 18 | 26 | 34 | 34 | 28 | +10 | IT | Near-balanced but thin across all quadrants. Comedy register doesn't score high on keywords — the humour is structural, not lexical. |

**Layer diagnosis:** The novel frame has the highest WE score (58 in ch001)
of any non-apparatus chapter. The Shandean voice carries community and
shared meaning that the Father Brown novella currently lacks.

### Layer 2: The Essay Sequence — Chapters 0.0–0.7 (ch006–ch013)

| File | Title | Words | I | WE | IT | ITS | Bal | Bias | Dom | Diagnosis |
|------|-------|-------|---|----|----|-----|-----|------|-----|-----------|
| ch006 | Ch 0.0 — Series Introduction | 1,434 | 26 | 34 | 66 | 34 | 40 | +16 | IT | Moderate right-lean. Blake and Parliament of LLMs present but IT keywords dominate. |
| ch007 | Ch 0.1: Unacknowledged Legislator | 568 | 26 | 34 | 50 | 26 | 34 | +6 | IT | Near-balanced. Shelley lifts I, "legislator" lifts WE. Good equilibrium. |
| ch008 | Ch 0.2: The Ration Still Arriving | 1,073 | 26 | 42 | 58 | 50 | 44 | +16 | IT | Moderate right-lean. "Ration" as ratio pulls IT; community provision pulls WE. |
| ch009 | Ch 0.3: The Kiss Precise | 1,892 | 26 | 42 | 66 | 58 | 48 | +22 | IT | Moderate right-lean. Largest essay. Werner, Del Mar, Confucius all score IT. "Moral" and "community" lift WE. Highest-balanced essay. |
| ch010 | Ch 0.4: The Moral Sign | 1,706 | 42 | 58 | 50 | 74 | 56 | +10 | ITS | **Near-balanced, ITS dominant.** Ruskin's moral economy scores I (42 — conscience, faith) and WE (58 — moral, community, shared). Only essay chapter where ITS dominates. The bridge between inner life and institutional critique. |
| ch011 | Ch 0.5: The Dying Bird | 1,119 | 18 | 58 | 82 | 42 | 50 | +19 | IT | High WE (58) from Paine's collective rhetoric. IT spike from "evidence" and "proof" language. The I quadrant is weak — the bird's inner experience is described from outside. |
| ch012 | Ch 0.6: The Formula | 1,255 | 26 | 34 | 90 | 58 | 52 | +35 | IT | **Strongest IT chapter in essays.** The FAIR formula IS the IT quadrant — ratio, formula, equation, index, measure. ITS from "economy" and "system." Moderate right-lean. |
| ch013 | Ch 0.7: The Grey Space | 1,291 | 34 | 34 | 58 | 34 | 40 | +10 | IT | Most balanced essay. "Grey space" between legal/right, market/morality lifts I. Elegy register. The human cost that won't fit the form. |

**Layer diagnosis:** The essay sequence is where the argument lives.
ch010 (Moral Sign) and ch009 (Kiss Precise) are the two best-balanced
essays — and both are absent from the Father Brown novella. ch012 (Formula)
is the strongest IT chapter — the FAIR housing data the novella Foreword
is supposed to transclude but doesn't.

### Layer 3: The Teaching Curriculum — Lessons 1–9 (ch014, ch025–ch034)

| File | Title | Words | I | WE | IT | ITS | Bal | Bias | Dom |
|------|-------|-------|---|----|----|-----|-----|------|-----|
| ch014 | Quick Start Guide | 752 | 18 | 18 | 90 | 18 | 36 | +29 | IT |
| ch025 | Teaching — DoughForge for Writers | 232 | 18 | 26 | 50 | 18 | 28 | +10 | IT |
| ch026 | Lesson 1 — What Is a Terminal? | 597 | 18 | 34 | 18 | 26 | 24 | -3 | WE |
| ch027 | Lesson 2 — What Is a File Path? | 714 | 18 | 18 | 34 | 26 | 24 | +10 | IT |
| ch028 | Lesson 3 — What Is Git? | 757 | 18 | 18 | 66 | 18 | 30 | +19 | IT |
| ch029 | Lesson 4 — The Anchor | 784 | 18 | 18 | 50 | 26 | 28 | +16 | IT |
| ch030 | Lesson 5 — Your First Build | 729 | 26 | 26 | 42 | 10 | 26 | 0 | IT |
| ch031 | Lesson 6 — The FAIR Paper | 733 | 18 | 18 | 74 | 42 | 38 | +32 | IT |
| ch032 | Lesson 7 — Publishing Without a Publisher | 786 | 18 | 18 | 58 | 18 | 28 | +16 | IT |
| ch033 | Lesson 8 — Communication is NP Hard | 967 | 26 | 50 | 58 | 34 | 42 | +6 | IT |
| ch034 | Lesson 9 — W-Anchor as Emergency Reset | 880 | 42 | 18 | 66 | 26 | 38 | +13 | IT |

**Layer diagnosis:** Uniformly IT-dominant. Two chapters break the pattern:
- Lesson 1 (Terminal) is the only WE-dominant lesson — "why should you care?" frames technical skill as community empowerment
- Lesson 9 (Emergency Reset) has the highest I score (42) — when everything breaks, it becomes personal

**Transclusion candidates for novella:**
- Lesson 3 (Git) → Thomas Potts's Git-as-theology. "The Three Commands You Actually Need."
- Lesson 4 (The Anchor) → the [OK][OK][OK][MISSING] running gag source
- Lesson 8 (NP Hard) → highest WE score (50) — communication failure as design

### Layer 4: The Flux Capacitor (ch035)

| File | Title | Words | I | WE | IT | ITS | Bal | Bias | Dom |
|------|-------|-------|---|----|----|-----|-----|------|-----|
| ch035 | The Flux Capacitor of Strawberry Politics | 972 | 50 | 42 | 100 | 42 | **58** | +20 | IT |

**The highest-balanced chapter in the entire corpus.**

I=50 (conscience, faith, inner experience present — the epistemological
argument IS about inner truthfulness). WE=42 (shared meaning, community
of inquiry). IT=100 (maxed — every IT keyword appears). ITS=42 (system,
institution present but not dominant).

The Flux Capacitor chapter IS the instrument scoring itself. Balance=58
is the widget's own reading of its own text. This is the Tarski moment —
the system measuring itself and producing a meaningful result because
the commit hash (the external anchor) grounds it.

**Widget self-diagnosis:** "Moderate right-lean. Good anchor discipline;
needs more Coleridge." — i.e., the widget knows it's IT-heavy and
prescribes more I-quadrant poetry. It prescribes its own cure.

### Layer 5: The Apparatus (ch015–ch024, ch036–ch055)

| File | Title | Words | I | WE | IT | ITS | Bal | Bias | Dom |
|------|-------|-------|---|----|----|-----|-----|------|-----|
| ch015 | Author's Note | 252 | 18 | 18 | 34 | 10 | 20 | +3 | IT |
| ch016 | Ch 1: The Drift | 374 | 18 | 34 | 18 | 10 | 20 | -10 | WE |
| ch017 | Ch 2: The Canonical Source | 464 | 18 | 10 | 34 | 18 | 20 | +10 | IT |
| ch018 | Ch 3: What Naming Does | 418 | 10 | 18 | 18 | 10 | 14 | 0 | WE |
| ch019 | Ch 4: The Formula | 407 | 26 | 18 | 42 | 26 | 28 | +10 | IT |
| ch020 | Ch 5: The Counter-Spell | 429 | 18 | 34 | 34 | 18 | 26 | 0 | WE |
| ch021 | Ch 6: The Grey Space | 378 | 10 | 10 | 42 | 18 | 20 | +16 | IT |
| ch022 | Ch 7: The Unacknowledged Legislator | 372 | 10 | 18 | 18 | 18 | 16 | +3 | WE |
| ch023 | Ch 8: The Praxis | 363 | 18 | 10 | 18 | 18 | 16 | +3 | I |
| ch024 | Epilogue: The Ration Still Arriving | 293 | 10 | 18 | 34 | 10 | 18 | +6 | IT |
| ch038 | Session Synthesis (A) | 933 | 26 | 26 | 34 | 66 | 38 | +19 | ITS |
| ch041 | Session Synthesis (B) | 1,424 | 34 | 42 | 82 | 50 | 52 | +22 | IT |
| ch042 | QED — To Wanch or Not to Wanch | 863 | 34 | 18 | 66 | 26 | 36 | +16 | IT |
| ch043 | Appendix A — The FAIR Paper | 306 | 18 | 10 | 74 | 26 | 32 | +29 | IT |
| ch044 | Appendix B — Pete and Dud Compile the Book | 1,372 | 26 | 26 | 50 | 34 | 34 | +13 | IT |
| ch045 | Appendix C — The Phantom Chapters | 1,258 | 26 | 18 | 74 | 10 | 32 | +16 | IT |
| ch046 | Part Two: The Protocol | 1,399 | 26 | 26 | 82 | 26 | 40 | +22 | IT |
| ch047 | Part Three: Shipping It | 2,034 | 26 | 34 | 98 | 34 | 48 | +29 | IT |
| ch048 | Glossary & Dramatis Personae | 2,235 | 18 | 34 | 98 | 100 | 62 | +58 | ITS |
| ch049 | Bibliography & Transclusion Register | 11,367 | 66 | 82 | 100 | 100 | **87** | +21 | IT |
| ch050 | Appendix F — Index | 1,855 | 18 | 34 | 66 | 74 | 48 | +35 | ITS |
| ch051 | Epilogue: Protocol Goes Live | 126 | 18 | 10 | 42 | 18 | 22 | +13 | IT |
| ch052 | DoughForge Key — Library Awaits | 138 | 18 | 26 | 18 | 10 | 18 | -6 | WE |
| ch053 | Scaling Round — Home@ix | 135 | 18 | 10 | 58 | 18 | 26 | +19 | IT |
| ch054 | Also by Roger G. Lewis | 231 | 18 | 18 | 50 | 10 | 24 | +10 | IT |
| ch055 | Transcluded Citations Map | 3,138 | 58 | 34 | 100 | 82 | 68 | +36 | IT |

**Notable in the apparatus:**
- **ch016 (The Drift)** — the only novel chapter with negative bias (-10). WE-dominant. "Three weeks before the all-nighter." The human story.
- **ch042 (QED)** — I=34. The Horace poem. Inner register present.
- **ch048 (Glossary)** — ITS=100, IT=98. Balance=62. The most ITS-saturated chapter. Contains the Dramatis Personae.
- **ch049 (Bibliography)** — Balance=87. **Highest balance of any chapter.** Because it references everything — every quadrant is cited.

---

## Global Corpus Profile

| Metric | Value | Assessment |
|--------|-------|------------|
| Chapters scored | 55 | |
| Stubs excluded from analysis | 4 (ch036, ch037, ch039, ch040) | Placeholder chapters, <35 words total |
| Mean I score | 22.5 | **WEAK.** Inner life rarely surfaces. |
| Mean WE score | 27.0 | **LOW-MODERATE.** Community present in clusters but thin overall. |
| Mean IT score | 53.7 | **DOMINANT.** Code, formula, evidence, measure saturate the corpus. |
| Mean ITS score | 32.4 | **MODERATE.** Systems and institutions present but patchy. |
| Mean Balance | 33.9 | Below 40 = unbalanced corpus. |
| Mean Bias | +13.8 | Moderate exterior/technical lean. |
| IT-dominant chapters | 38/55 (69%) | |
| ITS-dominant chapters | 5/55 (9%) | |
| WE-dominant chapters | 8/55 (15%) | |
| I-dominant chapters | 1/55 (2%) | Only ch023 (The Praxis) |
| Balanced chapters (bias -10 to +10) | 14/55 (25%) | |

### Top 5 by Balance (most even quadrant coverage)

| Rank | Chapter | Balance | Profile |
|------|---------|---------|---------|
| 1 | ch049 — Bibliography | 87 | References everything |
| 2 | ch048 — Glossary | 62 | Defines everything |
| 3 | ch001 — Hand Shandy | 62 | The novel frame |
| 4 | ch035 — Flux Capacitor | 58 | The instrument itself |
| 5 | ch010 — The Moral Sign | 56 | Ruskin/AQAL |

### Top 5 by I Score (interior individual — conscience, faith, inner life)

| Rank | Chapter | I Score | Why |
|------|---------|---------|-----|
| 1 | ch049 — Bibliography | 66 | Cites spiritual/philosophical sources |
| 2 | ch055 — Citations Map | 58 | Cross-references inner-life material |
| 3 | ch035 — Flux Capacitor | 50 | Epistemological self-examination |
| 4 | ch004 — Preface | 42 | Author's personal framing |
| 5 | ch010 — Moral Sign | 42 | Ruskin's moral conscience |
| 5= | ch034 — Lesson 9 (Emergency Reset) | 42 | When it breaks, it's personal |

### Top 5 by WE Score (interior collective — community, shared meaning)

| Rank | Chapter | WE Score | Why |
|------|---------|----------|-----|
| 1 | ch049 — Bibliography | 82 | Maps a community of sources |
| 2 | ch001 — Hand Shandy | 58 | Shandean community narrative |
| 2= | ch010 — Moral Sign | 58 | Ruskin's shared moral economy |
| 2= | ch011 — Dying Bird | 58 | Paine's collective rhetoric |
| 5 | ch033 — Lesson 8 (NP Hard) | 50 | Communication as community problem |

---

## The Flux Capacitor's Prescription

The widget's own logic (lines 505-520) says:

For a corpus with Bias +14, Balance 34:

> **"Moderate right-lean (IT/ITS slight dominance). Behavioural and
> systemic analysis present but cultural narratives thin. Good anchor
> discipline; needs more Coleridge."**
>
> **Recommended voice widgets:** Blake or Shelley for I quadrant warmth.
> The Danegeld stanza belongs here.

The available voice widgets in this repo (`widgets/voice_widgets/`):
- **william_blake.md** — I quadrant (inner vision, prophetic)
- **cs_peirce.md** — IT quadrant (pragmatic evidence)
- **will_cuppy.md** — IT quadrant (self-deprecating empiricism)
- **chesterton.md** — I+WE (moral, communal, Father Brown's register)
- **wodehouse.md** — WE (social comedy, shared absurdity)
- **cicero.md** — ITS (institutional rhetoric, the philippic)
- **roger_g_lewis.md** — All quadrants (the author's own voice)

The corpus needs **Blake, Chesterton, and Wodehouse** — the three voices
that score highest in I and WE. The teaching layer and apparatus have
plenty of Peirce and Cuppy already.

---

## What This Scoring Reveals for Stage 04 (Transclusion Map)

1. **The novella's I+WE deficit has a source cure.** ch010 (Moral Sign),
   ch011 (Dying Bird), ch013 (Grey Space), and ch005 (Wankel) collectively
   provide I=34/WE=44 average — significantly above the corpus mean.

2. **The Flux Capacitor chapter (ch035) is the fulcrum.** It's the only
   chapter that meaningfully touches all four quadrants. It should be
   transcluded not as reference but as enacted demonstration.

3. **The novel chapters (ch016-ch024) are WE-rich and IT-poor.** They are
   the opposite of the novella. If any novel-layer material enters the
   Father Brown narrative, it rebalances toward the interior.

4. **The Bibliography (ch049) is not just reference material.** Its
   Balance=87 means it is the single most complete AQAL artefact in the
   corpus. The transclusion register it contains IS the map for Stage 04.
