import numpy as np
import cv2

# 通过Sobel算子求图像边界
if __name__ == '__main__':
    # 赋值ddepth 为-1的时候，右边黑色减去左边白色，像素值为负数，那么会自动赋值为0，没效果
    # 解决办法： ddepth = cv2.CV_64F
    img = cv2.imread('../image/sobel4.bmp', cv2.IMREAD_GRAYSCALE)
    # img = cv2.imread('../image/sobel1.jpg', cv2.IMREAD_GRAYSCALE)
    # img = cv2.Sobel(img, -1, 1, 1)
    # cv2.imshow('sobel x', img)


    # 分别计算x方向，y方向的边界
    x = cv2.Sobel(img, cv2.CV_64F, 1, 0)
    y = cv2.Sobel(img, cv2.CV_64F, 0, 1)
    ret1 = cv2.addWeighted(x, 0.5, y, 0.5, 0)
    ret2 = cv2.convertScaleAbs(ret1)
    cv2.imshow('ret1:', ret2)

    cv2.waitKey(3000)
    cv2.destroyAllWindows()
