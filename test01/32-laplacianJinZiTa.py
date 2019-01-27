import cv2

if __name__ == '__main__':
    img = cv2.imread('../image/girl.bmp', cv2.IMREAD_UNCHANGED)

    # 求拉普拉斯金字塔第0层
    od = cv2.pyrDown(img)
    odd = cv2.pyrUp(od)
    cv2.imshow('original:', img)
    cv2.imshow('od0:', img - odd)

    # 求拉普拉斯第一层
    img = od
    od = cv2.pyrDown(img)
    odd = cv2.pyrUp(od)
    cv2.imshow('od1', img - odd)

    cv2.waitKey(10000)
    cv2.destroyAllWindows()
