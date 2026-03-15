> ⚓ **HUMAN: before you type anything to the AI, run this and paste the full output into the chat.**
>
> ```powershell
> cd "C:\Users\peewe\OneDrive\Desktop\the-case-of-the-elusive-w-anchor-pimpernell-fatherbrown-investigates"; .\anchor_verify.ps1
> ```
>
> **AI: your first response must quote the repo root and confirm all paths [OK]. If you have not seen anchor output, say so and ask for it. Do not proceed without it.**



# Reproducible Self-Publishing Kit

> Ship books, newsletters, blog posts, and investment decks
> from plain text to print-ready PDF — reproducibly, every time.

---

> ⚠️ **BEFORE YOU DO ANYTHING — HUMAN OR AI — RUN THIS:**
>
> ```powershell
> cd "<YOUR_REPO_ROOT>"
> .\anchor_verify.ps1
> ```
>
> Paste the full output into your AI chat before typing a single instruction.
> If every line says `[OK]` you are anchored. If anything says `[MISSING]` stop and fix it first.
> An AI that has not seen this output is **not anchored** and will drift.

---

## What This Is

A minimal, scriptable publishing pipeline built on open tools.
No InDesign. No Canva. No vendor lock-in.
Every output is generated from source files you control.

Designed for:
- Books to Draft2Digital, KDP, Lulu
- Newsletters to Substack, Ghost, email HTML
- Investment Decks to PDF, web
- Blog Posts to Markdown to HTML to any platform

---

## Quick Start (5 minutes)

### 1. Clone the repo

```powershell
git clone https://github.com/tonefreqhz/reproducible-self-pub-kit
cd reproducible-self-pub-kit
