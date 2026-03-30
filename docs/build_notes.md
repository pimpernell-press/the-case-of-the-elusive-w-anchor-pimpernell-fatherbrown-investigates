# DoughForge — Cover Build Notes

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

---

## session_start.ps1 Audit — 30 March 2026

### Status: NOT READY TO SHIP

The session_start.ps1 coordinator exists in all five repos but is **not consistent
or fully deployed**. This repo (the-case-of-the-elusive-w-anchor) is the MASTER
LITERARY repo — the novel manuscript lives here.

#### Issues Found

1. **This repo's session_start.ps1** is the 189-line version. Missing the
   deletion guard and auto-restore from the homeix 224-line version.

2. **The W-Anchor CLAUDE.md** (this repo) had a path error at line 192:
   `.\tools\anchor_verify.ps1` → corrected to `.\anchor_verify.ps1`.
   The script lives at root in all repos, not in tools/.

3. **anchor_verify.ps1 here uses $PSScriptRoot** (correct, portable).
   anchor.py uses os.path.dirname (correct). This repo is the GOOD pattern.

4. **No PoshClaude.md call** in session_start.ps1. Any Claude entering via
   session_start does not get brand compliance rules.

5. **Dramatis personae, running gags, and chapter manifest** are in
   `The W-Anchor CLAUDE.md` but NOT in session_start output. A new Claude
   session loses the protocol unless it reads the named CLAUDE.md file.

#### What Needs to Happen

- [ ] Propagate deletion guard from homeix session_start.ps1
- [ ] Add PoshClaude.md + W-Anchor CLAUDE.md read to session_start
- [ ] Ensure session_start summary includes dramatis personae reference
- [ ] Build notes should be repo-specific (currently copied from DoughForge cover notes)

#### Forensic Evidence

See DoughForge/docs/build_notes.md for full hash table.

#### Protocol Tested in Beta

This repo IS the novel about building the protocol. The failures documented
here are book material. Chapter 1: The Crime Scene Survey. Chapter 5: The
Epilogue That Came First. The build notes ARE the plot.
