# 方框滤波
import cv2

if __name__ == '__main__':
    img = cv2.imread(r'E:\gaofeiSoftWare\PythonWorkSpace\openCV1\image\lenaNoise.png', cv2.IMREAD_UNCHANGED)
    cv2.imshow('origin', img)

    #方框滤波
    b = cv2.boxFilter(img, -1, (2,2), normalize=0)
    cv2.imshow('result-normalize=True', b)

    cv2.waitKey()
    cv2.destroyAllWindows()

