import cv2
import numpy as np
image = cv2.imread("../image_4.jpg")
img2 = cv2.imread("../image_7.jpg")
kernel = np.array([[-1,-1,-1],
                   [-1,9,-1],
                   [-1,-1,-1]])
sharpen = cv2.filter2D(image,-1,kernel)
cv2.imshow("Sharpened",sharpen)
gray = cv2.cvtColor(sharpen,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray)
binary = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,21,30)
cv2.imshow("Binary",binary)
erosion = cv2.erode(img2,kernel,iterations=2)
dilation = cv2.dilate(img2,kernel,iterations=2)
cv2.imshow("Erosion",erosion)
cv2.imshow("Dilation",dilation)
#Bitwise operations
rect = np.zeros((500,500),np.uint8)
cv2.rectangle(rect,(20,20),(190,385),255,-1)
circle = np.zeros((500,500),np.uint8)
cv2.circle(circle,(250,250),100,255,-1)
ellipse = cv2.ellipse(circle,(250, 400), (100, 50), 0, 0, 360, (255, 255, 0), 3) # yellow ellipse
cv2.imshow("E",ellipse)
bitwis_and = cv2.bitwise_and(rect,circle)
bitwis_or = cv2.bitwise_or(rect,ellipse)
bitwis_not = cv2.bitwise_not(rect,circle)
bitwis_xor = cv2.bitwise_xor(rect,ellipse)
cv2.imshow("Bitwise_xor",bitwis_xor)
cv2.imshow("Bitwise_not",bitwis_not)
cv2.imshow("Bitwise_or",bitwis_or)
cv2.imshow("Bitwise_and",bitwis_and)
cv2.waitKey(0)