import cv2

from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg' , -1)

plt.imshow(img)
plt.title('BGR Format Image')
plt.show()

cv2.imshow('OpenCV View' , img)

## Result of both might be differnet because of
## Opencv reads B G R format while
## Matplotlib reads R B G format.

img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
plt.imshow(img)
# plt.xticks([]) , plt.yticks([]) # remove x and y coordinates
plt.title('RGB Format Image') 
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()