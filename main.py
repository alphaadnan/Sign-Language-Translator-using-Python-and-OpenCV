import cv2
import sys
import random
import os
import numpy as np

cap=cv2.VideoCapture(0)
while (cap.isOpened()):
    ret, img = cap.read()
    cv2.rectangle(img, (20, 20), (220, 300), (255, 0, 0), 3)
    cv2.imshow("BGR Output", img)

    img2 = img[20:300,20:220]
    #img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale", img2)

    '''
    imgthreshold = cv2.inRange(img,cv2.cv.Scalar(3,3,125),cv2.cv.Scalar(40,40,255))
    cv2.imshow("Threshold", imgthreshold)
    '''

    k = 0xFF & cv2.waitKey(10)  # escape kep value = 27
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()