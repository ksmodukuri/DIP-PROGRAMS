# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 23:34:55 2019

@author: Mypc
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('lenna.jpg',0)
plt.subplot(1,2,1)
plt.title("input img")
plt.imshow(img , cmap = 'gray')
fft= np.fft.fft2(img)
mag = np.abs(fft)
pha = np.angle(fft)
mag = 0
out= mag*np.e**(1*pha)
print(out)
out = np.fft.ifft2(out)
img1= 20*np.log(np.abs(out))
print(img1)
plt.subplot(1,2,2)
plt.title("mag=0")
plt.imshow(img1, cmap = 'gray')


 
