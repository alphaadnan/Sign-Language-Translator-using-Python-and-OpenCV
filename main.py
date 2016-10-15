import cv2
import sys
import random
import os
import numpy as np

cap=cv2.VideoCapture(0)
while (cap.isOpened()):
    ret, img = cap.read()
    cv2.rectangle(img, (20, 20), (300, 300), (255, 0, 0), 3)
    cv2.imshow("BGR Output", img)

    img1 = img[20:300,20:300]

    imCopy = img1.copy()
    
    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    ret, thresh1 = cv2.threshold(blur, 10, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    cv2.imshow("Threshold", thresh1)

    contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(imCopy, contours, -1, (0, 255, 0))
    cv2.imshow('draw contours', imCopy)


    k = 0xFF & cv2.waitKey(10)  # escape kep value = 27
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
