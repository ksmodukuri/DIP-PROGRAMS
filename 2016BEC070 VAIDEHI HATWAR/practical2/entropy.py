# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 00:23:44 2019

@author: Mypc
"""

import numpy as np
import cv2
import math

img = cv2.imread('lena.jpg',0)
histogram = cv2.calcHist([img],[0],None,[256],[0,256])
total = np.sum(histogram)
z= 0
for i in range(256):
    p = histogram[i]/total
    if p != 0:
        z=z-p * math.log(p, 2)
    else:
        pass

print("Entropy is ",z[0])



