# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 17:05:47 2019

@author: KARTIK
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread("D:\Btech practicals\DIP\pout.jpg",0)
plt.subplot(231)
plt.imshow(img,cmap='gray')

pixels=np.zeros(256)
for i in img:
    for j in i:
        pixels[j]=pixels[j]+1
    total=sum(pixels)
for i in range(256):
    pixels[i]=pixels[i]/total
for i in range(256):
    pixels[i]=pixels[i]+pixels[i-1]
for i in range(256):
    pixels[i]=pixels[i]*255
    pixels[i]=round(pixels[i])
    
for i in range(len(img)):
    for j in range(len(img[0])):
        img[i][j]=pixels[img[i][j]]
        
plt.subplot(232)
plt.imshow(img,cmap='gray')
