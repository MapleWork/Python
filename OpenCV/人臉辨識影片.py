import numpy as np
import  cv2

cascPath = "D:\\Data\\Face Recognition\\haarcascade_frontalface_default.xml"

face_cascade = cv2.CascadeClassifier(cascPath)

cap = cv2.VideoCapture('D:\\Data\\Face Recognition\\tw.mp4')

ret, frame = cap.read()
avg = cv2.blur(frame, (4, 4))
avg_float = np.float32(avg)


while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret == False:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor = 1.3,
        minNeighbors = 4,
        minSize = (30,30)
    )
    
    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    
    cv2.imshow('video',frame)
    
    if cv2.waitKey(30) & 0xff == 27:
        break
        
cap.release()
cv2.destroyAllWindows()
