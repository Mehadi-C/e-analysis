#import numpy.core.multiarray
from traceback import print_tb
import cv2
#opencv_traincascade -w 24 -h 24 -numPos 180 -data data -bg bg.txt -vec object.vec

def check_image(path):
    img = cv2.imread(path)
    faceCascade = cv2.CascadeClassifier("cascade.xml")
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray,1.1,4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    return img


def mkvid(path,outpath):
    limit = 10
    curr = 1
    print(path)
    faceCascade = cv2.CascadeClassifier("cascade.xml")

    cap = cv2.VideoCapture(path)
    ret, frame = cap.read()    
    fshape = frame.shape
    fheight = 500# fshape[0]
    fwidth = 500 #fshape[1]
    fourcc = cv2.VideoWriter_fourcc(*'VP80')
    output = outpath+'/output.webm'
    print(output)
    out = cv2.VideoWriter(output, fourcc, 20.0, (fheight,fwidth))
    
    while(cap.isOpened() & (curr<limit)):
        ret, frame = cap.read()
        if ret==True:
            imgGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            #resized_image = cv2.resize(imgGray, (200, 200))
            faces = faceCascade.detectMultiScale(imgGray,1.2,3)
            for (x,y,w,h) in faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            resized_image = cv2.resize(frame, (fheight,fwidth))
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
    return output


if __name__ == "__main__":
    res = check_image('./originals/sample.png')
    print(res)
    cv2.imwrite('./processed/sample.png',res)
    #cv2.imshow("Respult",res)
    #cv2.waitKey(0)