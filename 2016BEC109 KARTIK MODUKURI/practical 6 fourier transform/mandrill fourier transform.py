# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 09:15:24 2019

@author: KARTIK
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread(r"D:\Btech practicals\DIP\mandrill.jpg",0)
f1 = np.fft.fft2(img1)
fshift1 = np.fft.fftshift(f1)
magnitude_spectrum1 = 20*np.log(np.abs(fshift1))
phase_spectrum1 = np.angle(fshift1)

plt.subplot(331)
plt.imshow(img1,cmap='gray')

plt.subplot(332)
plt.imshow(magnitude_spectrum1,cmap = 'gray')

plt.subplot(333)
plt.imshow(phase_spectrum1,cmap='gray')

img2 = cv2.imread(r"D:\Btech practicals\DIP\2_gray.jpg",0)  
f2 = np.fft.fft2(img2)
fshift2 = np.fft.fftshift(f2)
magnitude_spectrum2 = 20*np.log(np.abs(fshift2))
phase_spectrum2 = np.angle(fshift2)

plt.subplot(334)
plt.imshow(img2,cmap='gray')

plt.subplot(335)
plt.imshow(magnitude_spectrum2,cmap = 'gray')

plt.subplot(336)
plt.imshow(phase_spectrum2,cmap='gray')

combined1 = np.multiply(np.abs(f1), np.exp(1j*np.angle(f2)))
imgCombined1 = np.real(np.fft.ifft2(combined1))

plt.subplot(337)
plt.imshow(imgCombined1,cmap='gray')

combined2 = np.multiply(np.abs(f2), np.exp(1j*np.angle(f1)))
imgCombined2 = np.real(np.fft.ifft2(combined2))

plt.subplot(338)
plt.imshow(imgCombined2,cmap='gray')
