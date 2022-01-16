#import numpy.core.multiarray
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


def mkvid():
    limit = 100
    curr = 1

    faceCascade = cv2.CascadeClassifier("cascade.xml")

    cap = cv2.VideoCapture("soljer_Trim.mp4")
    ret, frame = cap.read()    
    fshape = frame.shape
    print(frame.shape)
    fheight = 500# fshape[0]
    fwidth = 500 #fshape[1]
    fourcc = 0#cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (fheight,fwidth))
    
    while(cap.isOpened() & (curr<limit)):
        ret, frame = cap.read()
        if ret==True:
            imgGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            #resized_image = cv2.resize(imgGray, (200, 200))
            faces = faceCascade.detectMultiScale(imgGray,1.2,3)
            for (x,y,w,h) in faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            resized_image = cv2.resize(frame, (fheight,fwidth))
            print(resized_image.shape)
            out.write(resized_image.astype('uint8'))
            curr += 1
            #cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()

    out.release()

    cv2.destroyAllWindows()


mkvid()
#test_video()