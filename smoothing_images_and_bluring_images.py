import cv2
import numpy as np
import matplotlib.pyplot as plt

# img = cv2.imread('test_images/opencv-logo.png')
# img = cv2.imread('test_images/water.png')
img = cv2.imread('test_images/lena.jpg')
img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB) # for plot image in matplotlib.

# low pass filter helps to remove noise from images and blurring the images.
# high pass filter helps to find edges from images

# kernel = [1/(kernel height * kernel width)] * [kernel_matrix]

kernel = np.ones((5,5) , np.float32) / 25
dst = cv2.filter2D(img , -1 ,kernel)

## blur - averaging algorithm
blur = cv2.blur(img , (5,5) )

## gaussian filter : use difference weighted kernel in x and y direction 
gblur = cv2.GaussianBlur(img, (5,5) , 0)

## MedianBlur : rplace each pixel with th median of its neighboring pixel value.
## its more useful with salt and papper noise.
## note : kernel size must be odd and greater then 1. for 1 it shows original image.
mblur = cv2.medianBlur(img,5)


## Bilateral Filter :preserving the edge in image
bilateral = cv2.bilateralFilter(img , 9 , 75 , 75)


titles = ['Original Image','2D Convolution','Blur','Gaussian blur','Median Filter','Bilateral Filter']
images = [img , dst, blur , gblur , mblur , bilateral]

for i in range(len(images)):
    plt.subplot(2,3,i+1) 
    plt.imshow(images[i] , 'gray')
    plt.title(titles[i])
    plt.xticks([]) , plt.yticks([])

plt.show()