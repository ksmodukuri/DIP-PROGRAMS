
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread(r'C:\\Users\\DSPLAB_USER\\Desktop\\dip prachi\\lena1204.png',0)

new_img = np.zeros((225*2,225*2))

for i in range(225):
    for j in range(225):
       new_img[i*2:i*2+2,j*2:j*2+2] = img[i][j]

plt.subplot(1,2,1)
plt.imshow(img,cmap = 'gray')
plt.subplot(1,2,2)
plt.imshow(new_img,cmap = 'gray')

#%%


new_img_shrink = np.zeros((225,225))

for i in range(113):
    new_img_shrink[i,:] = img[2*i-1,:]


for i in range(113):
    new_img_shrink[:,i] = new_img_shrink[:,2*i-1]


final_img = new_img_shrink[:113,:113]
plt.subplot(1,2,1)
plt.imshow(img,cmap = 'gray')
plt.subplot(1,2,2)
plt.imshow(final_img, cmap = 'gray')

#%%

n = 5

new_img = np.zeros((225*n,225*n))

for i in range(225):
    for j in range(225):
       new_img[i*n:i*n+n,j*n:j*n+n] = img[i][j]


plt.subplot(1,2,1)
plt.imshow(img,cmap = 'gray')
plt.subplot(1,2,2)
plt.imshow(new_img,cmap = 'gray')

#%%
new_img = np.zeros((112,112))

for i in range(112):
    for j in range(112):
       new_img[i][j] = np.max(img[i*2:i*2+2,j*2:j*2+2])


plt.subplot(1,2,1)
plt.imshow(img,cmap = 'gray')
plt.subplot(1,2,2)
plt.imshow(new_img,cmap = 'gray')
#%%
new_img = np.zeros((112,112))

for i in range(112):
    for j in range(112):
       new_img[i][j] = np.min(img[i*2:i*2+2,j*2:j*2+2])


plt.subplot(1,2,1)
plt.imshow(img,cmap = 'gray')
plt.subplot(1,2,2)
plt.imshow(new_img,cmap = 'gray')

#%%
new_img = np.zeros((112,112))

for i in range(112):
    for j in range(112):
       new_img[i][j] = np.sum(img[i*2:i*2+2,j*2:j*2+2])/4


plt.subplot(1,2,1)
plt.imshow(img,cmap = 'gray')
plt.subplot(1,2,2)
plt.imshow(new_img,cmap = 'gray')

#%%
