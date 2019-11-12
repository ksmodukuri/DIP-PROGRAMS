# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 23:38:04 2019

@author: Neha Kala
"""



import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('lena.png',0)
plt.subplot(331)
plt.title("Grayscale_Lena",fontsize=20)
plt.imshow(img,cmap="gray")

def binary(n):
    num = [int(i) for i in list('{0:0b}'.format(n))]
    for j in range(8 - len(num)):
        num.insert(0,0)        
    return num

def decimal(listt):
    x = 0
    for i in range(8):
        x = x + int(listt[i])*(2**(7-i))
    return x


def bit_slicing(bit,img):
    z = np.zeros([512,512])
    for i in range(512):
        for j in range(512):
            x = binary(img[i][j])
            for k in range(8):
                if k == bit:
                    x[k] = x[k]
                else:
                    x[k] = 0
            x1 = decimal(x)
            z[i][j] = x1
    return z


plt.subplot(332)
plt.title("Bit_slice_7",fontsize=20)
plt.imshow(bit_slicing(0,img),cmap = 'gray')
plt.subplot(333)
plt.title("Bit_slice_6",fontsize=20)
plt.imshow(bit_slicing(1,img),cmap = 'gray')
plt.subplot(334)
plt.title("Bit_slice_5",fontsize=20)
plt.imshow(bit_slicing(2,img),cmap = 'gray')
plt.subplot(335)
plt.title("Bit_slice_4",fontsize=20)
plt.imshow(bit_slicing(3,img),cmap = 'gray')
plt.subplot(336)
plt.title("Bit_slice_3",fontsize=20)
plt.imshow(bit_slicing(4,img),cmap = 'gray')
plt.subplot(337)
plt.title("Bit_slice_2",fontsize=20)
plt.imshow(bit_slicing(5,img),cmap = 'gray')
plt.subplot(338)
plt.title("Bit_slice_1",fontsize=20)
plt.imshow(bit_slicing(6,img),cmap = 'gray')
plt.subplot(339)
plt.title("Bit_slice_0",fontsize=20)
plt.imshow(bit_slicing(7,img),cmap = 'gray')    