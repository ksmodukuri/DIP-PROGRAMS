# -*- coding: utf-8 -*-


import cv2
from matplotlib import pyplot as plt

img = cv2.imread(r"D:\Btech practicals\DIP\lena.png",0)

img_1 = cv2.blur(img,(5,5))

plt.subplot(321)
plt.imshow(img,cmap = 'gray')
plt.title('Original Image')
plt.subplot(322)
plt.imshow(img_1,cmap = 'gray')
plt.title('Average filter')

gausian_blur = cv2.GaussianBlur(img,(5,5),0)

plt.subplot(323)
plt.imshow(img,cmap = 'gray')
plt.title('Original Image')

plt.subplot(324)
plt.imshow(gausian_blur,cmap='gray')
plt.title('Gausian blurred')

median_blur = cv2.medianBlur(img,5)

plt.subplot(325)
plt.imshow(img,cmap = 'gray')
plt.title('Original Image')

plt.subplot(326)
plt.imshow(median_blur,cmap='gray')
plt.title('Median blurred')

