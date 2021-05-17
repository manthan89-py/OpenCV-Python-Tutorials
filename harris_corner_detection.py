import cv2
import numpy as np

img = cv2.imread('test_images/chessboard.png')
img = cv2.resize(img , (512,512))

cv2.imshow("original",img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

dst = cv2.cornerHarris(gray , 2,3,0.04)
dst = cv2.dilate(dst , None)

img[dst > 0.01*dst.max()] = [0,0,255]

cv2.imshow('dst' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()