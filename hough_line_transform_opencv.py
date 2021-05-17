import cv2
import numpy as np

img = cv2.imread('test_images/sudoku.png')
grey_img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

######## Standard Hough Transform #########
 
# 1 Edge Detection
edges = cv2.Canny(grey_img , 50 , 150 , apertureSize=3)
cv2.imshow('canny' , edges)

# 2 Convert lines to Hough lines ( Standard Method )
lines = cv2.HoughLines(edges, 1 , np.pi / 180 , 200)


for line in lines:
    rho , theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho

    # x1 stores (r*cos(theta) - 1000*sin(theta))
    x1 = int(x0 + 1000*(-b))
    # y1 stores (r*sin(theta) + 1000*(cos(theta)))
    y1 = int(y0 + 1000*(a))
    # x2 stores (r*cos(theta) + 1000*sin(theta))
    x2 = int(x0 - 1000*(-b))
    # y2 stores (r*sin(theta) - 1000*(cos(theta)))
    y2 = int(y0 - 1000*(a))

    cv2.line(img , (x1,y1) , (x2,y2) , (0,0,255) , 2)

cv2.imshow('image' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()

## Problem : Lines are not perfactly detected.