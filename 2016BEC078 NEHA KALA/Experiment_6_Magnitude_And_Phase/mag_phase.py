# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 23:25:05 2019

@author: Neha Kala
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread("bw1.jpg",0)
plt.subplot(221)
plt.imshow(img, cmap = 'gray')

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude = 20*np.log(1+np.abs(fshift))
plt.subplot(222)
plt.imshow(magnitude, cmap = 'gray')

ishift = np.fft.ifftshift(fshift)
img1 = np.fft.ifft2(ishift)
img1 = np.abs(img1)
plt.subplot(223)
plt.imshow(img1, cmap = 'gray')

phase=np.angle(fshift)
plt.subplot(224)
plt.imshow(phase, cmap = 'gray')


####
img=cv2.imread("wb1.jpg",0)
plt.subplot(221)
plt.imshow(img, cmap = 'gray')

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude = 20*np.log(1+np.abs(fshift))
plt.subplot(222)
plt.imshow(magnitude, cmap = 'gray')

ishift = np.fft.ifftshift(fshift)
img1 = np.fft.ifft2(ishift)
img1 = np.abs(img1)
plt.subplot(223)
plt.imshow(img1, cmap = 'gray')

phase=np.angle(fshift)
plt.subplot(224)
plt.imshow(phase, cmap = 'gray')


