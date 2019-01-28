import numpy as np
import matplotlib.pyplot as plt
import cv2

if __name__ == '__main__':
    img = cv2.imread('../image/lena.bmp', cv2.IMREAD_GRAYSCALE)

    f = np.fft.fft2(img)    # 返回一个傅里叶变换后的复数数组
    fshift = np.fft.fftshift(f)     # 将零频率分量移动到频谱中心
    result = 20 * np.log(np.abs(fshift))    # 设置频谱范围，将频谱映射到【0， 255】范围内，以便显示图像

    plt.subplot(221)
    plt.imshow(img, cmap='gray')
    plt.axis('off')

    plt.subplot(222)
    plt.imshow(result, cmap='gray')
    plt.axis('off')

    plt.show()
