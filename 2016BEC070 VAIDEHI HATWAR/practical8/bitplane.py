# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 23:46:22 2019

@author: Mypc
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r'images.jpg',0)

psnr=10*np.log10((255*255)/(1/(225*225)*np.sum(img)*np.sum(img)))
print('psnr',psnr)

def cov_binary(num):
    binary_num = [int(i) for i in list('{0:0b}'.format(num))]
    for j in range(8 - len(binary_num)):
        binary_num.insert(0,0)        
    return binary_num
def conv_decimal(listt):
    x = 0
    for i in range(8):
        x = x + int(listt[i])*(2**(7-i))
    return x
def discriminate_bit(bit,img):
    z = np.zeros([225,225])
    for i in range(225):
        for j in range(225):
            x = cov_binary(img[i][j])
            for k in range(8):
                if k == bit:
                    x[k] = x[k]
                else:
                    x[k] = 0
            x1 = conv_decimal(x)
            z[i][j] = x1
    return z
for i in range(1,9):
    plt.subplot(2,5,i)
    plt.imshow(discriminate_bit(i-1,img),cmap = 'gray')
    plt.xticks([]), plt.yticks([])