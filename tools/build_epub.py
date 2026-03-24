#!/usr/bin/env python3
"""Build EPUB from book.yaml — W-Anchor Pimpernell"""
import yaml, subprocess, sys, os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO)

with open("book.yaml") as f:
    cfg = yaml.safe_load(f)

# Collect chapter files from book.yaml
sections = [ch["file"] for ch in cfg.get("chapters", [])]

# Prepend foreword if it exists
foreword = "manuscripts/foreword_the_canary.md"
if os.path.exists(foreword) and foreword not in sections:
    sections.insert(0, foreword)

# Append ch10 if it exists and isn't listed
ch10 = "manuscripts/ch10_the_paradox_of_the_helpful_vandal.md"
if os.path.exists(ch10) and ch10 not in sections:
    sections.append(ch10)

# Verify all exist
missing = [s for s in sections if not os.path.exists(s)]
if missing:
    print("MISSING FILES:")
    for m in missing:
        print(f"  {m}")
    sys.exit(1)

print(f"Building EPUB from {len(sections)} source files...")
os.makedirs("dist", exist_ok=True)

title = cfg.get("title", "The Case of the Elusive W-Anchor")
author = cfg.get("author", "Roger G. Lewis")
out = "dist/the-case-of-the-elusive-w-anchor.epub"

# Cover image — use jpg if available
cover = "assets/front_cover.jpg"
if not os.path.exists(cover):
    cover = "assets/front_cover.png"

cmd = [
    "pandoc",
    "--from=markdown",
    "--to=epub3",
    f"--metadata=title:{title}",
    f"--metadata=author:{author}",
    f"--metadata=lang:{cfg.get('lang', 'en-GB')}",
    f"--metadata=date:{cfg.get('date', '2026')}",
    f"--metadata=rights:{cfg.get('rights', '')}",
    f"--metadata=description:{cfg.get('description', '')}",
    f"--epub-cover-image={cover}",
    "--toc",
    "--toc-depth=2",
    "--resource-path=.:",
    "-o", out,
] + sections

print(f"  pandoc ... [{len(sections)} files] -> {out}")
print(f"  Cover: {cover}")
result = subprocess.run(cmd, capture_output=True, text=True)

if result.returncode == 0:
    size = os.path.getsize(out)
    print(f"\n  SUCCESS: {out} ({size:,} bytes)")
else:
    print(f"\n  FAILED (exit {result.returncode})")
    if result.stderr:
        print(result.stderr[:3000])
    sys.exit(1)
