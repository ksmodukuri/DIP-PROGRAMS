# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 21:26:10 2019

@author: Admin
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r'D:\Btech practicals\DIP\lena5.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(gray)
cv2.imshow("Gray_original",gray)
cv2.imwrite('2_gray.jpg',gray)
for i in range(512):
    for j in range(512):
        k=gray[i][j]
        if k<128:
            gray[i][j]=0
        elif k>127 and k<256:
            gray[i][j]=255
cv2.imwrite('Quantized_2_gray.jpg',gray)
cv2.imshow("Gray_histogram",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()