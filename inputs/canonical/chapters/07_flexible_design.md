# 6) Flexible by design: kids books  technical  academic

Different writers have different habits. Good. The workflow should adapt without breaking.

This kit is deliberately permissive:

write in Markdown from an LLM, a text editor, Obsidian, VS Code, Notepadwhatever
keep structure simple: headings, lists, blockquotes, code fences
avoid format-fragile tricks that only one output understands
A safe subset of Markdown for predictable builds
Use freely:

/ ## / ### headings
bullet/numbered lists
blockquotes (>)
code fences (triple backticks)
emphasis (italic, bold)
links
Be cautious with:

raw HTML for layout (varies by output)
manual spacing tricks (multiple blank lines; renderers differ)
forcing pagination for EPUB/DOCX (they dont have pages in the same way)
Formatting philosophy (for tired humans)
If you cant explain why a formatting trick exists in one sentence, it doesnt belong in the canonical manuscript.
