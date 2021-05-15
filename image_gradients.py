import cv2
import numpy as np
import matplotlib.pyplot as plt

# Image Gradient : directional change in intensity or color in image.
# img = cv2.imread('test_images/messi5.jpg' , cv2.IMREAD_GRAYSCALE)
img = cv2.imread('test_images/lena.jpg' , cv2.IMREAD_GRAYSCALE)

##### Laplacian Gradient : detect edges in images. ######

# 64 bit float type. It supports negative number
# negative slop due to induced by transformaing the image white to black.
# NOTE : kernelsize must be odd

lap = cv2.Laplacian(img,cv2.CV_64F , ksize=1)

# take absolute value and convert it into unsigned interger 8 bit.
lap = np.uint8(np.absolute(lap))



                                ##### Sobel Gradient ######

sobelX = cv2.Sobel(img , cv2.CV_64F , 1, 0 )
sobelY = cv2.Sobel(img , cv2.CV_64F , 0, 1 )

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX , sobelY)

titles = ['image' , 'Laplacian', 'sobelX' , 'sobelY', 'Sobel Combined']
images = [img , lap , sobelX , sobelY , sobelCombined]


for i in range(len(images)):
    plt.subplot(2,3, i+1)
    plt.imshow(images[i] , 'gray')
    plt.title(titles[i])
    plt.xticks([]) , plt.yticks([])


plt.show()