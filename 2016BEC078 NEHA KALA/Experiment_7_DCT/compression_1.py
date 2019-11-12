# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 23:34:52 2019

@author: Neha Kala
"""


import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.fftpack import dct,idct

img = cv2.imread('lena.png',0)
z = np.zeros([512,512])

for i in range(64):
    for j in range(64):
        img8 = img[i*8:i*8+8, j*8:j*8+8]
        dct0 = dct(img8)
        dct1 = np.transpose(dct0)
        dct2 = dct(dct1)
        
        for m in range(8):
            for n in range(8):
                if m >= 4 or n >=4:
                    dct2[m][n] = 0
       
        idct0 = idct(dct2)
        idct1 = np.transpose(idct0)
        idct2 = np.round(idct(idct1)/256)
       
        z[i*8:i*8+8, j*8:j*8+8] = idct2
       
        
plt.subplot(121)      
plt.imshow(img,cmap='gray')
plt.title('Original Lena',fontsize=25)
plt.subplot(122)        
plt.imshow(z,cmap='gray')
plt.title('after compression',fontsize=25)
cv2.imwrite('Figure_1.png',z)
cv2.imwrite('Figure_2.png',img)

psnr = 10*np.log10((255*255)/(1/(512*512)*np.sum(z-img)*np.sum(z-img)))
print('PSNR Value:',psnr)