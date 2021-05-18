import cv2
# object detection based on Haar cascade classifier

#image face detection
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# img = cv2.imread('test_images/test.jpg')

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0),3)

# cv2.imshow('img', img)
# cv2.waitKey(0)

# cv2.destroyAllWindows()


# video face detection

## You have to download cascade file from internet
## Download link is in readme.md file of this repository

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# img = cv2.imread('test_images/test.jpg')
cap = cv2.VideoCapture(0) 

while cap.isOpened():
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0),3)


    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()

cap.release()