import cv2
import numpy as np
image = cv2.imread("../image_2.jpg")
cv2.imshow("original",image)
array1 = np.ones(image.shape,np.uint8)*150
array2 = np.ones(image.shape,np.uint8)*50
cv2.putText(array1, text="Level-150", org=(10, 50), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
           fontScale=1, color=(255, 0, 0), thickness=2)
cv2.putText(array2, text="Level-50", org=(10, 50), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
           fontScale=1, color=(0, 255, 0), thickness=2)
resize1 = cv2.resize(array1,(250,250))
resize2 = cv2.resize(array2,(250,250))
resize3 = cv2.resize(image,(250,250))
array12 = cv2.hconcat((resize1,resize2,resize3))
cv2.imshow("Array12",array12)
cv2.imwrite("../Horizontal.jpg", array12)
cv2.waitKey(0)
