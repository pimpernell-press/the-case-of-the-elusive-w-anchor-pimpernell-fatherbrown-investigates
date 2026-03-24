"""
build_audio_catalogue.py  -  Build audio for a single catalogue book.
Automatically chunks chapters that exceed ElevenLabs 10,000 char limit.
"""
import re
import os
from pathlib import Path
from elevenlabs.client import ElevenLabs
from elevenlabs.core.api_error import ApiError

API_KEY  = os.environ.get("ELEVENLABS_API_KEY", "sk_7895340258df580e23af2deea22f2a304ac3c209f0b8a9c6")
VOICE_ID = "qagNgSjYmMZcUoy5Zp4J"
MODEL    = "eleven_multilingual_v2"
MAX_CHARS = 9500

BOOK_SLUG    = "philosoetry"
CHAPTERS_DIR = Path("C:/Users/peewe/Documents/DoughForge/chapters/catalogue/philosoetry")
AUDIO_DIR    = Path("C:/Users/peewe/Documents/DoughForge/outputs/audio/philosoetry")
AUDIO_DIR.mkdir(parents=True, exist_ok=True)

def clean(text):
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"`[^`]+`", "", text)
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^---+$", "", text, flags=re.MULTILINE)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

def split_chunks(text):
    sentences = re.split(r"(?<=[.!?])\s+", text)
    chunks, current = [], ""
    for sentence in sentences:
        if len(current) + len(sentence) + 1 > MAX_CHARS:
            if current:
                chunks.append(current.strip())
            current = sentence
        else:
            current += (" " if current else "") + sentence
    if current:
        chunks.append(current.strip())
    return chunks

def generate_audio(client, text):
    audio_iter = client.text_to_speech.convert(
        text=text,
        voice_id=VOICE_ID,
        model_id=MODEL,
        output_format="mp3_44100_128",
    )
    return b"".join(audio_iter)

client   = ElevenLabs(api_key=API_KEY)
chapters = sorted(CHAPTERS_DIR.glob("ch*.md"))
print(f"Found {len(chapters)} chapters in {CHAPTERS_DIR}\n")

for ch in chapters:
    narration = clean(ch.read_text(encoding="utf-8"))
    if len(narration.strip()) < 30:
        print(f"  SKIP (too short): {ch.name}")
        continue
    out = AUDIO_DIR / ch.with_suffix(".mp3").name
    if out.exists():
        print(f"  EXISTS (skip): {out.name}")
        continue
    words = len(narration.split())
    chars = len(narration)
    print(f"  {ch.name}  {words:,} words / {chars:,} chars  ->  {out.name}")
    try:
        if chars <= MAX_CHARS:
            audio_bytes = generate_audio(client, narration)
        else:
            chunks = split_chunks(narration)
            print(f"    Splitting into {len(chunks)} chunks...")
            audio_bytes = b""
            for i, chunk in enumerate(chunks, 1):
                print(f"    Chunk {i}/{len(chunks)} ({len(chunk):,} chars)...", end=" ", flush=True)
                audio_bytes += generate_audio(client, chunk)
                print("done")
        out.write_bytes(audio_bytes)
        print(f"    Saved")
    except ApiError as e:
        if "quota_exceeded" in str(e.body):
            print(f"\n  QUOTA EXCEEDED on {ch.name} -- top up and re-run.")
            break
        else:
            print(f"  ERROR on {ch.name}: {e}")
            break

print(f"\nDone. Audio in {AUDIO_DIR}")
