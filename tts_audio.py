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

model = whisper.load_model("base")
result = model.transcribe("videos/spedup.mp3")

srt_writer = get_writer(output_format="srt", output_dir=r"C:\Users\dmneh\Desktop\ADHDTrap")
srt_writer(result, "ADHDTrap/videos/spedup.mp3")