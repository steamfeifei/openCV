import cv2
import matplotlib.pyplot as plt

if __name__ == '__main__':
    img = cv2.imread('../image/boat.jpg', cv2.IMREAD_UNCHANGED)
    # img = cv2.imread('../image/lena.bmp', cv2.IMREAD_GRAYSCALE)
    print(img,img.shape,type(img))
    plt.hist(img.ravel(), 256)
    plt.show()
