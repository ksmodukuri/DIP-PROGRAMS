# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 23:54:20 2019

@author: Neha Kala
"""


from matplotlib import pyplot as plt
import cv2
img1=cv2.imread("BW.png",0)
plt.subplot(221)
plt.title("Input_1",fontsize=20)
plt.imshow(img1,cmap="gray")
img2=cv2.imread("WB.png",0)
plt.subplot(222)
plt.title("Input_2",fontsize=20)
plt.imshow(img2,cmap="gray")


#Addition
new_img=cv2.add(img1,img2)
plt.subplot(223)
plt.title("Addition of images",fontsize=20)
plt.imshow(new_img,cmap="gray")



#subtraction
new_img=cv2.subtract(img1,img2)
plt.subplot(224)
plt.title("Subtraction of images",fontsize=20)
plt.imshow(new_img,cmap="gray")



==================================================
from matplotlib import pyplot as plt
import cv2
img1=cv2.imread("BW.png",0)
plt.subplot(221)
plt.title("Input_1",fontsize=20)
plt.imshow(img1,cmap="gray")
img2=cv2.imread("WB.png",0)
plt.subplot(222)
plt.title("Input_2",fontsize=20)
plt.imshow(img2,cmap="gray")


#Multiplication
new_img=img1*img2
plt.subplot(223)
plt.title("Multiplication of images",fontsize=20)
plt.imshow(new_img,cmap="gray")



#Division
new_img=img1/img2
plt.subplot(224)
plt.title("Division of images",fontsize=20)
plt.imshow(new_img,cmap="gray")

