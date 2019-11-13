import cv2
from matplotlib import pyplot as plt
import numpy as np
imgg = cv2.imread('checkerboard_new.jpg')
img = imgg[:,:,0]
mask_1 = np.array([[-1,0,1],[-2,0,2],[-1,0 ,1]])
mask_2 = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
img = np.pad(img,1,'constant')
blankimg = np.zeros([512,512])
for i in range(512):
    for j in range(512):
        mull = img[i:i+3,j:j+3]*mask_1
        blankimg[i][j] = np.sum(mull)      
plt.subplot(221)
plt.imshow(img,cmap='gray')
plt.title('Original Image')
plt.subplot(222)
plt.imshow(blankimg,cmap = 'gray')
plt.title('Sobel X')
GX = np.zeros([512,512])
GX = blankimg
blankimg = np.zeros([512,512])

for i in range(512):
    for j in range(512):
        mull = img[i:i+3,j:j+3]*mask_2
        blankimg[i][j] = np.sum(mull)
plt.subplot(223)
plt.imshow(blankimg,cmap = 'gray')
plt.title('Sobel Y')
GY = np.zeros([512,512])
GY = blankimg
G = (GX**2+GY**2)**0.5
plt.subplot(224)
plt.imshow(G,cmap='gray')
plt.title('G = (Gx^2+Gy^2)^0.5')
psnr = 10*np.log10((255*255)/(1/(512*512)*np.sum(blankimg-imgg[:,:,0])*np.sum(blankimg-imgg[:,:,0])))
print("psnr = ",psnr)