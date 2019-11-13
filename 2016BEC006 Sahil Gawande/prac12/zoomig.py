import numpy as np
import cv2
from matplotlib import pyplot as plt

a = cv2.imread('lena.png',0)
cv2.imwrite('12original.png',a)
plt.imshow(a,cmap='gray')

##Alternate rows and colomns delete
a2 = np.zeros([256,256])
for i in range(256):
    for j in range(256):
        l=a[i*2][j*2]
        a2[i][j] = l
        
plt.imshow(a2,cmap='gray')
cv2.imwrite('12shrink.png',a2)

img = cv2.imread('lena.png',0)
cv2.imwrite('12original1.png',img)

##Average COmpression
a1=np.zeros([512,512])
for i in range(0,512,2):
    for j in range(0,512,2):
        patch_img = img[i:i+2, j:j+2]
        avg = np.average(patch_img)
        a1[i][j] = np.round(avg)            
a2 = np.delete(a1, np.s_[1::2], 0)
a2 = np.delete(a2, np.s_[1::2], 1) 
plt.imshow(a2, cmap='gray')
cv2.imwrite('avgcmp.png',a2)

##Max Compression
a1=np.zeros([512,512])
for i in range(0,512,2):
    for j in range(0,512,2):
        patch_img = img[i:i+2, j:j+2]
        avg = np.max(patch_img)
        a1[i][j] = np.round(avg)            
a2 = np.delete(a1, np.s_[1::2], 0)
a2 = np.delete(a2, np.s_[1::2], 1) 
plt.imshow(a2, cmap='gray')
cv2.imwrite('maxcmp.png',a2)

##min compression
a1=np.zeros([512,512])
for i in range(0,512,2):
    for j in range(0,512,2):
        patch_img = img[i:i+2, j:j+2]
        avg = np.min(patch_img)
        a1[i][j] = np.round(avg)            
a2 = np.delete(a1, np.s_[1::2], 0)
a2 = np.delete(a2, np.s_[1::2], 1) 
plt.imshow(a2, cmap='gray')
cv2.imwrite('mincmp.png',a2)

##Alternate rows and coloumns
a2 = np.delete(img, np.s_[1::2], 0)
a2 = np.delete(a2, np.s_[1::2], 1) 
plt.imshow(a2, cmap='gray')
cv2.imwrite('altcmp.png',a2)

#Zooming
a = np.array(np.zeros([512,512]))
for i in range(256):
    for j in range(256):
        p = a2[i][j]
        a[i*2][j*2]=p
        l= a[i*2][j*2]
        a[i*2 + 1][j*2 + 1]=l
        a[i*2 + 1][j*2]=l
        a[i*2][j*2 + 1]=l       
plt.imshow(a, cmap='gray')
cv2.imwrite('zooming.png',a)