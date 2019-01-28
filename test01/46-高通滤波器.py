import numpy as np
import matplotlib.pyplot as plt
import cv2

if __name__ == '__main__':
    img = cv2.imread('../image/lena.bmp', cv2.IMREAD_GRAYSCALE)

    # 傅里叶变换
    f  = np.fft.fft2(img)
    fftshift = np.fft.fftshift(f)

    # 覆盖
    rows, cols = img.shape
    crow, col = int(rows / 2), int(cols / 2)
    fftshift[crow - 10:crow + 10, col - 10:col + 10] = 0
    ishift = np.fft.ifftshift(fftshift)
    iimg = np.fft.ifft2(ishift)
    iimg = np.abs(iimg)

    # 图像显示
    plt.subplot(121)
    plt.imshow(img, cmap='gray')

    plt.subplot(122)
    plt.imshow(iimg, cmap='gray')

    plt.show()



    