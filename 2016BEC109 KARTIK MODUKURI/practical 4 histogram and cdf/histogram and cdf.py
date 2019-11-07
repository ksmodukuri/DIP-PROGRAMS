# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 09:18:42 2019

@author: students
"""

#histogram
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"D:\Btech practicals\DIP\lena.jpg")
intensity = np.zeros(256) 
t1 = img[:,:,0]
for i in t1:
    for j in i:
        intensity[j] += 1
plt.subplot(321)       
plt.plot(intensity)

for i in range(len(intensity)):
    intensity[i] = intensity[i]/(512*512)
cdf = []
a = 0
for i in intensity:
    a += i
    cdf.append(a)
    
hist1 = cv2.calcHist([img],[0],None,[256],[0,256])
plt.subplot(322)
plt.plot(hist1)

intensity = np.zeros(256)
t2 = img[:,:,1]
for i in t2:
    for j in i:
        intensity[j] += 1
plt.subplot(323)       
plt.plot(intensity)

hist1 = cv2.calcHist([img],[1],None,[256],[0,256])
plt.subplot(324)
plt.plot(hist1)

intensity = np.zeros(256)
t3 = img[:,:,2]
for i in t3:
    for j in i:
        intensity[j] += 1
plt.subplot(325)       
plt.plot(intensity)

hist1 = cv2.calcHist([img],[2],None,[256],[0,256])
plt.subplot(326)
plt.plot(hist1)

plt.plot(cdf)