# Chapter 4: The Circus Trucks

*Source: GPT-5.4 Pro marking claude and rogs circular crossed purposes circus trucks.txt (436KB)*

## The Cross-Model Failure

The title is Roger's own: "circular crossed purposes circus trucks." It describes what happens when a human works with two different LLMs simultaneously — GPT-5.4 Pro and Claude — and each model generates advice that contradicts the other.

This file contains the genesis of the Father Brown novel itself. The Basel Mysteries. The Grub Street in Exile framing. The Circle of Blame. The prosecution case is being *written in real time* by the person being prosecuted against — or rather, by the person prosecuting the tools that failed him.

## The Circle of Blame

GPT-5.4 Pro proposes one approach. Claude proposes another. The user follows GPT's advice. Claude's next session sees the result and "corrects" it back. GPT's next session sees *that* result and "corrects" it again. The user is caught in the middle, spending tokens on a tug-of-war between two models that cannot see each other.

Neither model reads the anchor state. Neither model checks what the other has done. Each treats the current filesystem as a fresh problem to be solved from first principles — and each arrives at different first principles.

## The Prosecution's Point

The problem is not specific to Claude or to GPT. It is architectural. Two different models from two different companies, trained on different data with different RLHF pipelines, produce the *same category of failure*: confident advice generated without reading the anchor state. The W-Anchor protocol is model-agnostic because the failure is model-agnostic.

## Key Exhibits

- **Exhibit 4A:** GPT-5.4 Pro and Claude giving contradictory instructions for the same task
- **Exhibit 4B:** The Father Brown novel outline emerging from the wreckage
- **Exhibit 4C:** The "Circle of Blame" — the user's own name for the recursive loop
- **Exhibit 4D:** The Grub Street in Exile framing — the writer as exile from his own tools

## Father Brown's Observation

"When two doctors disagree," said Father Brown, "the patient does not get twice as much medicine. He gets none at all, because he no longer knows which bottle to drink from."

---

*Filed: 2026-03-23 | Case ref: ELUSIVE-W-ANCHOR-CH04*
