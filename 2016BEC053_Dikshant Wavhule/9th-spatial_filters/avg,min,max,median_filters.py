import cv2
from matplotlib import pyplot as plt
import numpy as np

imgg = cv2.imread('slt.png')
img = imgg[:,:,0]
mask = np.array([[1/25,1/25,1/25,1/25,1/25],[1/25,1/25,1/25,1/25,1/25],[1/25,1/25,1/25,1/25,1/25],[1/25,1/25,1/25,1/25,1/25],[1/25,1/25,1/25,1/25,1/25]])
img = np.pad(img,2,'constant')
blankimg = np.zeros([512,512])

for i in range(512):
    for j in range(512):
        mull = img[i:i+5,j:j+5]*mask
        blankimg[i][j] = np.sum(mull)
        
plt.subplot(121)
plt.imshow(img,cmap='gray')
plt.title('Original Image')
plt.subplot(122)
plt.imshow(blankimg,cmap = 'gray')
plt.title('Average Filter')
psnr = 10*np.log10((255*255)/(1/(512*512)*np.sum(blankimg-imgg[:,:,0])*np.sum(blankimg-imgg[:,:,0])))
print("psnr = ",psnr)


#==============================================================================


import cv2
from matplotlib import pyplot as plt
import numpy as np

imgg = cv2.imread('slt.png')
img = imgg[:,:,0]
mask = np.array([[1/25,1/25,1/25,1/25,1/25],[1/25,1/25,1/25,1/25,1/25],[1/25,1/25,1/25,1/25,1/25],[1/25,1/25,1/25,1/25,1/25],[1/25,1/25,1/25,1/25,1/25]])
img = np.pad(img,2,'constant')
blankimg = np.zeros([512,512])

for i in range(512):
    for j in range(512):
        mull = img[i:i+5,j:j+5]*mask
        blankimg[i][j] = np.min(mull)
        
plt.subplot(131)
plt.imshow(img,cmap='gray')
plt.title('Original Image')
plt.subplot(132)
plt.imshow(blankimg,cmap = 'gray')
plt.title('Min Filter')
psnr = 10*np.log10((255*255)/(1/(512*512)*np.sum(blankimg-imgg[:,:,0])*np.sum(blankimg-imgg[:,:,0])))
print("psnr = ",psnr)

blankimg = np.zeros([512,512])

for i in range(512):
    for j in range(512):
        mull = img[i:i+5,j:j+5]*mask
        blankimg[i][j] = np.max(mull)

plt.subplot(133)
plt.imshow(blankimg,cmap = 'gray')
plt.title('Max Filter')
psnr = 10*np.log10((255*255)/(1/(512*512)*np.sum(blankimg-imgg[:,:,0])*np.sum(blankimg-imgg[:,:,0])))
print("psnr = ",psnr)
#==============================================================================

import cv2
from matplotlib import pyplot as plt
import numpy as np
import statistics

imgg = cv2.imread('slt.png')
img = imgg[:,:,0]
mask = np.array([[1/25,1/25,1/25,1/25,1/25],[1/25,1/25,1/25,1/25,1/25],[1/25,1/25,1/25,1/25,1/25],[1/25,1/25,1/25,1/25,1/25],[1/25,1/25,1/25,1/25,1/25]])
img = np.pad(img,2,'constant')
blankimg = np.zeros([512,512])

for i in range(512):
    for j in range(512):
        mull = img[i:i+5,j:j+5]*mask
        a = mull.flatten()
        b = statistics.median(a)
        blankimg[i][j] = b
        
plt.subplot(121)
plt.imshow(img,cmap='gray')
plt.title('Original Image')
plt.subplot(122)
plt.imshow(blankimg,cmap = 'gray')
plt.title('Median Filter')
psnr = 10*np.log10((255*255)/(1/(512*512)*np.sum(blankimg-imgg[:,:,0])*np.sum(blankimg-imgg[:,:,0])))
print("psnr = ",psnr)
