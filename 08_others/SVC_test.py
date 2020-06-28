# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:36:39 2020

@author: joyce
resource:
https://medium.com/jameslearningnote/%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90-%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-%E7%AC%AC3-4%E8%AC%9B-%E6%94%AF%E6%8F%B4%E5%90%91%E9%87%8F%E6%A9%9F-support-vector-machine-%E4%BB%8B%E7%B4%B9-9c6c6925856b
https://www.itread01.com/content/1547640374.html
https://dotblogs.com.tw/kevinya/2018/06/13/110051
https://dotblogs.com.tw/kevinya/2018/06/13/082449

"""

import numpy as np
from sklearn.svm import SVC

clf = SVC(gamma='scale')

x = np.array([[1,1], [2,1], [3,1], [1,2], [2,2], [1,3], [6,1], [5,2], [6,2], [4,3], [5,3], [6,3], [3,4], [4,4], [5,4], [6,4]])
y = np.array([1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2])

clf.fit(x, y)
#clf.predict(x)

k = clf.predict([[-1,3]])
print(k)