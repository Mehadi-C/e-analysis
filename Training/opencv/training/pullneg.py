import urllib.request
import cv2
import numpy as np
import os

def pull_vid_frame():
    cap = cv2.VideoCapture("soljer_Trim.mp4")
    pic_num = 1
    save = True
    if not os.path.exists('ow_pos'):
        os.makedirs('ow_pos')
    
    while True:
        try:
            print(save)
            success, img = cap.read()
            imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            resized_image = cv2.resize(imgGray, (500, 500))
            if save:
                cv2.imwrite("ow_pos/"+str(pic_num)+".jpg",resized_image)
                pic_num += 1
            cv2.imshow("Output",imgGray)
            if cv2.waitKey(1) & 0xFF ==ord('q'):
                break;
            save = not save
        except Exception as e:
            print(str(e))  

pull_vid_frame()