# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 20:41:38 2019

@author: KARTIK
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r'D:\Btech practicals\DIP\lena.png',0)

def binn(num):
    bin_num = [int(i) for i in list('{0:0b}'.format(num))]
    for j in range(8 - len(bin_num)):
        bin_num.insert(0,0)        
    return bin_num

def decimal(listt):
    x = 0
    for i in range(8):
        x = x + int(listt[i])*(2**(7-i))
    return x

def bit_change(bit,img):
    z = np.zeros([512,512])
    for i in range(512):
        for j in range(512):
            x = binn(img[i][j])
            for k in range(8):
                if k == bit:
                    x[k] = x[k]
                else:
                    x[k] = 0
            x1 = decimal(x)
            z[i][j] = x1
    return z

if __name__ == "__main__":
    for i in range(1,9):
        plt.subplot(2,4,i)
        plt.imshow(bit_change(i-1,img),cmap = 'gray')
