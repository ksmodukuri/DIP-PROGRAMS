# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 23:52:49 2019

@author: Mypc
"""

 

import cv2
import numpy as np
from matplotlib import pyplot as plt
img_blur = cv2.imread('chess.png', 0)
kernelx = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
kernely = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
sobelx = cv2.filter2D(img_blur, -1, kernelx)  
sobely = cv2.filter2D(img_blur, -1, kernely)  
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img_blur, -1, kernelx)
img_prewitty = cv2.filter2D(img_blur, -1, kernely)
kernelx = np.array([[-1,0],[0,1]])
kernely = np.array([[0,-1],[1,0]])
robert_x = cv2.filter2D(img_blur, -1, kernelx)
robert_y = cv2.filter2D(img_blur, -1, kernely)
plt.subplot(241),plt.imshow(img_blur, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(242),plt.imshow(sobelx, cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(243),plt.imshow(sobely, cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.subplot(244),plt.imshow(img_prewittx, cmap = 'gray')
plt.title('Prewitt X'), plt.xticks([]), plt.yticks([])
plt.subplot(245),plt.imshow(img_prewitty, cmap = 'gray')
plt.title('Prewitt Y'), plt.xticks([]), plt.yticks([])
plt.subplot(246),plt.imshow(robert_x, cmap = 'gray')
plt.title('robert X'), plt.xticks([]), plt.yticks([])
plt.subplot(247),plt.imshow(robert_y, cmap = 'gray')
plt.title('Robert Y'), plt.xticks([]), plt.yticks([])
plt.show()

 
