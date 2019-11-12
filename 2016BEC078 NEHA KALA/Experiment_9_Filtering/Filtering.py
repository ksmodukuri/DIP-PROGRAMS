# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 23:39:43 2019

@author: Neha Kala
"""



#Averaging_filtering

import numpy as np
from matplotlib import pyplot as plt
import cv2

img1=cv2.imread("lena.png",0)
plt.subplot(241)
plt.title("Original_Lena",fontsize=20)
plt.imshow(img1,cmap="gray")
img=np.pad(img1, (1,1), 'constant', constant_values=(0,0))
new_img=np.zeros([512,512])
w=np.array([[1,1,1],[1,1,1],[1,1,1]])

for i in range(512):
    for j in range(512):
        z=img[i:i+3,j:j+3]*w
        a=np.sum(z)
        new_img[i][j]=int(a/9)
plt.subplot(242)        
plt.title("After_averaging",fontsize=20)
plt.imshow(new_img,cmap='gray')
psnr = 10*np.log10((255*255)/(1/(512*512)*np.sum(img1-new_img)*np.sum(img1-new_img)))
print('PSNR Value(Averaging):',psnr)


#minimum_filtering
new_img1=np.zeros([512,512])
w1=np.array([[1,1,1],[1,1,1],[1,1,1]])
for i in range(512):
    for j in range(512):
        z1=img[i:i+3,j:j+3]*w1
        a1=np.min(z1)
        
        new_img1[i][j]=int(a1)
        
plt.subplot(243)   
plt.title("Minimum_filtering",fontsize=20)     
plt.imshow(new_img1,cmap='gray')
psnr = 10*np.log10((255*255)/(1/(512*512)*np.sum(img1-new_img1)*np.sum(img1-new_img1)))
print('PSNR Value(minimum):',psnr)



#maximum_filtering

new_img2=np.zeros([512,512])
w2=np.array([[1,1,1],[1,1,1],[1,1,1]])

for i in range(512):
    for j in range(512):
        z2=img[i:i+3,j:j+3]*w2
        a2=np.max(z2)
        
        new_img2[i][j]=int(a2)
        
plt.subplot(244)        
plt.title("Maximum_filtering",fontsize=20)     
plt.imshow(new_img2,cmap='gray')
psnr = 10*np.log10((255*255)/(1/(512*512)*np.sum(img1-new_img2)*np.sum(img1-new_img2)))
print('PSNR Value(maximum):',psnr)


#median filtering
def med(w):
    r=[]
    for i in range(3):
        for j in range(3):
            r.append(w[i][j])
    r.sort()
    return r[5]
 
img1=cv2.imread("salt_lena.png",0)
img=np.pad(img1, (1,1), 'constant', constant_values=(0,0))
plt.subplot(245)
plt.title("Salt and Pepper Noise",fontsize=20)
plt.imshow(img,cmap="gray")

new_img=np.zeros([512,512])
w=np.array([[1,1,1],[1,1,1],[1,1,1]])

for i in range(512):
    for j in range(512):
        z=img[i:i+3,j:j+3]*w
        
        
        new_img[i][j]=med(z)
        
plt.subplot(246) 
plt.title("Median_Filtering",fontsize=20)       
plt.imshow(new_img,cmap='gray')
psnr = 10*np.log10((255*255)/(1/(512*512)*np.sum(img1-new_img)*np.sum(img1-new_img)))
print('PSNR Value(Median):',psnr)


#Gaussian_filtering
img1=cv2.imread("lena.png",0)
img=np.pad(img1, (1,1), 'constant', constant_values=(0,0))
g = cv2.GaussianBlur(img,(3,3),0)
plt.subplot(247)
plt.title("Gaussian_Filtering",fontsize=20)
plt.imshow(g,cmap='gray')
psnr = 10*np.log10((255*255)/(1/(512*512)*np.sum(img-g)*np.sum(img-g)))
print('PSNR Value(Gaussian):',psnr)
