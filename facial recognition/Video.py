import numpy as np
import cv2

# 將haarcascade_frontalface_default.xml的檔案位置放在cascPath
cascPath = "C:\\users\\bread\\AppData\\Roaming\\Python\\Python37\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml"

face_cascade = cv2.CascadeClassifier(cascPath) #告訴OpenCV使用人臉辨識分類器

cap = cv2.VideoCapture('D:\\jupyter\\test.mp4')  #匯入影片

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor = 1.3,
        minNeighbors = 4,     
        minSize = (30, 30)
        )
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2) 
        
    cv2.imshow('video',img)
   
    if cv2.waitKey(30) & 0xff == 27: # press 'ESC' to quit
        break
                
cap.release()
cv2.destroyAllWindows()
