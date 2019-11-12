# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 23:22:23 2019

@author: Mypc
"""


import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread("pout1.jpg",0)
cv2.imshow('Input Image',img)
z = np.zeros(256)
c = np.zeros(256)
print(img.shape)
for i in range (img.shape[0]):
    for j in range (img.shape[1]):
        k = img[i,j]
        z[k] = z[k] + 1
plt.plot(z)
plt.title('Histogram Without using function')
plt.show()
for i in range (256):  # Probablity of occurance
    c[i] = z[i]/(img.shape[0]*img.shape[1])
for i in range (255):
    c[i] = c[i] + c[i-1]
plt.plot(c)
plt.title('CDF')
plt.show()
c = c*255
c = np.round_(c)
print(c)
c=c.astype(np.uint8) # converted to int
print(c)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        g=img[i,j]
        img[i,j]=c[g]
cv2.imshow('Histogram Equalization',img)
cv2.waitKey()


 
