import gtts
from pydub import AudioSegment
from pydub.effects import speedup
import whisper
from whisper.utils import get_writer

with open ("randompost.txt", encoding='utf-8') as randomposts:
    posts = randomposts.read()

tts = gtts.gTTS(str(posts), lang="en-us", tld="us")

tts.save('test.mp3')

sound = AudioSegment.from_mp3("test.mp3")
sound = speedup(seg=sound, playback_speed=1.2)
sound.export("videos/spedup.mp3", format="mp3")  

model = whisper.load_model("base")
result = model.transcribe("videos/spedup.mp3")

srt_writer = get_writer(output_format="srt", output_dir="C:/Users/dmneh/Desktop/ADHDTrap/")
srt_writer(result, "C:/Users/dmneh/Desktop/ADHDTrap/videos/spedup.mp3")