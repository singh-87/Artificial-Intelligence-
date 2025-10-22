import cv2
import numpy as np
image = cv2.imread("../ryn.jpg")
cv2.imshow("Original Image",image)
face_detect = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
eye_detect = cv2.CascadeClassifier("haarcascade_eye.xml")
nose_detect = cv2.CascadeClassifier("haarcascade_mcs_nose.xml")
image_resize = cv2.resize(image,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_NEAREST)
gray = cv2.cvtColor(image_resize,cv2.COLOR_BGR2GRAY)
face_xywh = face_detect.detectMultiScale(gray,1.5,3)
for (x,y,w,h) in face_xywh:
    cv2.rectangle(image_resize,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h,x:x+w]
    roi_color = image_resize[y:y+h,x:x+w]
    nose_xywh = nose_detect.detectMultiScale(roi_gray,1.5,3)
    eyes_xywh = eye_detect.detectMultiScale(roi_gray,1.5,3)
    for (x, y, w, h) in eyes_xywh:
        cv2.rectangle(roi_color, (x, y), (x + w, y + h), (0, 255, 0), 2)
    for (x, y, w, h) in nose_xywh:
        cv2.rectangle(roi_color, (x, y), (x + w, y + h), (0, 0, 255), 2)
cv2.imshow("Final image",image_resize)
cv2.waitKey(0)

