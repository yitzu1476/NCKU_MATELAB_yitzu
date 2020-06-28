# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:37:35 2020

@author: joyce
"""

import cv2

# 輸入影片
# video_file 為影片位置 ex: d:/research/my_video.mp4
# cv2.VideoCapture(0) 為開啟電腦原始鏡頭, ex: 筆電前鏡頭
# 若有利用USB額外插入鏡頭, 可用 cv2.VideoCapture(1) 開啟
cap = cv2.VideoCapture('video_file')

# 讀取影片
while(True):
    ret, frame = cap.read()
    if ret:
        # 顯示影片
        cv2.imshow('original',frame)
        
        # 輸出影像
        # new_image_file 為圖片儲存位置
        cv2.imwrite('new_image_file',frame)
        
        # 於影像視窗按 'q' 可提前結束影像
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# 按q結束影片
cap.release()
cv2.waitKey(1)
cv2.destroyAllWindows()
