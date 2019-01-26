import cv2

# 通过Canny 算子计算边缘
if __name__ == '__main__':
    img = cv2.imread('../image/lena.bmp', cv2.IMREAD_GRAYSCALE)
    cannyImg = cv2.Canny(img, 100, 200)
    cannyImg2 = cv2.Canny(img, 64, 128)

    cv2.imshow('original', img)
    cv2.imshow('cannimg', cannyImg)
    cv2.imshow('cannimg2', cannyImg2)

    cv2.waitKey(10000)
    cv2.destroyAllWindows()
    