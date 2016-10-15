# Main Program : Recognizer

import cv2
import sys
import random
import os
import numpy as np

cap=cv2.VideoCapture(0)
while (cap.isOpened()):
    ret, img = cap.read()
    cv2.rectangle(img, (20, 20), (300, 300), (255, 0, 0), 3)
 #   cv2.imshow("BGR Output", img)

    img1 = img[20:300,20:300]
    img2 = cv2.imread("test.jpg",1)

    imCopy = img1.copy()

    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    ret, thresh1 = cv2.threshold(blur, 10, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    ret, thresh2 = cv2.threshold(blur, 10, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    cv2.imshow("Threshold", thresh1)

    contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt1 = contours[0]        #Real-Time Contour Reading

    contours, hierarchy = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt2 = contours[0]

    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    if((ret==0.0)or(ret>=0.001)and(ret<=0.009)):
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, "HELLO", (20, 450), font, 2, (0, 125, 155), 2)

    cv2.imshow("BGR Output", img)
    cv2.drawContours(imCopy, contours, -1, (0, 255, 0))
    cv2.imshow('Draw Contours', imCopy)


    k = 0xFF & cv2.waitKey(10)  # escape kep value = 27
    if k == 27:
        break



cap.release()
cv2.destroyAllWindows()