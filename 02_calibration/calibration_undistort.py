# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 20:53:57 2020

@author: joyce
"""

import cv2
import numpy as np

# 輸入影像
# image_file 為影像位置 ex: d:/research/my_image.jpg
img = cv2.imread('image_file')

# 參數設定
mtx = np.array([[0,0,0],[0,0,0],[0,0,0]])
dist = np.array([[0.0,0.0,0.0,0.0,0.0]])

mtx[0][0] = para1
mtx[0][1] = 0
mtx[0][2] = para2
mtx[1][0] = 0
mtx[1][1] = para3
mtx[1][2] = para4
mtx[2][0] = 0
mtx[2][1] = 0
mtx[2][2] = 1

dist[0][0] = para5
dist[0][1] = para6
dist[0][2] = para7
dist[0][3] = para8
dist[0][4] = para9

# 校正
undist = cv2.undistort(img, mtx, dist, None, mtx)

# 顯示圖片
cv2.imshow('original', img)
cv2.imshow('after', undist)

# 關閉圖片顯示視窗
# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()

