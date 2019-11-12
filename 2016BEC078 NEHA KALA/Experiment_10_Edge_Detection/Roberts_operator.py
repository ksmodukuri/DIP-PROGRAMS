# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 23:51:21 2019

@author: Neha Kala
"""

#Roberts Edge Detector
import numpy as np
from matplotlib import pyplot as plt
import cv2

img=cv2.imread("lena.png",0)
img1=np.pad(img, (1,1), 'constant', constant_values=(0,0))
plt.subplot(131)
plt.title("Grayscale_lena",fontsize=20)  
plt.imshow(img,cmap="gray")

new_img=np.zeros([512,512])
w=np.array([[1,0],[0,-1]])

for i in range(512):
    for j in range(512):
        z=img1[i:i+2,j:j+2]*w
        a=np.sum(z)
        
        new_img[i][j]=int(abs(a))
        
plt.subplot(132)        
plt.title("Vertical_mask_Roberts",fontsize=20)  
plt.imshow(new_img,cmap='gray')

new_img=np.zeros([512,512])
w1=np.array([[0,1],[-1,0]])

for i in range(512):
    for j in range(512):
        z=img1[i:i+2,j:j+2]*w1
        a=np.sum(z)
        
        new_img[i][j]=int(abs(a))
        
        
plt.subplot(133)        
plt.title("Horizontal_mask_Roberts",fontsize=20)  
plt.imshow(new_img,cmap='gray')


