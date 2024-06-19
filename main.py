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
    videoclip = VideoFileClip(f"videos/example_2.mp4")
    audioclip = AudioFileClip("audios/spedup.mp3")

    #Merging audio with video
    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    
    audio_duration = audioclip.duration
    r_time = random.randint(1, round(audio_duration))
    videoclip.save_frame("images/frame.png", t=r_time)
    
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

def split_video():
    audio_clip = AudioFileClip("audios/spedup.mp3")
    audio_duration = audio_clip.duration
    video_file = VideoFileClip("videos/export.mp4")

    if audio_duration <= 60:
        pass
    elif audio_duration > 60 and audio_duration <=120:
        n = 0
        m = 1
        while n <= 120:
            if n == 60 and m == 2:
                sub_clip = video_file.subclip(60, audio_duration)
                sub_clip = CompositeVideoClip([sub_clip])
                sub_clip.write_videofile(f"videos/video_parts/test_{m}.mp4", codec="libx264")
                break
            else:
                sub_clip = video_file.subclip(0, n+60)
                sub_clip = CompositeVideoClip([sub_clip])
                sub_clip.write_videofile(f"videos/video_parts/test_{m}.mp4", codec="libx264")
                n += 60
                m += 1   
    elif audio_duration > 120 and audio_duration <=180:
        n = 0
        m = 1
        while n <= 180:
            if n == 120 and m == 3:
                sub_clip = video_file.subclip(60, audio_duration)
                sub_clip = CompositeVideoClip([sub_clip])
                sub_clip.write_videofile(f"videos/video_parts/test_{m}.mp4", codec="libx264")
                break
            else:
                sub_clip = video_file.subclip(0, n+60)
                sub_clip = CompositeVideoClip([sub_clip])
                sub_clip.write_videofile(f"videos/video_parts/test_{m}.mp4", codec="libx264")
                n += 60
                m += 1   
    elif audio_duration > 180 and audio_duration <=240:
        n = 0
        m = 1
        while n <= 240:
            if n == 180 and m == 4:
                sub_clip = video_file.subclip(60, audio_duration)
                sub_clip = CompositeVideoClip([sub_clip])
                sub_clip.write_videofile(f"videos/video_parts/test_{m}.mp4", codec="libx264")
                break
            else:
                sub_clip = video_file.subclip(0, n+60)
                sub_clip = CompositeVideoClip([sub_clip])
                sub_clip.write_videofile(f"videos/video_parts/test_{m}.mp4", codec="libx264")
                n += 60
                m += 1   

    elif audio_duration > 240 and audio_duration <=300:
        n = 0
        m = 1
        while n <= 300:
            if n == 240 and m == 5:
                sub_clip = video_file.subclip(60, audio_duration)
                sub_clip = CompositeVideoClip([sub_clip])
                sub_clip.write_videofile(f"videos/video_parts/test_{m}.mp4", codec="libx264")
                break
            else:
                sub_clip = video_file.subclip(0, n+60)
                sub_clip = CompositeVideoClip([sub_clip])
                sub_clip.write_videofile(f"videos/video_parts/test_{m}.mp4", codec="libx264")
                n += 60
                m += 1   
split_video()

import generator

import instagram_automation