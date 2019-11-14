#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 15:44:10 2019

@author: romil
"""
from skimage import io
import numpy as np
import cv2
from matplotlib import pyplot as plt
img1 = io.imread('/home/romil/Downloads/export.png')
img1 = img1[:,:,2]
plt.subplot(3,3,1)
plt.imshow(img1,cmap = 'gray')
plt.title('image 1')

img2 = io.imread('/home/romil/Downloads/export (1).png')
img2 = 255 - img2[:,:,2]
plt.subplot(3,3,2)
plt.imshow(img2,cmap = 'gray')
plt.title('image 2')

new_img = img1 + img2
plt.subplot(3,3,3)
plt.imshow(new_img,cmap = 'gray')
plt.title('addition')

new_img = img2 - img1
plt.subplot(3,3,4)
plt.imshow(new_img,cmap = 'gray')
plt.title('subtraction')

new_img = img1 * img2
plt.subplot(3,3,5)
plt.imshow(new_img,cmap = 'gray')
plt.title('multiplication')

new_img = img2 / img1
plt.subplot(3,3,6)
plt.imshow(new_img,cmap = 'gray')
plt.title('division')

new_img = cv2.bitwise_or(img1,img2)
plt.subplot(3,3,7)
plt.imshow(new_img,cmap = 'gray')
plt.title('or')

new_img = cv2.bitwise_and(img1,img2)
plt.subplot(3,3,8)
plt.imshow(new_img,cmap = 'gray')
plt.title('and')