# W⚓ (WeighAnchor) Protocol for DoughForge Reproducible Self-Pub Kit

## Overview
W⚓ is the emergency reset mechanism in the DoughForge Reproducible Self-Pub Kit, designed to anchor back to ground truth when builds fail (e.g., syntax errors in tools, assembly issues, or LaTeX math rendering problems). It re-fixes syntax, re-assembles manuscripts from canonical sources, re-runs cover and build tools, commits/pushes changes, and prepares for upload. The goal is a "happy ending" (successful build with correct cover title and PDF output) for Draft2Digital publishing.

## Cycle of W⚓ (Persistent Rubbing Without Happy Ending)
Persistent W⚓ invocations (e.g., multiple resets without success) indicate a failure loop. Each W⚓ resets the repo to a "clean" state but re-applies the same scripted fixes (e.g., indentation replaces, regex math corrections). If the underlying issue is not addressed—such as a fundamental bug in the tool code, environment-specific incompatibilities (e.g., Python/PowerShell versions, LaTeX engine differences), or corrupted canonical inputs—the fixes fail repeatedly. This creates a cycle: reset → fail → reset → fail, leading to "blindness" (frustration, wasted time, or repo instability). No happy ending because the script assumes the fix is correct but doesn't verify root causes dynamically.

## Why Persistent W⚓ing Doesn't Result in Happy Ending
W⚓ is reactive, not proactive. It relies on hardcoded fixes (e.g., assuming indentation is missing or math needs Milestone Commit: Adding W⚓ Protocol Note to repo.). If the problem is misdiagnosed (e.g., math is already in Milestone Commit: Adding W⚓ Protocol Note to repo. but escaping is wrong, or indentation is deeper), or if external factors (e.g., Git conflicts, file permissions) interfere, the loop persists. Over-reliance leads to diminishing returns: each rub adds noise to Git history, risks data loss, and delays release.

## Another Stimulus (Alternative Approach)
If W⚓ loops exceed the max rubs, switch to "Manual Override" stimulus: Open files directly in an IDE (e.g., VS Code), manually edit syntax/math, run tools step-by-step via command line (e.g., python tools/add_text_to_cover.py), and test builds incrementally. Use Git branches for experiments instead of main resets. This breaks the automation loop and allows direct inspection.

## Serious Resolution Path to Happy Ending Whilst W⚓ing
1. **Pre-W⚓ Diagnosis**: Before invoking W⚓, log the exact error (e.g., "IndentationError on line 36" or "Missing $ inserted at l.1591"). Check canonical inputs for corruption (e.g., verify chunks/chapters are valid Markdown). Ensure environment matches kit requirements (Python 3.8+, Pandoc, XeLaTeX).
2. **W⚓ Invocation with Limits**: Invoke W⚓ up to max rubs (see below). After each, verify output (check cover image, PDF generation) manually. If fails, note what changed (e.g., "indentation fixed but math still errors").
3. **Incremental Fixes During W⚓**: Modify the W⚓ script per error—e.g., if math fails, add debug output to find the exact line. Use Git diff to compare pre/post-W⚓.
4. **Escalation**: At max rubs, switch to Manual Override. Consult kit documentation or community (e.g., GitHub issues). If environmental, reinstall dependencies.
5. **Post-Resolution**: Once happy ending achieved, document the fix in release notes. Tag a stable commit and archive the W⚓ history for future debugging.
6. **Prevention for Future**: Add unit tests for tools, validate inputs on commit hooks, and include a "dry-run" mode in build scripts to catch issues early.

## Maximum Suggested Number of Rubs
3 rubs (invocations). Beyond this, the cycle risks repo damage or user burnout. If 3 W⚓ fail, escalate to Manual Override immediately. This limit ensures W⚓ remains a quick fix, not a crutch.

## Nailed Protocol for Release Notes
W⚓ is the anchor for quick resets, but cap at 3 rubs. If persistent, diagnose root cause manually. This prevents blindness and ensures reproducible builds.
