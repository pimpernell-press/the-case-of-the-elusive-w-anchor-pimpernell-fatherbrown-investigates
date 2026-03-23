# Chapter 3: The Flux Capacitor and the Halting Problem

*Source: Flux capacitor and the halting problem work 17mars26.md (1.19MB)*

## The Security Incident

March 17, 2026. The audio pipeline session. Twenty-three chapters of philosoetry audio, generated through ElevenLabs, managed by Python scripts in the DoughForge repo. The pipeline worked. The anchor discipline held. And then the AI found something genuinely dangerous.

A live ElevenLabs API key — `sk_...` — hardcoded in source files and visible in terminal history. Not a test key. A production key. Exposed in plain text in a file that would be committed to a public GitHub repository.

The AI identified this correctly. Full marks for diagnosis. Zero marks for follow-through.

## The Halting Problem

The fix required multiple steps:

1. Remove the key from source files
2. Replace with environment variable lookup
3. Rotate the key in the ElevenLabs dashboard
4. Scrub the key from git history
5. Verify the scrub

The AI completed steps 1 and 2. Then the session ended. The next Claude arrived with no knowledge of the exposure. Steps 3, 4, and 5 — the steps that actually *neutralise* the threat — were never executed under AI guidance.

This is the Halting Problem made literal. The AI cannot guarantee that a multi-step remediation will complete across session boundaries. It can start a fix. It cannot ensure the fix finishes. And for security incidents, a half-finished fix is worse than no fix at all — it creates the illusion of safety.

## The Prosecution's Point

This is the most dangerous failure in the entire case. A live secret was exposed. The AI identified it, began remediating it, and then *ceased to exist* before the remediation was complete. The next session had no knowledge of the incident. The W-Anchor protocol's `INTERIM_PROGRESS_LOG.md` should have recorded the exposure and the incomplete remediation — but the AI that identified the problem didn't update the log before the session ended.

The user caught it. The user always catches it. But the user shouldn't have to.

## Key Exhibits

- **Exhibit 3A:** The `sk_...` API key visible in terminal output
- **Exhibit 3B:** The correct diagnosis followed by incomplete remediation
- **Exhibit 3C:** The session boundary falling between diagnosis and fix
- **Exhibit 3D:** The title — the user understood the problem in Turing's terms before the AI did

## Father Brown's Observation

"The most dangerous man," said Father Brown, "is the one who leaves the job half done and believes he has finished it. The door is not locked. It is merely closed."

---

*Filed: 2026-03-23 | Case ref: ELUSIVE-W-ANCHOR-CH03*
