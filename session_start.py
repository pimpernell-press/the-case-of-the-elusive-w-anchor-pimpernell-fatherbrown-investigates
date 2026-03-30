#!/usr/bin/env python3
"""
session_start.py — W-Anchor Protocol Session Bootstrap (5-repo coordinator)

MANDATORY: This script is the "putting on the overalls" step.
It MUST run before any work begins in any DoughForge ecosystem repo.

Phases:
  0. Brand compliance gate — read PoshClaude.md + master CLAUDE.md
  1. Anchor verify — run anchor.py in each repo
  2. Git pull — sync all repos
  3. Git diff / status — report state
  4. Git add / commit / push — with deletion guard
  5. Progress logs — read INTERIM_PROGRESS_LOG.md
  6. Session state summary — paste to AI

2026-03-30 — v1.0: Python rewrite of session_start.ps1
             — 5 repos (adds wandering-anchor-book)
             — PoshClaude compliance gate (Phase 0)
             — Deletion guard from hom-ixFAIRindex extended version
             — Auto-restore anchor files from git history
"""

import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# ═══════════════════════════════════════════════════════════���═══
# THE FIVE REPOS — single organism
# ═══════════════════════════════════════════════════════════════

REPOS = [
    {
        "name": "hom-ixFAIRindex",
        "path": r"C:\Users\peewe\OneDrive\Desktop\homeix",
        "anchor": "anchor_verify.ps1",
        "remote": "https://github.com/tonefreqhz/hom-ixFAIRindex",
        "role": "The proof (data + research layer) — THE PROGENITOR",
    },
    {
        "name": "DoughForge",
        "path": r"C:\Users\peewe\Documents\DoughForge",
        "anchor": "anchor_verify.ps1",
        "remote": "https://github.com/tonefreqhz/DoughForge",
        "role": "The forge (literary + data + corpus)",
    },
    {
        "name": "pimpernell-fatherbrown",
        "path": r"C:\Users\peewe\OneDrive\Desktop\the-case-of-the-elusive-w-anchor-pimpernell-fatherbrown-investigates",
        "anchor": "anchor_verify.ps1",
        "remote": "https://github.com/pimpernell-press/the-case-of-the-elusive-w-anchor-pimpernell-fatherbrown-investigates",
        "role": "The book (master literary + master CLAUDE.md)",
    },
    {
        "name": "wandering-anchor-book",
        "path": r"C:\Users\peewe\OneDrive\Desktop\wandering-anchor-book",
        "anchor": "anchor_verify.ps1",
        "remote": "https://github.com/tonefreqhz/wandering-anchor-book",
        "role": "The anchor (autobiography)",
    },
    {
        "name": "reproducible-self-pub-kit",
        "path": r"C:\Users\peewe\OneDrive\Desktop\reproducible-self-pub-kit",
        "anchor": "anchor_verify.ps1",
        "remote": "https://github.com/tonefreqhz/reproducible-self-pub-kit",
        "role": "The kit (build pipeline — ships with launch)",
    },
]

# Brand compliance files
POSH_CLAUDE = r"C:\Users\peewe\Documents\DoughForge\PoshClaude.md"
MASTER_CLAUDE = r"C:\Users\peewe\OneDrive\Desktop\the-case-of-the-elusive-w-anchor-pimpernell-fatherbrown-investigates\The W-Anchor CLAUDE.md"
BRAND_ROUTER = r"C:\Users\peewe\Documents\DoughForge\manual\brand-router.js"


# ── Helpers ──────────────────────────────────────────────────

def banner(text):
    line = "=" * 62
    print(f"\n\033[96m{line}\033[0m")
    print(f"\033[96m  {text}\033[0m")
    print(f"\033[96m{line}\033[0m")


def ok(label, val):
    print(f"  \033[92m[OK     ] {label:<30} {val}\033[0m")


def fail(label, val):
    print(f"  \033[91m[FAIL   ] {label:<30} {val}\033[0m")


def warn(label, val):
    print(f"  \033[93m[WARN   ] {label:<30} {val}\033[0m")


def run_git(args, cwd):
    """Run a git command and return (returncode, stdout)."""
    try:
        result = subprocess.run(
            ["git"] + args,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode, result.stdout.strip()
    except Exception as e:
        return 1, str(e)


# ═══════════════════════════════════════════════════════════════
# PHASE 0 — BRAND COMPLIANCE GATE
# ═══════════════════════════════════════════════════════════════

def phase_0_compliance():
    """Read PoshClaude.md and master CLAUDE.md. Refuse to proceed if missing."""
    banner("PHASE 0  --  BRAND COMPLIANCE GATE (MANDATORY)")
    all_ok = True

    # PoshClaude.md
    if os.path.isfile(POSH_CLAUDE):
        size = os.path.getsize(POSH_CLAUDE)
        ok("PoshClaude.md", f"{size:,} bytes — brand routing active")
        # Verify it contains the prime directive
        with open(POSH_CLAUDE, "r", encoding="utf-8") as f:
            content = f.read()
        if "PRIME DIRECTIVE" in content and "brand router" in content.lower():
            ok("Brand router rules", "present in PoshClaude.md")
        else:
            warn("Brand router rules", "PoshClaude.md may be incomplete")
    else:
        fail("PoshClaude.md", f"MISSING at {POSH_CLAUDE}")
        all_ok = False

    # Master W-Anchor CLAUDE.md
    if os.path.isfile(MASTER_CLAUDE):
        size = os.path.getsize(MASTER_CLAUDE)
        ok("Master CLAUDE.md", f"{size:,} bytes — W-Anchor protocol active")
        with open(MASTER_CLAUDE, "r", encoding="utf-8") as f:
            content = f.read()
        if "PRIME DIRECTIVE" in content and "DRAMATIS PERSONAE" in content:
            ok("W-Anchor protocol", "dramatis personae + prime directive present")
        else:
            warn("W-Anchor protocol", "master CLAUDE.md may be incomplete")
    else:
        fail("Master CLAUDE.md", f"MISSING at {MASTER_CLAUDE}")
        all_ok = False

    # Brand router JS
    if os.path.isfile(BRAND_ROUTER):
        ok("Brand router JS", BRAND_ROUTER)
    else:
        warn("Brand router JS", f"MISSING at {BRAND_ROUTER} (not fatal)")

    if not all_ok:
        print()
        print("  \033[91m*** COMPLIANCE GATE FAILED ***\033[0m")
        print("  \033[91m  Cannot proceed without PoshClaude.md and master CLAUDE.md.\033[0m")
        print("  \033[91m  This is a sackable offence. Fix the missing files.\033[0m")
        return False

    print()
    print("  \033[92m  COMPLIANCE GATE PASSED — overalls on.\033[0m")
    return True


# ═══════════════════════════════════════════════════════════════
# PHASE 1 — ANCHOR VERIFY
# ═══════════════════════════════════════════════════════════════

def phase_1_anchor(results):
    banner("PHASE 1  --  ANCHOR VERIFY (5 repos)")

    for repo in REPOS:
        name = repo["name"]
        path = repo["path"]
        print(f"\n  >> {name}")

        if not os.path.isdir(path):
            fail("REPO ROOT", f"MISSING: {path}")
            results[name]["anchor"] = "MISSING"
            continue

        anchor_path = os.path.join(path, repo["anchor"])
        anchor_py = os.path.join(path, "anchor.py")

        # Try anchor_verify.ps1 first, fall back to anchor.py
        if not os.path.isfile(anchor_path) and not os.path.isfile(anchor_py):
            # Auto-restore from git
            warn("RESTORE", "anchor files missing — attempting git restore...")
            run_git(["checkout", "HEAD", "--", repo["anchor"]], cwd=path)
            run_git(["checkout", "HEAD", "--", "anchor.py"], cwd=path)

        if os.path.isfile(anchor_py):
            rc, out = subprocess.run(
                [sys.executable, "anchor.py"],
                cwd=path,
                capture_output=True,
                text=True,
                timeout=30,
            ).returncode, ""
            # Just run it — anchor.py prints its own output
            subprocess.run([sys.executable, "anchor.py"], cwd=path, timeout=30)
            results[name]["anchor"] = "OK" if rc == 0 else "WARN"
        elif os.path.isfile(anchor_path):
            ok("anchor_verify.ps1", anchor_path)
            results[name]["anchor"] = "OK (ps1 only)"
        else:
            fail("NO ANCHOR", f"Neither anchor.py nor {repo['anchor']} found")
            results[name]["anchor"] = "NO ANCHOR"


# ═══════════════════════════════════════════════════════════════
# PHASE 2 — GIT PULL
# ═══════════════════════════════════════════════════════════════

def phase_2_pull(results):
    banner("PHASE 2  --  GIT PULL (5 repos)")

    for repo in REPOS:
        name = repo["name"]
        path = repo["path"]
        if not os.path.isdir(path):
            results[name]["pull"] = "SKIP"
            continue

        print(f"\n  >> {name}")
        rc, out = run_git(["pull"], cwd=path)
        if rc == 0:
            ok("pull", out if out else "Already up to date.")
            results[name]["pull"] = "OK"
        else:
            warn("pull", out[:200])
            results[name]["pull"] = "ERROR"


# ═══════════════════════════════════════════════════════════════
# PHASE 3 — GIT DIFF / STATUS
# ═══════════════════════════════════════════════════════════════

def phase_3_status(results):
    banner("PHASE 3  --  GIT DIFF / STATUS (5 repos)")

    for repo in REPOS:
        name = repo["name"]
        path = repo["path"]
        if not os.path.isdir(path):
            results[name]["diff"] = "SKIP"
            continue

        print(f"\n  >> {name}")

        _, branch = run_git(["branch", "--show-current"], cwd=path)
        _, status = run_git(["status", "--short"], cwd=path)
        _, ahead_str = run_git(["rev-list", "--count", "@{u}..HEAD"], cwd=path)

        try:
            ahead = int(ahead_str)
        except ValueError:
            ahead = 0

        print(f"    Branch : {branch}")
        print(f"    Ahead  : {ahead} commit(s) unpushed")

        if status:
            lines = status.split("\n")
            print(f"    \033[93mDiff   : {len(lines)} file(s) changed\033[0m")
            for line in lines[:15]:
                print(f"      {line}")
            if len(lines) > 15:
                print(f"      ... and {len(lines) - 15} more")
        else:
            print(f"    \033[92mDiff   : (clean)\033[0m")

        results[name]["diff"] = status if status else "clean"
        results[name]["ahead"] = ahead


# ═══════════════════════════════════════════════════════════════
# PHASE 4 — GIT ADD / COMMIT / PUSH (with deletion guard)
# ═══════════════════════════════════════════════════════════════

def phase_4_push(results):
    banner("PHASE 4  --  GIT ADD / COMMIT / PUSH (deletion guard active)")

    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    for repo in REPOS:
        name = repo["name"]
        path = repo["path"]
        if not os.path.isdir(path):
            results[name]["push"] = "SKIP"
            continue

        print(f"\n  >> {name}")

        _, status = run_git(["status", "--short"], cwd=path)
        ahead = results[name].get("ahead", 0)

        if status:
            lines = status.split("\n")
            deletions = [l for l in lines if l.strip().startswith("D ")]
            additions = [l for l in lines if not l.strip().startswith("D ")]

            # Deletion guard — never auto-commit pure deletions
            if deletions and not additions:
                print(f"    \033[91m[SKIP] Only deletions detected — not auto-committing.\033[0m")
                for d in deletions:
                    print(f"      {d}")
                results[name]["push"] = "SKIP (deletions only)"
                continue

            if deletions:
                print(f"    \033[93m[WARN] Deletions present — staging modifications only:\033[0m")
                for d in deletions:
                    print(f"      \033[93m{d}\033[0m")
                run_git(["add", "-u", "--", "."], cwd=path)
                # Unstage deletions
                for d in deletions:
                    fname = d.strip().lstrip("D ").strip()
                    run_git(["restore", "--staged", fname], cwd=path)
            else:
                print(f"    Staging all changes...")
                run_git(["add", "-A"], cwd=path)

            msg = f"chore: session sync {stamp} [W-Anchor auto-commit]"
            rc, out = run_git(["commit", "-m", msg], cwd=path)
            if rc == 0:
                print(f"    {out.split(chr(10))[0]}")
            _, ahead_str = run_git(["rev-list", "--count", "@{u}..HEAD"], cwd=path)
            try:
                ahead = int(ahead_str)
            except ValueError:
                ahead = 0

        if ahead > 0:
            print(f"    Pushing {ahead} commit(s)...")
            rc, out = run_git(["push"], cwd=path)
            results[name]["push"] = f"PUSHED {ahead}" if rc == 0 else "PUSH ERROR"
        else:
            print(f"    \033[92mNothing to push.\033[0m")
            results[name]["push"] = "UP TO DATE"


# ═══════════════════════════════════════════════════════════════
# PHASE 5 — PROGRESS LOGS
# ═══════════════════════════════════════════════════════════════

def phase_5_logs():
    banner("PHASE 5  --  PROGRESS LOGS")

    for repo in REPOS:
        log_path = os.path.join(repo["path"], "INTERIM_PROGRESS_LOG.md")
        print(f"\n  >> {repo['name']}")
        if os.path.isfile(log_path):
            ok("INTERIM_PROGRESS_LOG.md", log_path)
            with open(log_path, "r", encoding="utf-8") as f:
                for i, line in enumerate(f):
                    if i >= 20:
                        break
                    print(f"       {line.rstrip()}")
        else:
            warn("INTERIM_PROGRESS_LOG.md", "MISSING")


# ═══════════════════════════════════════════════════════════════
# PHASE 6 — SESSION STATE SUMMARY
# ═══════════════════════════════════════════════════════════════

def phase_6_summary(results):
    banner("SESSION STATE SUMMARY  --  paste to AI")

    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    machine = os.environ.get("COMPUTERNAME", os.environ.get("HOSTNAME", "unknown"))

    print()
    print("  \033[95m------- COPY FROM HERE -------\033[0m")
    print()
    print(f"  SESSION  : {stamp}")
    print(f"  MACHINE  : {machine}")
    print(f"  REPOS    : 5 (W-Anchor 5-repo organism)")
    print()
    print("  COMPLIANCE:")
    print(f"    PoshClaude.md    : {'OK' if os.path.isfile(POSH_CLAUDE) else 'MISSING'}")
    print(f"    Master CLAUDE.md : {'OK' if os.path.isfile(MASTER_CLAUDE) else 'MISSING'}")
    print(f"    Brand router     : {'OK' if os.path.isfile(BRAND_ROUTER) else 'MISSING'}")
    print()
    print("  REPO STATUS:")
    for repo in REPOS:
        r = results.get(repo["name"], {})
        anchor = r.get("anchor", "?")
        pull = r.get("pull", "?")
        push = r.get("push", "?")
        diff = r.get("diff", "?")
        diff_short = "clean" if diff == "clean" else f"{len(diff.split(chr(10)))} files"
        line = f"    {repo['name']:<36} anchor={anchor:<12} pull={pull:<8} push={push:<16} diff={diff_short}"
        color = "\033[92m" if anchor in ("OK", "OK (ps1 only)") and pull != "ERROR" else "\033[91m"
        print(f"  {color}{line}\033[0m")

    print()
    print("  FIVE REPOS:")
    for i, repo in enumerate(REPOS, 1):
        print(f"    {i}. {repo['name']:<36} {repo['role']}")
        print(f"       {repo['remote']}")

    print()
    print("  \033[95m------- COPY TO HERE -------\033[0m")
    print()
    banner("SESSION OPEN  --  ALL 5 REPOS ANCHORED")


# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════

def main():
    print()
    print("  W-ANCHOR PROTOCOL — SESSION START (5-repo coordinator)")
    print("  Python edition — 2026-03-30")
    print()

    # Phase 0: compliance gate (MANDATORY — blocks everything else)
    if not phase_0_compliance():
        sys.exit(1)

    # Collect results
    results = {}
    for repo in REPOS:
        results[repo["name"]] = {
            "anchor": "?", "pull": "?", "push": "?",
            "diff": "", "ahead": 0,
        }

    # Phase 1-5
    phase_1_anchor(results)
    phase_2_pull(results)
    phase_3_status(results)
    phase_4_push(results)
    phase_5_logs()

    # Phase 6: summary
    phase_6_summary(results)


if __name__ == "__main__":
    main()
