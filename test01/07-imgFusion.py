import cv2
a = cv2.imread('../image/add/boat.bmp')
b = cv2.imread('../image/add/lena.bmp')
result = cv2.addWeighted(a, 0.6, b, 0.4, 100)
cv2.imshow('a', a)
cv2.imshow('b', b)
cv2.imshow('result', result)
cv2.waitKey()
cv2.destroyAllWindows()