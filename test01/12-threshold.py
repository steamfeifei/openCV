# 阈值化处理图像
import numpy as np
import cv2



# 二进制阈值化
if __name__ == '__aa__':
    img = cv2.imread(r'E:\gaofeiSoftWare\PythonWorkSpace\openCV1\image\add\lena.bmp', cv2.IMREAD_UNCHANGED)
    cv2.imshow('img', img)

    # 二进制阈值化
    retval, dst = cv2.threshold(img, 178, 255,cv2.THRESH_BINARY)
    cv2.imshow('二进制阈值化', dst)

    # 反二进制阈值化
    retval, dst = cv2.threshold(img, 178, 255,cv2.THRESH_BINARY_INV)
    cv2.imshow('反二进制阈值化：', dst)


    cv2.waitKey()
    cv2.destroyAllWindows()

# 截断阈值化
if __name__ == '__aa__':
    img = cv2.imread(r'E:\gaofeiSoftWare\PythonWorkSpace\openCV1\image\add\lena.bmp', cv2.IMREAD_UNCHANGED)
    cv2.imshow('img', img)

    # 截断阈值化
    retval, dst = cv2.threshold(img, 178, 255, cv2.THRESH_TRUNC)
    cv2.imshow('截断阈值化', dst)

    cv2.waitKey()
    cv2.destroyAllWindows()

# 阈值化为0
if __name__ == '__main__':
    img = cv2.imread(r'E:\gaofeiSoftWare\PythonWorkSpace\openCV1\image\add\lena.bmp', cv2.IMREAD_UNCHANGED)
    cv2.imshow('img', img)

    # 阈值化为0
    retval, dst = cv2.threshold(img, 178, 255, cv2.THRESH_TOZERO)
    cv2.imshow('阈值化为0', dst)

    # 反阈值化为0
    retval, dst = cv2.threshold(img, 178, 255, cv2.THRESH_TOZERO_INV)
    cv2.imshow('反阈值化为0', dst)

    cv2.waitKey()
    cv2.destroyAllWindows()