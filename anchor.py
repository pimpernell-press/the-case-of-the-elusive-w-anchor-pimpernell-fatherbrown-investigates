import os

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))

MANUSCRIPTS_DIR = os.path.join(REPO_ROOT, "manuscripts")
CH01 = os.path.join(MANUSCRIPTS_DIR, "ch01_the_crime_scene_survey.md")
CH02 = os.path.join(MANUSCRIPTS_DIR, "ch02_the_choosing_of_dragons.md")
CH03 = os.path.join(MANUSCRIPTS_DIR, "ch03_the_flux_capacitor.md")
CH04 = os.path.join(MANUSCRIPTS_DIR, "ch04_the_circus_trucks.md")
CH05 = os.path.join(MANUSCRIPTS_DIR, "ch05_the_epilogue_that_came_first.md")
CH06 = os.path.join(MANUSCRIPTS_DIR, "ch06_the_work_to_six_forty_one.md")
CH07 = os.path.join(MANUSCRIPTS_DIR, "ch07_the_wanking_in_circles.md")
CH08 = os.path.join(MANUSCRIPTS_DIR, "ch08_the_nine_one_one_call.md")
CH09 = os.path.join(MANUSCRIPTS_DIR, "ch09_the_verdict.md")
ALL_CHAPTERS = [CH01, CH02, CH03, CH04, CH05, CH06, CH07, CH08, CH09]

PUBLICATION_DIR = os.path.join(REPO_ROOT, "publication")
MANUSCRIPT = os.path.join(PUBLICATION_DIR, "manuscript.md")
METADATA_YAML = os.path.join(PUBLICATION_DIR, "metadata.yaml")
FRONT_MATTER_DIR = os.path.join(PUBLICATION_DIR, "front_matter")
FOREWORD_FOSTER = os.path.join(FRONT_MATTER_DIR, "foreword.md")
FOREWORD_BUMPER = FOREWORD_FOSTER
DEDICATION_BUMPER = os.path.join(FRONT_MATTER_DIR, "dedication.md")
PREFACE_BUMPER = os.path.join(FRONT_MATTER_DIR, "preface.md")
MANUSCRIPT_BUMPER = MANUSCRIPT

OUTPUTS_DIR = os.path.join(REPO_ROOT, "dist")
OUTPUT_EPUB = os.path.join(OUTPUTS_DIR, "the-case-of-the-elusive-w-anchor.epub")
OUTPUT_PDF = os.path.join(OUTPUTS_DIR, "the-case-of-the-elusive-w-anchor.pdf")
OUTPUT_DOCX = os.path.join(OUTPUTS_DIR, "the-case-of-the-elusive-w-anchor.docx")
OUTPUT_EPUB_BUMPER = OUTPUT_EPUB
OUTPUT_PDF_BUMPER = OUTPUT_PDF
OUTPUT_DOCX_BUMPER = OUTPUT_DOCX

ASSETS_DIR = os.path.join(REPO_ROOT, "assets")
COVER_DIR = os.path.join(ASSETS_DIR, "cover")
FONTS_DIR = os.path.join(ASSETS_DIR, "fonts")
IMAGES_DIR = os.path.join(ASSETS_DIR, "images")
BASE_COVER = os.path.join(COVER_DIR, "base_cover.png")
FINAL_COVER = os.path.join(COVER_DIR, "front_cover.jpg")
BASE_COVER_BUMPER = BASE_COVER
FINAL_COVER_BUMPER = FINAL_COVER

TOOLS_DIR = os.path.join(REPO_ROOT, "tools")
SCRIPTS_DIR = os.path.join(REPO_ROOT, "scripts")
PUBLISH_DIR = os.path.join(REPO_ROOT, "publish")
DOCS_DIR = os.path.join(REPO_ROOT, "docs")
WIDGETS_DIR = os.path.join(REPO_ROOT, "widgets")
RESERVOIR_DIR = os.path.join(REPO_ROOT, "reservoir")
SRC_DIR = os.path.join(REPO_ROOT, "src")
PREAMBLE_TEX = os.path.join(PUBLISH_DIR, "cover_preamble.tex")
PREAMBLE_TEX_BUMPER = PREAMBLE_TEX
ANCHOR_MD = os.path.join(REPO_ROOT, "ANCHOR.md")
PROGRESS_LOG = os.path.join(REPO_ROOT, "INTERIM_PROGRESS_LOG.md")

BOOK_TITLE = "The Case of the Elusive W-Anchor"
BOOK_TITLE_STANDARD = BOOK_TITLE
BOOK_TITLE_BUMPER = BOOK_TITLE
BOOK_SUBTITLE_BUMPER = "Pimpernell Father Brown Investigates"
BOOK_AUTHOR = "Roger G. Lewis"
FOREWORD_AUTHOR = ""
EDITION_BUMPER = "First Edition"
EDITION_PRICE = ""
PUBLISHER = "Pimpernell Press"

POWERSHELL_CD_NOTE = "\n  cd to repo root before running any tool.\n"

_ch = " ".join(f'"{c}"' for c in ALL_CHAPTERS)
BUILD_EPUB = f'pandoc {_ch} --from=markdown --to=epub3 --epub-cover-image="{FINAL_COVER}" --toc --toc-depth=2 --metadata title="{BOOK_TITLE}" --metadata author="{BOOK_AUTHOR}" -o "{OUTPUT_EPUB}"'
BUILD_PDF = f'pandoc {_ch} --from=markdown --pdf-engine=lualatex --toc --toc-depth=2 --metadata title="{BOOK_TITLE}" --metadata author="{BOOK_AUTHOR}" -o "{OUTPUT_PDF}"'
BUILD_DOCX = f'pandoc {_ch} --from=markdown --toc --toc-depth=2 --metadata title="{BOOK_TITLE}" --metadata author="{BOOK_AUTHOR}" -o "{OUTPUT_DOCX}"'
BUILD_EPUB_BUMPER = BUILD_EPUB
BUILD_PDF_BUMPER = BUILD_PDF
BUILD_DOCX_BUMPER = BUILD_DOCX

REQUIRED_PATHS = {
    "Repo Root": REPO_ROOT, "Manuscripts": MANUSCRIPTS_DIR,
    "Ch01": CH01, "Ch02": CH02, "Ch03": CH03, "Ch04": CH04, "Ch05": CH05,
    "Ch06": CH06, "Ch07": CH07, "Ch08": CH08, "Ch09": CH09,
    "Publication": PUBLICATION_DIR, "Metadata": METADATA_YAML,
    "Assets": ASSETS_DIR, "Cover Dir": COVER_DIR, "Base Cover": BASE_COVER,
    "Tools": TOOLS_DIR, "Anchor MD": ANCHOR_MD,
}
REQUIRED_PATHS_BUMPER = {}
GENERATED_PATHS = {
    "Dist": OUTPUTS_DIR, "EPUB": OUTPUT_EPUB, "PDF": OUTPUT_PDF,
    "DOCX": OUTPUT_DOCX, "Cover": FINAL_COVER, "SRC": SRC_DIR,
}
GENERATED_PATHS_BUMPER = {}

if __name__ == "__main__":
    print("\n=== W-Anchor Path Verification ===\n")
    ok = True
    for k, v in REQUIRED_PATHS.items():
        e = os.path.exists(v)
        if not e: ok = False
        print(f"  [{'OK     ' if e else 'MISSING'}] {k:<16} {v}")
    print("\n  -- Generated --\n")
    for k, v in GENERATED_PATHS.items():
        e = os.path.exists(v)
        print(f"  [{'OK     ' if e else 'not yet'}] {k:<16} {v}")
    print("\n  " + ("OK All required verified." if ok else "STOP: Missing paths.") + "\n")
