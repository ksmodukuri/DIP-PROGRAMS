# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 23:28:55 2019

@author: Mypc
"""

 
import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
img = cv2.imread('baboon.jpg',0)
plt.subplot(2,3,1)
plt.title('input image')
plt.imshow(img,cmap='gray')
a=np.fft.fft2(img)
fshift = np.fft.fftshift(a)
magnitude_spectrum = 20*np.log(np.abs(fshift))
d=np.angle(fshift)
plt.subplot(2,3,2)
plt.title('magnitude plot')
plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.subplot(2,3,3)
plt.title('phase plot')
plt.imshow(d, cmap = 'gray')
img1 = cv2.imread('lenna.jpg',0)
plt.subplot(2,3,4)
plt.title('input image')
plt.imshow(img1,cmap='gray')
a1=np.fft.fft2(img1)
fshift = np.fft.fftshift(a1)
magnitude_spectrum1 = 20*np.log(np.abs(fshift))
d1=np.angle(fshift)
plt.subplot(2,3,5)
plt.title('magnitude plot')
plt.imshow(magnitude_spectrum1, cmap = 'gray')
plt.subplot(2,3,6)
plt.title('phase plot')
plt.imshow(d1, cmap = 'gray')
plt.show()
cv2.waitKey(0)
#cv2.distroyAllWindow()