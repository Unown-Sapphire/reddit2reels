from moviepy.editor import * # type: ignore
from moviepy.video.tools.subtitles import SubtitlesClip

import subreddit
print("Found Subreddit post!")

import tts_audio
print("Finished Composing Audio!")

def videoEditing():
    #Collecting Video and Audio files
    videoclip = VideoFileClip("videos/example.mp4")
    audioclip = AudioFileClip("videos/spedup.mp3")

    #Merging audio with video
    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip

    audio_duration = audioclip.duration
    #Subtitles generator
    generator = lambda txt: TextClip(txt, font='Arial', fontsize=80, color='white', method="caption", stroke_color="black", stroke_width=2, size=(1080, None))
    subs = SubtitlesClip('spedup.srt', generator)
    subtitles = SubtitlesClip(subs, generator)
    sub_clip = CompositeVideoClip([videoclip, subtitles.set_pos(('center','center'))])
    #Cropping the video
    sub_clip = sub_clip.subclip(0, audio_duration)
    sub_clip.write_videofile("videos/export.mp4", codec="libx264")
    print("Your video is ready!")

videoEditing()