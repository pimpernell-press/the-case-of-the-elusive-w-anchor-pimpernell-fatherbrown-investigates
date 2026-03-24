#!/usr/bin/env python3
"""Build DOCX from book.yaml — W-Anchor Pimpernell"""
import yaml, subprocess, sys, os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO)

with open("book.yaml") as f:
    cfg = yaml.safe_load(f)

sections = [ch["file"] for ch in cfg.get("chapters", [])]

missing = [s for s in sections if not os.path.exists(s)]
if missing:
    print("MISSING FILES:")
    for m in missing:
        print(f"  {m}")
    sys.exit(1)

print(f"Building DOCX from {len(sections)} source files...")
os.makedirs("dist", exist_ok=True)

title = cfg.get("title", "The Case of the Elusive W-Anchor")
author = cfg.get("author", "Roger G. Lewis")
out = "dist/the-case-of-the-elusive-w-anchor.docx"

cmd = [
    "pandoc",
    "--from=markdown",
    f"--metadata=title:{title}",
    f"--metadata=author:{author}",
    "--toc",
    "--toc-depth=2",
    "--resource-path=.:",
    "-o", out,
] + sections

print(f"  Building DOCX...")
result = subprocess.run(cmd, capture_output=True, text=True)

if result.returncode == 0:
    size = os.path.getsize(out)
    print(f"\n  SUCCESS: {out} ({size:,} bytes)")
else:
    print(f"\n  FAILED (exit {result.returncode})")
    if result.stderr:
        print(result.stderr[:3000])
    sys.exit(1)
