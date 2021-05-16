import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('test_images/lena.jpg', 0)
# img = np.zeros((200,200) , np.uint8)
# cv2.rectangle(img ,(0,50) , (100,100), (127) , -1)

# b,g,r = cv2.split(img)

# cv2.imshow('Main image' , img)
# cv2.imshow('Blue Channel' , b)
# cv2.imshow('Green Channel' , g)
# cv2.imshow('Red Channel' , r)

# Histogram in Matplotlib

# plt.hist(img.ravel() , 256 , [0,256])
# plt.hist(b.ravel() , 256 , [0,256])
# plt.hist(g.ravel() , 256 , [0,256])
# plt.hist(r.ravel() , 256 , [0,256])
# plt.title('Histogram of Color Image(lena.jpg)')
# plt.show()


# Histogram in Opencv

hist = cv2.calcHist([img], [0] , None , [256],[0,256])
plt.plot(hist)
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
