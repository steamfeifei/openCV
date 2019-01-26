import cv2
import numpy as np

if __name__ == '__aa__':
    img = cv2.imread('../image/dilation.bmp', cv2.IMREAD_UNCHANGED)
    k = np.ones((5, 5), np.uint8)
    r = cv2.dilate(img, k, iterations=5)
    cv2.imshow('original', img)
    cv2.imshow('res', r)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    img = cv2.imread('E:\openCV\openCV\images\IMG_0167.JPG', cv2.IMREAD_UNCHANGED)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, None, fx=10, fy=10)
    retval, img = cv2.threshold(img, 148, 255, cv2.THRESH_BINARY)
    cv2.imshow('original', img)
    print(img)

    img = cv2.erode(img, np.ones((5, 5), np.uint8), iterations=1)
    cv2.imshow('ret', img)

    img = cv2.dilate(img, np.ones((5, 5), np.uint8), iterations=1)
    cv2.imshow('aa', img)

    cv2.waitKey(3000)
    cv2.destroyAllWindows()

