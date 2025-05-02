from gtts import gTTS
import os

# Example learning content
text = "This is your subconscious learning audio content. Relax and absorb the knowledge."

# Convert to speech
tts = gTTS(text)
os.makedirs("audio", exist_ok=True)
tts.save("audio/learning_audio.mp3")
print("✅ Audio saved as audio/learning_audio.mp3")
