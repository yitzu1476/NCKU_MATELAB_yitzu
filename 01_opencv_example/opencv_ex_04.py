# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 13:55:42 2020

@author: joyce
"""

# resource
# https://www.itread01.com/content/1544296868.html

import cv2
import numpy as np

# 輸入影像
# image_file 為影像位置 ex: d:/research/my_image.jpg
img = cv2.imread('image_file')

# 參數設定
# a = 對比度設定，數值越大對比度越大，1為不調整
# b = 亮度設定，數值越大亮度越大，0為不調整
a = 1
b = 0

# 影像處理，除去數值超過範圍之影響
new_img = img * float(a) + b
new_img[new_img > 255] = 255
new_img[new_img < 0] = 0
new_img = np.round(new_img)
new_img = new_img.astype(np.uint8)

# 顯示影像
cv2.imshow('original', img)
cv2.imshow('after', new_img)

# 關閉圖片顯示視窗
# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()