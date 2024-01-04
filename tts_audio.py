import gtts
from playsound import playsound

with open ("randompost.txt") as randomposts:
    posts = randomposts.read()

posts = posts.split("\n")
tts = gtts.gTTS(posts[2], lang="en-us")
tts.save("test.mp3")
playsound("test.mp3")