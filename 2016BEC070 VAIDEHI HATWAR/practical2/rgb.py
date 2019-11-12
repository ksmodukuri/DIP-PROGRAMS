# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 22:27:53 2019

@author: Mypc
"""

import cv2
image = cv2.imread('lena.jpg') #original image
cv2.imshow('lena', image)
b = image.copy()
b[:, :, 0] = 0 # set green and red channels to 0
b[:, :, 1] = 0
g = image.copy()
g[:, :, 0] = 0 # set blue and red channels to 0
g[:, :, 2] = 0
r = image.copy()
r[:, :, 1] = 0 # set blue and green channels to 0
r[:, :, 2] = 0
cv2.imshow('B-RGB', b) # RGB - Blue
cv2.imshow('G-RGB', g) # RGB - Green
cv2.imshow('R-RGB', r) # RGB - Red
cv2.waitKey(0)

