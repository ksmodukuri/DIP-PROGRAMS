# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 23:34:13 2019

@author: Neha Kala
"""



import numpy as np
from matplotlib import pyplot as plt
import cv2
import math
from scipy.fftpack import dct

img=cv2.imread('lena.png',0)
d=dct(img)

N=4
z=np.zeros([N,N,N,N])

def a(num,N):
    if num == 0:
        return np.sqrt(1/N)
    else:
        return np.sqrt(2/N)

for k in range(N):
    for l in range(N):
        for m in range(N):
            for n in range(N):
                z[k][l][m][n] =  z[k][l][m][n] + a(k,N)*a(l,N)*math.cos(((2*m+1)*3.142*k)/(2*N))*math.cos(((2*n+1)*3.142*l)/(2*N))
                
count = 1                
for i in range(N):
    for j in range(N):
        plt.subplot(N,N,count)
        plt.imshow(z[i][j],cmap = 'gray')
        count +=  1