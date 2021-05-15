import cv2
import numpy as np

img = cv2.imread('test_images/gradient.png' , 0)

_ , th1 = cv2.threshold(img,50,255,cv2.THRESH_BINARY)
_ , th2 = cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)
_ , th3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
_ , th4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
_ , th5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow('threshold' , th1)
cv2.imshow('threshold2' , th2)
cv2.imshow('threshold3' , th3)
cv2.imshow('threshold4' , th4)
cv2.imshow('threshold5' , th5)

cv2.imshow('image' , img)

cv2.waitKey(0)
cv2.destroyAllWindows()