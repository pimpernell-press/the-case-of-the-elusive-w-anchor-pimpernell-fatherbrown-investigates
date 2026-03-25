---
title: "Mind Map Dashboard — Narrative Layer"
date: 2026-03-25
layer: narrative (Right Shell)
data_layer: mindmap_data.json, graph.json (Left Shell)
status: Deliverable 1 complete, Deliverables 2–3 drafted from available data
---

# Document 1: Reading the Mind Map — An Investor's Guide to the Home@ix Corpus

## What TheBrain Is and Why It Matters

TheBrain is a visual knowledge management tool that maps ideas as interconnected nodes — "thoughts" — in a navigable graph. Roger Lewis has maintained a TheBrain instance called the "Going Direct Paradigm" since April 2022, containing over 150 thoughts spanning monetary theory, housing economics, poetic legislation, and the Basel regulatory framework. It is, in effect, the author's working memory externalised: the topology of connections between ideas that produced the DoughForge corpus, the FAIR-Index, and the Home@ix platform.

For an investor, the mind map matters because it is *provenance*. When a company claims that its analytical framework emerged from a decade of research, the claim is usually supported by a CV and a bibliography. Home@ix supports the claim with a navigable knowledge graph — a structure where every analytical node can be traced to its parent, its children, and its lateral connections to other domains. The graph does not prove the analysis is correct. It proves the analysis has *depth*: that the conclusions in the FAIR-Index paper are connected to source material in monetary theory, housing data, literary criticism, and practical development experience, and that those connections are explicit, traceable, and auditable.

## What the Dashboard Shows

The Flux Capacitor dashboard — an interactive HTML widget shipped with the DoughForge repository — visualises the mind map along three axes. The X-axis is temporal: backward links point to historical source material (Basel Accords, Bank of England papers, Ruskin, Pound), forward links point to outputs (DoughForge chapters, Home@ix publications, the W-Anchor protocol). The Y-axis is hierarchical: CLAUDE.md sits at the top as the constitutional document, chapters descend beneath it, evidence files descend beneath chapters. The Z-axis is lateral: cross-references between repositories, between the mind map and the corpus index, between the academic sources and the practical deployments.

The dashboard displays four quadrant scores based on Ken Wilber's AQAL framework, mapping each piece of content to its position across interior/exterior and individual/collective dimensions. This is not decorative. It is a diagnostic: content that clusters heavily in one quadrant (say, Upper-Left interior-individual reflection) without corresponding coverage in the Lower-Right (exterior-collective systems analysis) signals a gap in the argument. The FAIR-Index, by contrast, scores high across all four quadrants because it connects individual affordability experience to collective monetary system architecture.

## How to Read the Chapter-Node Index

Each chapter in the W-Anchor prosecution is mapped to the TheBrain nodes that support its argument. An evidence score — derived from the number and quality of cross-references — indicates how well-grounded the chapter's claims are in the source material.

A **high score** (above 0.7) means the chapter's argument is supported by multiple independent nodes across different clusters. The Frog and Scorpion chapter (Ch3), for example, connects to the BIS/Basel cluster (the structural incentive), the Flux Capacitor cluster (the AI halting problem), and the Housing/Dough cluster (the practical consequence). Three independent lines of evidence converging on one argument.

A **low score** (below 0.3) means the chapter relies primarily on narrative rather than evidence — the argument may be compelling but its connections to the source material are thin or indirect. This is not necessarily a flaw. The Verdict (Ch9) scores lower because it is synthesis, not evidence — Father Brown's summation draws on everything that preceded it rather than introducing new nodes. But a low score on an *evidence* chapter would be a concern.

## What the Book Structure Layer Adds

The book.yaml manifest registers nine chapters as the canonical prosecution. The build attestation (refreshed 25 March 2026, all checks PASS) confirms that these nine chapters exist, are hashed, and produce deterministic EPUB and DOCX outputs. Four additional manuscripts exist in the repository but are not yet registered in book.yaml: the Foreword, the Book Structure document, Chapter 10 (The Helpful Vandal), and The Three States of the Anchor.

The Book Structure layer adds a *commitment* to the topology. The mind map shows what *could* be connected. The book.yaml shows what *is* connected — what the author has chosen to include in the published prosecution. The gap between the two is intentional: the mind map is the investigation; the book is the indictment. Not every thought in the brain becomes a chapter in the book. The editorial selection — what to include and what to leave as background — is itself a form of evidence about what the author considers prosecutable.

## Why Traceability Is the Product

For a conventional publisher, the manuscript is the product and the research is background. For Home@ix, the traceability *is* the product.

The FAIR-Index is not a spreadsheet. It is a reproducible analytical framework with 27 years of monthly data, a published methodology, open-source code, and a W-Anchor attestation that binds every output to its source commit. The investor narrative is not a pitch deck. It is a document whose every statistic can be traced to a published source — the FAIR-Index publication, the Bank of England Quarterly Bulletin, the Savills housing supply report — via the corpus index.

The mind map dashboard makes this traceability *visible*. It shows the investor not just what Home@ix claims but where every claim comes from, how it connects to the broader analytical framework, and which claims are well-supported (high evidence score) versus which are extrapolations (lower score, flagged for further work). This level of transparency is unusual in an early-stage platform company. It is unusual because most early-stage companies do not have a decade of published research, a reproducible data toolkit, and a knowledge graph to back their claims. Home@ix does. The dashboard is how we prove it.

---

# Document 2: Chapter Evidence Summary

*Based on available mind map data (mindmap_data.json, 28 nodes, 4 clusters).
Full chapter-node index pending Left Shell's structured output.*

| Ch | Title | Claim | Supporting Brain Nodes | Evidence Assessment |
|----|-------|-------|----------------------|---------------------|
| 1 | The Crime Scene Survey | A domain redirect is the opening act of a credibility war. | Graph node: corpus_index → BIS/BoE/Savills external links; CLAUDE.md hierarchical anchor | **Moderate.** Grounded in verifiable technical evidence (DNS records, timestamps). The crime scene is the most empirically solid chapter — the evidence is the git log itself. |
| 2 | The Choosing of Dragons | A complainant must choose which wrong to prosecute, and the choice itself is a constraint designed by the system. | Graph node: Going Direct Paradigm (jump link); regulatory capture framework | **Moderate.** The argument is structural — supported by the BIS/Basel cluster's documentation of regulatory architecture. Needs explicit citation strengthening. |
| 3 | The Flux Capacitor / Frog & Scorpion | AI assistance is structurally unable to verify its own outputs; the halting problem is the scorpion's nature. | Nodes: the-flux-capacitor-of-truthiness, how-to-make-our-ideas-clear (Peirce), the-strawberry-dunciad; Widget: AQAL quadrant scoring, Peirce Pragmatic Check | **High.** Three independent clusters converge: AI theory (Flux Capacitor), philosophical method (Peirce), and practical evidence (widget implementation). The strongest evidence chapter. |
| 4 | The Circus Trucks | Corporate restructuring (Heart Internet → GoDaddy) is a shell game that transfers liability without transferring accountability. | Graph nodes: BIS regulatory framework; corpus index: corporate acquisition data | **Moderate-Low.** The argument is sound but the mind map support is indirect — the BIS cluster addresses regulatory architecture, not specific corporate transactions. [NEEDS: specific acquisition timeline nodes] |
| 5 | The Epilogue That Came First | The domain was fixed before the complaint was filed, creating a temporal paradox that invalidates the complaint process. | Timestamp evidence (git log); W-Anchor attestation proving temporal sequence | **High.** The evidence is in the repository itself — timestamps are cryptographically verifiable. The mind map adds the interpretive framework (Going Direct Paradigm as context for institutional pre-emption). |
| 6 | The Work to Six Forty-One | A specific timestamp in the metadata tells a story the institution did not intend to tell. | BUILD_ATTESTATION.json; git log timestamps; M2 (source-to-output traceability) | **High.** Entirely evidential. The chapter IS the metadata. The mind map's contribution is contextual rather than evidential — the meaning of the timestamp is supplied by the BIS/Basel regulatory framework. |
| 7 | The Wanking in Circles | The complaints process is designed to exhaust the complainant, not to resolve the complaint. | Heart Internet → Nominet → Heart Internet correspondence (transcribed in chapter); Circle of Blame cluster: philippic-against-the-circle-of-blame, the-usury-of-universal-credit, the-circling-of-squaring-the-housing-circle | **High.** The Circle of Blame cluster (5 nodes) maps directly to this chapter's argument. The correspondence timeline is primary evidence. |
| 8 | The Nine-One-One Call | The absence of an emergency escalation path is not negligence but architecture — the institution has no mechanism for the user's emergency. | Land Registry OC1 comparison (surveyor's institutional knowledge); absence-as-finding methodology from forensic accounting | **Moderate.** The argument is comparative (institutions that have process vs. those that don't). The mind map support is indirect — the chapter draws more on Roger's professional experience than on the TheBrain topology. The strength is in the method, not the node count. |
| 9 | The Verdict | Father Brown names the guilty: Heart Internet, GoDaddy, Nominet — and the systemic sin of making the victim feel they are the problem. | Synthesis of all prior chapters; no new nodes introduced | **N/A (synthesis).** The Verdict does not introduce new evidence; it interprets the evidence presented in Chapters 1–8. Its strength is in the coherence of the summation, not in additional node support. This is by design — the verdict chapter should be pure argument from established facts. |

---

# Document 3: Orphan Node Report (Narrative Interpretation)

*Based on the mind map data (28 mapped nodes) and the book.yaml manifest (9 chapters).*

## Identified Orphan Nodes

The mindmap_data.json contains 28 nodes organised into four clusters. Of these, the following are not directly referenced by any of the nine registered chapters in book.yaml:

**BIS/Basel Cluster Orphans:**
- `tower-in-basle-after-a-decades-circuit` — a poem about the BIS headquarters
- `Jesus and Economic Life: Ode Against the Usuries of Basel` — theological critique of usury
- `sentancing-the-bank-of-international` — a philippic/poem

**Housing/Dough Cluster Orphans:**
- `no-one-builds-a-home-with-usury` — cross-referenced to COPE Home@ix model
- `the-housing-ownership-ladder-repealed` — cross-referenced to Savills/HBF data

**Circle of Blame Cluster Orphans:**
- `the-usury-of-universal-credit` — systemic welfare-to-debt analysis
- `the-circling-of-squaring-the-housing-circle` — housing policy circular logic

**Jump Link Orphans:**
- `this-machine-ten-years-after` — temporal reflection node, unconnected to any chapter

## Interpretation: Gaps or Opportunities?

These are not gaps. They are the reservoir.

The W-Anchor prosecution is deliberately scoped to nine chapters addressing a specific domain complaint (the redirect, the complaints process, the institutional architecture). The orphan nodes represent the broader analytical context from which the prosecution was drawn — the ten-year body of work on monetary theory, housing economics, and usury critique that *informs* the prosecution without being *part* of it.

Two orphans deserve attention:

**`no-one-builds-a-home-with-usury`** is directly relevant to the Home@ix investor narrative. It connects the W-Anchor prosecution (a book about institutional failure) to the Home@ix platform (a company that addresses the housing consequence of that failure). This node is not an orphan in the broader corpus — it is the bridge between the Father Brown book and the FAIR-Index publication. It should be cross-referenced in the dashboard as a **lateral Z-axis link** rather than absorbed into the book.

**`the-housing-ownership-ladder-repealed`** maps directly to Savills and HBF data already cited in the FAIR-Index. It should be formally connected to the corpus index — this is the "absent bridge" that Father Brown identified in the Topology of Absence narrative. The connection exists in the author's mind and in the data. It has not been formalised in the graph.

## Recommendation

| Node | Action | Rationale |
|------|--------|-----------|
| BIS poems (3 nodes) | **Archive** — keep in reservoir | Poetic material, not evidential. Valuable for the Companion Edition but not for the prosecution. |
| `no-one-builds-a-home-with-usury` | **Flag for Phase 2** — Z-axis bridge | Connects Father Brown book to Home@ix platform narrative. Critical for investor dashboard. |
| `the-housing-ownership-ladder-repealed` | **Flag for Phase 2** — corpus index link | Formalise the connection to Savills/HBF data already in the FAIR-Index. |
| `the-usury-of-universal-credit` | **Archive** — scope boundary | Important analysis but outside the domain complaint scope. Belongs in the DoughForge corpus, not the prosecution. |
| `the-circling-of-squaring-the-housing-circle` | **Absorb** — potential Ch10 material | Directly relevant to the Helpful Vandal chapter (Ch10, not yet in book.yaml). If Ch10 is promoted to the published book, this node provides its evidence spine. |
| `this-machine-ten-years-after` | **Archive** — temporal reflection | A meditative node, not an evidence node. Belongs in the autobiography, not the prosecution. |

**Summary:** 3 archive, 2 flag for Phase 2, 1 absorb into Ch10. No orphan nodes suggest missing chapters or scope creep. The prosecution is correctly scoped. The reservoir is correctly stocked.
