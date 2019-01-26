import numpy as np
import cv2

# 形态操作：梯度图像操作
if __name__ == '__main__':
    img = cv2.imread('../image/gradient.bmp', cv2.IMREAD_UNCHANGED)
    cv2.imshow('original', img)

    img = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel=np.ones((10, 10), np.uint8))
    cv2.imshow('ret', img)

    cv2.waitKey(3000)
    cv2.destroyAllWindows()
