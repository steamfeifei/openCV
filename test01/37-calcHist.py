import matplotlib.pyplot as plt
import cv2

# 通过openCV 计算直方图数据 的数目
if __name__ == '__main__':
    img = cv2.imread('../image/boat.jpg', cv2.IMREAD_UNCHANGED)
    histb = cv2.calcHist([img], [0], None, [256], [0, 255])
    histg = cv2.calcHist([img], [1], None, [256], [0, 255])
    histr = cv2.calcHist([img], [2], None, [256], [0, 255])

    plt.plot(histb,'b.')
    plt.plot(histg,'g-')
    plt.plot(histr,'y-')

    plt.show()
