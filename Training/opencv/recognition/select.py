import cv2
import numpy as np

cap= cv2.VideoCapture("soljer_Trim.mp4")

def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img,(x,y), ((x+w), (y+h)), (255, 0, 255), 3, 1)

def selTrack():
    tracker= cv2.TrackerCSRT_create()
    success, img = cap.read()
    bbox = cv2.selectROI("Tracking", img, False)
    tracker.init(img, bbox)
    main(tracker,bbox)

def autoTrack():
    faceCascade = cv2.CascadeClassifier("cascade.xml")
    success, img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray,1.4,3)
    for (x,y,w,h) in faces:
        bbox = x,y,w,h
        break;
    tracker= cv2.TrackerCSRT_create()
    success, img = cap.read()
    tracker.init(img, bbox)
    drawBox(img, bbox)
    main(tracker,bbox)

def menu(img):
    freeze = True
    while freeze:
        if cv2.waitKey(1) & 0xff ==ord('p'):
            freeze = False
        if cv2.waitKey(1) & 0xff ==ord('q'):
            exit()
        if cv2.waitKey(1) & 0xff ==ord('c'):
            print("select")
            selTrack()
        if cv2.waitKey(1) & 0xff ==ord('a'):
            print("select")
            autoTrack()

def main(tracker,bbox):
    while True:
        timer= cv2.getTickCount()
        success, img = cap.read()

        success,bbox = tracker.update(img)
        print(bbox)
        if success:
            drawBox(img, bbox)
        else:
            autoTrack()
            cv2.putText(img, "Lost", (75, 50), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 0, 0), 2)

        fps = cv2.getTickFrequency()/(cv2.getTickCount() - timer)
        cv2.putText(img, str(int(fps)), (75, 50), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 0, 0), 2)

        cv2.imshow("Tracking", img)

        if cv2.waitKey(1) & 0xff ==ord('p'):
            menu(img)
            
autoTrack()