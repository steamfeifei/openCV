import cv2
import numpy as np

# 开运算， 先腐蚀图片再膨胀图片，针对的都是白色
if __name__ == '__main__':
    img = cv2.imread('../image/opening.bmp', cv2.IMREAD_UNCHANGED)
    cv2.imshow('original', img)

    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel=np.ones((10, 10), np.uint8))
    cv2.imshow('morphologyEx', img)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()