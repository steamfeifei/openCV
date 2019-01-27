import numpy as np
import cv2

if __name__ == '__main__':
    # 读取图像
    img = cv2.imread('../image/lena.bmp', cv2.IMREAD_UNCHANGED)

    # 保存图像
    cv2.imwrite('../image/write/gaofei.bmp', img)

    # 显示图像
    cv2.imshow('图像标题', img)

    # 读取像素
    print('图片的像素为：', img)

    # 修改像素
    img[:200, :200] = 0
    cv2.imshow('修改像素后的图片:', img)

    # 读取像素的方法
    print(img.item(200, 201, 0))

    # 设置图片像素的方法
    img.itemset((200, 201, 0), 255)
    img.itemset((200, 201, 1), 255)
    img.itemset((200, 201, 2), 255)
    cv2.imshow('update three ', img)

    # 读取图像属性
    print('图像的形状为：', img.shape)
    print('图像的像素大小为：', img.size)
    print('图像的数据类型为：', img.dtype)

    # 图像的感兴趣区域ROI
    face = img[0:200, 0:200, 0]
    cv2.imshow('ROI:', face)
    print(face.shape)

    # 通道拆分和合并
    print('通道的拆分：', cv2.split(img))
    print('通道的合并：', cv2.merge(cv2.split(img)))
    cv2.imshow('merge',  cv2.merge(cv2.split(img)))

    # openCV 加法
    cv2.imshow('img + img:', img + img)
    cv2.imshow('cv2.add:', cv2.add(img, img))

    cv2.imshow('图像融合:', cv2.addWeighted(img, 0.8, img, 0.5, 0))

    # 图像缩放
    resizeimg = cv2.resize(img, (100, 300))
    cv2.imshow('resizeimg:', resizeimg)

    resizeimg1 = cv2.resize(img, None, fx=0.5, fy=0.5)
    cv2.imshow('resize1:', resizeimg1)

    # 图像旋转
    flipimg = cv2.flip(img, 1)
    cv2.imshow('flipimg:', flipimg)

    flipimg1 = cv2.flip(img, 0)
    cv2.imshow('flipimg1:', flipimg1)

    flipimg2 = cv2.flip(img, -1)
    cv2.imshow('flipimg2:', flipimg2)

    # 阈值分割
    # 二进制阈值化
    retval, binary = cv2.threshold(img, 147, 255, cv2.THRESH_BINARY)
    cv2.imshow('binary:', binary)
    # 反二进制阈值化
    retval, binary_inv = cv2.threshold(img, 147, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow('binary_inv', binary_inv)
    # 截断阈值化
    retval, trunc = cv2.threshold(img, 147, 255, cv2.THRESH_TRUNC)
    cv2.imshow('trunc', trunc)
    # 阈值化为0
    retval, tozero = cv2.threshold(img, 147, 255, cv2.THRESH_TOZERO)
    cv2.imshow('tozero', tozero)
    # 反阈值化为0
    retvak, tozero_inv = cv2.threshold(img, 147, 255, cv2.THRESH_TOZERO_INV)
    cv2.imshow('tozero_inv', tozero_inv)

    # 滤波
    # 均值滤波
    blur = cv2.blur(img, (10, 10))
    cv2.imshow('blur', blur)
    # 方框滤波
    boxFilter = cv2.boxFilter(img, -1, (5, 5), normalize=True)
    cv2.imshow('boxfilter:', boxFilter)
    # 高斯滤波  核大小必须为奇数
    gauss = cv2.GaussianBlur(img, (11, 11), sigmaX=0, sigmaY=0)
    cv2.imshow('gauss', gauss)
    # 种植滤波
    medianblur = cv2.medianBlur(img, 11)
    cv2.imshow('medianblur', medianblur)

    # 图像腐蚀  针对的是二值图像
    erode = cv2.erode(img, np.ones((3, 3), np.uint8), iterations=5)
    cv2.imshow('erode', erode)
    # 图像膨胀
    dilate = cv2.dilate(img, np.ones((3, 3), np.uint8), iterations=5)
    cv2.imshow('dilate', dilate)
    # 开运算 先腐蚀在膨胀
    open = cv2.morphologyEx(img, cv2.MORPH_OPEN, np.ones((3, 3), dtype=np.uint8))
    cv2.imshow('open', open)
    # 闭运算  先膨胀再腐蚀
    close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, np.ones((3, 3), dtype=np.uint8))
    cv2.imshow('close', close)

    # 梯度操作
    tidu = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, np.ones((3, 3), np.uint8))
    cv2.imshow('tidu', tidu)
    # 图像黑帽  闭运算 - 原始图像
    result = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, np.ones((3, 3), np.uint8))
    cv2.imshow('result', result)
    # 图像顶帽  原始图像 - 开运算
    result = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, np.ones((3, 3), np.uint8))
    cv2.imshow('topHat', result)

    # 图像边界
    # Soble 算子
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
    sobelx = cv2.convertScaleAbs(sobelx)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)
    sobely = cv2.convertScaleAbs(sobely)
    sobel = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
    cv2.imshow('sobel', sobel)
    # Scharr 算子
    scharrx = cv2.Scharr(img, cv2.CV_64F, 1, 0)
    scharrx = cv2.convertScaleAbs(scharrx)
    scharry = cv2.Scharr(img, cv2.CV_64F, 0, 1)
    scharry = cv2.convertScaleAbs(scharry)
    scharr = cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)
    cv2.imshow('scharr', scharr)
    # 拉普拉斯算子
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    laplacian = cv2.convertScaleAbs(laplacian)
    cv2.imshow('laplacian', laplacian)
    # canny 算子
    canny = cv2.Canny(img, 100, 200)
    cv2.imshow('canny', canny)

    # 图像金字塔
    # 向上取样
    up = cv2.pyrUp(img)
    cv2.imshow('up', up)
    # 向下取样
    down = cv2.pyrDown(img)
    cv2.imshow('down', down)
    # 拉普拉斯金字塔  原图像 - 向下取样再向上取样的图像
    o = img
    od = cv2.pyrDown(o)
    odd = cv2.pyrUp(od)
    lapPyr = o - odd
    cv2.imshow('laplacian0', lapPyr)

    o1 = od
    od = cv2.pyrDown(o1)
    odd = cv2.pyrUp(od)
    lapPyr = o1 - odd
    cv2.imshow('laplacian1', lapPyr)

    #  图像轮廓
    gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
    retval, o = cv2.threshold(gray, 148, 255, cv2.THRESH_BINARY)    # 变为二值图像
    contours, hierarchy = cv2.findContours(o, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)       # 计算图像轮廓
    o1 = o
    print(len(contours))
    o2 = cv2.drawContours(o, contours, 1819, (255, 0, 0), 1)
    cv2.imshow('original:', o1)
    cv2.imshow('o2:', o2)

    cv2.waitKey(6000)      #等待键盘按下，默认0，无线等待
    cv2.destroyAllWindows()
