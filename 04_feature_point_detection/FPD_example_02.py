# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 20:13:34 2020

@author: joyce
"""

import cv2

# 輸入影像
# image_file 為影像位置 ex: d:/research/my_image.jpg
img = cv2.imread('image_file')

# FAST特徵偵測
fast = cv2.FastFeatureDetector_create()
fast.setNonmaxSuppression(0)
kp = fast.detect(img,None)

# 繪製特徵位置
for i in range(len(kp)):
    aft_img = cv2.circle(img, (int(kp[i].pt[0]), int(kp[i].pt[1])), 3, (0, 255, 255), -1)

# 顯示圖片
cv2.imshow('after', aft_img)

# 關閉圖片顯示視窗
# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()
