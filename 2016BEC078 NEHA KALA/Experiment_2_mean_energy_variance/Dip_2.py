# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 22:44:31 2019

@author: Neha Kala
"""


import numpy as np
import cv2
from matplotlib import pyplot as plt
img=cv2.imread("Lena.png")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
zero = np.zeros([512,512])
red = cv2.imread("Lena.png")
red[:,:,1]=zero
red[:,:,2]=zero
plt.imshow(red)

blue = cv2.imread("Lena.png")
blue[:,:,0]=zero
blue[:,:,1]=zero
plt.imshow(blue)

green = cv2.imread("Lena.png")
green[:,:,0]=zero
green[:,:,2]=zero
plt.imshow(green)

gray = cv2.imread("Lena.png")
gray[:,:,0]=gray[:,:,2]
gray[:,:,1]=gray[:,:,2]
plt.imshow(gray)
plt.imshow(img[:,:,0])
plt.imshow(img[:,:,1])
plt.imshow(img[:,:,2])


