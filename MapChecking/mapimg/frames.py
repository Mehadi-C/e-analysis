import urllib.request
import cv2
import numpy as np
import os

def pull_vid_frame():
    cap = cv2.VideoCapture("video.mp4")
    pic_num = 1
    save = 12
    if not os.path.exists('a'):
        os.makedirs('a')
    
    while True:
        try:
            print(save)
            success, img = cap.read()
            #imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            #resized_image = cv2.resize(imgGray, (500, 500))
            if save == 12:
                cv2.imwrite("a/"+str(pic_num)+".jpg",img)
                pic_num += 1
                save = 0
            cv2.imshow("Output",img)
            if cv2.waitKey(1) & 0xFF ==ord('q'):
                break;
            save+=1
        except Exception as e:
            print(str(e))  

pull_vid_frame()