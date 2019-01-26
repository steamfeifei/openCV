import numpy as np
import cv2

a = cv2.imread('../../images/2.jpg')
cv2.imshow('图片', a)
b = cv2.resize(a, (100, 100))
cv2.imshow('b', b)
c = cv2.resize(a, (200, 300))
cv2.imshow('c', c)
d = cv2.resize(c, None, fx=1.5, fy=1.5)
cv2.imshow('d', d)
rows, cols, aa = d.shape
print(rows, cols, aa)
e = cv2.resize(d, (round(rows * 0.75), round(cols * 0.8)))
cv2.imshow('e', e)

cv2.waitKey()
cv2.destroyAllWindows()
