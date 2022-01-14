import urllib.request
import cv2
import numpy as np
import os

print('okok')

def store_net_images():
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00017222'   
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    pic_num = 206
    
    if not os.path.exists('neg'):
        os.makedirs('neg')
        
    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "neg/"+str(pic_num)+".jpg")
            img = cv2.imread("neg/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, (200, 200))
            cv2.imwrite("neg/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e))  

def pull_vid_frame():
    cap = cv2.VideoCapture("negatives1.mp4")
    pic_num = 1
    if not os.path.exists('ow_neg'):
        os.makedirs('ow_neg')
    
    while True:
        try:
            success, img = cap.read()
            imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            resized_image = cv2.resize(imgGray, (200, 200))
            cv2.imwrite("ow_neg/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
            cv2.imshow("Output",imgGray)
            if cv2.waitKey(1) & 0xFF ==ord('q'):
                break;
        except Exception as e:
            print(str(e))  




def write_desc_file():
    for file_type in ['neg']:
        
        for img in os.listdir(file_type):

            if file_type == 'pos':
                line = file_type+'/'+img+' 1 0 0 50 50\n'
                with open('info.dat','a') as f:
                    f.write(line)
            elif file_type == 'neg':
                line = file_type+'/'+img+'\n'
                with open('null.txt','a') as f:
                    f.write(line)
                    
write_desc_file()