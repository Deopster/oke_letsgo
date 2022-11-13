from io import StringIO
from get_image import Bing
from song import SONG
import cv2
import numpy as np
from urllib.request import urlopen
import time
import glob
import requests
from PIL import Image
frameSize = (1920, 1080)
out = cv2.VideoWriter('output_video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 1, frameSize)
song = SONG('2XBYB2JH1TLMkmfWsoh5s9wKMPk3EZ_tsWdPHG487uYl9xPimmEh89Yk2SljBnTY')
bing = Bing()
words = song.find()
del words[0]
for i in words:
    if i!='' and i != '(' and i!=')':
        bing.run(str(i))
print("finish")