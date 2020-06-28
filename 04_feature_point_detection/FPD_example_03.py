# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 20:22:25 2020

@author: joyce
"""

# resource
# https://chtseng.wordpress.com/2017/06/02/%E5%81%B5%E6%B8%AC%E7%A7%BB%E5%8B%95%E4%B8%AD%E7%9A%84%E7%89%A9%E9%AB%94%E4%B8%A6%E5%8F%96%E5%BE%97%E5%85%B6%E5%BD%B1%E5%83%8F/

import cv2
import numpy as np
import imutils

# 設定kernel
blur = np.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])
edged = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])

# 開啟相機
cap = cv2.VideoCapture(0)

while True:
    # 讀取影像
    _, img1 = cap.read()
    _, img2 = cap.read()
    aft_frame = img2
    
    # 參數預設
    all_a = []
    all_x = []
    all_y = []
    all_w = []
    all_h = []
    
    # 影像灰階且模糊化
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    blur1 = cv2.filter2D(gray1,-1,blur)
    blur2 = cv2.filter2D(gray2,-1,blur)
    
    # 影像比對且邊緣銳化
    diff = cv2.absdiff(blur1, blur2)
    diff = cv2.filter2D(diff, -1, edged)
    
    # 抓取特徵位置
    find = False
    contours = cv2.findContours(diff,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        ara = cv2.contourArea(contour)
        if x > 20 and x+w < 560 and ara > 2000 and ara < 8000:
            find = True
            all_a.append(ara)
            all_x.append(x)
            all_y.append(y)
            all_w.append(w)
            all_h.append(h)
    if find == True:
        max_a = max(all_a)
        for item in range(len(all_a)):
            if max_a == all_a[item]:
                max_index = item
                x = all_x[item]
                y = all_y[item]
                w = all_w[item]
                h = all_h[item]
        # 繪製特徵位置
        aft_frame = cv2.rectangle(img2, (x, y), (x+w, y+h), (255,0,0), 5)
        
    # 顯示影像
    cv2.imshow('after', aft_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 按q結束影片
cap.release()
cv2.waitKey(1)
cv2.destroyAllWindows()
    
