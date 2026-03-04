# 7) Quick timeline + firstship checklist

Getting to shipped is mostly reducing avoidable surprises.

A sane timeline (pamphlet edition)
Write in the canonical Markdown
Build PDF/EPUB/DOCX locally
Spot-check the usual failure points
Commit the changes that produced the shippable build
Upload/distribute
Tag the release (optional, but helpful)
firstship checklist (fast, not fancy)
Content sanity

Title/subtitle/author match YAML and cover
Contents list matches headings (or is clearly manual and accurate)
No accidental everything is code sections (unclosed fences)
Build sanity

PDF opens, fonts look normal, headings look right
EPUB opens in at least one reader (Calibre is fine)
DOCX opens and headings are real headings (not bold paragraphs)
Common output gotchas

Scene breaks are consistent (pick one style and stick to it)
Images (if any) render and are correctly sized
Smart punctuation renders cleanly (XeLaTeX usually behaves)
The two-minute preview rule
If you only have two minutes, check:

the title/first page
the contents/nav
one code block
one major section break
Most disasters show up right there.
