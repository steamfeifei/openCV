import cv2

img = cv2.imread('../../images/2.jpg')
cv2.namedWindow('Demo')
cv2.imshow('Demo', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(img)