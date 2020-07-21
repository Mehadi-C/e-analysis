#camera.py# import the necessary packages
import cv2# defining face detector
face_cascade = cv2.CascadeClassifier("./Resources/haarcascade_frontalface_default.xml")
ds_factor=0.6

class VideoCamera(object):
    def __init__(self,abceee):
       #capturing video
       print(abceee)
       file = "./ok/" + abceee 
       self.video = cv2.VideoCapture(file)
    
    def __del__(self):
        #releasing camera
        self.video.release()


# cap= cv2.VideoCapture("./ok/duelists-valorant.mp4")

    def get_frame(self):
        #extracting frames
        ret, frame = self.video.read()
        frame=cv2.resize(frame,None,fx=ds_factor,fy=ds_factor,
        interpolation=cv2.INTER_AREA)                    
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        face_rects=face_cascade.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in face_rects:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            break        
            
        # encode OpenCV raw frame to jpg and displaying it
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()