#!/usr/bin/env python3
"""Parse Going Direct Paradigm Brain export and build chapter-node dashboard."""
import json, sys, io, os
from collections import defaultdict, Counter

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

BRAIN_DIR = r'C:\Users\peewe\Documents\DoughForge\assets\going_direct_paradigm'
OUT_DIR = r'C:\Users\peewe\OneDrive\Desktop\the-case-of-the-elusive-w-anchor-pimpernell-fatherbrown-investigates\docs'

def load_jsonl(path):
    items = []
    with open(path, encoding='utf-8-sig') as f:
        for line in f:
            line = line.strip()
            if line:
                items.append(json.loads(line))
    return items

# Load
thoughts = load_jsonl(os.path.join(BRAIN_DIR, 'thoughts.json'))
links = load_jsonl(os.path.join(BRAIN_DIR, 'links.json'))
attachments = load_jsonl(os.path.join(BRAIN_DIR, 'attachments.json'))

thought_map = {t['Id']: t['Name'] for t in thoughts}

# Build graph
children = defaultdict(list)
parents = defaultdict(list)
jumps = defaultdict(list)

for l in links:
    a, b = l['ThoughtIdA'], l['ThoughtIdB']
    kind = l.get('Kind', 0)
    direction = l.get('Direction', 0)
    if kind == 1:
        if direction == 1:
            children[a].append(b)
            parents[b].append(a)
        else:
            children[b].append(a)
            parents[a].append(b)
    elif kind == 3:
        jumps[a].append(b)
        jumps[b].append(a)

attach_count = defaultdict(int)
for a in attachments:
    attach_count[a.get('SourceId', '')] += 1

# Chapter themes
chapter_themes = {
    'ch01': {'kw': ['wankel', 'rotary', 'domain', 'redirect', 'credibility', 'dns'], 'title': 'Ever Had a Wankel?', 'act': 'I'},
    'ch02': {'kw': ['fair', 'index', 'plagiar', 'equation', 'reverse', 'narrowboat', 'economist'], 'title': 'The Globe', 'act': 'I'},
    'ch03': {'kw': ['doughforge', 'generate', 'kill', 'gk', 'chesterton', 'father brown', 'forensic'], 'title': 'Monica and the GK Spot', 'act': 'I'},
    'ch04': {'kw': ['gradient', 'mentor', 'betray', 'first edition', 'venture capital', 'fund'], 'title': 'Candida, Tobin, Colour', 'act': 'I'},
    'ch05': {'kw': ['algorithm', 'kubla', 'xanadu', 'nelson', 'hypertext', 'transclusion', 'complete'], 'title': 'The Xanadu Problem', 'act': 'II'},
    'ch06': {'kw': ['parliament', 'llm', 'artificial intellig', 'shelley', 'unacknowledged', 'legislat'], 'title': 'The Parliament Responds', 'act': 'II'},
    'ch07': {'kw': ['cryptograph', 'lighthouse', 'cipher', 'letter', 'handwritten', 'mathematics'], 'title': 'The Lighthouse Letters', 'act': 'II'},
    'ch08': {'kw': ['sweden', 'cabin', 'bread', 'sourdough', 'bake', 'solitude', 'dough'], 'title': 'The Swedish Cabin', 'act': 'II'},
    'ch09': {'kw': ['ration', 'anagram', 'financial instrument', 'offshore', 'network', 'werner'], 'title': 'The Ration Still Arriving', 'act': 'III'},
    'ch10': {'kw': ['vandal', 'fix', 'deny', 'complaint', 'institutional', 'regulator', 'ombudsman'], 'title': 'The Helpful Vandal', 'act': 'III'},
    'ch11': {'kw': ['publish', 'evidence', 'w-anchor', 'protocol', 'epub', 'build', 'git', 'format'], 'title': 'The Build That Worked', 'act': 'III'},
    'ch12': {'kw': ['verdict', 'guilty', 'penance', 'prison', 'system', 'record', 'justice', 'crime'], 'title': 'The Verdict', 'act': 'III'},
}

# Match thoughts to chapters
chapter_nodes = defaultdict(lambda: {'primary': [], 'secondary': []})
matched = set()

for t in thoughts:
    nl = t['Name'].lower()
    tid = t['Id']
    for ch, info in chapter_themes.items():
        for kw in info['kw']:
            if kw in nl:
                chapter_nodes[ch]['primary'].append(tid)
                matched.add(tid)
                break

# Secondary: children of primary
for ch in chapter_themes:
    for pid in chapter_nodes[ch]['primary']:
        for cid in children.get(pid, []):
            if cid not in matched:
                chapter_nodes[ch]['secondary'].append(cid)
                matched.add(cid)

orphans = [t for t in thoughts if t['Id'] not in matched]

# Categorise all thoughts
categories = {
    'monetary': ['money', 'credit', 'bank', 'debt', 'interest', 'monetary', 'currency', 'central bank', 'bis', 'basel', 'usury'],
    'housing': ['housing', 'home', 'mortgage', 'affordable', 'builder', 'potton', 'fair-index', 'timber', 'custom build'],
    'political': ['oligarch', 'government', 'parliament', 'democracy', 'politic', 'power', 'state', 'regime', 'war'],
    'technology': ['ai', 'digital', 'internet', 'blockchain', 'algorithm', 'software', 'tech', 'data'],
    'philosophy': ['peirce', 'tarski', 'ruskin', 'wilber', 'aqal', 'consciousness', 'philosophy', 'truth'],
    'literary': ['blake', 'shelley', 'coleridge', 'poem', 'poetry', 'dough', 'conquest', 'grub street'],
    'economics': ['econom', 'gdp', 'inflation', 'market', 'trade', 'capital', 'wealth', 'price'],
}

cat_counts = {}
for cat, kws in categories.items():
    count = 0
    for t in thoughts:
        nl = t['Name'].lower()
        if any(kw in nl for kw in kws):
            count += 1
    cat_counts[cat] = count

# Write Node Index
with open(os.path.join(OUT_DIR, 'procurement_engine_node_index.md'), 'w', encoding='utf-8') as f:
    f.write('# Going Direct Paradigm — Chapter-Node Index\n\n')
    f.write('**Source:** DoughForge/assets/going_direct_paradigm/ (TheBrain JSONL export)\n')
    f.write(f'**Thoughts:** {len(thoughts)} | **Links:** {len(links)} | **Attachments:** {len(attachments)}\n')
    f.write(f'**Date:** 2026-03-25\n\n')
    f.write('> **NOTE:** The 12 chapters in wandering-anchor-book/manuscripts/chapters/ are\n')
    f.write('> the **Wandering Anchor novel** (Roger Merryweather, Hannah Shandy, Father Brown),\n')
    f.write('> not Home@ix business case chapters. This index maps the Going Direct Paradigm\n')
    f.write('> intellectual topology to the novel\'s thematic structure.\n\n---\n\n')

    f.write('## Topology Summary\n\n')
    f.write('| Category | Node Count |\n|----------|----------|\n')
    for cat in sorted(cat_counts, key=cat_counts.get, reverse=True):
        f.write(f'| {cat.title()} | {cat_counts[cat]} |\n')
    f.write(f'| Uncategorised | {len(thoughts) - sum(cat_counts.values())} |\n')
    f.write(f'| **Total** | **{len(thoughts)}** |\n\n---\n\n')

    f.write('## Chapter-to-Node Mapping\n\n')
    for ch in sorted(chapter_themes.keys()):
        info = chapter_themes[ch]
        prim = chapter_nodes[ch]['primary']
        sec = chapter_nodes[ch]['secondary']
        att_p = sum(attach_count.get(n, 0) for n in prim)
        f.write(f'### {ch.upper()}: {info["title"]} (Act {info["act"]})\n\n')
        f.write(f'**Primary nodes:** {len(prim)} | **Secondary:** {len(sec)} | **Attachments:** {att_p}\n\n')
        if prim:
            f.write('| Node ID | Name | Children | Attachments |\n')
            f.write('|---------|------|----------|-------------|\n')
            for nid in prim[:15]:
                name = thought_map.get(nid, '?')[:60]
                nc = len(children.get(nid, []))
                na = attach_count.get(nid, 0)
                f.write(f'| `{nid[:12]}` | {name} | {nc} | {na} |\n')
            if len(prim) > 15:
                f.write(f'| ... | *({len(prim)-15} more)* | | |\n')
        else:
            f.write('*No primary nodes matched. Chapter relies on narrative rather than Brain evidence.*\n')
        f.write('\n')

    f.write('---\n\n## Orphan Nodes (Top 30 by attachment count)\n\n')
    f.write('Thoughts with no chapter assignment, ranked by evidence richness.\n\n')
    f.write('| Node ID | Name | Children | Attachments |\n')
    f.write('|---------|------|----------|-------------|\n')
    orphans_sorted = sorted(orphans, key=lambda t: attach_count.get(t['Id'], 0), reverse=True)
    for t in orphans_sorted[:30]:
        name = t['Name'][:60]
        nc = len(children.get(t['Id'], []))
        na = attach_count.get(t['Id'], 0)
        f.write(f'| `{t["Id"][:12]}` | {name} | {nc} | {na} |\n')
    f.write(f'\n**Total orphans:** {len(orphans)} of {len(thoughts)} thoughts ({round(len(orphans)/len(thoughts)*100)}%)\n')

# Write Dashboard
with open(os.path.join(OUT_DIR, 'procurement_engine_dashboard.md'), 'w', encoding='utf-8') as f:
    f.write('# Going Direct Paradigm — Evidence Dashboard\n\n')
    f.write('**Source:** DoughForge/assets/going_direct_paradigm/ (1,675 thoughts, 3,071 links, 1,398 attachments)\n')
    f.write('**Mapped to:** wandering-anchor-book/manuscripts/chapters/ch01-ch12 (Wandering Anchor novel)\n')
    f.write('**Date:** 2026-03-25\n\n')
    f.write('> **NOTE:** Evidence Score = (attachments on primary nodes / primary node count) x 100.\n')
    f.write('> A score of 100% means every primary node has at least one attachment (PDF, URL, document).\n\n')

    f.write('| Ch | Act | Title | Primary | Secondary | Attachments | Evidence Score |\n')
    f.write('|----|-----|-------|---------|-----------|-------------|----------------|\n')

    total_p = total_s = total_a = 0
    for ch in sorted(chapter_themes.keys()):
        info = chapter_themes[ch]
        prim = chapter_nodes[ch]['primary']
        sec = chapter_nodes[ch]['secondary']
        att_p = sum(attach_count.get(n, 0) for n in prim)
        ev = round(att_p / max(len(prim), 1) * 100)
        total_p += len(prim)
        total_s += len(sec)
        total_a += att_p
        f.write(f'| {ch[2:]} | {info["act"]} | {info["title"][:35]} | {len(prim)} | {len(sec)} | {att_p} | {ev}% |\n')

    total_ev = round(total_a / max(total_p, 1) * 100)
    f.write(f'| **ALL** | | **TOTAL** | **{total_p}** | **{total_s}** | **{total_a}** | **{total_ev}%** |\n')

    f.write(f'\n**Coverage:** {len(matched)} of {len(thoughts)} thoughts mapped ({round(len(matched)/len(thoughts)*100)}%)\n')
    f.write(f'**Orphans:** {len(orphans)} thoughts with no chapter assignment ({round(len(orphans)/len(thoughts)*100)}%)\n')

    f.write('\n---\n\n## Gap Analysis\n\n')
    f.write('### Chapters with weak evidence backing\n\n')
    for ch in sorted(chapter_themes.keys()):
        prim = chapter_nodes[ch]['primary']
        if len(prim) < 5:
            f.write(f'- **{ch.upper()}** ({chapter_themes[ch]["title"]}): only {len(prim)} primary nodes. ')
            f.write('Chapter narrative exceeds Brain evidence.\n')

    f.write('\n### High-value orphan clusters\n\n')
    f.write('These orphan nodes have significant attachments but no chapter home:\n\n')
    for t in orphans_sorted[:10]:
        na = attach_count.get(t['Id'], 0)
        if na > 0:
            f.write(f'- **{t["Name"][:60]}** ({na} attachments)\n')

# Write Brain Import XML
with open(os.path.join(OUT_DIR, 'brain_import_procurement_layer.xml'), 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<BrainData>\n')
    f.write('  <!-- TheBrain Import: Book Structure Layer -->\n')
    f.write('  <!-- Adds chapter parent thoughts linked to existing Going Direct Paradigm nodes -->\n')
    f.write('  <!-- Import this WITHOUT replacing existing data -->\n\n')

    # Book root thought
    f.write('  <Thought>\n')
    f.write('    <Name>Wandering Anchor — Book Structure</Name>\n')
    f.write('    <Id>book-structure-root</Id>\n')
    f.write('    <Kind>1</Kind>\n')
    f.write('  </Thought>\n\n')

    for ch in sorted(chapter_themes.keys()):
        info = chapter_themes[ch]
        ch_id = f'book-{ch}'
        f.write(f'  <Thought>\n')
        f.write(f'    <Name>{ch.upper()}: {info["title"]}</Name>\n')
        f.write(f'    <Id>{ch_id}</Id>\n')
        f.write(f'    <Kind>1</Kind>\n')
        f.write(f'  </Thought>\n')

        # Link chapter to book root
        f.write(f'  <Link>\n')
        f.write(f'    <ThoughtIdA>book-structure-root</ThoughtIdA>\n')
        f.write(f'    <ThoughtIdB>{ch_id}</ThoughtIdB>\n')
        f.write(f'    <Kind>1</Kind>\n')
        f.write(f'    <Relation>1</Relation>\n')
        f.write(f'    <Direction>1</Direction>\n')
        f.write(f'  </Link>\n')

        # Link chapter to primary nodes (as jump links to preserve existing topology)
        for nid in chapter_nodes[ch]['primary'][:20]:
            f.write(f'  <Link>\n')
            f.write(f'    <ThoughtIdA>{ch_id}</ThoughtIdA>\n')
            f.write(f'    <ThoughtIdB>{nid}</ThoughtIdB>\n')
            f.write(f'    <Kind>3</Kind>\n')
            f.write(f'    <Meaning>Book chapter reference</Meaning>\n')
            f.write(f'  </Link>\n')
        f.write('\n')

    f.write('</BrainData>\n')

print('=== FILES WRITTEN ===')
print(f'  {os.path.join(OUT_DIR, "procurement_engine_node_index.md")}')
print(f'  {os.path.join(OUT_DIR, "procurement_engine_dashboard.md")}')
print(f'  {os.path.join(OUT_DIR, "brain_import_procurement_layer.xml")}')
print(f'\nDashboard summary:')
print(f'  Thoughts: {len(thoughts)}')
print(f'  Mapped: {len(matched)} ({round(len(matched)/len(thoughts)*100)}%)')
print(f'  Orphans: {len(orphans)} ({round(len(orphans)/len(thoughts)*100)}%)')
