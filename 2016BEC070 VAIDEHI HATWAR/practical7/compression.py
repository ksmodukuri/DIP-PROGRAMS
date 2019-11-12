# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 23:07:51 2019

@author: Mypc
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.fftpack import dct,idct

img=cv2.imread('lenna.jpg',0)
z=np.zeros([225,225])
for i in range(28):
    for j in range(28):
        img1=img[i*8:i*8+8,j*8:j*8+8]
        dct0=dct(img1)
        dct1=np.transpose(dct0)
        dct2=dct(dct1)
        
        for m in range(8):
            for n in range(8):
                if m>=4 or n>=4:
                    dct2[m][n]=0
        idct0=idct(dct2)
        idct1=np.transpose(idct0)
        idct2=np.round(idct(idct1)/256)
        z[i*8:i*8+8,j*8:j*8+8]=idct2
plt.subplot(121)
plt.imshow(img,cmap='gray')

plt.title('image')
plt.subplot(122)
plt.imshow(z,cmap='gray')

plt.title('compression')

psnr=10*np.log10((255*255)/(1/(225*225)*np.sum(z-img)*np.sum(z-img)))
print('psnr',psnr)
 

