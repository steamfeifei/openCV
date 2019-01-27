import numpy as np
import cv2

if __name__ == '__main__':
    img = cv2.imread('../image/boat.bmp', cv2.IMREAD_GRAYSCALE)
    mask = np.ones(img.shape, dtype=np.uint8)
    mask[200:400, 200:400] = 255
    mask_img = cv2.bitwise_and(img, mask)

    cv2.imshow('original:', img)
    cv2.imshow('mask:', mask)
    cv2.imshow('mask_img:', mask_img)

    cv2.waitKey(10000)
    cv2.destroyAllWindows()

