import gtts
<<<<<<< HEAD
import ffmpeg_downloader 
from pydub import AudioSegment
from pydub.effects import speedup
=======
import subreddit
>>>>>>> d66bd2d2fc1ae05dbb92b32f76dc4b10a362efe9

with open ("randompost.txt", encoding='utf-8') as randomposts:
    posts = randomposts.read()

tts = gtts.gTTS(str(posts), lang="en-us", tld="us")

tts.save('test.mp3')

sound = AudioSegment.from_mp3("test.mp3")
sound.save("videos/export.wav", format="wav")