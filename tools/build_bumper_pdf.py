import subprocess, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from anchor import (
    BUILD_PDF_BUMPER, OUTPUT_PDF_BUMPER, POWERSHELL_CD_NOTE,
    REQUIRED_PATHS_BUMPER, PREAMBLE_TEX_BUMPER
)

print()
print("=== DoughForge W-Anchor -- Bumper Edition PDF Build ===")
print(POWERSHELL_CD_NOTE)

# Preflight
missing = [label for label, path in REQUIRED_PATHS_BUMPER.items() if not os.path.exists(path)]
if not os.path.exists(PREAMBLE_TEX_BUMPER):
    missing.append("Preamble TeX Bumper")
if missing:
    print("\n  STOP: Missing required inputs:")
    for m in missing:
        print(f"    MISSING: {m}")
    sys.exit(1)
print("  Preflight OK -- all required inputs present.")

# Build
print()
print("--- Pandoc PDF Build ---")
print(f"  Command: {BUILD_PDF_BUMPER}")
print()

result = subprocess.run(BUILD_PDF_BUMPER, shell=True, capture_output=True, text=True)

if result.stdout.strip():
    print(result.stdout)
if result.stderr.strip():
    print("  [pandoc stderr]")
    print(result.stderr)

if result.returncode != 0:
    print(f"\n  FAILED (exit code {result.returncode})")
    sys.exit(result.returncode)

size_kb = os.path.getsize(OUTPUT_PDF_BUMPER) // 1024
print(f"  PDF written: {OUTPUT_PDF_BUMPER}  ({size_kb} KB)")
print()
print("=== PDF Build Complete ===")
print(f"  PDF: {OUTPUT_PDF_BUMPER}")
