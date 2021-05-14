import cv2
import numpy as np

img = cv2.imread('sudoku.png' , 0)

cv2.imshow('Main Image' , img)

_ , th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img , 255 , cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,5)
th3 = cv2.adaptiveThreshold(img , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,9,5)

cv2.imshow('simple threshold' , th1)
cv2.imshow('adaptive threshold - mean' , th2)
cv2.imshow('adaptive threshold - gaussian' , th3)
cv2.waitKey(0)
cv2.destroyAllWindows()