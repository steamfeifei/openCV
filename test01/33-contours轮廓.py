import cv2

if __name__ == '__main__':
    o = cv2.imread('E:\openCV\openCV\image\contours.bmp')
    # 将图像分为二值化
    gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    # 参数为
    #     img 原始的二值图像       cv2.RETR_TREE  轮廓的树形模式      cv2.CHAIN_APPROX_SIMPLE 轮廓的近似方法为保留终点坐标
    # 返回值：
    #     img 返回修改后的二值图像    轮廓数组
    contours,hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    co = o.copy()
    r = cv2.drawContours(co, contours, 2, (0, 255, 0), 6)
    cv2.imshow('original:', o)
    cv2.imshow('img2', r)

    cv2.waitKey(10000)
    cv2.destroyAllWindows()

