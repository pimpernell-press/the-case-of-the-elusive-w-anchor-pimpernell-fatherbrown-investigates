# Build and Publish Launcher (double-click this .ps1 file)
cd ''
& '.\Tools\rebuild_publish.ps1'
Write-Host 'Build complete! Check MyBook/outputs/ for PDF, EPUB, DOCX.'
Read-Host 'Press Enter to exit'
