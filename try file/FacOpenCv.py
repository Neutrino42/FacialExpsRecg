import cv2
import os 
import sys
import json
import time
import numpy as np
from keras.models import model_from_json

# face_cascade = cv2.CascadeClassifier(r'E:\Python3.6\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml') # 加载人脸特征库
# eye_cascade = cv2.CascadeClassifier(r'E:\Python3.6\Lib\site-packages\cv2\data\haarcascade_eye.xml')

# emotion_labels = ['angry', 'fear', 'happy', 'sad', 'surprise', 'neutral']

# if __name__ == '__main__':
#     # ret, frame = cap.read() # 读取一帧的图像
#     img = cv2.imread("hhh.jpg")
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 转灰

#     faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.15, minNeighbors = 5, minSize = (5, 5)) # 检测人脸
#     for(x, y, w, h) in faces:
#         cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2) # 用矩形圈出人脸

#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#     cv2.imshow('Face Recognition', gray)

#     cv2.destroyAllWindows()
#     # print('Hello Word')

# load json and create model arch
json_file = open('/.../model.json','r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)

# load weights into new model
model.load_weights('/.../model.h5')

def predict_emotion(face_image_gray): # a single cropped face
    resized_img = cv2.resize(face_image_gray, (48,48), interpolation = cv2.INTER_AREA)
    # cv2.imwrite(str(index)+'.png', resized_img)
    image = resized_img.reshape(1, 1, 48, 48)
    list_of_list = model.predict(image, batch_size=1, verbose=1)
    angry, fear, happy, sad, surprise, neutral = [prob for lst in list_of_list for prob in lst]
    return [angry, fear, happy, sad, surprise, neutral]

# -------------------直接预测-----------------------
img_gray = cv2.imread("hhh.jpg")
img_gray = cv2.cvtColor(img_gray, cv2.COLOR_BGR2GRAY)
angry, fear, happy, sad, surprise, neutral = predict_emotion(img_gray)

# -------------------人脸预测-----------------------
# 加载检测器
faceCascade = cv2.CascadeClassifier(r'E:\Python3.6\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml') # 加载人脸特征库

# 图像灰化
img_gray = cv2.imread("hhh.jpg")
img_gray = cv2.cvtColor(img_gray, cv2.COLOR_BGR2GRAY)

# 人脸检测
faces = faceCascade.detectMultiScale(
        img_gray,
        scaleFactor=1.1,
        minNeighbors=1,# minNeighbors=5比较难检测
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

# 表情画框
for (x, y, w, h) in faces:
    face_image_gray = img_gray[y:y+h, x:x+w]
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    angry, fear, happy, sad, surprise, neutral = predict_emotion(face_image_gray)