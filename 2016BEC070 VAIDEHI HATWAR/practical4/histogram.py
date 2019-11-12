# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 22:48:26 2019

@author: Mypc
"""



import cv2
import numpy as np
import matplotlib.pyplot as plt 
img = cv2.imread('chess.png',1) 
plt.subplot(3,3,1)
plt.title('original img')
plt.imshow(img)
histr = cv2.calcHist([img],[0],None,[256],[0,256]) 
plt.subplot(3,3,2)
plt.title('histogram with command ')
plt.plot(histr) 
c=np.zeros(256)
print(img.shape)
for i in img:
    for j in i:
        c[j]=c[j]+1
plt.subplot(3,3,3)
plt.title('histogram without command')
plt.plot(c)        
img1=np.rot90(img)
plt.subplot(3,3,4)
plt.title('original img')
plt.imshow(img1) 
histr1 = cv2.calcHist([img1],[0],None,[256],[0,256]) 
plt.subplot(3,3,5)
plt.title('histogram with command')
plt.plot(histr1) 
c=np.zeros(256)
print(img.shape)
for i in img1:
    for j in i:
        c[j]=c[j]+1
plt.subplot(3,3,6)
plt.title('histogram without command')
plt.plot(c)      
img2 = cv2.imread('images.png',1) 
plt.subplot(3,3,7)
plt.title('original img')
plt.imshow(img2)
histr2 = cv2.calcHist([img],[0],None,[256],[0,256]) 
plt.subplot(3,3,8)
plt.title('histogram with command')
plt.plot(histr2) 
c1=np.zeros(256)
print(img.shape)
for i in img2:
    for j in i:
        c1[j]=c1[j]+1
plt.subplot(3,3,9)
plt.title('histogram without command')
plt.plot(c)        
  




