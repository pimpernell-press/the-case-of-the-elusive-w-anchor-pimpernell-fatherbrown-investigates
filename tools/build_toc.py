"""
build_toc.py
Reads book.yaml -> writes src/nav.xhtml and src/toc.ncx
Includes both chapters: and appendices: sections.
"""
import os, yaml
from anchor import REPO_ROOT

BOOK_YAML = os.path.join(REPO_ROOT, "book.yaml")
SRC_DIR   = os.path.join(REPO_ROOT, "src")
os.makedirs(SRC_DIR, exist_ok=True)

with open(BOOK_YAML, encoding="utf-8") as f:
    book = yaml.safe_load(f)

chapters   = book.get("chapters",   [])
appendices = book.get("appendices", [])
title      = book.get("title", "Book")

# ── nav.xhtml ────────────────────────────────────────────────────────────────

def nav_li(ch):
    return f'      <li><a href="../{ch["file"]}">{ch["title"]}</a></li>'

chapter_items   = "\n".join(nav_li(ch) for ch in chapters)
appendix_items  = "\n".join(nav_li(ap) for ap in appendices)

appendix_block = ""
if appendices:
    appendix_block = f"""
        <li><span>Appendices</span>
          <ol>
    {appendix_items}
          </ol>
        </li>"""

nav_xhtml = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:epub="http://www.idpf.org/2007/ops">
<head><title>Table of Contents</title></head>
<body>
  <nav epub:type="toc" id="toc">
    <h1>Table of Contents</h1>
    <ol>
{chapter_items}{appendix_block}
    </ol>
  </nav>
</body>
</html>"""

nav_path = os.path.join(SRC_DIR, "nav.xhtml")
with open(nav_path, "w", encoding="utf-8") as f:
    f.write(nav_xhtml)
print(f"Written: {nav_path}")

# ── toc.ncx ──────────────────────────────────────────────────────────────────

all_entries = chapters + appendices          # flat list for NCX play order
play_order  = 1

ncx_points = []
for ch in chapters:
    ncx_points.append(f"""  <navPoint id="{ch['id']}" playOrder="{play_order}">
    <navLabel><text>{ch['title']}</text></navLabel>
    <content src="../{ch['file']}"/>
  </navPoint>""")
    play_order += 1

if appendices:
    # NCX has no native nesting for appendices — add a label navPoint then entries
    ncx_points.append(f"""  <navPoint id="appendices-heading" playOrder="{play_order}">
    <navLabel><text>Appendices</text></navLabel>
    <content src="../{appendices[0]['file']}"/>
  </navPoint>""")
    play_order += 1
    for ap in appendices:
        ncx_points.append(f"""  <navPoint id="{ap['id']}" playOrder="{play_order}">
    <navLabel><text>{ap['title']}</text></navLabel>
    <content src="../{ap['file']}"/>
  </navPoint>""")
        play_order += 1

toc_ncx = f"""<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
<head><meta name="dtb:uid" content="{title}"/></head>
<docTitle><text>{title}</text></docTitle>
<navMap>
{"\n".join(ncx_points)}
</navMap>
</ncx>"""

ncx_path = os.path.join(SRC_DIR, "toc.ncx")
with open(ncx_path, "w", encoding="utf-8") as f:
    f.write(toc_ncx)
print(f"Written: {ncx_path}")

