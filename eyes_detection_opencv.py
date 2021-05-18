import cv2
import numpy as np

# You have to download both cacasde file from internet
# Download link is in readme.md file of this repository.

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

# img = cv2.imread('test_images/test.jpg')
cap = cv2.VideoCapture(0) 

while cap.isOpened():
    _, img = cap.read()

    # face detection      
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0),3)

        # for eyes deteciton
        roi_gray = gray[y:y+h , x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eyes_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey) , (ex+ew,ey+eh),(0,255,0) , 3)

    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()

cap.release()