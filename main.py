from moviepy.editor import * # type: ignore
from moviepy.video.tools.subtitles import SubtitlesClip

import subreddit
print("Wow1")
import tts_audio
print("Wow2")

def videoEditing():
    videoclip = VideoFileClip("videos/example.mp4")
    audioclip = AudioFileClip("videos/spedup.mp3")

    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip

    sub_clip = videoclip.subclip(0, 64) #crops the clip from 0 to 100 seconds
    generator = lambda txt: TextClip(txt, font='Arial', fontsize=24, color='white')
    subs = SubtitlesClip('spedup.srt', generator)
    subtitles = SubtitlesClip(subs, generator)
    sub_clip = CompositeVideoClip([videoclip, subtitles.set_pos(('center','bottom'))])
    sub_clip.write_videofile("videos/export.mp4")
    print("Wow3")

videoEditing()
 