import re
from pathlib import Path
from elevenlabs.client import ElevenLabs
from elevenlabs import save

API_KEY  = "sk_7895340258df580e23af2deea22f2a304ac3c209f0b8a9c6"
VOICE_ID = "qagNgSjYmMZcUoy5Zp4J"
MODEL    = "eleven_multilingual_v2"

CHAPTERS = [
    ("chapters/DoughForge Novel Ch1.md",  "outputs/audio_ch1.mp3"),
    ("chapters/DoughForge Novel Ch2.md",  "outputs/audio_ch2.mp3"),
    ("chapters/DoughForge Novel Ch3.md",  "outputs/audio_ch3.mp3"),
    ("chapters/DoughForge Novel Ch4.md",  "outputs/audio_ch4.mp3"),
    ("chapters/DoughForge Novel Ch5.md",  "outputs/audio_ch5.mp3"),
    ("chapters/DoughForge Novel Ch6.md",  "outputs/audio_ch6.mp3"),
    ("chapters/DoughForge Novel Ch7.md",  "outputs/audio_ch7.mp3"),
    ("chapters/DoughForge Novel Ch8.md",  "outputs/audio_ch8.mp3"),
    ("chapters/DoughForge Novel Epilogue.md", "outputs/audio_epilogue.mp3"),
]

def clean(text: str) -> str:
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"`[^`]+`", "", text)
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^---+$", "", text, flags=re.MULTILINE)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

client = ElevenLabs(api_key=API_KEY)
Path("outputs").mkdir(exist_ok=True)

for src_path, out_path in CHAPTERS:
    src = Path(src_path)
    if not src.exists():
        print(f"SKIP (not found): {src_path}")
        continue
    narration = clean(src.read_text(encoding="utf-8"))
    print(f"Sending {len(narration.split()):,} words → {out_path}")
    audio = client.text_to_speech.convert(
        text          = narration,
        voice_id      = VOICE_ID,
        model_id      = MODEL,
        output_format = "mp3_44100_128",
    )
    save(audio, out_path)
    print(f"  Saved ✓")

print("\nAll done.")
