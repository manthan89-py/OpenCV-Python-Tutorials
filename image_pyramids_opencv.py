import cv2
import numpy as np

## Pyramid : Using Blur and subsample we downscale the image in low size.
## Use for Reduce the size of images.

img = cv2.imread('test_images/lena.jpg')
layer = img.copy()

# 1. Gaussian Pyramid 

# pyrDown : reduce the size
# pyrUp   : increase the size

# applying pyrUp on pyrdowned image will not be same as original.
# pyrdown image lose data at the time of compression.
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    # cv2.imshow(str(i) , layer)


# 2. Laplacian Pyramid
# Difference between that level in gaussian pyramid and expanded version of its upper level
# in gaussian pyramid
# Its like edge detection

layer = gp[5]
cv2.imshow('final upper layer',layer)
lp = [layer]

for i in range(5,0,-1):
    gaussian_expaned = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1],gaussian_expaned)
    cv2.imshow(str(i) , laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()
