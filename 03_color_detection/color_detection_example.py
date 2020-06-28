# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 15:42:01 2020

@author: joyce
"""

import cv2
import numpy as np
import imutils

# 輸入影像
# image_file 為影像位置 ex: d:/research/my_image.jpg
img = cv2.imread('image_file')
aft_img = img

# 影像轉換為HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 顏色範圍設定
lower = np.array([0,50,120])
upper = np.array([10,255,255])

# 執行顏色辨識
red_mask = cv2.inRange(hsv, lower, upper)
contours = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
for contour in contours:
    # 取得顏色面積
    area = cv2.contourArea(contour)
    # 框選顏色區域
    x, y, w, h = cv2.boundingRect(contour)
    aft_img = cv2.rectangle(aft_img, (x, y), (x+w, y+h), (255,0,0), 5)

# 顯示圖片
cv2.imshow('after', aft_img)

# 關閉圖片顯示視窗
# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()