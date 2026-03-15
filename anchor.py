import os

# W-Anchor Protocol — reproducible-self-pub-kit
# Every path in the build derives from here. Never hardcode elsewhere.

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
PUBLICATION_DIR = os.path.join(REPO_ROOT, "publication")
MANUSCRIPT = os.path.join(PUBLICATION_DIR, "manuscript.md")
OUTPUTS_DIR = os.path.join(REPO_ROOT, "outputs")
ASSETS_DIR = os.path.join(REPO_ROOT, "assets")
COVER_DIR = os.path.join(ASSETS_DIR, "cover")
BASE_COVER = os.path.join(COVER_DIR, "base_cover.png")
FINAL_COVER = os.path.join(COVER_DIR, "front_cover.jpg")

if __name__ == "__main__":
    paths = {
        "Repo Root":    REPO_ROOT,
        "Publication":  PUBLICATION_DIR,
        "Manuscript":   MANUSCRIPT,
        "Outputs":      OUTPUTS_DIR,
        "Assets":       ASSETS_DIR,
        "Base Cover":   BASE_COVER,
        "Final Cover":  FINAL_COVER,
    }
    print("\n=== W-Anchor Protocol — Path Verification ===\n")
    all_ok = True
    for name, path in paths.items():
        status = "✓ OK     " if os.path.exists(path) else "✗ MISSING"
        if not os.path.exists(path):
            all_ok = False
        print(f"  [{status}] {name}: {path}")
    print()
    if all_ok:
        print("  ✓ All paths verified. Build environment is clean.\n")
    else:
        print("  ✗ One or more paths missing. Fix before building.\n")
