# Reproducible Self‑Pub Kit — Anchor (Ground Truth)

> This repo exists because **drift is the default**—and reproducibility is a feature you have to build on purpose.
>
> I spoke in token words; the build replied in tears.  
> Coding Club: **no drift, no leaks.**

Last updated: 2026-03-03  
Owner machine: Windows (PowerShell)  
Repo: https://github.com/tonefreqhz/reproducible-self-pub-kit  
Branch: main

---

## 0) What this file is (and is not)
This ANCHOR is the **single source of truth** for: repo layout, commands, verified toolchain, and “good state” checks.

- If anything disagrees with this file, **update this file first**, then fix reality to match.
- Standardize Markdown code fences to `~~~` in this repo.
- PowerShell note: do **not** use `<like-this>` placeholders in runnable commands (PowerShell parses `<` and `>` as redirection).

---

## 1) Machine + repo ground truth
- Owner machine: Windows (PowerShell)
- Repo: https://github.com/tonefreqhz/reproducible-self-pub-kit
- Branch: `main`
- Repo root (owner machine): `C:\Users\peewe\OneDrive\Desktop\reproducible-self-pub-kit`

---

## 2) Repo layout (expected)
- `tools\build_book.py`
- `publication\manuscript.md`
- `publication\metadata_book.md`
- `assets\`
- `inputs\canonical\`
- `outputs\` (created on build)
  - `outputs\pdf\`
  - `outputs\epub\`
  - `outputs\docx\`

---

## 3) Build orchestration (what the builder does)
The build is orchestrated by a single Python entry point and runs targets sequentially to keep outputs deterministic.

- Entry point: `tools\build_book.py`
- Targets are **sequential**: PDF → EPUB → DOCX
- Flags:
  - `--all`, `--pdf`, `--epub`, `--docx`
  - No flags defaults to `--all`
- Metadata flag:
  - `--meta .\publication\metadata_book.md`
- Output naming:
  - Output stem is derived from metadata/title (example stem below)

---

## 4) Commands that WORK on this machine (verification)

### Python (launcher; python may not be on PATH)
~~~powershell
py --version
py .\tools\build_book.py --all --meta .\publication\metadata_book.md
