# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 23:29:08 2019

@author: Neha Kala
"""

import numpy as np
from matplotlib import pyplot as plt
import cv2

img1=cv2.imread("lena.png",0)
img2=cv2.imread("baboon.jpg",0)

f1 = np.fft.fft2(img1)
fshift1 = np.fft.fftshift(f1)
magnitude1 = 20*np.log(1+np.abs(fshift1))
mag1=np.abs(fshift1)

f2 = np.fft.fft2(img2)
fshift2= np.fft.fftshift(f2)
magnitude2 = 20*np.log(1+np.abs(fshift2))
mag2=np.abs(fshift2)

phase1=np.angle(fshift1)
phase2=np.angle(fshift2)

j=complex(0,-1)

def changer(mag,phase):
    mix = mag*np.exp(j*phase)
    mix_time=np.abs(np.fft.ifft2(mix))
    mix_time=np.rot90(mix_time,2)
    return mix_time

x = changer(mag1,phase2)
y = changer(mag2,phase1)
plt.subplot(121)
plt.imshow(x,cmap='gray')
plt.subplot(122)
plt.imshow(y,cmap='gray')
