import numpy as np
import matplotlib.pyplot as plt
import cv2

if __name__ == '__main__':
    img = cv2.imread('../image/equ.bmp', cv2.IMREAD_GRAYSCALE)
    hist = cv2.equalizeHist(img)

    plt.hist(img.ravel(), 256)
    plt.show()
    plt.hist(img.ravel(), 256)
    plt.show()

    cv2.imshow('original:', img)
    cv2.imshow('hist:', hist)

    cv2.waitKey(10000)
    cv2.destroyAllWindows()