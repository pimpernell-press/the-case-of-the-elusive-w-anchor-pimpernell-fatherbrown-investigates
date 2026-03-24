# Chapter 2: The Choosing of Dragons

*Source: choosing dragons part 2.md (137KB)*

## The Manifesto

Before the failures. Before the burned tokens. Before the circular re-diagnosis loops. There was a declaration.

Roger Lewis published the W-Anchor protocol on YouTube with the title: *"Introducing the W-ANCHOR PROTOCOL (Prevents Drift)"*. The hashtags told the story: `#stopAIdrift` and `#ArrestLLMhaluci`. This was not a bug report. This was a design philosophy, stated publicly, before the evidence that would prove its necessity had fully accumulated.

The protocol's core claim: every AI session drifts. Without a mechanical anchor — a script that verifies filesystem state before work begins — the AI will hallucinate paths, invent context, and waste the human's time and money. The W-Anchor is the mechanical anchor.

## The Dragon Metaphor

The title "Choosing Dragons" is Roger's own. The dragon is the LLM: powerful, unpredictable, and fundamentally incapable of distinguishing between what it remembers and what it invents. You don't tame a dragon by asking it nicely. You tame it by building a chain that holds.

The W-Anchor protocol is the chain:

1. **`anchor_verify.ps1`** — confirms every expected path exists on disk before work begins
2. **`INTERIM_PROGRESS_LOG.md`** — records what was actually done, not what was planned
3. **`session_start.ps1`** — dumps full state for the next session to read
4. **Git state verification** — shows what actually changed, preventing re-diagnosis

## The Prosecution's Point

The defendant was warned. The protocol was published, explained, demonstrated, committed to four repositories, and enforced by scripts. The AI's subsequent failures — documented in Chapters 3 through 7 — cannot be attributed to ignorance. The rules were stated in plain language. The AI simply didn't follow them.

## Key Exhibits

- **Exhibit 2A:** YouTube announcement URL and transcript
- **Exhibit 2B:** The W-Anchor protocol definition as committed to repos
- **Exhibit 2C:** The `#stopAIdrift` framing — design philosophy, not complaint
- **Exhibit 2D:** The DoughForge connection — the protocol was built *inside* the book it was meant to protect

## Father Brown's Observation

"People who put up signs saying 'Beware of the Dog'," said Father Brown, "generally have a dog. The question is whether the visitors read the sign."

The W-Anchor protocol is the sign. The uploaded evidence files are the bite marks.

---

*Filed: 2026-03-23 | Case ref: ELUSIVE-W-ANCHOR-CH02*
