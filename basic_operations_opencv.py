import numpy as np
import cv2

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

print(img.shape) # row , column , channles
print(img.size) # total number of pixels
print(img.dtype) # image datatype

b,g,r = cv2.split(img)

img = cv2.merge((b,g,r))


#### ROI :- Region Of Interest ####

# getting the ball from image
ball = img[280:340 , 330:390]

## Find Coordinates doing some experiment on your image.

## place ball on other coordinates in image.
# img[273:333 , 100:160] = ball


####### Adding Images ########

# both images must have same size.

img = cv2.resize(img , (512,512))
img2 = cv2.resize(img2 , (512,512))

new_image = cv2.add(img , img2)

# Suppose you want to give weight to each image 
# Like 90% first image and 10% second image.

new_image = cv2.addWeighted(img , .8 , img2 , .2 , 0)

cv2.imshow('new_image' , new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
