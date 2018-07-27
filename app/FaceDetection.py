import numpy as np
import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('../static/classifier/haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('../static/classifier/haarcascade_eye.xml')

while():
    # img = cv2.imread('../static/image/snapshot.jpg')
    ret, img = cap.read()
    gray = img  # cv2.cvtColor(img, cv2.COLOR_BAYER_BG2GRAY)  # load input image in grayscale mode

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
