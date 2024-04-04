import elevenlabs
from elevenlabs import generate, play
import os
from dotenv import load_dotenv

# Load API keys
load_dotenv()
elevenlabs.set_api_key(os.getenv("ELEVENLABS_API_KEY"))

audio = generate(
    text="何か話そうよ！",
    voice="天月",
    model="eleven_multilingual_v2"
)
play(audio)