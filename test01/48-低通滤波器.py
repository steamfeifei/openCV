import numpy as np
import matplotlib.pyplot as plt
import cv2

if __name__ == '__main__':
    img = cv2.imread('../image/lena.bmp', 0)

    # 正向傅里叶变化
    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    dftshift = np.fft.fftshift(dft)

    # 低通滤波
    rows, cols = img.shape
    crow, col = int(rows / 2), int(cols / 2)
    mask = np.zeros((rows, cols, 2), np.uint8)
    mask[crow - 50:crow + 50, col - 50:col + 50] = 1

    fshift = dftshift * mask

    # 反向傅里叶变换
    ishift = np.fft.ifftshift(fshift)
    iImg = cv2.idft(ishift)
    iImg = cv2.magnitude(iImg[:,:,0], iImg[:,:,1])

    plt.subplot(121)
    plt.title('original')
    plt.axis('off')
    plt.imshow(img, cmap='gray')

    plt.subplot(122)
    plt.title('result')
    plt.axis('off')
    plt.imshow(iImg, cmap='gray')

    plt.show()


