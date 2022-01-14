import numpy.core.multiarray
import cv2
#opencv_traincascade -w 24 -h 24 -numPos 180 -data data -bg bg.txt -vec object.vec
def test_image():
    faceCascade = cv2.CascadeClassifier("cascade.xml")

    img = cv2.imread('Switch_Overwatch_01.jpg')

    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray,1.1,4)


    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)



    cv2.imshow("Respult",img)
    cv2.waitKey(0)
    
def test_video():
    cap = cv2.VideoCapture("soljer_Trim.mp4")
    faceCascade = cv2.CascadeClassifier("cascade.xml")
    while True:
        try:
            success, img = cap.read()
            imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            #resized_image = cv2.resize(imgGray, (200, 200))
            faces = faceCascade.detectMultiScale(imgGray,1.2,3)

            for (x,y,w,h) in faces:
                cv2.rectangle(imgGray,(x,y),(x+w,y+h),(255,0,0),2)



            cv2.imshow("Respult",imgGray)
            if cv2.waitKey(1) & 0xFF ==ord('q'):
                break;
        except Exception as e:
            print(str(e)) 
            
test_video()