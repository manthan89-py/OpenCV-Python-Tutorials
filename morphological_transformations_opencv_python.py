import cv2
import numpy as np
import matplotlib.pyplot as plt

## Morpholocial transformation are some simple operation based on the image shape.
## For this we need two things :- Image , kernel => which decide nature of operation.
## This operation only performs on BINARY images that why we read image in grayscale.

img = cv2.imread('smarties.png' , cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img,220,225,cv2.THRESH_BINARY_INV)

## Dilation : Increase the area
kernel = np.ones((2,2) , np.uint8)
dilation = cv2.dilate(mask,kernel,iterations=3)

## Erosion : Erode the corner
erosion = cv2.erode(mask , kernel , iterations=3)

## Opening : erosion + dilation
opening = cv2.morphologyEx(mask , cv2.MORPH_OPEN , kernel , iterations=3)

## Closing : dilation + erosion
closing = cv2.morphologyEx(mask , cv2.MORPH_CLOSE, kernel , iterations=3)

## Morphological Gradient : dilation - erosion
gradient = cv2.morphologyEx(mask , cv2.MORPH_GRADIENT, kernel , iterations=3)

## Top Hat : input_image - opening
th = cv2.morphologyEx(mask , cv2.MORPH_TOPHAT, kernel , iterations=3)

titles = ['image','mask','dilation','erosion','opening','closing','gradient','tophat']
images = [img,mask,dilation,erosion,opening,closing,gradient,th]

for i in range(len(images)):
    plt.subplot(2,4,i+1) 
    plt.imshow(images[i] , 'gray')
    plt.title(titles[i])
    plt.xticks([]) , plt.yticks([])

plt.show()