from moviepy.editor import * # type: ignore
from moviepy.video.tools.subtitles import SubtitlesClip
import random
import subreddit
print("Found Subreddit post!")

import tts_audio
print("Finished Composing Audio!")

n = random.randint(1,2)

def videoEditing():
    #Collecting Video and Audio files
    videoclip = VideoFileClip(f"videos/example_{n}.mp4")
    audioclip = AudioFileClip("audios/spedup.mp3")

    #Merging audio with video
    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip

    audio_duration = audioclip.duration
    #Subtitles generator
    generator = lambda txt: TextClip(txt, font=r'fonts/Burbank Big Condensed Black.otf', fontsize=100, color='white', method="caption", stroke_color="black", stroke_width=4, size=(1080, None))
    subs = SubtitlesClip('spedup.srt', generator)
    subtitles = SubtitlesClip(subs, generator)
    sub_clip = CompositeVideoClip([videoclip, subtitles.set_pos(('center','center'))])
    #Cropping the video
    sub_clip = sub_clip.subclip(0, audio_duration)
    sub_clip.write_videofile("videos/export.mp4", codec="libx264")
    print("Your video is ready!")

videoEditing()

import instagram_automation