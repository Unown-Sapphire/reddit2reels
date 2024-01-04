import gtts
import itertools
from playsound import playsound

with open ("randompost.txt") as randomposts:
    posts = randomposts.read()

posts = posts.split("\n")

lines = []
lineNo = 0


for line_num, line in itertools.zip_longest(posts, lines):
    lines.append(line_num)
    if line != "":
        tts = gtts.gTTS(lines[lineNo], lang="en-us", tld="us")
        lineNo += 1
        print("Next line")
    else:
        print("seems to be a blank line :()")
        continue       
tts.save("test.mp3")