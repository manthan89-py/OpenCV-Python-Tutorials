import cv2
import numpy as np

# height width channls
img1 = np.zeros((250,500,3) , np.uint8)
img1 = cv2.rectangle(img1,(200,0),(300,100) , (255,255,255) , -1)
img2 = cv2.imread('test_images/messi5.jpg')

cv2.imshow('Main image1' , img1)
cv2.imshow('Main image2' , img2)

img2 = cv2.resize(img2 ,(500,250)) # width height
print(img1.shape)
print(img2.shape)

# Bitwise Operations #

bitAnd = cv2.bitwise_and(img1 , img2)
bitOr = cv2.bitwise_or(img1 , img2)
bitXor = cv2.bitwise_xor(img1 , img2)
bitnot1 = cv2.bitwise_not(img1)
bitnot2 = cv2.bitwise_not(img2)

# cv2.imshow('bitAnd' , bitAnd)
# cv2.imshow('bitOr' , bitOr)
# cv2.imshow('bitXor' , bitXor)
# cv2.imshow('bitnot1' , bitnot1)
# cv2.imshow('bitnot2' , bitnot2)

cv2.waitKey(0)
cv2.destroyAllWindows()
