# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 23:38:24 2019

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
pha = 0
out =np.abs(fft)*np.exp(1j*pha)
print(out)
out = np.fft.ifft2(out)
New_img = 20*np.log(np.abs(out))
print(New_img)
plt.subplot(1,2,2)
plt.title("pha=0")
plt.imshow(New_img , cmap = 'gray')

