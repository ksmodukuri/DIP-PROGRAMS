# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 22:28:36 2019

@author: Mypc
"""


import cv2
import matplotlib.pyplot as plt
import numpy
a=cv2.imread("lena.jpg")
sum=0; 
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        for k in range(a.shape[2]):
            sum=sum+a[(i,j,k)]
m=sum/(220*220*3)
print("Mean:",m)
m1=numpy.mean(a)
print("Mean:",m1)

x=(a-m)**2
sum1=0;
for i in range(x.shape[0]):
    for j in range(x.shape[1]):
        for k in range(x.shape[2]):
            sum1=sum1+x[(i,j,k)]
v=sum1/((220*220*3)-1)
print("Variance :",v)            
v1=numpy.var(a)
print("Variance:",v1)
cv2.waitKey(0)
