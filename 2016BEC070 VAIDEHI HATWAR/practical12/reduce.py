# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 22:59:25 2019

@author: Mypc
"""

import numpy as np
import matplotlib.pyplot as plt 
import cv2
img=cv2.imread("lenna.jpg",0)
plt.subplot(221)
plt.imshow(img,cmap='gray');plt.axis('off');plt.title('Orinal')
print(img.shape[0],img.shape[1])
a=np.zeros((256,256))
for i in range(0,256):
    for j in range(0,256):
        a[i,j]=img[2*i,2*j]
        j=j+1
    i=i+1    
plt.subplot(222)
plt.imshow(a,cmap='gray');plt.axis('off');plt.title('Resize 256')
print(a.shape[0],a.shape[1])
b=np.zeros((128,128))
for i in range(0,128):
    for j in range(0,128):
        b[i,j]=a[2*i,2*j]
        j=j+1
    i=i+1    
plt.subplot(223)
plt.imshow(b,cmap='gray');plt.axis('off');plt.title('Resize  128')
print(b.shape[0],b.shape[1])
c=np.zeros((64,64))
for i in range(0,64):
    for j in range(0,64):
        c[i,j]=b[2*i,2*j]
        j=j+1
    i=i+1    
plt.subplot(224)
plt.imshow(c,cmap='gray');plt.axis('off');plt.title('Resize  64')
print(c.shape[0],c.shape[1])
 

