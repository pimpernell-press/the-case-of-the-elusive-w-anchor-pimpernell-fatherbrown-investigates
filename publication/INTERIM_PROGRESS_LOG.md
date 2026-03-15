# INTERIM_PROGRESS_LOG

## 2026-03-04  Chunk pipeline + build stabilization

### What we did
- Established/used PROJECT_ROOT anchoring to avoid CWD drift when running scripts.
- Created HTML chunk files under: inputs/canonical/chunks/
- Assembled chunks into the canonical manuscript: publication/pamphlet_issue_1.md
- Built outputs via Pandoc + XeLaTeX using:
  py .\tools\build_book.py --all --src .\publication\pamphlet_issue_1.md --meta .\publication\metadata_pamphlet_issue_1.md

### Current issue / known defect
- The assembled Markdown manuscript contains excessive horizontal rules ('---') between many lines.
  This likely came from chunk HTML containing <hr> plus the assembly separator '---', or from conversion choices.
  Result: readable builds may be degraded (visual separators everywhere).

### Outputs location
- outputs/pdf/
- outputs/epub/
- outputs/docx/

### Next steps
- Fix chunk HTML / assembly separator so '---' only appears between chunks (not between lines).
- Re-assemble and rebuild; then proofread outputs.
## WeighAnchor Command (W⚓)
When things go pear-shaped (drift detected), invoke WeighAnchor (short: W⚓) to reset to anchor ground truth. Icon: W⚓ for call anchor when weighing anchor. Added for posterity—human sweats blood, AI pulls socks up.
