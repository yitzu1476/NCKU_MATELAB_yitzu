# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 20:37:04 2020

@author: joyce
"""

import numpy as np
import cv2
import glob

# 參數設定
# a為校正板x軸交點數, b為y軸交點數
a = 8
b = 6
objpoints = []
imgpoints = [] 
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((a*b,3), np.float32)
objp[:,:2] = np.mgrid[0:a,0:b].T.reshape(-1,2)

# 輸入同資料夾影像
images = glob.glob('*.jpg')

for frame in images:
    img = cv2.imread(frame)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    # 尋找校正板交點
    ret, corners = cv2.findChessboardCorners(gray, (8,6),None)
    
    if ret == False:
        continue
    if ret == True:
        # 標注校正點
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)
        # 顯示標注結果
        img = cv2.drawChessboardCorners(img, (a,b), corners2,ret)
        cv2.imshow('img',img)
        # 顯示延遲
        cv2.waitKey(500)

# 關閉所有視窗
cv2.destroyAllWindows()

# 顯示校正參數
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img.shape[:2],None,None)
print(mtx)
print(dist)