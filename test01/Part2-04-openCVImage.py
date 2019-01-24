import numpy as np
import cv2

img = cv2.imread('../images/2.jpg', 1)   # 读入彩色图片数据
cv2.imshow('image', img)     # 显示图片数据,图片标题为image
k = cv2.waitKey(0)      # 程序等待时间键盘输入,参数0为永久知道键盘输入，1000为一秒输入一次
cv2.destroyAllWindows()     # 关闭所有打开的窗口
print(k)    # 打印在焦点图片上输入的键盘asiic码值
cv2.imwrite('../images/gaofei.png', img)    # 保存一个图像


