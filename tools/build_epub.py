#!/usr/bin/env python3
"""Build EPUB from book.yaml — DoughForge"""
import yaml, subprocess, sys, os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO)

with open("book.yaml") as f:
    cfg = yaml.safe_load(f)

# Collect all source files in order
sections = []
for key in [
    "front_matter", "part_1_poetry", "part_2_novel",
    "part_3_teaching", "part_4_synthesis", "appendices", "back_matter"
]:
    if key in cfg:
        sections.extend(cfg[key])

# Verify all exist
missing = [s for s in sections if not os.path.exists(s)]
if missing:
    print("MISSING FILES:")
    for m in missing:
        print(f"  {m}")
    sys.exit(1)

print(f"Building EPUB from {len(sections)} source files...")

# Ensure dist/ exists
os.makedirs("dist", exist_ok=True)

# Build EPUB
cmd = [
    "pandoc",
    "--from=markdown",
    "--to=epub3",
    f"--metadata=title:{cfg.get('title', 'DoughForge')}",
    f"--metadata=author:{cfg.get('author', 'Roger G. Lewis')}",
    f"--metadata=lang:{cfg.get('lang', 'en-GB')}",
    f"--metadata=date:{cfg.get('date', '2026')}",
    f"--metadata=rights:{cfg.get('rights', '')}",
    f"--metadata=description:{cfg.get('description', '')}",
    "--epub-cover-image=assets/cover/front_cover_bumper.jpg",
    "--css=assets/epub.css",
    "--toc",
    "--toc-depth=2",
    "--resource-path=.:",
    "-o", "dist/conquest_of_doughforge.epub",
] + sections

print(f"  pandoc {' '.join(cmd[1:5])} ... [{len(sections)} files] -> dist/conquest_of_doughforge.epub")
result = subprocess.run(cmd, capture_output=True, text=True)

if result.returncode == 0:
    size = os.path.getsize("dist/conquest_of_doughforge.epub")
    print(f"\n  SUCCESS: dist/conquest_of_doughforge.epub ({size:,} bytes)")
else:
    print(f"\n  FAILED (exit {result.returncode})")
    if result.stderr:
        print(result.stderr[:3000])
    sys.exit(1)
