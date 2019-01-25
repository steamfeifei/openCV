import numpy as np
import cv2

img = cv2.imread('../../images/2.jpg')
a = cv2.flip(img, -1)
cv2.imshow('a', a)
# cv2.imshow('a', img)
cv2.waitKey()
cv2.destroyAllWindows()
