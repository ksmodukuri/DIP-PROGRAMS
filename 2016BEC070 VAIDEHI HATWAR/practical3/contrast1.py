# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 11:15:01 2019

@author: Mypc
"""




import cv2
from matplotlib import pyplot as plt
img=cv2.imread("lena.jpg")

for r in range(0,225):
    for c in range(0,225):
        if img[:,:,1][r][c]>=0 and img[:,:,1][r][c]<127:
            img[:,:,1][r][c]=0
        elif img[:,:,1][r][c]>=64 and img[:,:,1][r][c]<255:
            img[:,:,1][r][c]=225
       

img[:,:,0]=img[:,:,1]
img[:,:,2]=img[:,:,1]
plt.imshow(img)