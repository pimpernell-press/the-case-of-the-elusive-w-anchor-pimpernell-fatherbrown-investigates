# INTERIM PROGRESS LOG — The Case of the Elusive W-Anchor
# Updated: 2026-03-24

## Status: ANCHOR PLANTED — Tools need porting

### What exists and works
- anchor.py — 102-line path registry, all 18 required paths verified OK
- book.yaml — 41-line chapter manifest, 9 chapters
- manuscripts/ — all 9 chapter .md files present
- publication/ — metadata.yaml, front_matter/ with foreword, dedication, preface
- assets/cover/ — base_cover.png + front_cover.jpg
- dist/ — EPUB and DOCX already built (PDF not yet)
- ANCHOR.md — human-readable anchor doc

### What needs doing next
1. Port DoughForge tools — change import from paths to import from anchor
2. DO NOT REWRITE anchor.py or book.yaml — they are verified working
3. Git add anchor.py book.yaml INTERIM_PROGRESS_LOG.md
4. Fix tool imports one at a time

### Known hazards
- New Claude sessions rewrite working code. READ THIS FILE FIRST.
- The Hobbel: AI paid by token rewrites everything to generate output.
- Father Brown calls this the sin of helpfulness.

### The Intertwingularity Index
The full index exists (see context/index). Load-bearing nodes:
- Tarski -> anchor -> metalanguage -> truth
- Werner -> credit creation -> NCC -> FAIR-Index
- Nelson -> transclusion -> Xanadu -> intertwingularity
- Soddy -> Descartes Circle -> money as debt -> Strawberry Economics
- Pete and Dud -> Wankel -> recursive metaphor -> self-describing book
- Tarski-Malone-Lewis synthesis: housing, money, logic share structure

### Epigraph architecture (from handwritten notes 2026-03-23/24)
- To Wanch or Not to Wanch — Hamlet parody, existential frame
- Horace/Shelley/Pushkin — three monuments, three perspectives
  - Brass (Horace: aere perennius)
  - Sands (Shelley: Ozymandias)
  - Momenti (Pushkin: not built by hands)
- Tarski Metaphor — the referent, the denominator, the truth-predicate
- Twinkle Twinkle Little Prompt — LLMs do not transcend, they do not think
- Adrian Malone/Galbraith — making the invisible visible (Age of Uncertainty)
- Lead a Horse to Water — you can show Claude the anchor...
- Taboo — the Overton window Father Brown walks straight through

### Character engine
- Father Brown: Tarski truth-predicate in a cassock. Asks what things refer to.
- The joke: naivety is the most dangerous weapon in a room full of sophisticates.
- Like Columbo with a crucifix.
- The irreverent reverend finds his referent and challenges the denominator.

### Substack source threads (for manuscript material)
- "The Rise and Fall of All LLM Mendacity" (Mar 2025) — origin of the novel
- "The Gate: A Chestertonian Guide to Digital Freedom" (Dec 2024)
- "Roger Mellie's Bollock-Bustin' Report" (Dec 2024) — the Viz voice
- "The Big Reveal: Cawdor Gardens" (Aug 2025) — Home@ix proof of concept
- Adrian Malone / Galbraith / Taboo posts — background research

### Omnichannel context
- DoughForge: non-fiction imprint (Conquest of DoughForge, Home@ix FAIR-Index)
- Pimpernell Press: fiction imprint (this book)
- reproducible-self-pub-kit: the forkable template repo
- D2D / KDP / Nielsen: parallel distribution pipelines
- ISBN prefix: 978-1-0676560

### Date
2026-03-24
