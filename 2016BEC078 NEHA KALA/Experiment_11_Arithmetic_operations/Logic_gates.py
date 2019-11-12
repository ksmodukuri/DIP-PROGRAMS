# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 23:55:54 2019

@author: Neha Kala
"""



from matplotlib import pyplot as plt
import cv2
img1=cv2.imread("BW.png",0)
plt.subplot(241)
plt.title("Input_1",fontsize=20)
plt.imshow(img1,cmap="gray")
img2=cv2.imread("WB.png",0)
plt.subplot(242)
plt.title("Input_2",fontsize=20)
plt.imshow(img2,cmap="gray")

not_img1= cv2.bitwise_not(img1, mask = None) 
plt.subplot(243)
plt.title("Input_1_NOT",fontsize=20)
plt.imshow(not_img1,cmap="gray")

not_img2 = cv2.bitwise_not(img2, mask = None) 
plt.subplot(244)
plt.title("Input_2_NOT",fontsize=20)
plt.imshow(not_img2,cmap="gray")

and_img=cv2.bitwise_and(img2, img1, mask = None)
plt.subplot(245)
plt.title("AND",fontsize=20)
plt.imshow(and_img,cmap="gray")



or_img=cv2.bitwise_or(img2, img1, mask = None)
plt.subplot(246)
plt.title("OR",fontsize=20)
plt.imshow(or_img,cmap="gray")



xor_img=cv2.bitwise_xor(img2, img1, mask = None)
plt.subplot(247)
plt.title("XOR",fontsize=20)
plt.imshow(xor_img,cmap="gray")





