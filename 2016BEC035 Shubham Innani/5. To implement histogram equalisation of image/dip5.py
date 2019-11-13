### Histogram Equlization
import numpy as np
import cv2
from matplotlib import pyplot as plt 

img=cv2.imread('pout.jpg',0)
size=img.shape
plt.imshow(img,cmap='gray')
z=np.zeros(256)
for i in img:
    for j in i:
        z[j]=z[j]+1
        
for i in range(256):
    z[i]=z[i]/(512*512)
    
for i in range(256):
    z[i]=z[i]+z[i-1]
    plt.plot(z)
        
for i in range(256):
    z[i]=round(z[i]*255)
    
for i in range(size[0]):
    for j in range(size[1]):
        img[i][j]=z[img[i][j]]
plt.imshow(img, cmap='gray')
        
