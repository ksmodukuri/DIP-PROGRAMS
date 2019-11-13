# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 20:36:11 2019

@author: Admin
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r"Downloads/lena.png")
r = img[:,:,0]
z = np.zeros((512,512))
img[:,:,1] = z
img[:,:,2] = z 
#plt.imshow(img)
cv2.imshow("Gray_histogram",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img2 = cv2.imread(r"Downloads/lena.png")
g = img2[:,:,1]
img2[:,:,0] = z
img2[:,:,2] = z
#plt.imshow(img2)
cv2.imshow("Gray_histogram",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

img3 = cv2.imread(r"Downloads/lena.png")
b = img3[:,:,2]
img3[:,:,0] = z
img3[:,:,1] = z
#plt.imshow(img3)
cv2.imshow("Gray_histogram",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
