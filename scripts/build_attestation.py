#!/usr/bin/env python3
"""
DoughForge Build Attestation — M1, M2, M3, M7, M11
Captures build state, hashes sources and outputs, checks manifest consistency.
Exit 0 = all checks pass. Exit 1 = any check fails.
"""

import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BOOK_YAML = os.path.join(REPO_ROOT, "book.yaml")
DIST_DIR = os.path.join(REPO_ROOT, "dist")
OUTPUTS_DIR = os.path.join(REPO_ROOT, "outputs")
ATTESTATION_JSON = os.path.join(DIST_DIR, "BUILD_ATTESTATION.json")
SUMMARY_MD = os.path.join(DIST_DIR, "BUILD_SUMMARY.md")

# Source files listed in book.yaml (parsed simply — no YAML library required)
EXPECTED_SOURCES = [
    "manuscripts/ch01_the_crime_scene_survey.md",
    "manuscripts/ch02_the_choosing_of_dragons.md",
    "manuscripts/ch03_the_flux_capacitor.md",
    "manuscripts/ch04_the_circus_trucks.md",
    "manuscripts/ch05_the_epilogue_that_came_first.md",
    "manuscripts/ch06_the_work_to_six_forty_one.md",
    "manuscripts/ch07_the_wanking_in_circles.md",
    "manuscripts/ch08_the_nine_one_one_call.md",
    "manuscripts/ch09_the_verdict.md",
]

# Additional source files that contribute to the build
EXTRA_SOURCES = [
    "book.yaml",
    "anchor.py",
    "manuscripts/ch03b_the_triple_word_score.md",
    "manuscripts/ch03_the_sin_of_helpfulness.md",
    "manuscripts/chapters/ch_cherry.md",
]

EXPECTED_OUTPUTS = [
    "dist/the-case-of-the-elusive-w-anchor.epub",
    "dist/the-case-of-the-elusive-w-anchor.pdf",
    "dist/the-case-of-the-elusive-w-anchor.docx",
]


def run_cmd(cmd):
    """Run a shell command, return stdout or empty string on failure."""
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=10,
                           cwd=REPO_ROOT)
        return r.stdout.strip()
    except Exception:
        return ""


def sha256_file(path):
    """Return hex SHA-256 of a file, or None if missing."""
    if not os.path.isfile(path):
        return None
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def get_tool_version(cmd):
    """Get version string from a --version command."""
    out = run_cmd(cmd)
    if out:
        return out.split("\n")[0]
    return "not installed"


def get_git_info():
    """Return commit hash and repo clean status."""
    commit = run_cmd(["git", "rev-parse", "HEAD"])
    status = run_cmd(["git", "status", "--porcelain"])
    return commit or "unknown", len(status) == 0


def build_source_manifest():
    """Hash all expected source files."""
    manifest = {}
    for rel in EXPECTED_SOURCES + EXTRA_SOURCES:
        full = os.path.join(REPO_ROOT, rel)
        h = sha256_file(full)
        if h:
            manifest[rel] = h
    return manifest


def build_output_manifest():
    """Hash all output files that exist."""
    manifest = {}
    for rel in EXPECTED_OUTPUTS:
        full = os.path.join(REPO_ROOT, rel)
        h = sha256_file(full)
        if h:
            manifest[rel] = h
    return manifest


def check_manifest_consistency(source_manifest):
    """M3: Compare expected source list to actual files on disk."""
    missing = []
    extra = []
    for rel in EXPECTED_SOURCES:
        if rel not in source_manifest:
            missing.append(rel)
    # Check for .md files in manuscripts/ not in our list
    ms_dir = os.path.join(REPO_ROOT, "manuscripts")
    if os.path.isdir(ms_dir):
        for f in os.listdir(ms_dir):
            if f.endswith(".md"):
                rel = f"manuscripts/{f}"
                if rel not in EXPECTED_SOURCES and rel not in [s for s in EXTRA_SOURCES if s.startswith("manuscripts/")]:
                    extra.append(rel)
    passed = len(missing) == 0
    return {"pass": passed, "missing": missing, "extra": extra}


def check_dirty_outputs(source_manifest, output_manifest):
    """M7: Detect outputs newer than sources without corresponding source changes."""
    unexplained = []
    if not output_manifest:
        return {"pass": True, "unexplained_deltas": []}

    # Check if any attestation already exists
    prev_path = ATTESTATION_JSON
    if os.path.isfile(prev_path):
        try:
            with open(prev_path, "r", encoding="utf-8") as f:
                prev = json.load(f)
            prev_sources = prev.get("source_manifest", {})
            prev_outputs = prev.get("output_manifest", {})
            # If outputs changed but sources didn't, that's dirty
            for rel, h in output_manifest.items():
                prev_h = prev_outputs.get(rel)
                if prev_h and prev_h != h:
                    # Output changed — did any source also change?
                    source_changed = any(
                        prev_sources.get(s) != source_manifest.get(s)
                        for s in source_manifest
                    )
                    if not source_changed:
                        unexplained.append(rel)
        except (json.JSONDecodeError, KeyError):
            pass  # No valid previous attestation — skip delta check

    return {"pass": len(unexplained) == 0, "unexplained_deltas": unexplained}


def write_summary(att):
    """Write BUILD_SUMMARY.md from attestation dict."""
    lines = [
        "# Build Attestation Summary",
        "",
        f"**Timestamp:** {att['timestamp']}",
        f"**Commit:** `{att['commit_hash'][:12]}`",
        f"**Repo clean:** {'Yes' if att['repo_clean'] else 'No — uncommitted changes'}",
        "",
        "## Tool Versions",
        "",
    ]
    for tool, ver in att["tool_versions"].items():
        lines.append(f"- **{tool}:** {ver}")

    lines += [
        "",
        "## Source Manifest",
        "",
        "| File | SHA-256 (first 12) |",
        "|------|--------------------|",
    ]
    for f, h in sorted(att["source_manifest"].items()):
        lines.append(f"| `{f}` | `{h[:12]}` |")

    lines += [
        "",
        "## Output Manifest",
        "",
        "| File | SHA-256 (first 12) |",
        "|------|--------------------|",
    ]
    if att["output_manifest"]:
        for f, h in sorted(att["output_manifest"].items()):
            lines.append(f"| `{f}` | `{h[:12]}` |")
    else:
        lines.append("| *(no outputs built yet)* | — |")

    mc = att["manifest_consistency"]
    lines += [
        "",
        "## Checks",
        "",
        f"- **M3 Manifest Consistency:** {'PASS' if mc['pass'] else 'FAIL'}",
    ]
    if mc["missing"]:
        lines.append(f"  - Missing: {', '.join(mc['missing'])}")
    if mc["extra"]:
        lines.append(f"  - Extra (not in book.yaml): {', '.join(mc['extra'])}")

    dd = att["dirty_output_detection"]
    lines.append(f"- **M7 Dirty Output Detection:** {'PASS' if dd['pass'] else 'FAIL'}")
    if dd["unexplained_deltas"]:
        lines.append(f"  - Unexplained: {', '.join(dd['unexplained_deltas'])}")

    lines += [
        "",
        f"## Overall: {'PASS' if att['overall_pass'] else 'FAIL'}",
        "",
    ]
    return "\n".join(lines)


def main():
    commit, clean = get_git_info()

    tool_versions = {
        "python": get_tool_version([sys.executable, "--version"]),
        "pandoc": get_tool_version(["pandoc", "--version"]),
        "lualatex": get_tool_version(["lualatex", "--version"]),
    }

    source_manifest = build_source_manifest()
    output_manifest = build_output_manifest()
    manifest_consistency = check_manifest_consistency(source_manifest)
    dirty_output = check_dirty_outputs(source_manifest, output_manifest)

    overall = manifest_consistency["pass"] and dirty_output["pass"]

    attestation = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "commit_hash": commit,
        "repo_clean": clean,
        "tool_versions": tool_versions,
        "source_manifest": source_manifest,
        "output_manifest": output_manifest,
        "manifest_consistency": manifest_consistency,
        "dirty_output_detection": dirty_output,
        "overall_pass": overall,
    }

    # Ensure dist/ exists
    os.makedirs(DIST_DIR, exist_ok=True)

    with open(ATTESTATION_JSON, "w", encoding="utf-8") as f:
        json.dump(attestation, f, indent=2)
    print(f"[OK] BUILD_ATTESTATION.json written to {ATTESTATION_JSON}")

    summary = write_summary(attestation)
    with open(SUMMARY_MD, "w", encoding="utf-8") as f:
        f.write(summary)
    print(f"[OK] BUILD_SUMMARY.md written to {SUMMARY_MD}")

    # Print summary to console
    print()
    print(summary)

    if overall:
        print("[OK] All checks passed.")
        return 0
    else:
        print("[FAIL] One or more checks failed.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
