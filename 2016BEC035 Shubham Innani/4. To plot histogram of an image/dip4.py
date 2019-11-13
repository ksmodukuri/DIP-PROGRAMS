import numpy as np
import cv2
from matplotlib import pyplot as plt
img1=cv2.imread('lena.jpg',0) 
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)) 
z=np.zeros(256) 
for i in img1: 
    for j in i:
        z[j]=z[j]+1 
plt.plot(z)  
z1=cv2.calcHist([img1],[0],None,[256],[0,256]) 
plt.plot(z1) 
img=cv2.imread('checker.png',0) 
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  
z=np.zeros(256) 
for i in img: 
    for j in i:
        z[j]=z[j]+1 
plt.plot(z) 
z1=cv2.calcHist([img],[0],None,[256],[0,256]) 
plt.plot(z1) 

img=cv2.imread('bw.jpg',0) 
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  
z=np.zeros(256) 
for i in img:
    for j in i:
        z[j]=z[j]+1
plt.plot(z)
z1=cv2.calcHist([img],[0],None,[256],[0,256]) 
plt.plot(z1)
x=np.rot90(img1) 
plt.imshow(cv2.cvtColor(x,cv2.COLOR_BGR2RGB)) 
z=np.zeros(256) 
for i in img:
    for j in i: 
        z[j]=z[j]+1 
plt.plot(z) 
z1=cv2.calcHist([img],[0],None,[256],[0,256]) 
plt.plot(z1)
imga=cv2.imread('lena.jpg',0) 
plt.imshow(cv2.cvtColor(imga, cv2.COLOR_BGR2RGB)) 
z=np.zeros(256) 
for i in imga:
    for j in i:
        z[j]=z[j]+1 
for i in range(256):
    z[i]=z[i]/(512*512) 
for i in range(256):
    z[i]=z[i]+z[i-1] 
plt.plot(z) 
