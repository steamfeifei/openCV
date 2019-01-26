import numpy as np
import cv2

if __name__ == '__main__':
    img = cv2.imread('../image/blackhat.bmp', cv2.IMREAD_UNCHANGED)
    cv2.imshow('original', img)
    img = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel=np.ones((10, 10), np.uint8))
    cv2.imshow('ret', img)

    cv2.waitKey(3000)
    cv2.destroyAllWindows()