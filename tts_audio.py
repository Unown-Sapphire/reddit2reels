import gtts
from pydub import AudioSegment
from pydub.effects import speedup
import whisper
from whisper.utils import get_writer

with open ("randompost.txt", encoding='utf-8') as randomposts:
    posts = randomposts.read()

tts = gtts.gTTS(str(posts), lang="en-us", tld="us")

tts.save('test.mp3')
print("Saved Normal Audio")

sound = AudioSegment.from_mp3("test.mp3")
sound = speedup(seg=sound, playback_speed=1.2)
sound.export("videos/spedup.mp3", format="mp3")  

print('Saved Speeded up version of audio')

word_options = {
    "max_line_count": 1,
    "max_line_width": 20
}

model = whisper.load_model('base')
audio = whisper.load_audio("videos/spedup.mp3")
result = whisper.transcribe(model, audio, word_timestamps=True)

# Save as an SRT file
srt_writer = get_writer("srt", ".")
srt_writer(result, "videos/spedup.mp3", {"max_words_per_line":3})