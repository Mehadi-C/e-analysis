import cv2
import numpy as np
from PIL import Image

transform = None
refPt = []
cropping = False

def find_transform():
    global transform
    primary = np.array([[0,380],
                        [340,0],
                        [340,380],
                         ])

    secondary = np.array([[0,625],
                          [565,0],
                          [565,625],
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


def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result

def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    global refPt, cropping, transform
    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        t = transform(np.array([[x,y]]))
        print(refPt)
        print(t[0])
        cv2.circle(imgCropped, (x,y), 2, (0, 255, 0), thickness=1, lineType=8, shift=0)
        cv2.circle(bindCropped, (round(t[0][0]),round(t[0][1])-9), 2, (0, 255, 0), thickness=1, lineType=8, shift=0)



find_transform()

img= cv2.imread('val3.jpg')
bind= cv2.imread('bind.jpg')
bindCropped = bind[15:640,53:620]
imgCropped = img[30:410, 70:410]
imgRot= rotate_image(imgCropped, 60)
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
        
