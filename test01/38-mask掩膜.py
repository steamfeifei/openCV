import matplotlib.pyplot as plt
import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread('../image/girl.bmp', cv2.IMREAD_GRAYSCALE)
    mask = np.zeros(img.shape, dtype=np.uint8)
    mask[200:400, 200:400] = 255

    imghist = cv2.calcHist([img], [0], None, [256], [0, 255])
    hist = cv2.calcHist([img], [0], mask, [256], [0, 255])
    print(hist)
    plt.plot(imghist, 'r-')
    plt.plot(hist,'b-')
    plt.show()
