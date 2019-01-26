import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread(r'E:\gaofeiSoftWare\PythonWorkSpace\openCV1\images\IMG_0174.JPG', cv2.IMREAD_UNCHANGED)
    cv2.imshow('bgr', img)

    img = cv2.resize(img, None, fx=10, fy=10)
    cv2.imshow('resizeimg', img)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', img)
    ret, img = cv2.threshold(img, 145, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow('erzhihua', img)
    print(img)

    kernel = np.ones((2, 2), np.uint8)
    img = cv2.erode(img, kernel, iterations=3)
    cv2.imshow('erode', img)

    img = cv2.medianBlur(img, 13)
    cv2.imshow('medianBlur', img)

    ret, img = cv2.threshold(img, 145, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow('erzhihua2', img)

    cv2.waitKey()
    cv2.destroyAllWindows()

