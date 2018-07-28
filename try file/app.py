import cv2
import os 

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(r'E:\Python3.6\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml') # 加载人脸特征库
eye_cascade = cv2.CascadeClassifier(r'E:\Python3.6\Lib\site-packages\cv2\data\haarcascade_eye.xml')


if __name__ == '__main__':
    while(True):
        ret, frame = cap.read() # 读取一帧的图像
        gray = frame #cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 转灰

        faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.15, minNeighbors = 5, minSize = (5, 5)) # 检测人脸
        for(x, y, w, h) in faces:
            cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2) # 用矩形圈出人脸

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        cv2.imshow('Face Recognition', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release() # 释放摄像头
    cv2.destroyAllWindows()
    # print('Hello Word')
