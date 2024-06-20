from moviepy.editor import * # type: ignore
from moviepy.video.tools.subtitles import SubtitlesClip
import random

def chunks(L, n):
    for i in range(0, len(L), n):
        yield L[i:i+n]  

with open('spedup copy.srt', "r+", encoding="utf-8") as srtfile:
    text = "Today I fucked up by testing to see if anyone in my office actually wanted to talk to me."
    srttext = srtfile.read()
    splitchunks = list(chunks(text.split(" "),3))
    splitsrtchunks = list(chunks(srttext.split("\n"),4))
    indexlist = []
    for x in splitchunks:
        xindex = splitchunks.index(x)
        splitchunks[xindex] =  " ".join(x).rstrip()
    for chunk,y in zip(splitsrtchunks,splitchunks):
        for x in chunk:
            if x == y:
                indexlist.append(chunk)
    length = len(indexlist)
    while length > 0:
        for x in indexlist:
            splitsrtchunks.pop(0)
            length -= 1
    srtfile.truncate(0)
    srtfile.seek(0)
    for x in splitsrtchunks:
        element = "\n".join(x)
        element = f"{element} \n"
        srtfile.write(element)
    time = ((indexlist[-1])[1].split("-->"))[-1].split(":")[-1].strip("0").replace(",",".")
    
        
            

def videoEditing():
    #Collecting Video and Audio files
    videoclip = VideoFileClip(f"videos/example_2.mp4")
    audioclip = AudioFileClip("audios/spedup.mp3")

    #Merging audio with video
    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    img_clip = ImageClip("images/output.png").set_start(0).set_duration(7).resize(height=328, width=864).set_pos(("center","top"))

    audio_duration = audioclip.duration
    #Subtitles generator
    generator = lambda txt: TextClip(txt, font=r'fonts/Burbank Big Condensed Black.otf', fontsize=100, color='white', method="caption", stroke_color="black", stroke_width=4, size=(1080, None))
    subs = SubtitlesClip('spedup.srt', generator)
    subtitles = SubtitlesClip(subs, generator)
    sub_clip = CompositeVideoClip([videoclip, subtitles.set_pos(('center','center')), img_clip])
    #Cropping the video
    sub_clip = sub_clip.subclip(0, audio_duration)
    sub_clip.write_videofile("videos/test.mp4", codec="libx264")
    print(f"Your video is ready!")

