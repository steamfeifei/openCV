import numpy as np
import cv2

# 图像顶帽
if __name__ == '__main__':
    img = cv2.imread('../image/tophat.bmp', cv2.IMREAD_UNCHANGED)
    cv2.imshow('original', img)

    img = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel=np.ones((5, 5),dtype=np.uint8))
    cv2.imshow('ret', img)

    cv2.waitKey(3000)
    cv2.destroyAllWindows()
