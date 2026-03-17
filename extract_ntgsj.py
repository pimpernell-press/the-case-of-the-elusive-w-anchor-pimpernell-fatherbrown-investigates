import json
import csv
from pathlib import Path
from bs4 import BeautifulSoup
from datetime import datetime

POSTS_DIR  = Path(r"C:\Users\peewe\OneDrive\Desktop\Roger Books\notthegrubstreetjournal.com\wp-json\wp\v2\posts")
OUTPUT_CSV = Path(r"C:\Users\peewe\OneDrive\Desktop\the-case-of-the-elusive-w-anchor-pimpernell-fatherbrown-investigates\reservoir\ntgsj_index.csv")
OUTPUT_DIR = Path(r"C:\Users\peewe\OneDrive\Desktop\the-case-of-the-elusive-w-anchor-pimpernell-fatherbrown-investigates\reservoir\ntgsj_posts")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)

rows = []

for json_file in sorted(POSTS_DIR.glob("*.json")):
    with open(json_file, encoding="utf-8") as f:
        try:
            post = json.load(f)
        except json.JSONDecodeError:
            continue

    post_id  = post.get("id", "")
    title    = post.get("title", {}).get("rendered", "")
    date_raw = post.get("date", "")
    status   = post.get("status", "")
    link     = post.get("link", "")
    excerpt  = BeautifulSoup(post.get("excerpt", {}).get("rendered", ""), "html.parser").get_text(strip=True)[:300]
    content  = BeautifulSoup(post.get("content", {}).get("rendered", ""), "html.parser").get_text(strip=True)

    try:
        date_obj = datetime.fromisoformat(date_raw)
        date_str = date_obj.strftime("%Y-%m-%d")
        year     = date_obj.year
    except:
        date_str = date_raw[:10]
        year     = date_raw[:4]

    in_gap = "YES" if "2020-06-03" <= date_str <= "2022-07-21" else "no"

    rows.append({"id": post_id, "date": date_str, "year": year, "in_gap": in_gap,
                 "title": title, "status": status, "excerpt": excerpt, "link": link})

    md_filename = OUTPUT_DIR / f"{date_str}_{post_id}.md"
    with open(md_filename, "w", encoding="utf-8") as md:
        md.write(f"# {title}\n\n**Date:** {date_str}  \n**ID:** {post_id}  \n**URL:** {link}  \n\n---\n\n{content}")

rows.sort(key=lambda x: x["date"])

with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["id","date","year","in_gap","title","status","excerpt","link"])
    writer.writeheader()
    writer.writerows(rows)

print(f"Indexed {len(rows)} posts -> {OUTPUT_CSV}")
print(f"Markdown files -> {OUTPUT_DIR}")
gap_posts = [r for r in rows if r["in_gap"] == "YES"]
print(f"Gap period posts found in JSON: {len(gap_posts)}")
if rows:
    print(f"Date range: {rows[0]['date']} -> {rows[-1]['date']}")
