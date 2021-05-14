import numpy as np
import cv2

img = cv2.imread('messi5.jpg')

print(img.shape) # row , column , channles
print(img.size) # total number of pixels
print(img.dtype) # image datatype

b,g,r = cv2.split(img)

img = cv2.merge((b,g,r))

cv2.imshow('image' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()
