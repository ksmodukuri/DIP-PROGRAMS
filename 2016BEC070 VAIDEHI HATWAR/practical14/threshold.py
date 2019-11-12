# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 09:55:39 2019

@author: DSPLAB_USER
"""



import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('new.jpg',0)
# global thresholding
ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# adaptive thresholding
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
images = [img, 0, th1,
          img, 0, th3,
          img, 0, th2]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Original Noisy Image','Histogram',"Adaptive thresholding"]
for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(# Otsu's thresholding
images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()

