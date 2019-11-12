# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 23:17:04 2019

@author: Mypc
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt       
img= cv2.imread('chess.png',1) 
plt.subplot(2,2,1)
plt.title('original img')
plt.imshow(img)
histr= cv2.calcHist([img],[0],None,[256],[0,256]) 
plt.subplot(2,2,2)
plt.title('histogram with command ')
plt.plot(histr) 
c=np.zeros(256)
print(img.shape)
for i in img:
    for j in i:
        c[j]=c[j]+1
plt.subplot(2,2,3)
plt.title('histogram without command ')
plt.plot(c)        
for i in range(256):
    c[i]=c[i]/(256*256)
for i in range(256):
    c[i]=c[i]+c[i-1]
plt.subplot(2,2,4)
plt.title('cdf')
plt.plot(c)    


 

