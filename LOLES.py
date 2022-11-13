import numpy as np
import glob
from PIL import Image, ImageOps, ImageFont
from PIL import ImageDraw

def photoshop(filename,name):
    img = Image.open("./files/"+filename)
    resize = ImageOps.pad(img, (1920,940), color='black',centering=(0.5, 0))
    border = (0, 0, 0, 140)
    final = ImageOps.expand(resize, border=border, fill='black')
    draw_text = ImageDraw.Draw(final)
    draw_text.text(
        (960, 995),
        name,
        font=ImageFont.truetype(font="./TradeGothicLT-BoldCondTwenty.ttf",size=100),
        fill=('#9c2121'),
        anchor = "mm"
    )
    final.save("./final/"+filename)
