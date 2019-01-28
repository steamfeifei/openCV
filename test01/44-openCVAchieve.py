import numpy as np
import matplotlib.pyplot as plt
import cv2

if __name__ == '__main__':
    img = cv2.imread('../image/lena.bmp', 0)

    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    dshift = np.fft.fftshift(dft)
    result = 20 * np.log(cv2.magnitude(dshift[:,:,0], dshift[:,:,1]))

    plt.subplot(121)
    plt.title('original')
    plt.axis('off')
    plt.imshow(img, cmap='gray')

    plt.subplot(122)
    plt.title('result')
    plt.axis('off')
    plt.imshow(result, cmap='gray')

    plt.show()