from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os

filler_color = (255,255,255)
stroke_color = (0,0,0)
font = ImageFont.truetype(font=r"fonts\Poppins-Bold.ttf", size=100)

frame = Image.open("images/frame.png").convert("RGBA")
title = Image.open("output.png").convert("RGBA")
frame1 = frame.filter(ImageFilter.GaussianBlur(radius=50))
title = title.resize(size=(1026, 389))

n = 1

for file in os.listdir("videos/video_parts"):
    combined = Image.new(mode="RGBA", size=frame.size)
    W, H = combined.size
    drawer = ImageDraw.Draw(combined)
    _, _, w, h = drawer.textbbox((0, 0), f"Part {n}", font=font)
    combined.paste(frame1, (0,0))
    combined.paste(title, (27, 268), title)
    drawer.text(xy=((W-w)/2, (H-h)/2), text=f"Part {n}", fill=filler_color, stroke_fill=stroke_color, stroke_width=3, font=font)
    combined.save(f"images/thumbnail_{n}.png")
    n+=1