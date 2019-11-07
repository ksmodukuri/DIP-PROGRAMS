# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 09:16:00 2019

@author: KARTIK
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

def a(small_patch,q):
    m = 16
    return np.mean(small_patch) - np.std(small_patch)*(np.sqrt(q/m-q))

def b(small_patch,q):
    m = 16
    if(np.std(small_patch)==0):
        return np.mean(small_patch)
    else:
        return np.mean(small_patch) + np.std(small_patch)*(np.sqrt(m-q/q))


img = cv2.imread(r"C:\Users\itsna\Desktop\ops\lena.png",0)
plt.subplot(121)
plt.title("original image")
plt.imshow(img,cmap='gray')

for i in range(128):
    for j in range(128):
        small_img = img[i*4:i*4+4,j*4:j*4+4]
        patch = small_img - np.mean(small_img)
        patch[patch >= 0] = 1
        patch[patch < 0] = 0
        q = 16 - np.count_nonzero(patch)
        patch[patch >= 0] = b(small_img,q)
        patch[patch < 0] = a(small_img,q)
        
        img[i*4:i*4+4,j*4:j*4+4] = patch

plt.subplot(122)
plt.title("original image after coding")
plt.imshow(img,cmap='gray')

        
