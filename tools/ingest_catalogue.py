"""
ingest_catalogue.py  -  Batch ingest all EPUBs from a staging folder
into per-book chapter directories.
"""
import re, sys
from pathlib import Path
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

STAGING = Path(r"C:\Users\peewe\OneDrive\Desktop\Reedsy E Pubs Rog")
OUT_ROOT = Path("chapters/catalogue")

def html_to_md(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.find_all(["nav", "aside"]):
        tag.decompose()
    text = soup.get_text(separator="\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

def slug(name: str) -> str:
    return re.sub(r"[^\w\-]", "-", name.lower())[:60].rstrip("-")

def ingest_epub(epub_path: Path):
    print(f"\n── {epub_path.name}")
    try:
        book = epub.read_epub(str(epub_path))
    except Exception as e:
        print(f"  ERROR reading: {e}")
        return

    book_slug = slug(epub_path.stem)
    outdir = OUT_ROOT / book_slug
    outdir.mkdir(parents=True, exist_ok=True)

    items = [i for i in book.get_items()
             if i.get_type() == ebooklib.ITEM_DOCUMENT]

    written = 0
    total_words = 0
    for idx, item in enumerate(items, start=1):
        content = item.get_content().decode("utf-8", errors="replace")
        md = html_to_md(content)
        if len(md.strip()) < 50:
            continue
        words = len(md.split())
        fname = outdir / f"ch{idx:02d}.md"
        fname.write_text(md, encoding="utf-8")
        total_words += words
        written += 1

    print(f"  {written} chapters  |  ~{total_words:,} words  →  {outdir}")

OUT_ROOT.mkdir(parents=True, exist_ok=True)
epubs = sorted(STAGING.rglob("*.epub"))
print(f"Found {len(epubs)} EPUBs in {STAGING}\n")
for ep in epubs:
    ingest_epub(ep)

print("\n\nAll done.")
