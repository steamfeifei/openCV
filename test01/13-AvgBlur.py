# 均值滤波
import cv2

if __name__ == '__main__':
    img = cv2.imread(r'E:\gaofeiSoftWare\PythonWorkSpace\openCV1\image\lenaNoise.png', cv2.IMREAD_UNCHANGED)
    cv2.imshow('img', img)

    # 均值滤波
    a = cv2.blur(img, (3, 3))
    cv2.imshow('a', a)

    cv2.waitKey()
    cv2.destroyAllWindows()
