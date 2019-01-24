import numpy as np
# import cv2
#
# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = cap.read()     # 第一个参数为True/False,是否读到图片，第二个参数为截道德每一帧德图片
#     # print(ret, frame)
#     print(cap.get(3), cap.get(4))
#
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     cv2.imshow('frame', gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()
#
#
# cap = cv2.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2BGR)
#     cv2.imshow('frame', gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

import numpy as np
import cv2

