import cv2
import numpy as np

i = cv2.imread('../images/2.jpg', cv2.IMREAD_UNCHANGED)     # 读取没有改变原色彩的图像
p = i[100, 100]     #输入100行100列的像素值
# print(p, type(p))
cv2.imshow('original', i)
i[100, 100] = [255, 100, 100]
print(i[100, 100])
i[100: 150, 100: 150] = [255, 255, 255]
cv2.imshow('ret', i)
cv2.waitKey(0)
cv2.destroyAllWindows()

i = cv2.imread('../images/2.jpg', cv2.IMREAD_GRAYSCALE)
print(i.item(100, 100))
i.itemset((100, 100), 255)
print(i.item(100, 100))
