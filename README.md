# Reproducible Self-Publishing Kit

> Ship books, newsletters, blog posts, and investment decks
> from plain text to print-ready PDF — reproducibly, every time.

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

    git clone https://github.com/tonefreqhz/reproducible-self-pub-kit
    cd reproducible-self-pub-kit

### 2. Install dependencies

    pip install Pillow numpy

### 3. Add your assets

    assets/
      cover/
        base_cover.png     <- your AI-generated or designed cover
        stamp_clean.png    <- transparent PNG badge/stamp (optional)
      fonts/
        VT323-Regular.ttf  <- or any TTF font you prefer

### 4. Configure your book

Edit the config block at the top of scripts/build_cover.py:

    BASE_DIR = r'C:\path\to\YourProject'
    TITLE    = 'Your Book Title'
    SUBTITLE = 'Your Subtitle'
    AUTHOR   = 'Your Name'

### 5. Build your cover

    python scripts\build_cover.py

Output lands in covers/:

    covers/
      front_cover.png   <- web / GitHub
      front_cover.jpg   <- Draft2Digital print upload
      front_cover.gif   <- social preview

---

## Project Structure

    YourProject/
    +-- assets/
    |   +-- cover/
    |   |   +-- base_cover.png
    |   |   +-- stamp_clean.png
    |   |   +-- final_cover.jpg      <- mirrored after build
    |   +-- fonts/
    |       +-- VT323-Regular.ttf
    +-- covers/                       <- purged and rebuilt on every run
    +-- docs/
    |   +-- build_notes.md
    +-- scripts/
    |   +-- build_cover.py
    +-- book.yaml                     <- coming: single config for all scripts

---

## The Core Principle

Every output file is derived, never manually edited.
If you need to change something, change the source and rebuild.

This means:
- No mystery files in covers/ from six months ago
- No "which version did I upload?" confusion
- Every build is identical given the same inputs
- Works across books, decks, newsletters — same pattern

---

## Roadmap

- [ ] book.yaml config reader (replace hardcoded strings)
- [ ] build_interior.py — Markdown to print-ready PDF via Pandoc
- [ ] build_newsletter.py — Markdown to HTML email
- [ ] build_deck.py — Markdown to reveal.js / PDF deck
- [ ] GitHub Actions workflow — build on every push
- [ ] Draft2Digital API upload (when available)

---

## Live Example

DoughForge — the first book built with this kit:
- Repo: https://github.com/tonefreqhz/DoughForge
- Kit:  https://github.com/tonefreqhz/reproducible-self-pub-kit

---

Built by Roger G Lewis · MIT License
