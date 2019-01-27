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
    img[:200,:200] = 0
    cv2.imshow('修改像素后的图片:', img)

    # 读取像素的方法
    print(img.item(200, 201, 0))

    # 设置图片像素的方法
    img.itemset((200,201,0),255)
    img.itemset((200,201,1),255)
    img.itemset((200,201,2),255)
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

    #





    cv2.waitKey(6000)      #等待键盘按下，默认0，无线等待
    cv2.destroyAllWindows()
