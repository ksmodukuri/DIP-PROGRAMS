# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 21:50:27 2019

@author: Admin
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
#adaptive thresholding
img2 = cv2.imread(r'C:\Users\DSPLAB_USER\Desktop\2016bec017\threshold.jpg',0)
img2 = cv2.medianBlur(img2,5)

ret,th1 = cv2.threshold(img2,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img2,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img2, th1, th2, th3]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()