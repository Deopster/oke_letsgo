import cv2
import numpy as np
import glob
from PIL import Image

frameSize = (1920, 1080)

out = cv2.VideoWriter('output_video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 1, frameSize)
count = 0
for filename in glob.glob('C:/Users/andre/Pictures/*.jpg'):
    img = Image.open(filename)
    new_image = img.resize((1920, 1080))
    cv2_img = np.array(new_image)
    img = cv2.cvtColor(cv2_img, cv2.COLOR_RGB2BGR)
    out.write(img)
    count+=1
print(count)
out.release()