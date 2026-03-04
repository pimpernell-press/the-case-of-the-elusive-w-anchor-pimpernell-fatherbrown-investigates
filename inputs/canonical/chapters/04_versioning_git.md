# 3) Versioning with Git: stop selling yourself work you already did

Git is not here to turn you into a developer. Its here to prevent these disasters:

I fixed it yesterday. Where did it go?
Which draft did I upload?
I changed one tiny thing and now everything is different.
I need the previous subtitle back. The good one.
The writer-friendly Git minimum
You can get 90% of the value with three commands:

Thats it. No branching epic required.

What to commit (a sensible default)
Commit:

manuscripts (publication/*.md)
Anchor + logs (ANCHOR.md, publication/INTERIM_PROGRESS_LOG.md)
build scripts (tools/*)
templates/styles you own (if any)
referenced images
Avoid committing:

generated outputs (outputs/*) unless you explicitly want release artifacts in the repo
If you do commit outputs, do it deliberately (and ideally in a separate commit) so history stays readable.

A good commit message formula
Use: verb + object + reason

Examples:

Add epigraph and replace HTML breaks with \newpage
Clarify Anchor contract and add build checks
Fix heading levels to improve EPUB navigation
Your future self doesnt need poetry. They need context.
