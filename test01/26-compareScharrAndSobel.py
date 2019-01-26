import cv2

# 比较Sobel算子 和 Scharr 算子
if __name__ == '__main__':
    img = cv2.imread('../image/lena.bmp', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('original', img)

    # 使用Sobel算子
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
    sobelx = cv2.convertScaleAbs(sobelx)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)
    sobely = cv2.convertScaleAbs(sobely)

    sobelimg = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
    cv2.imshow('sobel', sobelimg)

    # 使用 Scharr 算子
    scharrx = cv2.Scharr(img, cv2.CV_64F, 1, 0)
    scharrx = cv2.convertScaleAbs(scharrx)
    scharry = cv2.Scharr(img, cv2.CV_64F, 0, 1)
    scharry = cv2.convertScaleAbs(scharry)

    scharrimg = cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)
    cv2.imshow('scharr', scharrimg)

    # 测试 取绝对值应该在每一次计算Scharr算子后 获取绝对值，不应该是都取玩以后再取 ，这样会消去一些点
    # 造成比正常图像更黑
    scharrx = cv2.Scharr(img, cv2.CV_64F, 1, 0)
    scharry = cv2.Scharr(img, cv2.CV_64F, 0, 1)
    scharrimg = cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)
    scharrimg = cv2.convertScaleAbs(scharrimg)
    cv2.imshow('scharrimgTest', scharrimg)

    cv2.waitKey(10000)
    cv2.destroyAllWindows()
