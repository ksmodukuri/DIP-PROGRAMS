#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 07:34:05 2019

@author: romil
"""

import cv2
from matplotlib import pyplot as plt
import numpy as np

lena = cv2.imread('/home/romil/Downloads/lena.png',0)
flower = cv2.imread('/home/romil/Downloads/baboon.png',0)

fourier_lena = np.fft.fft2(lena)
fourier_flower = np.fft.fft2(flower)

lena_mag, lena_phase = np.abs(fourier_lena), np.angle(fourier_lena)
flower_mag, flower_phase = np.abs(fourier_flower), np.angle(fourier_flower)
z = complex(0,1); 

flower_lena = flower_mag*np.exp(z*lena_phase);
lena_flower = lena_mag*np.exp(z*flower_phase);

final_flower_lena = np.fft.ifft2(flower_lena)
final_flower_lena = np.abs(final_flower_lena)

final_lena_flower = np.fft.ifft2(lena_flower)
final_lena_flower = np.abs(final_lena_flower)

plt.subplot(2,2,1)
plt.imshow(lena,cmap = 'gray')
plt.subplot(2,2,2)
plt.imshow(flower,cmap = 'gray')
plt.subplot(2,2,3)
plt.imshow(final_flower_lena,cmap = 'gray')
plt.subplot(2,2,4)
plt.imshow(final_lena_flower,cmap = 'gray')

