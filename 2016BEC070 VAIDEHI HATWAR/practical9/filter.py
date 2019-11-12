# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 23:47:41 2019

@author: Mypc
"""

import cv2
from matplotlib import pyplot as plt 
import numpy as np 
img = cv2.imread('lenna.jpg', 0)
kernel = np.array( [ [1,1,1], [1,1,1], [1,1,1] ])
kernel = 1.0/9.0 * kernel
mean = cv2.filter2D(img, -1, kernel)
median = cv2.medianBlur(img, 3) # going with 3*3 kernel size
g_low = cv2.GaussianBlur(img, (3,3), 0)
plt.subplot(221),plt.imshow(img, cmap='gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(mean, cmap='gray'),plt.title('mean')
plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(median, cmap='gray'),plt.title('median')
plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(g_low, cmap='gray'),plt.title('Gaussian')
plt.xticks([]), plt.yticks([])
plt.show()
psnr=10*np.log10((255*255)/(1/(225*225)*np.sum(img)*np.sum(img)))
print('psnr',psnr)

psnr1=10*np.log10((255*255)/(1/(225*225)*np.sum(mean)*np.sum(mean)))
print('psnr1',psnr1)
 
psnr2=10*np.log10((255*255)/(1/(225*225)*np.sum(median)*np.sum(median)))
print('psnr2',psnr2)

psnr3=10*np.log10((255*255)/(1/(225*225)*np.sum(g_low)*np.sum(g_low)))
print('psnr3',psnr3)