import os
import cv2
from glob import glob
def gener():
    frameSize = (1920, 1080)
    out = cv2.VideoWriter('output_video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 1, frameSize)
    count = 0
    pics=[]
    files=glob(os.path.join('C:/Users/andre/PycharmProjects/oke_letsgo/final/','*.jpg'))
    for i in files:
        pics.append(int(i[48:-4]))
    for filename in sorted(pics):
        print(filename)
        img = cv2.imread('C:/Users/andre/PycharmProjects/oke_letsgo/final/'+str(filename)+'.jpg')
        out.write(img)
    out.release()