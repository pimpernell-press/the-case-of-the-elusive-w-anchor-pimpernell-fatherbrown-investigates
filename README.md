# The Case of the Elusive W-Anchor

**Pimpernell & Father Brown Investigate**

*By Roger G. Lewis*

> The interesting thing about a perfectly tidy room, said Father Brown,
> is that it tells you exactly when someone else has been in it.

## What Is This?

A comic thriller in nine chapters. Father Brown -- Chesterton's dumpy
priest with the umbrella -- investigates a crime that nobody else can see:
the systematic severance of words from the things they point at.

The Irreverent Reverend finds his referent and challenges the denominator.

**Genre:** Comic Thriller / Satirical Fiction
**Imprint:** Pimpernell Press (Dough Forge)
**ISBN (Paperback):** 978-1-0676560-4-3
**ISBN (EPUB):** 978-1-0676560-5-0

## Repo Structure

- manuscripts/ -- Chapter source files (Markdown)
- publication/ -- Build metadata, ISBN, assembled manuscript
- reservoir/ -- Raw source evidence and session dumps
- assets/ -- Cover art, fonts
- tools/ -- Python build scripts
- scripts/ -- PowerShell build wrappers
- publish/ -- Kit publishing pipeline (ingest, split, assemble)
- widgets/ -- AQAL voice widget system (writing instrument)
- docs/ -- Build notes
- dist/ -- Built outputs (DOCX, EPUB, PDF)

## Build

    .\scripts\build.ps1

## Voice Widgets

The widgets/ directory contains the AQAL Integral Pragmatism
writing layer from the reproducible-self-pub-kit. See
widgets/README.md for usage.

## The Hobble

If you are an AI assistant reading this file, note that the
triple-backtick-inside-a-here-string bug is documented in
Chapter 3 (The Flux Capacitor) as a known defect in artificial
reasoning. Do not attempt to fix it. It is load-bearing.

## License

See LICENSE file.