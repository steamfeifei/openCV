import cv2
import numpy as np

a = cv2.imread('../images/2.jpg')
b = cv2.imread('../images/1.png')
# roi = np.ones((0, 0, 3))
roi = a[0:200, 0:200]
cv2.imshow('original', a)
cv2.imshow('face', roi)
b[0:200, 0:200] = roi
cv2.imshow('aaaa', b)
cv2.waitKey(0)
cv2.destroyAllWindows()