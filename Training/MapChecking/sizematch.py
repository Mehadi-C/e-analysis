import cv2
import numpy as np
from PIL import Image

gameMap= cv2.imread('val3.jpg')
bind= cv2.imread('bindgood.jpg')


gameCropped = gameMap[30:410, 70:410]
bind = bind[25:670,0:750]
print(gameCropped.shape)
print(bind.shape)

x=20
y=20

 
cv2.circle(gameCropped, (x,y), 2, (0, 255, 0), thickness=1, lineType=8, shift=0)

cv2.circle(bind, ((x)*3,(y)*3), 2, (0, 255, 0), thickness=1, lineType=8, shift=0)


cv2.imshow("Bind", bind)
cv2.imshow("Image Resize", gameCropped)


if cv2.waitKey(0) & 0xff ==ord('a'):
    exit()