# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 23:20:03 2019

@author: Neha Kala
"""


import numpy as np
import cv2
import matplotlib.pyplot as plt
img=cv2.imread("checkerboard.jpg",0)
img1=np.rot90(img)
plt.subplot(2,3,1)
plt.imshow(img)
H=cv2.calcHist([img],[0],None,[256],[0,256])
plt.subplot(2,3,2)
plt.plot(H)

z=np.zeros(256)
for i in img:
    for j in i:
        z[j]=z[j]+1
plt.subplot(2,3,3)
plt.plot(z)

plt.subplot(2,3,4)
plt.imshow(img1)
H=cv2.calcHist([img1],[0],None,[256],[0,256])
plt.subplot(2,3,5)
plt.plot(H)

z=np.zeros(256)
for i in img:
    for j in i:
        z[j]=z[j]+1
plt.subplot(2,3,6)
plt.plot(z)


for i in range(256):
    z[i]=z[i]/(256*256)
    
for i in range(256):
    z[i]=z[i]+z[i-1]
plt.plot(z)
plt.title('CDF')
