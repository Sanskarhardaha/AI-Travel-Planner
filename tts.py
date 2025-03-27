from gtts import gTTS
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def text_to_speech(text, filename="output.mp3"):
    """Convert text to speech using Google gTTS and save as an MP3 file."""
    try:
        tts = gTTS(text=text, lang="en")
        tts.save(filename)
        return filename
    except Exception as e:
        print(f"Error generating speech: {e}")
        return None
