# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 23:26:35 2019

@author: Mypc
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
img = cv2.imread('lenna.jpg',0)  
plt.subplot(2,2,1)
plt.imshow(img, cmap = 'gray')
plt.title('Input image')
a=np.fft.fft2(img)
fshift = np.fft.fftshift(a)
magnitude_spectrum = 20*np.log(np.abs(fshift))
plt.subplot(2,2,2)
plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('magnitude plot of fftshift')
b=np.fft.ifftshift(fshift)
m1 = 20*np.log(np.abs(b))
plt.subplot(2,2,3)
plt.imshow(m1, cmap = 'gray')
plt.title('magnitude plot of ifftshift')
c=np.fft.ifft2(b)
m3 = 20*np.log(np.abs(c))
plt.subplot(2,2,4)
plt.imshow(m3, cmap = 'gray')
plt.title('magnitude plot of ifft')
plt.show()
cv2.waitKey(0)
#cv2.distroyAllWindow()


 
