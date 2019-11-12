
#Histogram Equilization
import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread("pout.png",0)
plt.subplot(2,3,1)
plt.imshow(img,cmap='gray')

z=np.zeros(256)
for i in img:
    for j in i:
        z[j]=z[j]+1
    total=sum(z)
for i in range(256):
    z[i]=z[i]/total
for i in range(256):
    z[i]=z[i]+z[i-1]
for i in range(256):
    z[i]=z[i]*255
    z[i]=round(z[i])
size=np.shape(img)
for i in range(size[0]):
    for j in range(size[1]):
        img[i][j]=z[img[i][j]]
        
plt.subplot(2,3,2)
plt.imshow(img,cmap='gray')
