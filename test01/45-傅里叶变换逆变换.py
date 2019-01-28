import numpy as np
import matplotlib.pyplot as plt
import cv2

if __name__ == '__main__':
    img = cv2.imread('../image/boat.bmp', cv2.IMREAD_GRAYSCALE)

    # 实现傅里叶变换
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)

    ifshift = np.fft.ifftshift(fshift)
    iimg = np.fft.ifft2(ifshift)

    iimg = np.abs(iimg)

    plt.subplot(121)
    plt.imshow(img, cmap='gray')
    plt.axis('off')

    plt.subplot(122)
    plt.imshow(iimg, cmap='gray')
    plt.axis('off')

    plt.show()
