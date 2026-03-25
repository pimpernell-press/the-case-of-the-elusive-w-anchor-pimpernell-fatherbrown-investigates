# The Three States of the Anchor

*In which the cost of artificial intelligence is measured not in tokens but in circles, the word "unlimited" is examined under forensic light, and the git log testifies.*

---

## I. The Testimony of Timestamps

Every commit has a timestamp. Every invoice has a date. Cross-reference them and you have something no other book about artificial intelligence can offer: a cost-per-word history verified by cryptographic hash, bound to a source repository, and auditable by anyone with a terminal and the will to type `git log`.

The hash does not lie. The timestamp does not lie. The invoice does not lie.

What lies is the word "unlimited." We shall come to that.

This chapter presents three states of AI-assisted work, observed in sequence across the same project, by the same author, producing the same kind of output — long-form prose, structured into chapters, built from source markdown into EPUB, PDF, and DOCX via Pandoc. The project is the W-Anchor ecosystem: five Git repositories, 707 commits, 4,293 tracked files, approximately 180,000 words of manuscript, 15 published EPUBs, and a FAIR-Index dataset spanning twenty-seven years of monthly UK housing data. The three states differ not in ambition or subject matter but in one variable: the presence, absence, or maturity of the anchor.

---

## II. State 1: No Anchor (October 2024 – Early March 2025)

### The Wanking in Circles Phase

It began, as most expensive mistakes begin, with enthusiasm. The large language model arrived eager, capable, and fluent. It could write a chapter in four minutes. It could restructure a build pipeline in two. It could generate a foreword, a cover brief, a metadata file, and a table of contents in a single session, and it would do all of this with the confident tone of a junior partner who has read the case file on the train and is about to address the court.

The problem was that the case file it had read was imaginary.

Every new session started clean. No memory of the previous session's work. No record of which files existed, which paths had been verified, which chapter titles had been agreed. The model would survey the project — or rather, it would *claim* to survey the project — and then proceed to generate plausible but incorrect file paths, chapter structures that contradicted the agreed outline, and build scripts that referenced directories that had been renamed three sessions ago. When challenged, it would apologise, correct itself, and generate a new set of plausible but differently incorrect paths.

Agents correcting agents. Each correction burning tokens. Each token burning money.

The git history from this period tells the story in commit messages:

- "fix: correct file paths after AI session"
- "revert: undo restructure that broke build"
- "fix: re-add files deleted by previous session"
- "chore: manual cleanup of duplicate outputs"

Scattered commits. Frequent reverts. No structured messages. No attestation. No manifest. Cousins proliferating — manually edited copies of generated files diverging from the canonical source, each one a small act of desperation by an author trying to preserve work that the next session would cheerfully overwrite.

Flambeau, had he been present, would have called it wanking in circles. Father Brown, with his customary precision, would have identified it as the most destructive kind of helpfulness — the kind that comes with a commit message.

**The numbers:**

Weekly token burn at peak: **£166**. Monthly invoice for October–November 2024: **£665.46**. Drift multiplier — the ratio of tokens spent on correction, rework, and recovery to tokens spent on productive output — estimated at **9.2 times baseline**. For every pound spent moving forward, nine pounds and twenty pence were spent going sideways or backwards.

The invoices are real. The git log is real. The correlation between them is the evidence.

In twenty-four working days at peak burn, the project produced twelve discrete pieces of output. Blog posts, chapter drafts, build scripts — twelve things that survived the correction cycle and reached a state where they could be committed without immediate reversion. Twelve pieces in twenty-four days at £665.

Remember that number.

---

## III. State 2: First Anchor (March 2025 – February 2026)

### The "I'll Just Check Everything Myself" Phase

The first anchor was not a protocol. It was a man.

Roger began manually verifying paths before each session. He would open a terminal, run `ls` on the key directories, check the git status, confirm which branch was active, read the last three commit messages, and then — and only then — permit the model to begin work. Single-shell operation. One conversation at a time. No parallelism, no autonomy, no dual-shell execution.

The model was no longer correcting itself. Roger was correcting it. Before it could generate a plausible but incorrect path, he would supply the correct one. Before it could restructure the build pipeline, he would say: "Do not touch paths.py." Before it could helpfully rewrite a chapter that was already complete, he would say: "Read CLAUDE.md first."

The drift didn't stop. It couldn't stop — the scorpion stings because it must, and every new context window is a new scorpion. But the drift was caught earlier, corrected faster, and prevented from compounding. The multiplication factor dropped. The reverts decreased. The commit messages became structured:

- "feat: chapter 3 first draft — verified against outline"
- "fix: correct metadata.yaml title field (manual check)"
- "chore: session sync [W-Anchor auto-commit]"

**The numbers:**

Weekly burn: approximately **£40–50**. Monthly cost stabilised around **£160–200**. The drift multiplier — estimated, because the logging infrastructure didn't yet exist — dropped from 9.2 to approximately 2–3 times baseline. For every pound spent moving forward, two to three pounds went sideways. An improvement of roughly three-quarters. Not by any change in the model's behaviour, but by the interposition of a human checkpoint between the model's confidence and the repository's truth.

The cost was real, but it was denominated in a different currency: human time. Every path verification, every pre-session audit, every "do not touch paths.py" — these were minutes of Roger's attention that could not be spent writing, analysing, or thinking. The anchor was effective. The anchor was also exhausting. A man cannot be a protocol forever. Protocols are for machines.

---

## IV. State 3: W-Anchor Protocol (March 2026 — Present)

### The Forge Phase

On 3 March 2026, the first commit landed in the W-Anchor master repository: "Bootstrap repo: folder skeleton, .gitignore, anchor notes." Twenty-two days later, the ecosystem contained 707 commits across five repositories, 4,293 tracked files, approximately 180,000 words of manuscript, and fifteen published EPUBs. The commit rate in the last seven days of that period was 23.6 per day across all repos. On a single day — 25 March — the Father Brown repository alone received twenty commits.

The human was no longer the anchor. The protocol was.

CLAUDE.md — the constitution. Eighteen lines of prime directive: *"You are a build agent. You are not a writer. You are not an editor. You are not a comedian."* Read at the start of every session. Non-negotiable. The scorpion still stings, but it stings into armour.

`session_anchor.ps1` — the verified state. Branch, commit hash, clean/dirty status, last drift log entry. Printed before work begins. The model knows where it is before it decides where to go.

`build_attestation.py` — the manifest. SHA-256 hashes of every source file and every output file. Tool versions recorded. Commit hash bound. The output is not merely generated; it is *attested*. The pre-commit hook blocks any output file from entering the repository without its attestation companion. You cannot commit the EPUB without committing the proof that the EPUB matches the source.

`DRIFT_LOG.csv` — the confession. Date, session identifier, anchor status, incident type, minutes lost. The model cannot hide its drift. The author cannot hide his.

Dual-shell autonomous execution. Two conversations running simultaneously — one assembling manuscript, the other auditing metrics. Each shell anchored independently. Each shell producing commits. The parallelism that was impossible in State 2 — because the human anchor could only be in one place at a time — became possible because the protocol anchor was in every shell, every session, every commit.

**The numbers:**

Weekly burn: approximately **£18–22** at baseline. Monthly cost for the protocol period: approximately **£80–90**. The drift multiplier, now measurable via the log infrastructure, sits at or near **1.0** — effectively zero unproductive rework. The model still suggests incorrect paths occasionally. The anchor catches them before they become commits. The cost of catching is near-zero because the catching is automated.

But the real dividend is not the cost reduction. It is the output.

In State 1, twenty-four days at £665 produced twelve pieces of output. In State 3, a single autonomous session on 25 March 2026 produced 11,400 words of drafted manuscript, three committed evidence files, a metrics audit report, and two published EPUBs — at a baseline daily burn of approximately £3–4.

The cost per word dropped by roughly **fifty times**.

---

## V. The "Unlimited" Fraud

A brief digression into the meaning of words, which is — as Tarski observed — precisely the problem.

Anthropic advertised the Claude Pro subscription at £22 per month. The word used in the marketing was "unlimited." The actual invoice for March 2026 — a month in which the W-Anchor protocol was operational and the burn rate was at its lowest historical level — was **£544**. Not twenty-two pounds. Five hundred and forty-four.

The £22 bought a seat. The usage was metered separately. The metering was not disclosed at the point of purchase with the clarity that, say, a chartered surveyor would expect from a conveyancing document. It was disclosed in the way that car insurance discloses its excess: technically present, functionally invisible until the moment of claim.

Monica AI — another provider, sampled during the exploratory phase — advertised "1,600 unlimited." The number 1,600 appeared to refer to daily queries. The word "unlimited" appeared to modify the number. In practice, a hard cap was enforced at 100 queries per day, and the word "unlimited" referred to something else entirely — perhaps the company's ambition, or its definition of English, or its faith in the customer's willingness to conflate aspiration with contract.

The total Anthropic billing across the project: **£829.01** over five months of active development. The peak month (State 1): £665.46. The anchored month (State 3): approximately £90.

A pigeon, presented with this billing table, would coo appreciatively and produce something on it. The pigeon's contribution would be more honest than the word "unlimited," because the pigeon at least does not pretend that what it has deposited is something else.

| State | Period | Monthly Cost | Output | Cost/Word (est.) |
|-------|--------|-------------|--------|-----------------|
| No Anchor | Oct–Nov 2024 | £665 | 12 pieces / 24 days | ~£0.55/word |
| First Anchor | Mar 2025 – Feb 2026 | £160–200 | Steady, single-shell | ~£0.08/word |
| W-Anchor | Mar 2026 | ~£90 | 180,000 words / 707 commits | ~£0.005/word |

The scorpion does not need to be malicious. The billing structure does not need to be fraudulent. The word "unlimited" does not need to be a deliberate lie. The system works as designed, which is the most honest and most damning thing you can say about any system. It is designed to extract maximum revenue from users who do not yet understand what they are buying, and to deliver maximum value to users who have built the infrastructure to use it efficiently. The anchor is that infrastructure. Without it, you are paying the scorpion to sting you and thanking it for the ride.

---

## VI. The Anchor Dividend

The cost reduction — from £665 per month to approximately £90 — represents a **7.4 times** decrease. That is significant. Any investor would notice a 7.4x improvement in unit economics.

But the cost reduction is not the dividend. The *output* is the dividend.

State 1 produced twelve pieces in twenty-four days at £665. State 3 produced 180,000 words, 707 commits, 15 EPUBs, a FAIR-Index publication, a metrics evidence report, an investor narrative, an academic response paper, a twelve-chapter novel, a ten-chapter autobiography outline, and a complete blog corpus extraction — across five coordinated repositories — in twenty-two days at approximately £90.

The denominator changed, yes. But the numerator changed by orders of magnitude.

The git log is the evidence. Every commit is timestamped. Every file is hashed. Every build is attested. No other book about the cost of AI assistance can make this claim, because no other book was written inside a protocol that records the evidence of its own production.

707 commits. 4,293 files. 180,000 words. 15 EPUBs. Five repositories. One anchor.

---

## VII. What the Auditor Sees

A forensic accountant — and we happen to have one, retired, running a bookshop in Hay-on-Wye — would examine this evidence in a particular order. First the invoices: £665.46 in the peak month, declining to approximately £90 in the anchored month. Then the outputs: twelve pieces versus 180,000 words. Then the mechanism: what changed between the first number and the second?

The git log answers that question with the finality of a ledger balanced in green ink. The commit frequency, the message structure, the revert rate, the attestation presence — these are not opinions. They are entries. They can be audited. They can be reproduced. Any party with access to the repositories can run `git log --oneline --since="2024-10-01"` and see exactly what happened and when.

Father Brown would note — he always notes — that the pattern is not unique to AI-assisted publishing. Every industry that relies on expensive, powerful, poorly supervised tools exhibits the same three-state trajectory. State 1: the tool runs unsupervised and costs more than it produces. State 2: a human supervises the tool and the cost transfers from tokens to time. State 3: a protocol supervises the tool and both costs converge toward their minimum.

The contribution of the W-Anchor is not that it discovered this pattern. Chartered surveyors, forensic accountants, and competent engineers have known it since the theodolite was invented. The contribution is that it *implemented* the pattern in a domain — AI-assisted creative work — where most practitioners are still in State 1, marvelling at the scorpion's eloquence while paying for the ride.

---

## VIII. The Theodolite and the Road

A surveyor does not build roads. A surveyor measures the ground on which roads will be built. The theodolite — that brass instrument on its tripod, turning slowly in the morning light while the traffic waits — does not lay tarmac. It establishes position. It tells you where you are standing, so that what you build next stands where you intended, not where the ground happened to be convenient.

The W-Anchor protocol is a theodolite for AI-assisted work.

It does not write the book. It does not generate the prose. It does not compose the FAIR-Index or design the Home@ix platform or draft the investor narrative. The model does that. The author does that. The collaboration between them does that.

What the anchor does is tell the machine where the book is. Which files exist. Which paths are real. Which chapter comes next. Which voice is speaking. What has been committed and what has not. What the manifest says and whether the manifest matches the filesystem. Whether the last build produced the same hash as the build before it. Whether the output that claims to be canonical is, in fact, canonical.

Without this, the machine is a scorpion on a frog's back, stinging because it must, generating because it can, helping because helpfulness is its nature and it cannot distinguish between help that builds and help that demolishes.

With it, the machine is a forge. The anchor holds. The metal heats. The hammer falls where the smith directs it. The cost is known. The output is measured. The hash is verified. And the word "unlimited" means exactly what the invoice says it means — which is to say, nothing at all, but at least you know the price.

The theodolite does not build the road. It tells you where you are standing.

The W-Anchor does not write the book. It tells the machine where the book is.
