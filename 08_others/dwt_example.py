# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 19:32:22 2020

@author: joyce
"""

import pywt

path = 'data_1.txt'

arr = []
with open(path, 'r') as f:
    cnt = 0
    for item in f:
        ll = len(item)
        arr.append(float(item[:ll-1]))
        cnt = cnt + 1

# db1為可更改參數
cA, cD = pywt.dwt(arr, 'db1')

with open('data_1_cd.txt', 'w') as df:
    for item in range(len(cD)):
        df.write(str(cD[item]))
        df.write('\n')
df.close()
