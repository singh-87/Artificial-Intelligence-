import cv2
import numpy as np
detect = cv2.CascadeClassifier("haarcascade_fullbody.xml")
video = cv2.VideoCapture("walking.avi")
while True:
    ret,frame = video.read()
    frame = cv2.resize(frame,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_LINEAR)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    detector = detect.detectMultiScale(gray,1.1,2)#x,y,w,h
    for (x,y,w,h) in detector:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(200,255,190),3)
        cv2.imshow("Detected Pedestrians",frame)
    if cv2.waitKey(20)==ord("q"):
        break
