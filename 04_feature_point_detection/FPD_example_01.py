# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 20:01:20 2020

@author: joyce
"""

import cv2
from matplotlib import pyplot as plt

# 輸入影像
# image_file 為影像位置 ex: d:/research/my_image.jpg
img1 = cv2.imread('image_file')
img2 = cv2.imread('image_file')

# 建立ORB特徵偵測
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# 建立關聯性連結
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1,des2)

# 繪製關聯線條
matches = sorted(matches, key = lambda x:x.distance)
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None, flags=2)

# 顯示圖片
plt.imshow(img3),plt.show()