import gtts
import subreddit

with open ("randompost.txt", encoding='utf-8') as randomposts:
    posts = randomposts.read()

tts = gtts.gTTS(str(posts), lang="en-us", tld="us")

tts.save('test.mp3')