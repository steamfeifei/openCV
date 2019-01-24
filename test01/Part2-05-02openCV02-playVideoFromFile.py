import numpy as np
import cv2

'''
    从文件中导入视频文件
'''

# 方法二：报错
if __name__ == '__main__':
    # cap = cv2.VideoCapture(r'E:\gaofeiSoftWare\studyDirs\01-python-全栈三期-版本管理工具介绍.mp4')
    cap = cv2.VideoCapture(r'E:\\gaofeiSoftWare\\PythonWorkSpace\\openCV1\\videos\\1.mp4')
    while cap.isOpened():
        print(1)
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

