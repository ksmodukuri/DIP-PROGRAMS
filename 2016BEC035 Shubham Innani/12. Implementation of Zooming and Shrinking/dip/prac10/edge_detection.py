import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage.filters import roberts, sobel, sobel_h, sobel_v, prewitt, prewitt_v, prewitt_h
img = cv2.imread('cb.png',0)
plt.imshow(img,cmap='gray')

## Prewitt Operator
img1 = np.pad(img,1,mode='constant')
prewitt_operatorx =np.array([[1, 1 , 1],[0, 0 , 0],[-1, -1 , -1]])
prewitt_operatory =np.array([[1, 0 , -1],[1, 0 , -1],[1, 0 , -1]])
a=np.zeros([512,512])
b=np.zeros([512,512])

for i in range(512):
    for j in range(512):
        patch_img = img1[i:i+3, j:j+3]
        pval =np.sum(np.multiply(patch_img, prewitt_operatorx))
        a[i:i+1, j:j+1] = abs(pval)
        
for i in range(512):
    for j in range(512):
        patch_img = img1[i:i+3, j:j+3]
        pval =np.sum(np.multiply(patch_img, prewitt_operatory))
        b[i:i+1, j:j+1] = abs(pval)        
c =abs(np.sqrt(a**2 +b**2))
 
plt.subplot(2,3,1)
plt.imshow(abs(a),cmap='gray')
plt.title('Horizontal Edges')
plt.subplot(2,3,2)
plt.imshow(abs(b),cmap='gray')
plt.title('Vertical Edges')
plt.subplot(2,3,3)
plt.imshow(abs(c),cmap='gray')
plt.title('Edges')
plt.subplot(2,3,4)
plt.imshow(abs(prewitt_h(img)),cmap='gray')
plt.title('Horizontal Edges Fn')
plt.subplot(2,3,5)
plt.imshow(abs(prewitt_v(img)),cmap='gray')
plt.title('Vertical Edges Fn')
plt.subplot(2,3,6)
plt.imshow(abs(prewitt(img)),cmap='gray')
plt.title('Total Edges Fn')
plt.subplots_adjust(hspace=0.35, wspace=0.35)

##Sobel Operator
sobel_operatorx =np.array([[1, 2 , 1],[0, 0 , 0],[-1, -2 , -1]])
sobel_operatory =np.array([[1, 0 , -1],[2, 0 , -2],[1, 0 , -1]])
a=np.zeros([512,512])
b=np.zeros([512,512])

for i in range(512):
    for j in range(512):
        patch_img = img1[i:i+3, j:j+3]
        pval =np.sum(np.multiply(patch_img, sobel_operatorx))
        a[i:i+1, j:j+1] = pval
for i in range(512):
    for j in range(512):
        patch_img = img1[i:i+3, j:j+3]
        pval =np.sum(np.multiply(patch_img, sobel_operatory))
        b[i:i+1, j:j+1] = pval
c =abs(np.sqrt(a**2 +b**2))

plt.subplot(2,3,1)
plt.imshow(abs(a),cmap='gray')
plt.title('Horizontal Edges')
plt.subplot(2,3,2)
plt.imshow(abs(b),cmap='gray')
plt.title('Vertical Edges')
plt.subplot(2,3,3)
plt.imshow(abs(c),cmap='gray')
plt.title('Edges')
plt.subplot(2,3,4)
plt.imshow(abs(sobel_h(img)),cmap='gray')
plt.title('Horizontal Edges Fn')
plt.subplot(2,3,5)
plt.imshow(abs(sobel_v(img)),cmap='gray')
plt.title('Vertical Edges Fn')
plt.subplot(2,3,6)
plt.imshow(abs(sobel(img)),cmap='gray')
plt.title('Total Edges Fn')
plt.subplots_adjust(hspace=0.35,wspace=0.35)

## Robert Operator
robertx = np.array([[1, 0],[0,-1]])
roberty= np.array([[ 0, 1],[-1, 0]])
a=np.zeros([512,512])
b=np.zeros([512,512])
for i in range(512):
    for j in range(512):
        patch_img = img1[i:i+2, j:j+2]
        pval =np.sum(np.multiply(patch_img, robertx))
        a[i:i+1, j:j+1] = abs(pval)
        
for i in range(512):
    for j in range(512):
        patch_img = img1[i:i+2, j:j+2]
        pval =np.sum(np.multiply(patch_img, roberty))
        b[i:i+1, j:j+1] = abs(pval)
c =abs(np.sqrt(a**2 +b**2))

plt.subplot(2,2,1)
plt.imshow(a,cmap='gray')
plt.title('Horizontal Edges')
plt.subplot(2,2,2)
plt.imshow(b,cmap='gray')
plt.title('Vertical Edges')
plt.subplot(2,2,3)
plt.imshow(b,cmap='gray')
plt.title('Total Edges')
plt.subplot(2,2,4)
plt.imshow(roberts(img), cmap='gray')
plt.title('Edges with Fn')
plt.subplots_adjust(hspace=0.35, wspace=0.35)