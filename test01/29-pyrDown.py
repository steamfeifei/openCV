import cv2

# 向下取样
if __name__ == '__main__':
    img = cv2.imread('../image/lena.bmp', cv2.IMREAD_UNCHANGED)

    # 向下取样
    img1 = cv2.pyrDown(img)
    img2 = cv2.pyrDown(img1)
    img3 = cv2.pyrDown(img2)
    img4 = cv2.pyrDown(img3)

    cv2.imshow('img1:', img1)
    cv2.imshow('img2:', img2)
    cv2.imshow('img3:', img3)
    cv2.imshow('img4:', img4)

    cv2.waitKey(3000)
    cv2.destroyAllWindows()
