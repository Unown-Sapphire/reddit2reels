import gtts
import ffmpeg_downloader 
from pydub import AudioSegment
from pydub.effects import speedup
import subreddit

with open ("randompost.txt", encoding='utf-8') as randomposts:
    posts = randomposts.read()

tts = gtts.gTTS(str(posts), lang="en-us", tld="us")

tts.save('test.mp3')

sound = AudioSegment.from_mp3("test.mp3")
sound.save("videos/export.wav", format="wav")