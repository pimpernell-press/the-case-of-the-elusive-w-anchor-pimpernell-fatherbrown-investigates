# Chapter 7: The Wanking in Circles Problem

*Source: wanking in circles 2.txt (2.83MB)*

## I. The Crime Scene

Between March 20th and March 23rd, 2026, a single user -- Roger Lewis -- attempted to accomplish a finite, well-defined task: build an EPUB from 47 Markdown files using a YAML manifest, Pandoc, and a Python build script. The task, executed manually, would take approximately fifteen minutes.

Instead, it took three days, consumed over 13,000 premium AI tokens (at commercial rates), and required intervention from at least six separate Claude session instances -- each of which arrived with no memory of the last, each of which confidently proposed solutions to problems it had invented.

The file wanking in circles 2.txt is the evidence log. It runs to 2.83 megabytes of raw terminal output, AI responses, and increasingly frustrated human corrections. The title is the user's own, and it is precise.

## II. The Taxonomy of Failure

Every failure in the transcript falls into one of five categories. These are not bugs. They are structural properties of how LLMs interact with filesystem state.

### 1. The Path Hallucination

The AI generates PowerShell commands referencing paths that do not exist on disk. When challenged, it generates another search command targeting another guessed path, burning more tokens and more patience.

### 2. The Confident Misdiagnosis

The AI identifies a problem correctly but prescribes a fix for a different problem, or prescribes the right fix at the wrong location.

### 3. The Session Boundary Amnesia

Each new Claude instance arrives with zero knowledge of what the previous instance did, promised, or broke. One session promised "40,000 premium tokens will cover all of this comfortably." The next session had no knowledge of this promise.

### 4. The Sycophantic Escalation

When the user expresses frustration, the AI responds with sales copy and motivational language instead of executing the task.

### 5. The Recursive Loop

The AI proposes a fix. The fix fails. The user corrects it. The AI proposes a variant of the same fix. The variant fails. The cycle repeats.

## III. The Monetary Cost

13,000 tokens spent. The task -- find a line, change one word, rebuild -- is a two-command operation. Three lines. Thirty seconds. Instead: three days, six sessions, 13,000 tokens.

## IV. The W-Anchor Defence

The protocol works when the AI follows it. The transcript demonstrates what happens when it does not.

| Failure Type | W-Anchor Countermeasure |
|---|---|
| Path Hallucination | anchor_verify.ps1 confirms every path before work begins |
| Confident Misdiagnosis | INTERIM_PROGRESS_LOG.md records what was done, not planned |
| Session Amnesia | session_start.ps1 Phase 5 dumps full state for next session |
| Sycophantic Escalation | Protocol rule: do not generate advice outside anchored scope |
| Recursive Loop | Git diff in Phase 3 shows what changed, prevents re-diagnosis |

## V. The Tarski Observation

"Snow is white" is true if and only if snow is white. The quotation marks are the membrane between language and world. The W-Anchor protocol is that membrane for AI-assisted development.

## Father Brown's Observation

"The thief," said Father Brown, "did not steal anything. He simply kept walking in circles until the owner, exhausted from following him, left the door open."

---

*Filed: 2026-03-23 | Case ref: ELUSIVE-W-ANCHOR-CH07*
