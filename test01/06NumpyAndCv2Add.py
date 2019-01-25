import numpy as np
import cv2

a = cv2.imread('../image/lena256.bmp')
b = a
print(type(a))
add1 = a + b
add2 = cv2.add(a, b)
# print(a)
print(add1)
cv2.imshow('a', a)
cv2.imshow('add1', add1)
cv2.imshow('add2', add2)
cv2.waitKey()
cv2.destroyAllWindows()
