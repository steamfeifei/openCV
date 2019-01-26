import numpy as np
import cv2

if __name__ == '__main__':
    # 读入图像
    img = cv2.imread('../image/add/lena.bmp', cv2.IMREAD_UNCHANGED)

    # 显示图像
    cv2.imshow('showImg', img)

    # 保存文件
    cv2.imwrite('../image/write/write.bmp', img)

    print('像素img为：\n',img)
    print(img.shape)

    for i in range(10, 60):
        img[i, 99] = 255

    cv2.imshow('fuzhihoudeimg', img)
    # img[88, 99] = 255
    # print(img[88, 99])

    print('item:', img.item(55, 55))
    print(img.itemset((55, 55), 255))


    # 读取图像属性
    print(img.shape)
    print('像素数目：', img.size)
    print('图像类型：', img.dtype)
    print('图像的感兴趣区域：', img[200 : 400, 200 : 400])

    # 拆分通道
    img = cv2.imread('../image/logo.png', cv2.IMREAD_UNCHANGED)
    cv2.imshow('img--', img)
    print('拆分通道：', *cv2.split(img))
    print(img.shape)

    img = cv2.merge(cv2.split(img))
    cv2.imshow('merge', img)

    img1 = img
    img2 = img
    img = img1 + img2
    cv2.imshow('img1 + img2:', img)

    img = cv2.add(img1, img2)
    cv2.imshow('cv2.add:', img)

    # 图像融合
    img = cv2.addWeighted(img1, 1, img2, 1, 0)
    cv2.imshow('addWeighted', img)

    # 类型转换
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray:', img)
    print('gray --> bgr: ', img.shape)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.imshow('gray --> bgr', img)
    print('gray --> bgr: ', img.shape)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imshow('bgr --> rgb: ', img)

    # 图像缩放
    a = cv2.resize(img, (500, 300))
    cv2.imshow('imgresize:', a)

    b = cv2.resize(img, None, fx=0.5, fy=0.5)
    cv2.imshow('fx,fy', b)

    # 图像翻转
    c = cv2.flip(img, 1)
    cv2.imshow('>0', c)
    cv2.imshow('=0', cv2.flip(img, 0))
    cv2.imshow('<0', cv2.flip(img, -1))

    # 阈值分割
    img = cv2.imread('../image/logo.png', cv2.IMREAD_UNCHANGED)
    retval, dst = cv2.threshold(img, 148, 255, cv2.THRESH_BINARY)
    cv2.imshow('dst', dst)

    retval, dst = cv2.threshold(img, 148, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow('dst', dst)

    retval, dst = cv2.threshold(img, 148, 256, cv2.THRESH_TRUNC)
    cv2.imshow('dst', dst)

    retval, dst = cv2.threshold(img, 148, 256, cv2.THRESH_TOZERO)
    cv2.imshow('dst', dst)

    retval, dst = cv2.threshold(img, 148, 256, cv2.THRESH_TOZERO_INV)
    cv2.imshow('dst', dst)

    # 均值滤波
    cv2.imshow('juzhilvbo:', cv2.blur(img, (3, 3)))
    #方框滤波
    cv2.imshow('fangkuanglvbo', cv2.boxFilter(img, -1, (3, 3) ,normalize=False) )
    # 高斯滤波
    cv2.imshow('gaosilvbo', cv2.GaussianBlur(img, (3, 3), sigmaX= 0, ))

    # 延时
    cv2.waitKey(3000)

    # 关闭所有窗口
    cv2.destroyAllWindows()




