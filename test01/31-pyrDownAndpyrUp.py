import cv2

# 先向下取样再向上取样
# 先向上取样再向下取样
if __name__ == '__main__':
    img = cv2.imread('../image/girl.bmp', cv2.IMREAD_UNCHANGED)

    # 先向上取样再向下取样
    img1 = cv2.pyrUp(img)
    img2 = cv2.pyrDown(img1)
    cv2.imshow('original:', img)
    cv2.imshow('img1:', img1)
    cv2.imshow('img2:', img2)
    cv2.imshow('img2 - original', img2 - img)

    # 先向下取样再向上取样
    # img1 = cv2.pyrDown(img)
    # img2 = cv2.pyrUp(img1)
    # cv2.imshow('original:', img)
    # cv2.imshow('img1:', img1)
    # cv2.imshow('img2:', img2)
    # cv2.imshow('img2 - original', img2 - img)

    cv2.waitKey(3000)
    cv2.destroyAllWindows()
