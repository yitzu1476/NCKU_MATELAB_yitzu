# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:45:40 2020

@author: joyce
"""

# resourse
# http://aishack.in/tutorials/image-convolution-examples/
# https://medium.com/%E9%9B%9E%E9%9B%9E%E8%88%87%E5%85%94%E5%85%94%E7%9A%84%E5%B7%A5%E7%A8%8B%E4%B8%96%E7%95%8C/%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-ml-note-convolution-neural-network-%E5%8D%B7%E7%A9%8D%E7%A5%9E%E7%B6%93%E7%B6%B2%E8%B7%AF-bfa8566744e9

import cv2
import numpy as np

# 輸入影像
# image_file 為影像位置 ex: d:/research/my_image.jpg
img = cv2.imread('image_file')

# 多種kernel
sharpen = np.array([[1,1,1],[1,-7,1],[1,1,1]])
edged = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
strut = np.array([[-1,-1,0],[-1,0,1],[0,1,1]])
blur = np.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])
horizon = np.array([[-1,-1,-1],[2,2,2],[-1,-1,-1]])
vertical = np.array([[-1,2,-1],[-1,2,-1],[-1,2,-1]])
deg45 = np.array([[-1,-1,2],[-1,2,-1],[2,-1,-1]])
sobel_edge_h = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
sobel_edge_v = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])

# kernel = 欲使用之kernel
kernel = sharpen
new_img = cv2.filter2D(img,-1,kernel)

# 顯示影像
cv2.imshow('new',new_img)

# 關閉圖片顯示視窗
# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()