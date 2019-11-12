# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 22:47:46 2019

@author: Neha Kala
"""

import cv2
from matplotlib import pyplot as plt
img=cv2.imread("lenagray.jpg")

for r in range(0,255):
    for c in range(0,255):
        if img[:,:,1][r][c]>=0 and img[:,:,1][r][c]<127:
            img[:,:,1][r][c]=0
        elif img[:,:,1][r][c]>=64 and img[:,:,1][r][c]<255:
            img[:,:,1][r][c]=225
        

img[:,:,0]=img[:,:,1]
img[:,:,2]=img[:,:,1]
plt.imshow(img)