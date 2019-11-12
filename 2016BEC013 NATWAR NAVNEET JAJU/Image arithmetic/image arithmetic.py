# -*- coding: utf-8 -*-

import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread(r"D:\Btech practicals\DIP\black_box.png",0)
img2 = cv2.imread(r"D:\Btech practicals\DIP\car_image.png",0)
img3 = cv2.imread(r"D:\Btech practicals\DIP\whit_box.png",0)
add = img1+img2
plt.subplot(131)
plt.imshow(img1,cmap='gray')
plt.subplot(132)
plt.imshow(img2,cmap='gray')
plt.subplot(133)
plt.imshow(add,cmap='gray') 
plt.title("addition")

sub = img2 - img3
plt.subplot(131)
plt.imshow(img2,cmap='gray')
plt.subplot(132)
plt.imshow(img3,cmap='gray')
plt.subplot(133)
plt.imshow(sub,cmap='gray')
plt.title("subtraction")

mul = img1*img2
plt.subplot(131)
plt.imshow(img1,cmap='gray')
plt.subplot(132)
plt.imshow(img2,cmap='gray')
plt.subplot(133)
plt.imshow(mul,cmap='gray')
plt.title("multiplication")

div = img2/img3
plt.subplot(131)
plt.imshow(img2,cmap='gray')
plt.subplot(132)
plt.imshow(img3,cmap='gray')
plt.subplot(133)
plt.imshow(div,cmap='gray')
plt.title("division")

orr = cv2.bitwise_or(img1,img2)
plt.subplot(131)
plt.imshow(img2,cmap='gray')
plt.subplot(132)
plt.imshow(img1,cmap='gray')
plt.subplot(133)
plt.imshow(orr,cmap='gray')
plt.title("bitwise or")

aand = cv2.bitwise_and(img3,img2)
plt.subplot(131)
plt.imshow(img2,cmap='gray')
plt.subplot(132)
plt.imshow(img3,cmap='gray')
plt.subplot(133)
plt.imshow(aand,cmap='gray')
plt.title("bitwise and")

xor = cv2.bitwise_xor(img3,img2)
plt.subplot(131)
plt.imshow(img2,cmap='gray')
plt.subplot(132)
plt.imshow(img3,cmap='gray')
plt.subplot(133)
plt.imshow(xor,cmap='gray')
plt.title("bitwise xor")

imgg = cv2.imread(r'D:\Btech practicals\DIP\blackbox_2.jpg')
notn = cv2.bitwise_not(imgg)
plt.subplot(131)
plt.imshow(imgg,cmap='gray')
plt.subplot(133)
plt.imshow(notn,cmap='gray')
plt.title("bitwise not")