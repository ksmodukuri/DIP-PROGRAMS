# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 22:40:11 2019

@author: Mypc
"""

import cv2
a=cv2.imread("lenna.jpg",0)
cv2.imshow('lenna',a)
b="lena.jpg"
cv2.imwrite(b,a)
print(a)
cv2.waitKey(0)
cv2.destroyAllWindows('lenna')

 

