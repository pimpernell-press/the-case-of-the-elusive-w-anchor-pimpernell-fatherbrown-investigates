import os

ROOT = r'C:\Users\peewe\reproducible-self-pub-kit'
os.makedirs(os.path.join(ROOT, 'docs'), exist_ok=True)

README = r"""# Reproducible Self-Publishing Kit

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

Built by Roger S Lewis · MIT License
"""

BUILD_NOTES = r"""# DoughForge — Cover Build Notes

## What We Built

A Python cover compositor that:
- Loads a base AI-generated cover image (assets/cover/base_cover.png)
- Overlays VT323 monospace title, subtitle, and author text with green glow
- Composites an approval stamp (assets/cover/stamp_clean.png) centred below subtitle
- Purges and rebuilds the covers/ folder on every run
- Outputs front_cover.png, front_cover.jpg, front_cover.gif
- Mirrors final_cover.png and final_cover.jpg back to assets/cover/

## Canvas Spec

| Property     | Value                                       |
|--------------|---------------------------------------------|
| Dimensions   | 1024 x 1792 px                              |
| Colour space | RGBA during compositing, RGB for final JPG  |
| Print target | Draft2Digital (JPG, 96 DPI minimum)         |
| Font         | VT323-Regular.ttf @ 120pt / 60pt / 52pt     |

## File Locations

| File                           | Purpose                            |
|--------------------------------|------------------------------------|
| assets/cover/base_cover.png    | AI-generated background            |
| assets/cover/stamp_clean.png   | Transparent PNG approval stamp     |
| assets/fonts/VT323-Regular.ttf | Display font                       |
| scripts/build_cover.py         | Cover compositor script            |
| covers/front_cover.png         | Final PNG for web / GitHub         |
| covers/front_cover.jpg         | Final JPG for Draft2Digital upload |
| covers/front_cover.gif         | Final GIF for social / preview     |

## How to Run

    cd C:\Users\peewe\DoughForge
    python scripts\build_cover.py

## Key Design Decisions

- Purge before write: shutil.rmtree(covers/) prevents stale files reaching publisher
- Sized by height: stamp resized as 16% of H regardless of source PNG aspect ratio
- Percentage-based layout: all Y positions are fractions of H, resolution-independent
- Glow layer: Gaussian blur at 50% opacity gives terminal/CRT aesthetic

## Dependencies

    pip install Pillow numpy

## Adapting for Other Projects

Change only the config block at the top of build_cover.py:

    BASE_DIR = r'C:\Users\peewe\YourProject'
    TITLE    = 'Your Title'
    SUBTITLE = 'Your Subtitle'
    AUTHOR   = 'Your Name'

Eventually this config block will be replaced by a book.yaml reader.
"""

with open(os.path.join(ROOT, 'README.md'), 'w', encoding='utf-8') as f:
    f.write(README)
print('Written: README.md')

with open(os.path.join(ROOT, 'docs', 'build_notes.md'), 'w', encoding='utf-8') as f:
    f.write(BUILD_NOTES)
print('Written: docs/build_notes.md')
