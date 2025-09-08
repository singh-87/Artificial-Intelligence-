import cv2
import numpy as np
video = cv2.VideoCapture(0)
while True:
    ret,frame = video.read()
    #cv2.imshow("Video",frame)
    v_flip = cv2.flip(frame,0)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    array1 = np.array([[0,0,0,0,0],
                       [0,0,0,0,0],
                       [0,0,0,0,0],
                       [0,0,0,0,0],
                       [0,0,0,0,0],
                       ],np.uint8)
    array_resize = cv2.resize(array1,(640,480))
    frame = cv2.resize(frame,(300,300))
    blur = cv2.GaussianBlur(frame,(5,5),0)
    ones = np.ones(frame.shape, np.uint8) * 150
    cv2.imshow("array_resize",array_resize)
    print(frame.shape)
    add = cv2.add(frame,ones)#Add function will increase brightness of image
    sub = cv2.subtract(frame,ones)
    com = cv2.hconcat((frame,add,blur))
    cv2.imshow("Com",com)
    #cv2.imshow("Combine",add)
    #cv2.imshow("vertical",v_flip)
    cv2.imshow("hsv",hsv)
    if cv2.waitKey(30)==ord("s"):
        break