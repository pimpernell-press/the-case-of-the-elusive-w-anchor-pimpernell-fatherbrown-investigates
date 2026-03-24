import re
from pathlib import Path
from elevenlabs.client import ElevenLabs
from elevenlabs import save

# ── CONFIG ──────────────────────────────────────────────────────────────
API_KEY   = "sk_5dd269a2307f67c0549a247d55a7be6435e94949918ca7eb"
VOICE_ID  = "qagNgSjYmMZcUoy5Zp4J"
MODEL     = "eleven_multilingual_v2"
OUTPUT    = Path("outputs/audiobook_sample_ch1.mp3")
WORD_CAP  = 500
# ────────────────────────────────────────────────────────────────────────

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

def cap_words(text: str, n: int) -> str:
    if n <= 0:
        return text
    words = text.split()
    return " ".join(words[:n])

src = Path("chapters/DoughForge Novel Ch1.md")
raw = src.read_text(encoding="utf-8")
narration = clean(raw)
if WORD_CAP:
    narration = cap_words(narration, WORD_CAP)

print(f"Sending {len(narration.split())} words to ElevenLabs...")

client = ElevenLabs(api_key=API_KEY)
audio  = client.text_to_speech.convert(
    text          = narration,
    voice_id      = VOICE_ID,
    model_id      = MODEL,
    output_format = "mp3_44100_128",
)

OUTPUT.parent.mkdir(exist_ok=True)
save(audio, str(OUTPUT))
print(f"Saved → {OUTPUT}")
