# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 23:41:48 2019

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
m = 20*np.log(np.abs(fshift))
b=np.fft.ifftshift(fshift)
c=np.fft.ifft2(b)
c1=np.angle(fshift)
img1=cv2.imread('baboon.jpg',0)  
plt.subplot(2,2,2)
plt.imshow(img1, cmap = 'gray')
plt.title('Input image')
a1=np.fft.fft2(img1)
fshift1 = np.fft.fftshift(a1)
m1= 20*np.log(np.abs(fshift1))
b1=np.fft.ifftshift(fshift1)
c2=np.fft.ifft2(b1)
c3=np.angle(fshift1)
#Recompute frequency responses by swapping the phases
out1 = np.abs(fshift) * np.exp(1j*c3)
out2 = np.abs(fshift1) * np.exp(1j*c1)
#Find the inverse images
out1 = np.fft.ifft2(out1)
out2 = np.fft.ifft2(out2)
#Show the images
plt.subplot(2,2,3)
plt.imshow(abs(out1),cmap='gray')
plt.subplot(2,2,4)
plt.imshow(abs(out2),cmap='gray')
plt.show()
cv2.waitKey(0)
#cv2.distroyAllWindow()


 
