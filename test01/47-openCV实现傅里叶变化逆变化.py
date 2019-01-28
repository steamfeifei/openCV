import numpy as np
import matplotlib.pyplot as plt
import cv2

if __name__ == '__main__':
    img = cv2.imread('../image/lena.bmp', 0)

    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    dftshift = np.fft.fftshift(dft)

    ishift = np.fft.ifftshift(dftshift)
    iImg = cv2.idft(ishift)

    img1 = cv2.magnitude(iImg[:,:,0], iImg[:,:,1])

    plt.subplot(121)
    plt.title('result')
    plt.axis('off')
    plt.imshow(img1, cmap='gray')

    plt.subplot(122)
    plt.title('original')
    plt.axis('off')
    plt.imshow(img, cmap='gray')

    plt.show()

