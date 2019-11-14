import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('/home/romil/Pictures/lena.jpg',0)

new_img = np.zeros((512,512))

for i in range(256):
    for j in range(256):
       new_img[i*2:i*2+2,j*2:j*2+2] = img[i][j]

plt.subplot(241)
plt.imshow(img,cmap = 'gray')
plt.title('original image',fontsize=20)
plt.subplot(242)
plt.imshow(new_img,cmap = 'gray')
plt.title('Image Zooming',fontsize=20)

img1= np.zeros((256,256))

for i in range(128):
    img1[i,:] = img[2*i-1,:]

for i in range(128):
    img1[:,i] = img1[:,2*i-1]

img2 = img1[:128,:128]

plt.subplot(243)
plt.imshow(img2, cmap = 'gray')
plt.title('Image Shrinking',fontsize=20)

n = 4
new_img = np.zeros((256*n,256*n))
for i in range(256):
    for j in range(256):
       new_img[i*n:i*n+n,j*n:j*n+n] = img[i][j]

plt.subplot(244)
plt.imshow(new_img,cmap = 'gray')
plt.title('Zoomed by 4X',fontsize=20)

new_img = np.zeros((128,128))

for i in range(128):
    for j in range(128):
       new_img[i][j] = np.max(img[i*2:i*2+2,j*2:j*2+2])

plt.subplot(245)
plt.imshow(new_img,cmap = 'gray')
plt.title('Max',fontsize=20)

new_img = np.zeros((128,128))

for i in range(128):
    for j in range(128):
       new_img[i][j] = np.min(img[i*2:i*2+2,j*2:j*2+2])

plt.subplot(246)
plt.imshow(new_img,cmap = 'gray')
plt.title('Min',fontsize=20)

new_img = np.zeros((128,128))

for i in range(128):
    for j in range(128):
       new_img[i][j] = np.sum(img[i*2:i*2+2,j*2:j*2+2])/4

plt.subplot(247)
plt.imshow(new_img,cmap = 'gray')
plt.title('Averaging',fontsize=20)