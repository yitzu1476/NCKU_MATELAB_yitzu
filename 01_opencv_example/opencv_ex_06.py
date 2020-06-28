# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 15:06:12 2020

@author: joyce
"""

# resource
# https://blog.gtwang.org/programming/opencv-drawing-functions-tutorial/

import cv2

# 輸入影像
# image_file 為影像位置 ex: d:/research/my_image.jpg
img = cv2.imread('image_file')

# 加入文字
# (影像, 文字, 座標, 字型, 大小, 顏色, 線條寬度, 線條種類)
text = 'Hello World!'
text_img = cv2.putText(img, text, (10, 80), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1, cv2.LINE_AA)

# 加入直線
# (影像, 開始座標, 結束座標, 顏色, 線條寬度)
line_img = cv2.line(img, (0, 0), (255, 255), (0, 0, 255), 5)

# 加入方框
# (影像, 頂點座標, 對向頂點座標, 顏色, 線條寬度)
# 若線條寬度為負, 則方框內部顏色填滿
box_img = cv2.rectangle(img, (20, 60), (120, 160), (0, 255, 0), 2)

# 加入圓圈
# (影像, 圓心座標, 半徑, 顏色, 線條寬度)
# 若線條寬度為負, 則圓圈內部顏色填滿
ball_img = cv2.circle(img,(90, 210), 30, (0, 255, 255), 3)

# 顯示圖片
cv2.imshow('after', img)

# 關閉圖片顯示視窗
# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()

