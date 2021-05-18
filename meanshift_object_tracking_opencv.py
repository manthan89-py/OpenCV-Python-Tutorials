import cv2
import numpy as np

cap = cv2.VideoCapture('test_images/slow_traffic_small.mp4')

# read first frame
ret, frame = cap.read()

# initial location
x, y, width, height = 300, 200, 100, 50
tracked_window = (x,y,width,height)

# ROI 
roi = frame[y:y+height , x:x+width]
hsv_roi = cv2.cvtColor(roi , cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi , np.array((0.,60.,32.)) , np.array((180.,255.,255.)))
roi_hist = cv2.calcHist([hsv_roi] , [0] ,mask ,[180],[0,180] )
cv2.normalize(roi_hist , roi_hist , 0,255, cv2.NORM_MINMAX)

# setup termination criteria
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT , 10, 1)
# cv2.imshow('roi' , roi)

while True:
    ret, frame = cap.read()
    if ret == True:

        hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv] , [0] , roi_hist , [0,180] , 1)

        # mean shift
        ret ,track_window = cv2.meanShift(dst , tracked_window , term_crit)

        # draw it on image
        x,y,w,h = track_window

        final_image = cv2.rectangle(frame , (x,y) , (x+w,y+h) , (0,0,255) , 3)

        # cv2.imshow('dst' , dst)
        cv2.imshow('final_image' , final_image)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
