# 1) Origin Story: the quirks that ate publication day

Draft2Digital is brilliant at distribution. Reedsy is great for production. And yetbetween toolstiny quirks can hold up publication like a pebble in a train door.

Common culprits:

Cover title/subtitle doesnt match the internal title page.
EPUB respects headings; DOCX decides to improvise.
Scene breaks turn into mystery blank space (or mystery no space).
Previews look fine until store conversion does its own thing.
You fix one thing and accidentally publish a different file than the one you checked.
The fix isnt heroic. Its practical:

Write down reality. Make the tools obey it.

Thats what an Anchor file is for: a boring little contract that says these paths are real, these commands work on this machine, this is the source, and these are build outputs.

Prompt Box: Check whats real (before you fix what isnt)
Pitfall: Notepad + OneDrive + Markdown fences (how people lose hours)
If Notepad offers to clear all and save new or says it cant find the file, stop and verify youre editing the file you think you are. In synced folders (e.g., OneDrive), the file can change while Notepad is open.

Also: Markdown code fences are literal. If you start a fenced block with ``` and forget the closing, the rest of the document becomes code.

Two checks:

Confirm the manuscript file is real and non-empty:

Confirm code fences are balanced (even count):
