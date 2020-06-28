# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:52:39 2020

@author: joyce
"""

# resorce
# https://www.itread01.com/content/1547978590.html

import cv2

# 輸入影像
# image_file 為影像位置 ex: d:/research/my_image.jpg
img = cv2.imread('image_file')

# 轉為灰階
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 特殊顏色code, 參見參考資料
code_img = cv2.cvtColor(img,53)

# 顯示圖片
cv2.imshow('original', img)
cv2.imshow('gray', gray_img)
cv2.imshow('code', code_img)

# 輸出圖片
# new_image_file 為圖片儲存位置
cv2.imwrite('new_image_file',gray_img)
cv2.imwrite('new_image_file',code_img)

# 關閉圖片顯示視窗
# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()