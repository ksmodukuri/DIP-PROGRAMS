# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 23:30:45 2019

@author: Mypc
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

img = cv2.imread('white_black.jpg',0)
plt.subplot(3,3,1)
plt.title('input image')
plt.imshow(img,cmap='gray')
a=np.fft.fft2(img)
fshift = np.fft.fftshift(a)
magnitude_spectrum = 20*np.log(np.abs(fshift))
d=np.angle(fshift)
plt.subplot(3,3,2)
plt.title('magnitude plot')
plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.subplot(3,3,3)
plt.title('phase plot')
plt.imshow(d, cmap = 'gray')

img1 = cv2.imread('white.jpg',0)
plt.subplot(3,3,4)
plt.title('input image')
plt.imshow(img1,cmap='gray')
a1=np.fft.fft2(img1)
fshift = np.fft.fftshift(a1)
magnitude_spectrum1 = 20*np.log(np.abs(fshift))
d1=np.angle(fshift)
plt.subplot(3,3,5)
plt.title('magnitude plot')
plt.imshow(magnitude_spectrum1, cmap = 'gray')
plt.subplot(3,3,6)
plt.title('phase plot')
plt.imshow(d1, cmap = 'gray')

img2= cv2.imread('black.png',0)
plt.subplot(3,3,7)
plt.title('input image')
plt.imshow(img2,cmap='gray')

a2=np.fft.fft2(img2)
fshift = np.fft.fftshift(a2)
magnitude_spectrum2 = 20*np.log(np.abs(fshift))
d2=np.angle(fshift)
plt.subplot(3,3,8)
plt.title('magnitude plot')
plt.imshow(magnitude_spectrum2, cmap = 'gray')
plt.subplot(3,3,9)
plt.title('phase plot')
plt.imshow(d2, cmap = 'gray')
plt.show()
cv2.waitKey(0)
#cv2.distroyAllWindow()
