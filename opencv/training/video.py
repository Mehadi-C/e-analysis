import cv2

def pull_vid_frame():
    cap = cv2.VideoCapture("soljer_Trim.mp4")

    while True:
        try:
            success, img = cap.read()
            cv2.imshow("Output",img)
            if cv2.waitKey(1) & 0xFF ==ord('q'):
                cv2.waitKey(-1)
                #break;
        except Exception as e:
            print(str(e))  

pull_vid_frame()