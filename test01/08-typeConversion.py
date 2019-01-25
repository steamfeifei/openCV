import cv2
import numpy as np

# 图像之间的类型转换
a = cv2.imread('../image/add/Python.png')
print(a.shape)
cv2.imshow('a', a)

# BGR --- > RGB
rgb = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
print(rgb.shape)
cv2.imshow('rgb', rgb)

#  BGR -- > GRAY
gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
print(gray.shape)
cv2.imshow('gray', gray)

#  GRAY -- > BGR
bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
print(bgr.shape)
cv2.imshow('bgr', bgr)
b, g, r = cv2.split(bgr)
print(b)
print(g)
print(r)


cv2.waitKey()
cv2.destroyAllWindows()

