# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 22:25:58 2019

@author: Mypc
"""

import cv2
import matplotlib.pyplot as plt 
a=cv2.imread("lena.jpg")
plt.subplot(1,4,1)
plt.imshow(a)
R=a[:,:,0]
plt.subplot(1,4,2)
plt.imshow(R)
G=a[:,:,1]
plt.subplot(1,4,3)
plt.imshow(G)
B=a[:,:,2]
plt.subplot(1,4,4)
plt.imshow(B)
cv2.waitKey(0)


