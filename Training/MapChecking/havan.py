import cv2
import numpy as np
from PIL import Image

transform = None
refPt = []
cropping = False

def find_transform():
    global transform
    primary = np.array([[200,21],
                        [315,232],
                        [10,294],
                         ])

    secondary = np.array([[621,40],
                          [937,605],
                          [113,766],
                           ])

    # Pad the data with ones, so that our transformation can do translations too
    n = primary.shape[0]
    pad = lambda x: np.hstack([x, np.ones((x.shape[0], 1))])
    unpad = lambda x: x[:,:-1]
    X = pad(primary)
    Y = pad(secondary)

    # Solve the least squares problem X * A = Y
    # to find our transformation matrix A
    A, res, rank, s = np.linalg.lstsq(X, Y)

    transform = lambda x: unpad(np.dot(pad(x), A))



def click_and_crop(event, x, y, flags, param):
    global refPt, cropping, transform

    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        t = transform(np.array([[x,y]]))
        print(refPt)
        print(t[0])
        cv2.circle(imgCropped, (x,y), 2, (0, 255, 0), thickness=1, lineType=8, shift=0)
        cv2.circle(bindCropped, (round(t[0][0]),round(t[0][1])-9), 2, (0, 255, 0), thickness=1, lineType=8, shift=0)



find_transform()

img= cv2.imread('havengam.jpg')
bind = cv2.imread('habenmap.jpg')
bindCropped = bind#[15:640,53:620]
imgCropped = img[30:410, 70:410]
print(imgCropped.shape)
print(bindCropped.shape)
cv2.circle(imgCropped, (40, 200), 2, (0, 255, 0), thickness=1, lineType=8, shift=0)

cv2.imshow("Bind", bind)
cv2.imshow("Image Resize", imgCropped)

cv2.setMouseCallback("Bind", click_and_crop)
cv2.setMouseCallback("Image Resize", click_and_crop)
while True:
    cv2.imshow("Bind", bindCropped)
    cv2.imshow("Image Resize", imgCropped)
    key = cv2.waitKey(1) & 0xFF
    # if the 'c' key is pressed, break from the loop
    if key == ord("c"):
        break
        
