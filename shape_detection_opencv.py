import cv2
# import matplotlib.pyplot as plt

img = cv2.imread('test_images/shapes.jpg')

imgGrey = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

# find threshold 
_,thresh = cv2.threshold(imgGrey ,240 ,255 , cv2.THRESH_BINARY)

# find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE , cv2.CHAIN_APPROX_NONE)

# 2nd Argument epsilon : approximation accuracy
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour,True) , True)
    cv2.drawContours(img,[approx] , 0 , (255,0,0) , 5)

    # find coordinates
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    # shape name
    if len(approx) == 3:
        cv2.putText(img , 'Triangle' , (x-10,y-20) , cv2.FONT_HERSHEY_SIMPLEX , 0.5 , (255,255,255),2)
    
    elif len(approx) == 4:
        x, y , w ,h = cv2.boundingRect(approx)
        aspect_ratio = float(w)/h

        if aspect_ratio >= 0.95 and aspect_ratio <= 1.05:
            cv2.putText(img , 'Square' , (x-10,y-20) , cv2.FONT_HERSHEY_SIMPLEX , 0.5 , (0,0,0),2)
        else:
            cv2.putText(img , 'Rectangle' , (x-10,y-20) , cv2.FONT_HERSHEY_SIMPLEX , 0.5 , (0,0,0),2)

    elif len(approx) == 5:
        cv2.putText(img , 'Pentagon' , (x-10,y-10) , cv2.FONT_HERSHEY_SIMPLEX , 0.5 , (0,0,0),2)
    
    elif len(approx) == 6:
        cv2.putText(img , 'Hexagon' , (x-10,y-20) , cv2.FONT_HERSHEY_SIMPLEX , 0.5 , (0,0,0),2) 
    
    elif len(approx) == 10:
        cv2.putText(img , 'Star' , (x-10,y-20) , cv2.FONT_HERSHEY_SIMPLEX , 0.5 , (0,0,0),2)
    
    else:
        cv2.putText(img , 'Circle' , (x-10,y-20) , cv2.FONT_HERSHEY_SIMPLEX , 0.5 , (0,0,0),2)
    
cv2.imshow('Main Image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.imshow(img , 'gray')
# plt.title('Approximation of Shapes')
# plt.xticks([]) , plt.yticks([])
# plt.show()

