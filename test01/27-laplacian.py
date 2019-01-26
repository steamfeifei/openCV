import cv2

# 采用拉普拉斯算子计算边界
if __name__ == '__main__':
    img = cv2.imread('../image/lena.bmp', cv2.IMREAD_GRAYSCALE)
    laplacianimg = cv2.Laplacian(img, cv2.CV_64F)
    laplacianimg = cv2.convertScaleAbs(laplacianimg)
    cv2.imshow('laplacianimg', laplacianimg)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()
    