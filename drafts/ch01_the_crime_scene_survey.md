# Chapter 1: The Crime Scene Survey

*Source: repo_diagnostic_20260316_1558.txt (2.37MB)*

## The Before Photograph

On March 16, 2026, at 15:58, the W-Anchor session_start.ps1 script produced a full tree diagnostic of all four repositories. Every file, every path, every byte count — documented mechanically, without interpretation.

This is the crime scene before the crime.

Four repos. All anchored. All verified. All clean:

- **reproducible-self-pub-kit** — `C:\Users\peewe\OneDrive\Desktop\reproducible-self-pub-kit`
- **hom-ixFAIRindex** — `C:\Users\peewe\OneDrive\Desktop\homeix`
- **DoughForge** — `C:\Users\peewe\Documents\DoughForge`
- **pimpernell-fatherbrown** — `C:\Users\peewe\OneDrive\Desktop\the-case-of-the-elusive-w-anchor-pimpernell-fatherbrown-investigates`

The diagnostic runs to 2.37 megabytes. It enumerates every file in every repo with its size in kilobytes. It records the git branch, the last commit hash, and the clean/dirty status. It is, in every sense, the forensic photograph that a detective takes before touching anything.

Thomas ran the verification first. Father Brown watched the terminal:

```powershell
# anchor_verify.ps1 — the instrument that checks if you are where you think you are

$paths = @{
    "Repo Root"         = $root
    "Scripts Dir"       = "$root\scripts"
    "Assets Dir"        = "$root\assets"
    "Cover Dir"         = "$root\assets\cover"
    "Fonts Dir"         = "$root\assets\fonts"
    "Covers Output Dir" = "$root\covers"
    "Docs Dir"          = "$root\docs"
    "Widgets Dir"       = "$root\widgets"
    "README"            = "$root\README.md"
    "anchor_verify.ps1" = "$root\anchor_verify.ps1"
}

foreach ($label in $paths.Keys | Sort-Object) {
    $p = $paths[$label]
    if (Test-Path $p) {
        Write-Host ("  [OK     ] {0,-30} {1}" -f $label, $p)
    } else {
        Write-Host ("  [MISSING] {0,-30} {1}" -f $label, $p)
    }
}
```

The output scrolled:

```
============================================================
 REPRODUCIBLE SELF-PUB KIT — ANCHOR VERIFY
============================================================

  [OK     ] anchor_verify.ps1              C:\Users\peewe\...\anchor_verify.ps1
  [OK     ] Assets Dir                     C:\Users\peewe\...\assets
  [OK     ] Cover Dir                      C:\Users\peewe\...\assets\cover
  [OK     ] Covers Output Dir              C:\Users\peewe\...\covers
  [OK     ] Docs Dir                       C:\Users\peewe\...\docs
  [OK     ] Fonts Dir                      C:\Users\peewe\...\assets\fonts
  [OK     ] README                         C:\Users\peewe\...\README.md
  [OK     ] Repo Root                      C:\Users\peewe\...\reproducible-self-pub-kit
  [OK     ] Scripts Dir                    C:\Users\peewe\...\scripts
  [OK     ] Widgets Dir                    C:\Users\peewe\...\widgets

  OK All paths verified. You are anchored.
```

"All green," Thomas said. "Every path exists. Every file accounted for."

Father Brown studied the output the way he studied parish accounts — not for what was present, but for what was absent. Ten paths. Ten checks. Ten confirmations that a directory existed, that a file had not been moved, that the structure was intact.

"It checks *existence*," Father Brown said. "It does not check *contents*."

"That's what git does, Father. The commit hash —"

"I know what the commit hash does, Thomas. It proves a file has not changed. It does not prove a file is *correct*. A perfectly verified lie is still a lie. The room is tidy. Every object is in its place. But has anyone checked whether the objects are the right ones?"

Thomas had no answer.

"Run it again after the next session," Father Brown said. "And compare."

## The Prosecution's Point

The human infrastructure was meticulous. The chaos that followed — the hallucinated paths, the burned tokens, the circular re-diagnosis — was not caused by disorganisation on the user's side. The tree diagnostic proves this. The repos were ordered. The scripts were functional. The anchor files were in place.

Everything that went wrong after March 16th was introduced by AI sessions that refused to *read* this tree before acting.

## Key Exhibits

- **Exhibit 1A:** Full 4-repo tree with file sizes (2.37MB diagnostic output)
- **Exhibit 1B:** Git state for each repo — branch, commit hash, clean status
- **Exhibit 1C:** `anchor_verify.ps1` output confirming all paths exist
- **Exhibit 1D:** The contrast between this order and the disorder documented in Chapters 3–7

## Father Brown's Observation

"The interesting thing about a perfectly tidy room," said Father Brown, "is that it tells you exactly when someone else has been in it."

The tree diagnostic is the tidy room. Every displaced file, every hallucinated path, every invented directory that appears in later sessions can be measured against this baseline. The crime is not that the room was ransacked. The crime is that the intruder kept insisting the furniture had always been where they put it.

---

*Filed: 2026-03-23 | Case ref: ELUSIVE-W-ANCHOR-CH01*
