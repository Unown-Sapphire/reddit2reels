from moviepy.editor import * # type: ignore
from moviepy.video.tools.subtitles import SubtitlesClip
import random
<<<<<<< HEAD
=======
from skimage.filters import gaussian
from PIL import Image

import os, shutil
folder = 'videos/video_parts'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))
>>>>>>> 1dc292b3491559bc0681d9deb40abf53266b9ca0

from subreddit import random_title
print("Found Subreddit post!")

<<<<<<< HEAD
def chunks(L, n):
    for i in range(0, len(L), n):
        yield L[i:i+n]  

with open('spedup copy.srt', "r+", encoding="utf-8") as srtfile:
    text = random_title
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
=======
print(random_title)

import tts_audio
print("Finished Composing Audio!")
>>>>>>> 1dc292b3491559bc0681d9deb40abf53266b9ca0


def blur(image):
    return gaussian(image.astype(float), sigma=7)

sample_list = []

timing_list = []

new_list = []

with open(file="spedup.srt", mode="r+", encoding="utf-8") as file:
    file_line = file.readlines(-1)
    for line in file_line:
        x = line.rstrip("\n")
        new_list.append(x)
    sample_list = new_list
    new_list = [i for i in new_list if i != '']
    
    for element in new_list:
        if element.endswith(".") and random_title.endswith(element.rstrip(".")):
            location = new_list.index(element)
            print("located: " + element)
            timing = new_list[location-1]
            timing_list.append(timing)
            del new_list[0:location+1]
            break
        elif element.endswith("?") and random_title.endswith(element):
            location = new_list.index(element)
            print("located: " + element)
            timing = new_list[location-1]
            timing_list.append(timing)
            del new_list[0:location+1]
            break
        else:
            print("Element does not match?")
    
    writing_list = []
    for z in new_list:
        spaced_element = z + "\n"
        writing_list.append(spaced_element)
    a = 3
    while a <= len(sample_list):
        writing_list.insert(a, "\n")
        a += 4
    file.truncate(0)
    file.seek(0)
    for line in writing_list:
        file.write(line)

    print(writing_list)

print(timing_list)

for i in timing_list:
    print(i)
    time = i[23:len(i)]
    print(time)
    time = time.replace(",", ".")
    print(float(time))

n = random.randint(1,2)

def videoEditing():
<<<<<<< HEAD
    #Collecting Video and Audio files
    videoclip = VideoFileClip(f"videos/example_2.mp4")
=======
    #get audio duration
>>>>>>> 1dc292b3491559bc0681d9deb40abf53266b9ca0
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
<<<<<<< HEAD
    img_clip = ImageClip("images/output.png").set_start(0).set_duration(time).resize(height=328, width=864).set_pos(("center","top"))

    audio_duration = audioclip.duration
=======
    #save random point of video screenshot
    r_time = random.randint(1, round(audio_duration))
    videoclip.save_frame("images/frame.png", t=r_time)
    #set image clip pos
    title = Image.open("output.png").convert("RGBA")
    title = title.resize(size=(1026, 389)).save("output.png")
    img_clip = ImageClip("output.png").set_start(0).set_duration(time).set_pos(("center","center"))
>>>>>>> 1dc292b3491559bc0681d9deb40abf53266b9ca0
    #Subtitles generator
    generator = lambda txt: TextClip(txt, font=r'fonts/Burbank Big Condensed Black.otf', fontsize=100, color='white', method="caption", stroke_color="black", stroke_width=4, size=(1080, None))
    subs = SubtitlesClip('spedup.srt', generator)
    subtitles = SubtitlesClip(subs, generator)
    sub_clip = CompositeVideoClip([videoclip, subtitles.set_pos(('center','center')), img_clip])
    #Cropping the video
    sub_clip = sub_clip.subclip(0, audio_duration)
<<<<<<< HEAD
    sub_clip.write_videofile("videos/export.mp4", codec="libx264")
    print(f"Your video is ready!")
=======
    sub_clip.write_videofile("videos/export.mp4", codec="libx264", threads=4)
    print("Your video is ready!")
>>>>>>> 1dc292b3491559bc0681d9deb40abf53266b9ca0

# n = random.randint(1,2)

<<<<<<< HEAD
# def videoEditing():
#     #Collecting Video and Audio files
#     videoclip = VideoFileClip(f"videos/example_2.mp4")
#     audioclip = AudioFileClip("audios/spedup.mp3")

#     #Merging audio with video
#     new_audioclip = CompositeAudioClip([audioclip])
#     videoclip.audio = new_audioclip
    
#     audio_duration = audioclip.duration
#     r_time = random.randint(1, round(audio_duration))
#     videoclip.save_frame("images/frame.png", t=r_time)
    
#     #Subtitles generator
#     generator = lambda txt: TextClip(txt, font=r'fonts/Burbank Big Condensed Black.otf', fontsize=100, color='white', method="caption", stroke_color="black", stroke_width=4, size=(1080, None))
#     subs = SubtitlesClip('spedup.srt', generator)
#     subtitles = SubtitlesClip(subs, generator)
#     sub_clip = CompositeVideoClip([videoclip, subtitles.set_pos(('center','center'))])
#     #Cropping the video
#     sub_clip = sub_clip.subclip(0, audio_duration)
#     sub_clip.write_videofile("videos/export.mp4", codec="libx264")
#     print("Your video is ready!")

# videoEditing()

# def split_video():
#     audio_clip = AudioFileClip("audios/spedup.mp3")
#     audio_duration = audio_clip.duration
#     video_file = VideoFileClip("videos/export.mp4")

#     if audio_duration <= 60:
#         pass
#     elif audio_duration > 60 and audio_duration <=120:
#         n = 0
#         m = 1
#         while n <= 120:
#             if n == 60 and m == 2:
#                 sub_clip = video_file.subclip(60, audio_duration)
#                 sub_clip = CompositeVideoClip([sub_clip])
#                 sub_clip.write_videofile(f"videos/video_parts/test_{m}.mp4", codec="libx264")
#                 break
#             else:
#                 sub_clip = video_file.subclip(0, n+60)
#                 sub_clip = CompositeVideoClip([sub_clip])
#                 sub_clip.write_videofile(f"videos/video_parts/test_{m}.mp4", codec="libx264")
#                 n += 60
#                 m += 1   
#     elif audio_duration > 120 and audio_duration <=180:
#         n = 0
#         m = 1
#         while n <= 180:
#             if n == 120 and m == 3:
#                 sub_clip = video_file.subclip(60, audio_duration)
#                 sub_clip = CompositeVideoClip([sub_clip])
#                 sub_clip.write_videofile(f"videos/video_parts/test_{m}.mp4", codec="libx264")
#                 break
#             else:
#                 sub_clip = video_file.subclip(0, n+60)
#                 sub_clip = CompositeVideoClip([sub_clip])
#                 sub_clip.write_videofile(f"videos/video_parts/test_{m}.mp4", codec="libx264")
#                 n += 60
#                 m += 1   
#     elif audio_duration > 180 and audio_duration <=240:
#         n = 0
#         m = 1
#         while n <= 240:
#             if n == 180 and m == 4:
#                 sub_clip = video_file.subclip(60, audio_duration)
#                 sub_clip = CompositeVideoClip([sub_clip])
#                 sub_clip.write_videofile(f"videos/video_parts/test_{m}.mp4", codec="libx264")
#                 break
#             else:
#                 sub_clip = video_file.subclip(0, n+60)
#                 sub_clip = CompositeVideoClip([sub_clip])
#                 sub_clip.write_videofile(f"videos/video_parts/test_{m}.mp4", codec="libx264")
#                 n += 60
#                 m += 1   

#     elif audio_duration > 240 and audio_duration <=300:
#         n = 0
#         m = 1
#         while n <= 300:
#             if n == 240 and m == 5:
#                 sub_clip = video_file.subclip(60, audio_duration)
#                 sub_clip = CompositeVideoClip([sub_clip])
#                 sub_clip.write_videofile(f"videos/video_parts/test_{m}.mp4", codec="libx264")
#                 break
#             else:
#                 sub_clip = video_file.subclip(0, n+60)
#                 sub_clip = CompositeVideoClip([sub_clip])
#                 sub_clip.write_videofile(f"videos/video_parts/test_{m}.mp4", codec="libx264")
#                 n += 60
#                 m += 1   
# split_video()

# import generator

# import instagram_automation
=======
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
                sub_clip = video_file.subclip(n, n+60)
                sub_clip = CompositeVideoClip([sub_clip])
                sub_clip.write_videofile(f"videos/video_parts/test_{m}.mp4", codec="libx264")
                n += 60
                m += 1   
    elif audio_duration > 120 and audio_duration <=180:
        n = 0
        m = 1
        while n <= 180:
            if n == 120 and m == 3:
                sub_clip = video_file.subclip(120, audio_duration)
                sub_clip = CompositeVideoClip([sub_clip])
                sub_clip.write_videofile(f"videos/video_parts/test_{m}.mp4", codec="libx264")
                break
            else:
                sub_clip = video_file.subclip(n, n+60)
                sub_clip = CompositeVideoClip([sub_clip])
                sub_clip.write_videofile(f"videos/video_parts/test_{m}.mp4", codec="libx264")
                n += 60
                m += 1   
    elif audio_duration > 180 and audio_duration <=240:
        n = 0
        m = 1
        while n <= 240:
            if n == 180 and m == 4:
                sub_clip = video_file.subclip(180, audio_duration)
                sub_clip = CompositeVideoClip([sub_clip])
                sub_clip.write_videofile(f"videos/video_parts/test_{m}.mp4", codec="libx264")
                break
            else:
                sub_clip = video_file.subclip(n, n+60)
                sub_clip = CompositeVideoClip([sub_clip])
                sub_clip.write_videofile(f"videos/video_parts/test_{m}.mp4", codec="libx264")
                n += 60
                m += 1   

    elif audio_duration > 240 and audio_duration <=300:
        n = 0
        m = 1
        while n <= 300:
            if n == 240 and m == 5:
                sub_clip = video_file.subclip(240, audio_duration)
                sub_clip = CompositeVideoClip([sub_clip])
                sub_clip.write_videofile(f"videos/video_parts/test_{m}.mp4", codec="libx264")
                break
            else:
                sub_clip = video_file.subclip(n, n+60)
                sub_clip = CompositeVideoClip([sub_clip])
                sub_clip.write_videofile(f"videos/video_parts/test_{m}.mp4", codec="libx264")
                n += 60
                m += 1   
split_video()

import generator

import instagram_automation 
>>>>>>> 1dc292b3491559bc0681d9deb40abf53266b9ca0
