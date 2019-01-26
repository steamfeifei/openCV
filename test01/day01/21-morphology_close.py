import numpy as np
import cv2

if __name__ == '__main__':
    img = cv2.imread('E:\openCV\openCV\image\closing.bmp', cv2.IMREAD_UNCHANGED)
    cv2.imshow('original', img)

    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, np.ones((10, 10), np.uint8))
    cv2.imshow('true', img)
    
    cv2.waitKey()
    cv2.destroyAllWindows()