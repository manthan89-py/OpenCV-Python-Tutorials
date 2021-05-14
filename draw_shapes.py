import cv2
import numpy as np
# img = cv2.imread('lena.jpg', 1)

# img with numpy
img = np.zeros([600,600,3] , np.uint8 )

## Draw Line
img = cv2.line(img, (0,0),(255,255),(255,0,0),thickness=3)

## Arrowed line
img = cv2.arrowedLine(img, (0,255),(255,255),(0,255,0),thickness=3)

## Rectangle 
img = cv2.rectangle(img , (384,0),(450,330),(0,0,255),thickness=5)
# if thickness = -1 then it will filled with given color

## Circle
img = cv2.circle(img, (447,63),radius=63,color = (255,34,135),thickness=-1)

## Put Text
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'OpenCv',(10,450) ,font , 4 , (255,255,255), 10, cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()