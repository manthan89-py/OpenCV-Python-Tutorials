import cv2
import numpy as np

cap = cv2.VideoCapture('test_images/vtest.avi')

ret , frame1 = cap.read()
ret , frame2 = cap.read()
while cap.isOpened():

    # difference between first and second frame
    diff = cv2.absdiff(frame1,frame2)

    # convert it into gray ( for finding contours )
    gray = cv2.cvtColor(diff , cv2.COLOR_BGR2GRAY)

    # apply blur
    blur = cv2.GaussianBlur(gray , (5,5) , 0)

    # find threshold
    _ , th = cv2.threshold(blur , 20 , 255 , cv2.THRESH_BINARY)

    # dilate the images
    dilated = cv2.dilate(th, None , iterations=3)

    # find contours
    contours , _ = cv2.findContours(dilated , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)

    # draw contours
    # cv2.drawContours(frame1 , contours , -1 , (0,255,0) , 3)

    # Make rectangle around contours
    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 900:
            continue
        
        cv2.rectangle(frame1 ,(x,y) , (x+w,y+h) , (0,255,0) , 2)
        cv2.putText(frame1,'Status: Movement' , (10,40) , cv2.FONT_HERSHEY_SIMPLEX ,1 , (255,0,0), 3)

    cv2.imshow('feed' , frame1)
    frame1 = frame2
    ret , frame2 = cap.read()

    # again read the frame for only second frame2
    # that's how we calculate the difference between two frames

    if cv2.waitKey(40) == 27:
        break

cap.release()
cv2.destroyAllWindows()