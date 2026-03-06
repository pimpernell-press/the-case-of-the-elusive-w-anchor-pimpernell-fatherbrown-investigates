[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"

$sentinelStart = "<!-- STAGE1_D2D_BLOCK_START -->"
$sentinelEnd   = "<!-- STAGE1_D2D_BLOCK_END -->"

# Release Notes (rewrite every time)
$releaseNotes = @(
'# Reproducible SelfPub Kit  Release Notes (Stage 1)',
'',
'Stage 1 marks the it builds the same way twice milestone: a prose-first, Windows-friendly, reproducible selfpublishing workflow with a stable repo layout and repeatable output locations. This release intentionally prioritizes **general authors** and a **low-drama build** over covering every edge case in technical publishing.',
'',
'Last updated: 2026-03-04  ',
'Repo: https://github.com/tonefreqhz/reproducible-self-pub-kit  ',
'Branch: main',
'',
'---',
'',
'##  Whats included (Stage 1)',
'',
'This release provides:',
'',
'- A canonical repo layout designed to prevent drift (`inputs/`, `publication/`, `publish/`, `outputs/`, `vault/`).',
'- A working Windows (PowerShell) build workflow.',
'- Repeatable build outputs (PDF/EPUB/DOCX) written to consistent locations under `outputs/`.',
'',
'##  What success means in Stage 1',
'',
'A successful Stage 1 run means:',
'',
'- `git status -sb` is clean (no drift).',
'- The build completes without manual intervention.',
'- Outputs are produced in the expected folders (no where did my files go? moments).',
'',
'##  Known limitations (Stage 1)',
'',
'Stage 1 is optimized for prose-first books and marketing freebies. Technical manuscripts are **best-effort**.',
'',
'- **Math-heavy / LaTeX-style content** may fail PDF builds when the source contains fragile patterns (example: placeholder math like `$$X\$$` instead of `$$X$$`).',
'- **Encoding artifacts (mojibake)** from copy/paste can introduce characters that break Pandoc  XeLaTeX (examples observed: `Â\|Â`, stray `œ`).',
'',
'##  Roadmap: Technical Authors Edition (candidate)',
'',
'If there is sufficient interest, a Technical Authors Edition will add:',
'',
'- math normalization rules (safe delimiters, placeholder detection)',
'- encoding sanitation checks (mojibake detection + fixes)',
'- stronger diagnostics for Pandoc  XeLaTeX failures',
'',
'---',
''
)

Set-Content -Encoding UTF8 -Path .\RELEASE_NOTES.md -Value $releaseNotes

# Print/Build Notes (append once)
$printBuildPath = ".\PRINT_AND_BUILD_NOTES.md"
if (-not (Test-Path $printBuildPath)) {
  Set-Content -Encoding UTF8 -Path $printBuildPath -Value @("# Print and Build Notes", "")
}

$existing = Get-Content -Raw -Encoding UTF8 -Path $printBuildPath

if ($existing -notmatch [regex]::Escape($sentinelStart)) {

  $block = @(
    '',
    $sentinelStart,
    '',
    '---',
    '',
    '## Stage 1 promise (what this repo guarantees)',
    '',
    'If you follow the canonical workflow in this repo on Windows (PowerShell), Stage 1 guarantees:',
    '',
    '- reproducible builds (same inputs  same output locations)',
    '- a consistent, repeatable command surface (no mystery steps)',
    '- upload-ready artifacts for common distributors',
    '',
    'Stage 1 is optimized for prose-first content. Math-heavy technical publishing is best-effort in this release.',
    '',
    '---',
    '',
    '## Draft2Digital (ebook)  upload checklist',
    '',
    '### Build',
    '',
    'From repo root:',
    '',
    '~~~powershell',
    '.\publish\rebuild_publish.ps1',
    '~~~',
    '',
    'Confirm outputs exist (paths may vary by script target, but should be under `outputs/`):',
    '',
    '- `outputs\epub\... .epub` (preferred for D2D)',
    '- `outputs\docx\... .docx` (fallback)',
    '',
    '### Cover (ebook front)',
    '',
    'Prepare a front cover image (JPG/PNG). Suggested repo location:',
    '',
    '- `assets\cover\ebook_front.png`',
    '',
    '### Upload to Draft2Digital',
    '',
    '- Upload cover: use your front cover image',
    '- Upload book file: use the EPUB from `outputs\epub\`',
    '',
    '---',
    '',
    '## Print (if used)  interior + cover wrap',
    '',
    '### Interior PDF',
    'Use the print interior PDF generated under `outputs\pdf\`.',
    '',
    '### Cover wrap PDF (to do)',
    'Create a full wrap cover PDF sized to trim + spine + bleed. Suggested repo location:',
    '',
    '- `assets\cover\print_wrap.pdf`',
    '',
    $sentinelEnd,
    ''
  )

  Add-Content -Encoding UTF8 -Path $printBuildPath -Value $block
  Write-Host "Updated: PRINT_AND_BUILD_NOTES.md (block appended once)"
}
else {
  Write-Host "Skipped: PRINT_AND_BUILD_NOTES.md (block already present)"
}

Write-Host "Wrote: RELEASE_NOTES.md"
