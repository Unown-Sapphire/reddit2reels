from moviepy.editor import * # type: ignore

clip = VideoFileClip("example.mp4") #example clip

#Cropping Clips
sub_clip = clip.subclip(0, 100) #crops the clip from 0 to 100 seconds

#Adjusting volume of sub_clip idrk why it doesnt work for VideoFileClip
volume_clip = sub_clip.volumex(0.8)

txt_clip = TextClip("My Holidays 2013",fontsize=70,color='white')
txt_clip = txt_clip.set_duration(10)

video = CompositeVideoClip([clip, txt_clip]) #mixing the 
