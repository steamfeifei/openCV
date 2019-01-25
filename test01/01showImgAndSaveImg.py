import numpy as np
import cv2

# 显示文件
i = cv2.imread(r'../images/2.jpg')
cv2.imshow('Demo中文', i)     # 中文乱码
cv2.waitKey(0)
cv2.destroyAllWindows()

# 保存文件
cv2.imwrite(r'../images/2_1.jpg', i)
print(i)

