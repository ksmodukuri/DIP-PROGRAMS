# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 23:47:32 2019

@author: Neha Kala
"""


import numpy as np
from matplotlib import pyplot as plt
import cv2
img=cv2.imread("hexagon.png",0)
plt.subplot(141)
plt.title("Grayscale_Hexagon",fontsize=20)  
plt.imshow(img,cmap="gray")
img1=np.pad(img, (1,1), 'constant', constant_values=(0,0))
new_img1=np.zeros([512,512])
new_img2=np.zeros([512,512])
w=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])

for i in range(512):
    for j in range(512):
        z=img1[i:i+3,j:j+3]*w
        a=np.sum(z)
        new_img1[i][j]=int(abs(a))
        
plt.subplot(142)        
plt.title("Vertical_mask_sobel",fontsize=20)  
plt.imshow(new_img1,cmap='gray')
w1=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
for i in range(512):
    for j in range(512):
        z=img1[i:i+3,j:j+3]*w1
        a=np.sum(z)  
        new_img2[i][j]=int(abs(a)) 
plt.subplot(143)        
plt.title("Horizontal_mask_sobel",fontsize=20)  
plt.imshow(new_img2,cmap='gray')

y=((new_img1)**2+(new_img2)**2)**(1/2)
plt.subplot(144)
plt.title("Magnitude",fontsize=20)
plt.imshow(y,cmap='gray')



