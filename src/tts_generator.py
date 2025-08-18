from gtts import gTTS
import os
from config import OUTPUT_DIR, TTS_LANG

def text_to_speech(text: str, filename="explanation.mp3"):
    path = os.path.join(OUTPUT_DIR, "audio", filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tts = gTTS(text=text, lang=TTS_LANG)
    tts.save(path)
    return path
