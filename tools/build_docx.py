#!/usr/bin/env python3
"""Build DOCX from book.yaml — DoughForge"""
import yaml, subprocess, sys, os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO)

with open("book.yaml") as f:
    cfg = yaml.safe_load(f)

sections = []
for key in [
    "front_matter", "part_1_poetry", "part_2_novel",
    "part_3_teaching", "part_4_synthesis", "appendices", "back_matter"
]:
    if key in cfg:
        sections.extend(cfg[key])

missing = [s for s in sections if not os.path.exists(s)]
if missing:
    print("MISSING FILES:")
    for m in missing:
        print(f"  {m}")
    sys.exit(1)

print(f"Building DOCX from {len(sections)} source files...")
os.makedirs("dist", exist_ok=True)

cmd = [
    "pandoc",
    "--from=markdown",
    f"--metadata=title:{cfg.get('title', 'DoughForge')}",
    f"--metadata=author:{cfg.get('author', 'Roger G. Lewis')}",
    "--toc",
    "--toc-depth=2",
    "--resource-path=.:",
    "-o", "dist/conquest_of_doughforge.docx",
] + sections

print(f"  Building DOCX...")
result = subprocess.run(cmd, capture_output=True, text=True)

if result.returncode == 0:
    size = os.path.getsize("dist/conquest_of_doughforge.docx")
    print(f"\n  SUCCESS: dist/conquest_of_doughforge.docx ({size:,} bytes)")
else:
    print(f"\n  FAILED (exit {result.returncode})")
    if result.stderr:
        print(result.stderr[-3000:])
    sys.exit(1)
