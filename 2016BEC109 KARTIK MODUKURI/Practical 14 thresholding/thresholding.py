# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 10:15:41 2019

@author: KARTIK
"""

import cv2
from matplotlib import pyplot as plt
img=cv2.imread(r"D:\usimages\2008.png",0)
plt.subplot(321)
plt.imshow(img,cmap='gray')
plt.title('Original image',fontsize=20)

# global thresholding
ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
plt.subplot(322)
plt.imshow(th1,cmap='gray')
plt.title('Global Thresholding',fontsize=20)
# Otsu's thresholding
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
plt.subplot(323)
plt.imshow(th2,cmap='gray')
plt.title('Otsu Thresholding',fontsize=20)


th4 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
plt.subplot(324)
plt.imshow(th4,cmap='gray')
plt.title('Adaptive Mean Thresholding',fontsize=20)

th5 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
plt.subplot(325)
plt.imshow(th5,cmap='gray')
plt.title('Adaptive Gaussian Thresholding',fontsize=20)
