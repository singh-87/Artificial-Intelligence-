import cv2
import numpy as np
"""image = cv2.imread("../image_5.jpg")
img2 = cv2.imread("../image_7.jpg")
cv2.imshow("Original",image)
kernel1 = np.array([[-1,-1,-1],
                    [-1,9,-1],
                    [-1,-1,-1]])
kernel2 = np.array([[-1,-1,-1],
                    [-1,8,-1],
                    [-1,-1,-1]])
sharpen1 = cv2.filter2D(image,-1,kernel1)
sharpen2 = cv2.filter2D(image,-1,kernel2)
#cv2.imshow("Kernel1",sharpen1)
cv2.imshow("Kernel2",sharpen2)
kernel3 = np.ones((5,5),np.uint8)
erode = cv2.erode(img2,kernel3,iterations=2)
dilate= cv2.dilate(sharpen2,kernel3,iterations=2)
cv2.imshow("Erosion",erode)
cv2.imshow("Dilation",dilate)"""
#Bitwise Operations: OR,AND,NOR,NAND,XOR
rect = np.zeros((500,500),np.uint8)
cv2.rectangle(rect,(20,20),(200,385),255,-1)
rect2 = np.zeros((500,500),np.uint8)
cv2.circle(rect2,(250,250),100,255,-1)
bitwise_and = cv2.bitwise_and(rect,rect2)
bitwise_or = cv2.bitwise_or(rect,rect2)
bitwise_xor = cv2.bitwise_xor(rect,rect2)                           #If both are same, it will be 0 otherwise its 1
bitwise_not = cv2.bitwise_not(rect)
cv2.imshow("Bitwise xor",bitwise_xor)
cv2.imshow("Bitwise not",bitwise_not)
cv2.imshow("Bitwise and",bitwise_and)
cv2.imshow("Bitwise or",bitwise_or)
cv2.imshow("Rectangle",rect)
cv2.imshow("Circle",rect2)
cv2.waitKey(0)