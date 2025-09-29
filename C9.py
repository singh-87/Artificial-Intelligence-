"""import cv2
import numpy as np
detect = cv2.CascadeClassifier("haarcascade_plate_number.xml")
image = cv2.imread("car2.JPG")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
detector = detect.detectMultiScale(gray,1.1,1)
for (x,y,w,h) in detector:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,255),3)
    roi = image[y:y+h,x:x+w]
cv2.imshow("NumberPlate",image)
cv2.imshow("ROI",roi)
print(detector)
cv2.waitKey(0)"""
import cv2
import numpy as np
detect = cv2.CascadeClassifier("haarcascade_fullbody.xml")
video = cv2.VideoCapture("walking.avi")
while True:
    ret,frame = video.read()
    frame = cv2.resize(frame,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_LINEAR)#Scaling, making 50% size
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    detector = detect.detectMultiScale(gray,1.1,2)
    for (x,y,w,h) in detector:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(120,255,200),3)
        cv2.imshow("VideoIdentifier",frame)
    if cv2.waitKey(20)==ord("q"):
        break