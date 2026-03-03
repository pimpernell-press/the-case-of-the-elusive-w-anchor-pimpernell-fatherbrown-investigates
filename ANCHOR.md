\# Reproducible Self‑Pub Kit — Anchor (Ground Truth)



Last updated: 2026-03-03  

Owner machine: Windows (PowerShell)  

Repo: https://github.com/tonefreqhz/reproducible-self-pub-kit  

Branch: main



---



\## 1) Current state (what exists)

\- Repo root: `C:\\Users\\peewe\\OneDrive\\Desktop\\reproducible-self-pub-kit`

\- `tools/build\_book.py` exists and is committed/pushed.

\- Orchestrator:

&nbsp; - Sequential targets: PDF → EPUB → DOCX

&nbsp; - Flags: `--all`, `--pdf`, `--epub`, `--docx`

&nbsp; - No flags defaults to `--all`



---



\## 2) Commands that WORK on this machine

\- Use Python via launcher (\*\*python command not on PATH\*\*):

&nbsp; - `py --version` → Python 3.13.12 confirmed

&nbsp; - `py tools\\build\_book.py --all`



\- LaTeX engine present:

&nbsp; - `xelatex --version` works (TeX Live 2025)



---



\## 3) Git status (what was pushed)

\- Commit: `d43f679` on `main`

\- Message: "Add sequential multi-target build orchestration (pdf/epub/docx)"



---



\## 4) Pending installs / missing tools

\- Pandoc:

&nbsp; - `pandoc --version` failed (not recognized)

&nbsp; - Installing via: `winget install --id JohnMacFarlane.Pandoc -e`

&nbsp; - After install: reopen PowerShell, then run:

&nbsp;   - `pandoc --version`

&nbsp;   - `where.exe pandoc`



---



\## 5) Next build goal

Generate (from Markdown):

\- `outputs/pdf/book.pdf`

\- `outputs/epub/book.epub`

\- `outputs/docx/book.docx`



Toolchain target:

\- Pandoc for EPUB + DOCX

\- Pandoc + `--pdf-engine=xelatex` for PDF



---



\## 6) Manuscript source (update this)

Canonical source: Markdown  

Expected main file (change if different):

\- `publication\\manuscript.md`



Check:

\- `Test-Path .\\publication\\manuscript.md`



---



\## 7) Guardrails

\- Prefer `py` over `python` in all commands.

\- Keep builds deterministic + sequential.

\- Update this anchor whenever toolchain/paths change.



