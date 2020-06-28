# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:12:05 2020

@author: joyce
"""

# resource
# https://www.itread01.com/content/1542925983.html

import cv2

# 輸入影像
# image_file 為影像位置 ex: d:/research/my_image.jpg
# 第二參數 0 為使影像成為灰階
img = cv2.imread('image_file', 0)

# 邊緣檢測
x = cv2.Sobel(img,cv2.CV_16S,1,0)
y = cv2.Sobel(img,cv2.CV_16S,0,1)
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)

# 加權邊緣檢測
dst = cv2.addWeighted(absX,0.5,absY,0.5,0)

# X方向邊緣檢測, 影像顯示
cv2.imshow("absX", absX)

# Y方向邊緣檢測, 影像顯示
cv2.imshow("absY", absY)

# 整體邊緣檢測, 影像顯示
cv2.imshow("Result0", dst)

# 關閉圖片顯示視窗
# 按下任意鍵則關閉所有視窗 
cv2.waitKey(0)
cv2.destroyAllWindows()
