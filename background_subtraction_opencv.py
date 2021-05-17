import cv2
import numpy as np

cap = cv2.VideoCapture('test_images/vtest.avi')
# fgbg = cv2.createBackgroundSubtractorMOG2()
fgbg = cv2.createBackgroundSubtractorKNN()

while True:
    ret, frame = cap.read()
    if frame is None:
        break

    fgmask = fgbg.apply(frame)
    cv2.imshow('image', frame)
    cv2.imshow('FG mask' , fgmask)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

