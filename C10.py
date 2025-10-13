import cv2
import numpy as np
face_detect = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
eyes_detect = cv2.CascadeClassifier("haarcascade_eye.xml")
nose_detect = cv2.CascadeClassifier("haarcascade_mcs_nose.xml")
video = cv2.VideoCapture(0)
while True:
    ret,frame = video.read()
    frame_resize = cv2.resize(frame,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_LINEAR)
    gray = cv2.cvtColor(frame_resize,cv2.COLOR_BGR2GRAY)
    face_xywh = face_detect.detectMultiScale(gray,1.5,3)
    for (x,y,w,h) in face_xywh:
        cv2.rectangle(frame_resize,(x,y),(x+w,y+h),(255,0,0),10)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame_resize[y:y+h,x:x+w]
        eyes_xywh = eyes_detect.detectMultiScale(roi_gray,1.5,3)
        nose_xywh = nose_detect.detectMultiScale(roi_gray,1.5,3)
        for (x,y,w,h) in eyes_xywh:
            cv2.rectangle(roi_color, (x, y), (x + w, y + h), (0, 255, 0), 10)
        for (x,y,w,h) in nose_xywh:
            cv2.rectangle(roi_color, (x, y), (x + w, y + h), (0, 0, 255), 10)
    cv2.imshow("Face_detect",frame_resize)
    if cv2.waitKey(20)==ord("q"):
          break
video.release()
cv2.destroyAllWindows()