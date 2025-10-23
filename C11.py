import cv2
import numpy as np
#1.Convert BGR to HSV
#2. Hconcat It
video = cv2.VideoCapture(0)
lower_red = np.array([0,100,100])
upper_red = np.array([10,255,255])
while True:
    ret,frame = video.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,lower_red,upper_red)
    result = cv2.bitwise_and(frame,frame,mask=mask)
    contors, img = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i in contors:
        area = cv2.contourArea(i)
        if area > 500:
            x, y, w, h = cv2.boundingRect(i)  # To find x,y,w,h
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 3)
    hcon = cv2.hconcat((frame, result))
    cv2.imshow("BGR_Video", hcon)
    if cv2.waitKey(20)==ord("q"):
        break
video.release()
cv2.destroyAllWindows()