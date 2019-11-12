# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 10:44:12 2019

@author: Mypc
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
def a(block,q):
    m = 8
    mean=np.mean(block)
    std=np.std(block)
    return mean - std*(np.sqrt(q/m-q))
def b(block,q):
    m = 8
    mean=np.mean(block)
    std=np.std(block)
    if(std==0):
        return mean
    else:
        return mean +std*(np.sqrt(m-q/q))
img = cv2.imread("lena.jpg",0)
plt.subplot(121)
plt.title("Original image")
plt.imshow(img,cmap='gray')
for i in range(128):
    for j in range(128):
        img1 = img[i*4:i*4+4,j*4:j*4+4]
        patch = img1 - np.mean(img1)
        patch[patch >= 0] = 1
        patch[patch < 0] = 0
        q = 16 - np.count_nonzero(patch)
        patch[patch >= 0] = b(img1,q)
        patch[patch < 0] = a(img1,q)
        img[i*4:i*4+4,j*4:j*4+4] = patch
cv2.imwrite("img1.jpg",img)
plt.subplot(122)
plt.title("output image")
plt.imshow(img,cmap='gray')

         

