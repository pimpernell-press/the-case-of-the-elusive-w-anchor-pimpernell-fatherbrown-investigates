Write-Host ""
Write-Host "============================================================"
Write-Host " THE CASE OF THE ELUSIVE W-ANCHOR — ANCHOR VERIFY"
Write-Host "============================================================"
Write-Host ""

$root = $PSScriptRoot

$paths = @{
    "Repo Root"         = $root
    "Scripts Dir"       = "$root\scripts"
    "Assets Dir"        = "$root\assets"
    "Docs Dir"          = "$root\docs"
    "Widgets Dir"       = "$root\widgets"
    "Inputs Dir"        = "$root\inputs"
    "Manuscripts Dir"   = "$root\manuscripts"
    "Templates Dir"     = "$root\templates"
    "Tools Dir"         = "$root\tools"
    "Vault Dir"         = "$root\vault"
    "README"            = "$root\README.md"
    "anchor_verify.ps1" = "$root\anchor_verify.ps1"
}

$allOk = $true

foreach ($label in $paths.Keys | Sort-Object) {
    $p = $paths[$label]
    if (Test-Path $p) {
        Write-Host ("  [OK     ] {0,-30} {1}" -f $label, $p)
    } else {
        Write-Host ("  [MISSING] {0,-30} {1}" -f $label, $p)
        $allOk = $false
    }
}

Write-Host ""
if ($allOk) {
    Write-Host "  OK All paths verified. You are anchored."
} else {
    Write-Host "  WARNING: Missing paths detected. Fix before proceeding."
}
Write-Host ""
