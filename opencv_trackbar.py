import cv2
import numpy as np

def nothing(x):
    print(x)

img = np.zeros((300,512,3) , np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('B', 'image' , 0 , 255 , nothing)
cv2.createTrackbar('G', 'image' , 0 , 255 , nothing)
cv2.createTrackbar('R', 'image' , 0 , 255 , nothing)

switches = '0 : OFF\n 1 : ON'
cv2.createTrackbar(switches, 'image' , 0 , 1 , nothing)


while True:
    cv2.imshow('image' , img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    b = cv2.getTrackbarPos('B','image')
    g = cv2.getTrackbarPos('G','image')
    r = cv2.getTrackbarPos('R','image')
    switch = cv2.getTrackbarPos(switches,'image')

    if switch == 1:
        img[:] = [b,g,r]
    else:
        pass
    

cv2.destroyAllWindows()