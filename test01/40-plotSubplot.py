import numpy as np
import matplotlib.pyplot as plt
import cv2

# 调用plt.subplot 函数 定义窗口分布
if __name__ == '__main__':
    img = cv2.imread('../image/boatGray.bmp', cv2.IMREAD_GRAYSCALE)

    equalizeHist = cv2.equalizeHist(img)
    plt.subplot(121)
    plt.hist(img.ravel(), 256)
    plt.subplot(122)
    plt.hist(equalizeHist.ravel(), 256)
    plt.show()

    cv2.imshow('original:', img)
    cv2.imshow('equalizeHist:', equalizeHist)

    cv2.waitKey(10000)
    cv2.destroyAllWindows()
