import cv2

a = cv2.imread('../images/2.jpg', cv2.IMREAD_UNCHANGED)
b = cv2.imread('../images/2.jpg', cv2.IMREAD_GRAYSCALE)
print(a.shape)
print(b.shape)
print(a.size, a.shape[0] * a.shape[1] * a.shape[2])
print(b.size)
print(a.dtype)
print(b.dtype)
