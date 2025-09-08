import cv2
import numpy as np
# #1.
# img1 = cv2.imread("../image_1.jpg")
# img2 = cv2.imread("../image_4.jpg")
# add = cv2.add(img1,img2)
# sub = cv2.subtract(img1,img2)
# cv2.imshow("Original",img1)
# cv2.imshow("Original2",img2)
# cv2.imshow("Add",add)
# cv2.imshow("Sub",sub)

#2.
# img3 = cv2.imread("../image_3.jpg")
# gray_scale = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
# cv2.imshow("Ori",img3)
# cv2.imshow("Gray_scaled",gray_scale)
#3.
# video = cv2.VideoCapture(0)
# while True:
#     ret,frame = video.read()
#     cv2.imshow("Frame",frame)
#     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     cv2.imshow("Grey",gray)
#     if cv2.waitKey(0)==ord('q'):
#         break
#4.
array1 = np.array([
    [255, 255, 255, 255, 255],
    [255,   0,   0,   0,   0],
    [255, 255, 255, 255, 255],
    [0,   0,   0,   0, 255],
    [255, 255, 255, 255, 255]
],np.uint8)
resize_nearest = cv2.resize(array1, (640,480), interpolation=cv2.INTER_NEAREST)
cv2.imshow("arra",resize_nearest)
cv2.waitKey(0)