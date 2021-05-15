import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('test_images/smarties.png', 0)

## Canny Edge Detection : It is multi-stage algorithm useful for wide range of edge detection.
## Total 5 Steps : 
# (1) Noise Reduction
# (2) Gradient Calculation
# (3) Non-maximum supression
# (4) Double threshold
# (5) Edge Tracking by hysteresis
## All things will be done by using one simple function frmo OpenCV


### Using Matplotlib ###

canny = cv2.Canny(img ,100 ,200)


titles = ['Main image', 'Canny']
images = [img , canny]


for i in range(len(images)):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i] , 'gray')
    plt.title(titles[i])
    plt.xticks([]) , plt.yticks([])
    
plt.show()


### Using Trackbar ###

# def nothing(x):
#     pass
# cv2.namedWindow('threshold meter')
# cv2.createTrackbar('th1' , 'threshold meter' , 0 ,255 , nothing)
# cv2.createTrackbar('th2' , 'threshold meter', 0 , 255 , nothing)

# cv2.imshow('Image' , img)

# while True:
#     th1 = cv2.getTrackbarPos('th1','threshold meter')
#     th2 = cv2.getTrackbarPos('th2','threshold meter')
#     canny = cv2.Canny(img , th1 , th2 )
#     cv2.imshow('canny' , canny)

#     key = cv2.waitKey(1)
#     if key == 27:
#         break
    

# cv2.destroyAllWindows()