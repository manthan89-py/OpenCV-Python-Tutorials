import cv2
import numpy as np

img = cv2.imread('test_images/shapes.jpg')

cv2.imshow("original",img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray , 30 , 0.01 , 10)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img , (x,y) , 3 , (0,225,255) , -1)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

