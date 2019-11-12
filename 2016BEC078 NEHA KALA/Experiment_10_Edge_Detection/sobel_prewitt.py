# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 23:50:04 2019

@author: Neha Kala
"""

import numpy as np
from matplotlib import pyplot as plt
import cv2
 
 
img=cv2.imread("lena.png",0)
img1=np.pad(img, (1,1), 'constant', constant_values=(0,0))
plt.subplot(231)
plt.title("Grayscale_lena",fontsize=20)  
plt.imshow(img,cmap="gray")
#Sobel_operator
new_img=np.zeros([512,512])
w=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])

for i in range(512):
    for j in range(512):
        z=img1[i:i+3,j:j+3]*w
        a=np.sum(z)
        
        new_img[i][j]=int(abs(a))
        
plt.subplot(232)        
plt.title("Vertical_mask_sobel",fontsize=20)  
plt.imshow(new_img,cmap='gray')

w1=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
for i in range(512):
    for j in range(512):
        z=img1[i:i+3,j:j+3]*w1
        a=np.sum(z)
        
        new_img[i][j]=int(abs(a))
        
plt.subplot(233)        
plt.title("Horizontal_mask_sobel",fontsize=20)  
plt.imshow(new_img,cmap='gray')



#Prewitt_operator
new_img=np.zeros([512,512])
w=np.array([[-1,0,1],[-1,0,1],[-1,0,1]])

for i in range(512):
    for j in range(512):
        z=img1[i:i+3,j:j+3]*w
        a=np.sum(z)
        
        new_img[i][j]=int(abs(a))
        
plt.subplot(234)       
plt.title("Vertical_mask_Prewitt",fontsize=20)   
plt.imshow(new_img,cmap='gray')

w1=np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
for i in range(512):
    for j in range(512):
        z=img1[i:i+3,j:j+3]*w1
        a=np.sum(z)
        
        new_img[i][j]=int(abs(a))
        
plt.subplot(235)      
plt.title("Horizontal_mask_Prewitt",fontsize=20)  
plt.imshow(new_img,cmap='gray')

