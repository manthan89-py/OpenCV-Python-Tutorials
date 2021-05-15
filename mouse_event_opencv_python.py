import cv2
import numpy as np

def event_click(event , x , y , flags , param):
    # if event == cv2.EVENT_LBUTTONDOWN:
    #     print(x ,' ', y)
    #     strxy = str(x) + ', ' + str(y) 
    #     font = cv2.FONT_HERSHEY_SIMPLEX
    #     cv2.putText(img ,strxy, (x,y) , font , 0.5 , (255,255,0), 2)
    #     cv2.imshow('image' , img)
    # if event == cv2.EVENT_RBUTTONDOWN:
    #     blue = img[y,x,0] # BLUE
    #     green = img[y,x,1] # green
    #     red = img[y,x,2] # red
    #     strBGR = str(blue) + ', ' + str(green) +', ' + str(red) 
    #     font = cv2.FONT_HERSHEY_SIMPLEX
    #     cv2.putText(img ,strBGR, (x,y) , font , 0.5 , (0,0,0), 2)
    #     cv2.imshow('image' , img)

    ####### Advanced Events ########
    # if event == cv2.EVENT_LBUTTONDOWN:
    #     cv2.circle(img , (x,y) , 3 ,(0,0,255) , -1)
    #     points.append((x,y))
    #     if len(points) >= 2:
    #         cv2.line(img , points[-1] , points[-2] ,(0,255,0) ,2 , lineType=cv2.LINE_AA)
    #     cv2.imshow('image' , img)
     if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x,y,0] # BLUE
        green = img[x,y,1] # green
        red = img[x,y,2] # red
        cv2.circle(img , (x,y) , 3 ,(0,0,255) , -1)
        mycolorimage = np.zeros([512,512,3] , np.uint8)
        mycolorimage[:] = [blue,green,red]
        cv2.imshow('color image' , mycolorimage)





# img = np.zeros([512,512,3] , np.uint8)
img = cv2.imread('test_images/lena.jpg')
cv2.imshow('image' , img)
points = []
# window name must be same
cv2.setMouseCallback('image' , event_click)

cv2.waitKey(0)
cv2.destroyAllWindows()
