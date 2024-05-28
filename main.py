from moviepy.editor import * # type: ignore

def videoEditing():
    videoclip = VideoFileClip("videos/example.mp4")
    audioclip = AudioFileClip("test.mp3")

    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    sub_clip = videoclip.subclip(0, 64) #crops the clip from 0 to 100 seconds
    sub_clip = sub_clip.resize
    sub_clip.write_videofile("videos/export.mp4")

videoEditing()
