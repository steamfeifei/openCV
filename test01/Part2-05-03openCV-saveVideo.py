import numpy as np
import cv2

'''
    从文件中导入视频文件
'''

#保存视频
if __name__ == '__aa__':
    path = r'E:\\gaofeiSoftWare\\PythonWorkSpace\\openCV1\\videos\\2.avi'
    cap = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(path, fourcc, 20.0, (640, 480))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frame = cv2.flip(frame, 0)
            out.write(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


