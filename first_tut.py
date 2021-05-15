import cv2

# img = cv2.imread('test_images/lena.jpg',-1)

# cv2.imshow('image',img)

# k = cv2.waitKey(0)

# if k == 27:
#     cv2.destroyAllWindows()
# elif k == ord('s'):
#     cv2.imwrite('test_images/lena_copy_2.png' , img)
#     cv2.destroyAllWindows()


##########  Video Capture ###########

## If we want to load our video file we can do that by giving
# name of file in video capture.

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID') # need to save video

out = cv2.VideoWriter('output.avi',fourcc , 20 , (640,480)) # save live video


## isOpened is useful for to check if cap capture something.
while(cap.isOpened()):
    ret , frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
        cv2.imshow('manthan' , gray)

        out.write(frame)

        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # Frame height
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # Frame width

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()


