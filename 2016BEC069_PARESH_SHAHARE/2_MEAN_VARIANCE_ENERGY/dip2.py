# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 01:45:35 2019

@author: Paresh Shahare   
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import copy

img=cv2.imread("lena5.jpg")
plt.imshow(img)

rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
im=copy.deepcopy(img)

#cv2.imshow('Image_original',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

sum=0
for i in range(512):
    for j in range(512):
        sum = sum + gray[i][j]
mean1=sum/(512*512)
print('Average of grayscale image :: {}'.format(mean1))

s=0
for i in range(3):
    for j in range(512):
        for k in range(512):
            s+=img[:,:,i][j][k]
c_avg=s/(512*512*3)
print('Average of color image :: {}'.format(c_avg))

f_mean_c=cv2.mean(img)
f_mean_g=cv2.mean(gray)
c_mean=(f_mean_c[0]+f_mean_c[1]+f_mean_c[2])/3
g_mean=f_mean_g[0]
print('Average of color image using opencv function :: {}'.format(c_mean))
print('Average of grayscale image using opencv function :: {}'.format(g_mean))

#VARIANCE

v_s=0
for i in range(3):
    for j in range(512):
        for k in range(512):
            v_s=v_s+((img[:,:,i][j][k]-f_mean_c)**2/(512*512*3))
var=(v_s/(512*512*3))
# print(v_s.sum()/3)
print('variance of image :: {}'.format(var))

def entropy(signal):
        lensig=signal.size
        symset=list(set(signal))
        numsym=len(symset)
        propab=[np.size(signal[signal==i])/(1.0*lensig) for i in symset]
        ent=np.sum([p*np.log2(1.0/p) for p in propab])
        return ent
    
greyIm=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

N=5
S=greyIm.shape
E=np.array(greyIm)
for row in range(S[0]):
        for col in range(S[1]):
                Lx=np.max([0,col-N])
                Ux=np.min([S[1],col+N])
                Ly=np.max([0,row-N])
                Uy=np.min([S[0],row+N])
                region=greyIm[Ly:Uy,Lx:Ux].flatten()
                E[row,col]=entropy(region)
                
plt.imshow(E)
plt.imshow(E, cmap=plt.cm.jet)

img=cv2.imread("lena5.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img1=copy.deepcopy(img)
img2=copy.deepcopy(img)
img3=copy.deepcopy(img)

img1[:,:,1]=0
img1[:,:,2]=0
plt.subplot(131)
plt.imshow(img1)
cv2.imshow('Blue',img1)

img2[:,:,0]=0
img2[:,:,2]=0
plt.subplot(132)
plt.imshow(img2)
cv2.imshow('Green',img2)

img3[:,:,0]=0
img3[:,:,1]=0
plt.subplot(133)
plt.imshow(img3)
cv2.imshow('Red',img3)
cv2.imshow('Image_original',im)
cv2.waitKey(0)
cv2.destroyAllWindows()