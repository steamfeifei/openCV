import numpy as np
import cv2

if __name__ == '__main__':
    img = cv2.imread('../image/boat.jpg')
    img1 = cv2.imread('../image/boat.jpg')
    hist = cv2.calcHist([img], [0], None, [256], [0, 255])
    print(hist)