# -*- coding: utf-8 -*-
import cv2
import numpy as np


cap = cv2.VideoCapture('Pacman Vs Big Domino effect.mp4')
ret = cap.set(3, 640)
ret = cap.set(4, 480)

lower = np.array([20, 80, 80])
upper = np.array([30, 255, 255])


while True:
    # 获取每一帧
    ret, frame = cap.read()
    # 换到 HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 根据阈值构建掩模
    mask = cv2.inRange(hsv, lower, upper)
    # mask = cv2.inRange(hsv, lower_black, upper_black)
    # 对原图像和掩模位运算
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # 显示图像
    cv2.imshow('frame', cv2.resize(frame, (600,400)))
    cv2.imshow('mask', cv2.resize(mask, (600,400)))
    cv2.imshow('res', cv2.resize(res, (600,400)))


    k = cv2.waitKey(1)  # & 0xFF
    if k == ord('q'):
        break
        # 关闭窗口
cap.release()
cv2.destroyAllWindows()
        
 
