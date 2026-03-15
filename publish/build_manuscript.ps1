# build_manuscript.ps1
# Builds PDF and EPUB from publication/manuscript.md
# Requires: pandoc, a LaTeX distribution (MiKTeX or TeX Live)

$root = $PSScriptRoot | Split-Path -Parent
$src  = "$root\publication\manuscript.md"
$meta = "$root\publication\metadata.yaml"
$out  = "$root\manuscripts\catalogue staging"

if (-not (Test-Path $out)) { New-Item -ItemType Directory -Path $out | Out-Null }

$slug = "the-case-of-the-elusive-w-anchor"
$date = Get-Date -Format "yyyyMMdd"

Write-Host ""
Write-Host "=== Building EPUB ==="
pandoc $src $meta `
  --output "$out\$slug-$date.epub" `
  --epub-cover-image "$root\assets\cover\front_cover.png" `
  --toc --toc-depth=2

Write-Host ""
Write-Host "=== Building PDF ==="
pandoc $src $meta `
  --output "$out\$slug-$date.pdf" `
  --pdf-engine=xelatex `
  --toc --toc-depth=2 `
  --variable geometry:margin=1.2in `
  --variable fontsize=11pt `
  --variable linestretch=1.4

Write-Host ""
Write-Host "=== Build complete ==="
Write-Host "  EPUB: $out\$slug-$date.epub"
Write-Host "  PDF:  $out\$slug-$date.pdf"
Write-Host ""
