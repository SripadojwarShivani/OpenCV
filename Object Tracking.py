import cv2
import numpy as np
#captures the video from webcam
cap=cv2.VideoCapture(0)

while(1):
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lowerLimit=np.array([0,100,100])
    upperLimit=np.array([25,255,255])

#color range between UL and LL will be captured  and stored in mask from hsv 
    mask=cv2.inRange(hsv,lowerLimit,upperLimit)
    
    result=cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('result',result)

#waitkey is 1 millisecond and key pressed is equal to q then it exits the output
    if(cv2.waitKey(1) & 0xFF==ord('q')):
        break
        
destroyAllWindows()
    