import cv2
import datetime
cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

# 3: width, 4: height
# you can only able to some fix height and width like 1280x720
# If you set 700x700 then it will take 640x480
# If you set 3000x3000 then it will take 1280x720

cap.set(cv2.CAP_PROP_FRAME_WIDTH , 1208)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT , 720) 

print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

while(cap.isOpened()):
    ret , frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: '+str(cap.get(3)) +' Height: '+str(cap.get(4)) 
        date = 'Date: '+ str(datetime.datetime.now())

        cv2.putText(frame , text ,(10,50) , font , 1 ,(0,255,255) , 2 , lineType=cv2.LINE_AA) 
        
        cv2.putText(frame , date ,(10,90) , font , 1 ,(0,255,255) , 2 , lineType=cv2.LINE_AA) 
        
        cv2.imshow('image' , frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
