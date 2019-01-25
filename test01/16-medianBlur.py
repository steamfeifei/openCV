# 中值滤波
import cv2

if __name__ == '__main__':
    img = cv2.imread(r'E:\gaofeiSoftWare\PythonWorkSpace\openCV1\images\IMG_0166.JPG', cv2.IMREAD_UNCHANGED)
    # img = cv2.resize(img, None, fx=5, fy=5)
    cv2.imshow('img', img)

    cov = cv2.medianBlur(img, 3)
    cv2.imshow('cov', cov)

    cv2.waitKey()
    cv2.destroyAllWindows()