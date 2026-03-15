$ErrorActionPreference = "Stop"

$metaPath = ".\publication\metadata_pamphlet_issue_1.md"
$ts = Get-Date -Format "yyyyMMdd_HHmmss"

if (!(Test-Path $metaPath)) { throw "Missing: $metaPath" }

# Backup the current (broken) metadata file
New-Item -ItemType Directory -Force -Path ".\_backup" | Out-Null
Copy-Item $metaPath ".\_backup\metadata_pamphlet_issue_1.$ts.bak.md" -Force

# Replace with YAML-only (Pandoc metadata file)
$yaml = @"
---
title: "Reproducible SelfPub Kit"
subtitle: "Shipping Without Surprises  Issue 1"
author: "A writer whos published 11 books via Draft2Digital (since 2018)"
date: "2026-03-03"
lang: en-GB
---
"@

Set-Content -Path $metaPath -Value $yaml -Encoding utf8

Write-Host "Rewrote metadata YAML-only: $metaPath"
Write-Host ("First line now: " + (Get-Content $metaPath -TotalCount 1))
