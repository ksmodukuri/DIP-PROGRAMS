# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 10:42:34 2019

@author: DSPLAB_USER
"""

#import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lenna.jpg',0)

cv2.imshow('img',img)

half = cv2.resize(img, (0, 0), fx = 0.1, fy = 0.1) 
cv2.imshow('img',img)

stretch_near = cv2.resize(img, (780, 540),interpolation = cv2.INTER_NEAREST)
cv2.imshow('stretch_near',stretch_near)

cv2.waitKey()
#cv2.distroyAllWindows() 
plt.show()
