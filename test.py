from moviepy.editor import * # type: ignore
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.editor import VideoFileClip
import random
from skimage.filters import gaussian
from PIL import Image

def blur(image):
    return gaussian(image.astype(float), sigma=7)

new_list = []

random_title = "AITA for sending my twin daughters to separate schools?"

with open("spedup.srt", "r+", encoding="utf-8") as file:
    file_line = file.readlines(-1)
    for line in file_line:
        x = line.rstrip("\n")
        new_list.append(x)
    for i in new_list:
        if i == '':
            new_list.remove(i)
        else:
            pass
    a = 1
    b = 3

    for i in new_list:
        x = i.rsplit(".")
        for y in x:
            if y == "":
                x.remove(y)
            else:
                continue
        should_break = False    
        for y in x:
            if random_title.endswith(y):
                timing = new_list[a-2]
                print(timing)
                del new_list[0:a]
                a+=1
                should_break = True
                break
            else:
                a+=1
        if should_break:
            break
    time = timing[23:len(timing)]
    time = time.replace(",", ".")
    print(float(time))

    file.truncate(0)
    newer_list = []
    for i in new_list:
        spaced_string = i + "\n"
        newer_list.append(spaced_string)
    for element in newer_list:
        while b < len(newer_list) + 1:
            newer_list.insert(b, "\n")
            b+=4
    file.seek(0)        
    for element in newer_list:
        file.write(element)      

n = random.randint(1,2)

def videoEditing():
    #get audio duration
    audioclip = AudioFileClip("audios/spedup.mp3")
    audio_duration = audioclip.duration
    #Collecting Video and Audio files
    videoclip_blur = VideoFileClip(f"videos/example_2.mp4").subclip(0, time)
    videoclip_blur = videoclip_blur.fl_image(blur)
    videoclip = VideoFileClip(f"videos/example_2.mp4").subclip(time, audio_duration)
    

    #concantate blurred video and video
    videoclip = concatenate_videoclips([videoclip_blur, videoclip])

    #Merging audio with video
    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    #save random point of video screenshot
    r_time = random.randint(1, round(audio_duration))
    videoclip.save_frame("images/frame.png", t=r_time)
    #set image clip pos
    title = Image.open("output.png").convert("RGBA")
    title = title.resize(size=(1026, 389)).save("output.png")
    img_clip = ImageClip("output.png").set_start(0).set_duration(time).set_pos(("center","center"))
    #Subtitles generator
    generator = lambda txt: TextClip(txt, font=r'fonts/Burbank Big Condensed Black.otf', fontsize=100, color='white', method="caption", stroke_color="black", stroke_width=4, size=(1080, None))
    subs = SubtitlesClip('spedup.srt', generator)
    subtitles = SubtitlesClip(subs, generator)
    sub_clip = CompositeVideoClip([videoclip, subtitles.set_pos(('center','center')), img_clip])
    #Cropping the video
    sub_clip = sub_clip.subclip(0, 10)
    sub_clip.write_videofile("videos/export.mp4", codec="libx264", threads=4)
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
                sub_clip.write_videofile(f"videos/test_{m}.mp4", codec="libx264")
                break
            else:
                sub_clip = video_file.subclip(0, n+60)
                sub_clip = CompositeVideoClip([sub_clip])
                sub_clip.write_videofile(f"videos/test_{m}.mp4", codec="libx264")
                n += 60
                m += 1   
    elif audio_duration > 120 and audio_duration <=180:
        n = 0
        m = 1
        while n <= 180:
            if n == 120 and m == 3:
                sub_clip = video_file.subclip(60, audio_duration)
                sub_clip = CompositeVideoClip([sub_clip])
                sub_clip.write_videofile(f"videos/test_{m}.mp4", codec="libx264")
                break
            else:
                sub_clip = video_file.subclip(0, n+60)
                sub_clip = CompositeVideoClip([sub_clip])
                sub_clip.write_videofile(f"videos/test_{m}.mp4", codec="libx264")
                n += 60
                m += 1   
    elif audio_duration > 180 and audio_duration <=240:
        n = 0
        m = 1
        while n <= 240:
            if n == 180 and m == 4:
                sub_clip = video_file.subclip(60, audio_duration)
                sub_clip = CompositeVideoClip([sub_clip])
                sub_clip.write_videofile(f"videos/test_{m}.mp4", codec="libx264")
                break
            else:
                sub_clip = video_file.subclip(0, n+60)
                sub_clip = CompositeVideoClip([sub_clip])
                sub_clip.write_videofile(f"videos/test_{m}.mp4", codec="libx264")
                n += 60
                m += 1   

    elif audio_duration > 240 and audio_duration <=300:
        n = 0
        m = 1
        while n <= 300:
            if n == 240 and m == 5:
                sub_clip = video_file.subclip(60, audio_duration)
                sub_clip = CompositeVideoClip([sub_clip])
                sub_clip.write_videofile(f"videos/test_{m}.mp4", codec="libx264")
                break
            else:
                sub_clip = video_file.subclip(0, n+60)
                sub_clip = CompositeVideoClip([sub_clip])
                sub_clip.write_videofile(f"videos/test_{m}.mp4", codec="libx264")
                n += 60
                m += 1   
# split_video()