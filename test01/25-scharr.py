import cv2

# 使用scharr算子计算边界
if __name__ == '__main__':
    img = cv2.imread('../image/scharr.bmp', cv2.IMREAD_GRAYSCALE)

    scharrx = cv2.Scharr(img, cv2.CV_64F, 1, 0)
    scharrx = cv2.convertScaleAbs(scharrx)

    scharry = cv2.Scharr(img, cv2.CV_64F, 0, 1)
    scharry = cv2.convertScaleAbs(scharry)

    ret = cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)
    cv2.imshow('ret:', ret)

    cv2.waitKey(3000)
    cv2.destroyAllWindows()