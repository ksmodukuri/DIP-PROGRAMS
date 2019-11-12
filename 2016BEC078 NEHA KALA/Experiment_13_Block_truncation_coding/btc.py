# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 23:31:08 2019

@author: Neha Kala
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('lena.png', 0)
plt.subplot(121)
plt.imshow(img , cmap = 'gray')
plt.title('Original image',fontsize=20)

def a(x,q):
    return np.mean(x) - np.std(x)*np.sqrt(q/(4-q))

def b(x,q):
    if np.std(x) == 0:
        return np.mean(x)
    else:
        return np.mean(x) + (np.std(x)*np.sqrt((4-q)/q))
    
for i in range(256):
    for j in range(256):
        x = img[i*2:i*2+2,j*2:j*2+2]
        B = x - np.mean(x)             
        B[B >= 0] = 1
        B[B < 0] = 0        
        q = 4 - np.count_nonzero(b)
        B[B > 0] = b(x,q)
        B[B <= 0] = a(x,q)
        img[i*2:i*2+2,j*2:j*2+2] = B
plt.subplot(122)
plt.imshow(img , cmap = 'gray')
plt.title('After BTC',fontsize=20)
