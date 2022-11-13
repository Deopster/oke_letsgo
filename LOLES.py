import cv2
import numpy as np

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('output_video.avi')

# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream or file")

import cv2
import numpy as np
import glob
from PIL import Image

frameSize = (1920, 1080)

out = cv2.VideoWriter('output_video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 0.5, frameSize)
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
cap = cv2.VideoCapture('output_video.avi')
