import cv2
import numpy as np
# image = cv2.imread("../cow-salt-peper.png")
# img2 = cv2.imread("handwritten.png")
# gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
# org = cv2.imread("../image_8.jpg")
# cv2.imshow("Original",org)
#canny = cv2.Canny(org,50,200)#Edge detection
#cv2.imshow("Canny",canny)
img9 = cv2.imread("../image_9.jpg")
cv2.imshow("Ori",img9)
canny = cv2.Canny(img9,50,200)
cv2.imshow("canny",canny)
countours,ret = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)#Store all the boundary points
cv2.drawContours(img9,countours,-1,(150,100,255),10)
cv2.imshow("Contour",img9)
bird = cv2.imread("../birds.jpg")
cv2.imshow("Bird",bird)
gray = cv2.cvtColor(bird,cv2.COLOR_BGR2GRAY)
binary = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,21,30)
cv2.imshow("BInary_Bird",binary)
contors,img = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
for i in contors:
    print(cv2.contourArea(i))
    if cv2.contourArea(i)>200:
        x,y,w,h = cv2.boundingRect(i)
        cv2.rectangle(bird,(x,y),(x+w,y+h),(150,100,42),2)
cv2.imshow("output",bird)
# blu = cv2.blur(image,(3,3))#TO smoothen the image
# cv2.imshow("Normal Blur",blu)
# mb = cv2.medianBlur(image,3)
# cv2.imshow("MedianBlur",mb)
# gauss = cv2.GaussianBlur(image,(3,3),1)
# cv2.imshow("Gauss",gauss)
# ret,binary = cv2.threshold(gray,50,255,cv2.THRESH_BINARY)#Used for optical character recognition
# ada = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,30)
# cv2.imshow("adaptive",ada)
# cv2.imshow("binary",binary)
cv2.waitKey(0)