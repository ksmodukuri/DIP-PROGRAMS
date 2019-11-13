
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('Checkerboard.jpg',0)

plt.subplot(431)
plt.imshow(img,cmap='gray')
z=np.zeros(256)

for i in range(0,64):
    for j in range(0,64):
        z[img[i][j]] += 1
plt.subplot(432)
plt.plot(z) 

histr = cv2.calcHist([img],[0],None,[256],[0,256]) 
plt.subplot(433)
plt.plot(histr) 


img2=cv2.imread('lena.png',0)
plt.subplot(434)
plt.imshow(img2,cmap='gray')
z=np.zeros(256)

for i in range(0,512):
    for j in range(0,512):
        z[img2[i][j]] += 1
plt.subplot(435)
plt.plot(z) 

histr = cv2.calcHist([img2],[0],None,[256],[0,256]) 
plt.subplot(436)
plt.plot(histr) 


img3 = np.rot90(img)
plt.subplot(437)
plt.imshow(img3,cmap='gray')
z=np.zeros(256)

for i in range(0,64):
    for j in range(0,64):
        z[img3[i][j]] += 1
plt.subplot(438)
plt.plot(z) 

histr = cv2.calcHist([img3],[0],None,[256],[0,256]) 
plt.subplot(439)
plt.plot(histr) 
