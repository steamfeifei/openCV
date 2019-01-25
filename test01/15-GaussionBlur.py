# 高斯滤波
import cv2

if __name__ == '__main__':
    img = cv2.imread(r'E:\gaofeiSoftWare\PythonWorkSpace\openCV1\image\lenaNoise.png', cv2.IMREAD_UNCHANGED)
    cv2.imshow('origin', img)

    d = cv2.GaussianBlur(img, (3, 3), sigmaX=0)     #图像源，核大小， x方向权重
    cv2.imshow('高斯滤波', d)

    cv2.waitKey()
    cv2.destroyAllWindows()
