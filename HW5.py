import cv2
import numpy as np
image = cv2.imread("../image_3.jpg")
cv2.imshow("original",image)
array1 = np.ones(image.shape,np.uint8)*30
array2 = np.ones(image.shape,np.uint8)*120
array3 = np.ones(image.shape,np.uint8)*220
cv2.putText(array1, "Level-30", (10, 80), cv2.FONT_HERSHEY_SIMPLEX,
            3, (0, 0, 255), 8, )
cv2.putText(array2, "Level-120", (10, 80), cv2.FONT_HERSHEY_SIMPLEX,
            3, (255, 0, 0), 8)
cv2.putText(array3, "Level-220", (10, 80), cv2.FONT_HERSHEY_SIMPLEX,
            3, (0, 255, 0), 8)
resize1 = cv2.resize(array1,(100,100))
resize2 = cv2.resize(array2,(100,100))
resize3 = cv2.resize(array3,(100,100))
array123= cv2.hconcat((resize1,resize2,resize3))
arrayv123= cv2.vconcat((resize1,resize2,resize3))
cv2.imshow("Array123",array123)
cv2.imshow("Array123",arrayv123)
cv2.imwrite("./SaajanH.jpg", array123)
cv2.imwrite("./SaajanV.jpg", arrayv123)
#Getting text size
cv2.waitKey(0)