import cv2
import numpy as np

img = cv2.imread('test_images/opencv-logo.png')
imggray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
ret , threshold = cv2.threshold(imggray , 127 , 255 ,0)

# contours : numpy array of (x,y) coordinates of boundries of object.
# heirarchy : information about image topology
contours , heirarchy = cv2.findContours(threshold , cv2.RETR_TREE , cv2.CHAIN_APPROX_NONE)

print(f"Number of Contours : {str(contours)}")

# contourIdx = -1 i.e draw all contours
cv2.drawContours(img , contours , -1 , (0,255,0) , 5)

cv2.imshow("Original Image",img)
cv2.imshow("Gray image",imggray)
cv2.waitKey(0)
cv2.destroyAllWindows()
