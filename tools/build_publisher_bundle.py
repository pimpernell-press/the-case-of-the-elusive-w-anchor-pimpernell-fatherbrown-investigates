"""
build_publisher_bundle.py
Orchestrates all three format builds via book.yaml.
Copies outputs from dist/ to outputs/ for publisher delivery.
"""
import subprocess, shutil, sys, os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from anchor import REPO_ROOT

ROOT    = Path(REPO_ROOT)
DIST    = ROOT / "dist"
OUTPUTS = ROOT / "outputs"
OUTPUTS.mkdir(exist_ok=True)

TOOLS = ROOT / "tools"

print("\n=== DoughForge Standard Edition -- Publisher Bundle Build ===\n")

print("Step 1/3  Building EPUB...")
subprocess.run([sys.executable, str(TOOLS / "build_epub.py")],
               check=True, cwd=ROOT)
shutil.copy2(DIST / "doughforge.epub", OUTPUTS / "doughforge.epub")
print(f"  [OK] {OUTPUTS / 'doughforge.epub'}\n")

print("Step 2/3  Building PDF...")
subprocess.run([sys.executable, str(TOOLS / "build_pdf.py")],
               check=True, cwd=ROOT)
shutil.copy2(DIST / "doughforge.pdf", OUTPUTS / "doughforge.pdf")
print(f"  [OK] {OUTPUTS / 'doughforge.pdf'}\n")

print("Step 3/3  Building DOCX...")
subprocess.run([sys.executable, str(TOOLS / "build_docx.py")],
               check=True, cwd=ROOT)
shutil.copy2(DIST / "doughforge.docx", OUTPUTS / "doughforge.docx")
print(f"  [OK] {OUTPUTS / 'doughforge.docx'}\n")

print("=== Build Complete ===")
for f in ["doughforge.epub", "doughforge.pdf", "doughforge.docx"]:
    p = OUTPUTS / f
    print(f"  {'[OK    ]' if p.exists() else '[MISSING]'}  {p}")
print()
