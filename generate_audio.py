import os
import sys
import asyncio
import edge_tts

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

language = "English"

if os.path.exists("temp_language.txt"):
    with open("temp_language.txt", "r", encoding="utf-8") as f:
        language = f.read().strip()
        
print("Selected Language:", language)

script_path = "data/scripts/latest_script.txt"

if not os.path.exists(script_path):
    raise FileNotFoundError(
        f"Script not found: {script_path}"
    )

with open(script_path, "r", encoding="utf-8") as f:
    text = f.read()

print(f"Using script: {script_path}")

os.makedirs("audio", exist_ok=True)

from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

OUTPUT_FILE = f"audio/news_audio_{timestamp}.mp3"
VOICE_MAP = {
    "English": "en-IN-NeerjaNeural",
    "Hindi": "hi-IN-SwaraNeural",
    "Bengali": "bn-IN-TanishaaNeural",
    "Tamil": "ta-IN-PallaviNeural"
}

VOICE = VOICE_MAP.get(
    language,
    "en-IN-NeerjaNeural"
)

print("Selected Voice:", VOICE)

async def generate():
    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE,
        rate="+20%"
    )

    await communicate.save(OUTPUT_FILE)
    
    with open("latest_audio.txt", "w") as f:
        f.write(OUTPUT_FILE)

    print("Saved audio:", OUTPUT_FILE)



asyncio.run(generate())