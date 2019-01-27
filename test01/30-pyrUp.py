import cv2

# 向下取样
if __name__ == '__main__':
    img = cv2.imread('../image/lena.bmp', cv2.IMREAD_UNCHANGED)

    img1 = cv2.pyrUp(img)
    img2 = cv2.pyrUp(img1)
    img3 = cv2.pyrUp(img2)

    cv2.imshow('original:', img)
    cv2.imshow('result1:', img1)
    cv2.imshow('result2:', img2)
    cv2.imshow('result3:', img3)

    cv2.waitKey(3000)
    cv2.destroyAllWindows()
