import numpy as np
import cv2
import matplotlib.pyplot as plt

if __name__ == '__main__':
    img = cv2.imread('../image/girl.bmp', cv2.IMREAD_UNCHANGED)
    print(img.shape)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 使用 plt.imshow 显示图像
    # 显示灰色图片
    plt.subplot(221)
    plt.imshow(img, cmap=plt.cm.gray)
    plt.axis('off')
    plt.subplot(222)
    plt.imshow(img)
    plt.axis('off')
    plt.subplot(223)
    plt.imshow(gray)
    plt.axis('off')
    plt.subplot(224)
    plt.imshow(gray, cmap=plt.cm.gray )

    plt.show()
    plt.axis('off')

    # 显示彩色图片
    b, g, r = cv2.split(img)
    pltimg = cv2.merge([r, g, b])
    plt.imshow(pltimg)
    plt.show()
